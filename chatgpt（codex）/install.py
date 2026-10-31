#!/usr/bin/env python3
"""Copy the bundled skill into Codex's skill directory without overwriting."""
import argparse
import os
from pathlib import Path
import shutil

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path,
                        help='Parent skill directory. Defaults to CODEX_HOME/skills or ~/.codex/skills.')
    args = parser.parse_args()
    source = Path(__file__).resolve().parent / 'ai-style-design'
    parent = args.dest or (Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'skills')
    target = parent.expanduser().resolve() / 'ai-style-design'
    if not (source / 'SKILL.md').is_file():
        parser.error('Bundled SKILL.md was not found.')
    if target.exists() or target.is_symlink():
        parser.error('Destination already exists; no files changed: ' + str(target))
    parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)
    print('Installed: ' + str(target))
    print('Invoke $ai-style-design on your next turn. Restart Codex if it does not appear.')

if __name__ == '__main__':
    main()
