#!/usr/bin/env python3
"""Portable corpus lookup and keyword screening. Python standard library only."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def read_json(name):
    return json.loads((ROOT / 'references' / name).read_text(encoding='utf-8'))

def entries(category='all'):
    corpus = read_json('corpus_index.json')['skills']
    return [dict(e, category=c) for c, group in corpus.items()
            if category in ('all', c) for e in group.values()]

def diagnose(text):
    rules = read_json('diagnostic_rules.json')
    dimensions = []
    for key, rule in rules.items():
        matches = [term for term in rule['keywords'] if term.casefold() in text.casefold()]
        dimensions.append({'id': key, 'name': rule['name'], 'matched_terms': matches,
                           'deduction': min(rule['weight'], len(matches) * rule['deduction']),
                           'cap': rule['weight'], 'advice': rule['advice']})
    total = sum(d['deduction'] for d in dimensions)
    maximum = sum(d['cap'] for d in dimensions)
    return {'method': 'keyword-screen-v1', 'raw_deduction': total, 'maximum': maximum,
            'normalized_index': round(total / maximum * 100, 1), 'dimensions': dimensions,
            'note': 'Keyword screening only; review context. Not AI detection or aesthetic validation.'}

def positive_int(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError('must be greater than zero')
    return number

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    listing = sub.add_parser('list')
    listing.add_argument('--category', choices=['all', 'visual', 'narrative'], default='all')
    show = sub.add_parser('show')
    show.add_argument('id')
    search = sub.add_parser('search')
    search.add_argument('query')
    search.add_argument('--limit', type=positive_int, default=5)
    diagnostic = sub.add_parser('diagnose')
    inputs = diagnostic.add_mutually_exclusive_group(required=True)
    inputs.add_argument('--text')
    inputs.add_argument('--file', type=Path)
    args = parser.parse_args()
    if args.command == 'list':
        result = [{k: e[k] for k in ('id', 'name', 'category', 'description')}
                  for e in entries(args.category)]
    elif args.command == 'show':
        result = next((e for e in entries() if e['id'] == args.id), None)
        if result is None:
            parser.error('Unknown style ID: ' + args.id)
    elif args.command == 'search':
        terms = list(dict.fromkeys(re.findall(r'[^\W_]+(?:-[^\W_]+)*', args.query.casefold())))
        result = []
        for e in entries():
            haystack = json.dumps(e, ensure_ascii=False).casefold()
            matches = [t for t in terms if t in haystack]
            if matches:
                result.append({'id': e['id'], 'name': e['name'], 'category': e['category'],
                               'matched_terms': matches, 'term_count': len(matches)})
        result.sort(key=lambda e: (-e['term_count'], e['id']))
        result = result[:args.limit]
    else:
        try:
            text = args.file.read_text(encoding='utf-8-sig') if args.file else args.text
        except OSError as exc:
            parser.error(str(exc))
        result = diagnose(text)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
