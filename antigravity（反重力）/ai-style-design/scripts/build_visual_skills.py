# -*- coding: utf-8 -*-
import os

VISUAL_SKILLS = {
    "style-haipai-artdeco": {
        "name": "style-haipai-artdeco",
        "description": "民国海派与月份牌设计美学 Skill。融合传统工笔甜润名媛、西方透视明暗、早期 Art Deco 装饰与老上海石库门摩登，杜绝廉价艳俗影楼风。",
        "version": "1.0.0",
        "tags": ["haipai", "art-deco", "vintage-shanghai", "yuefenpai", "graphic-design", "anti-homogenization"],
        "title": "民国海派与月份牌设计美学 (Haipai & Yuefenpai Art Deco)",
        "chapter": "第一篇第1章",
        "soul": [
            "**核心哲学**：上海开埠后中西商业文明剧烈碰撞的产物。将中国传统工笔年画的吉庆民俗，与西方透视明暗技法、装饰艺术（Art Deco）及好莱坞摩登风潮熔铸一炉，开创近代中国第一套成熟的商业视觉与消费文化体系。",
            "**AI 常见同质化缺陷**：粗暴生成廉价影楼塑料古风、俗艳高光大红大紫、现代整容脸旗袍女郎，缺乏民国月份牌特有的擦笔水彩温润质感与金石骨相。",
            "**本 Skill 矫正法则**：\n  1. **擦笔水彩画法 (Airbrush-watercolor)**：微观上呈现细腻炭精粉打底与水彩层层轻薄渲染的柔和晕染，皮肤温润如玉，光泽内敛。\n  2. **中西折衷骨相**：结合修长合身的高领缎面改良旗袍、复古烫发波浪卷、西洋留声机与老石库门清水砖雕门楣。\n  3. **金石文人排版**：辅以民国双色石版套印老报纸美术字、六朝金石气雕版宋体与典雅如意花框。"
        ],
        "palette": [
            "- 胭脂复古红 (Vintage Carmine Rouge): `#9E2A2B` (焦点与花饰, 占25%)",
            "- 留声机洋金 (Phonograph Brass Gold): `#D4AF37` (几何线条与镶边, 占20%)",
            "- 沉香墨青 (Dark Agarwood Teal Blue): `#1E3F66` (深色服饰与背景底色, 占35%)",
            "- 象牙暖白纸 (Ivory Newsprint White): `#F7F4EB` (画幅底纸与留白, 占20%)"
        ],
        "materials": [
            "- 擦笔炭精粉柔和渐晕与轻薄水彩纸纹 (Airbrush carbon powder soft vignette and watercolor wash)",
            "- 高级真丝重磅绸缎微光漫反射 (Heavy silk satin soft diffused sheen)",
            "- 氧化做旧黄铜铸件与留声机喇叭光泽 (Aged oxidized brass with subtle patina)",
            "- 老上海石库门清水青砖与水刷石门楣 (Old shikumen grey brick and washed granitic plaster)"
        ],
        "optics": [
            "- 1930年代室内柔和漫射钨丝暖光 (Soft diffused 1930s tungsten interior illumination)",
            "- 轻微双色石版套印边缘渗透与柯达早期感光乳剂柔和微颗粒 (Lithographic ink registration bleed and vintage emulsion grain)",
            "- 严禁高硬度日光直射与刺眼赛博霓虹点光源。"
        ],
        "grid": [
            "- 留白与包边：经典的四方如意纹或Art Deco几何折线包边框，四周预留10%-15%边框饰带空间。",
            "- 构图法则：人物通常微侧身居中偏右，视线微挑看向虚空，上方或侧边预留书法题跋或商业标贴空间。"
        ],
        "forbidden": [
            "NO modern plastic 3D CGI rendering, NO shiny polyester cheap costumes",
            "NO anime face, NO modern studio photorealistic glamour kitsch",
            "NO oversaturated neon colors, NO chaotic cyberpunk cityscapes",
            "NO harsh direct flashes, NO digital plastic lens flares"
        ],
        "positive_prompt": "1930s vintage Shanghai Haipai Art Deco poster aesthetic, graceful Republican-era lady wearing tailored dark teal silk cheongsam `#1E3F66` with gold embroidery `#D4AF37`, sitting beside an antique brass phonograph in a Shikumen salon. Soft airbrush watercolor wash texture, delicate carbon pencil shading, muted carmine rouge accents `#9E2A2B`, warm ivory aged paper tone `#F7F4EB`. Classic geometric decorative border, elegant nostalgic atmosphere, soft tungsten ambient lighting, authentic Republican Shanghai commercial art masterpiece.",
        "negative_prompt": "modern photography, digital 3d render, plastic skin, anime girl, neon lights, oversaturated red, contemporary room, cheap costumes, messy background, text watermark, harsh flash.",
        "typography": [
            "- **主标题**：民国老美术字、民国铅印黑体、带有金石隶书顿挫感的定制美术体。",
            "- **副标与正文**：康熙字典体 / 经典仿宋体，字距舒展，竖排右起排版。"
        ],
        "voice_match": "`voice-zhangailing`（世俗苍凉工笔）或 `voice-luxun`（金石冷峻硬骨）。"
    },
    "style-socialist-realism": {
        "name": "style-socialist-realism",
        "description": "新中国现实主义与工农兵工业美学 Skill。以新兴木刻刀锋感、红光亮高大全英雄仰角与苏式重工业力量为内核，剔除浮夸软弱装饰。",
        "version": "1.0.0",
        "tags": ["socialist-realism", "woodcut", "propaganda-poster", "industrial", "graphic-design", "anti-homogenization"],
        "title": "新中国现实主义与工农兵工业美学 (Socialist Realism & Industrial Woodcut)",
        "chapter": "第一篇第2章",
        "soul": [
            "**核心哲学**：以苏联社会主义现实主义结合中国延安新兴木刻传统，艺术服务于人民工农兵与国家工业化建设。视觉充满无产阶级力量感、革命乐观主义与对重型钢铁机械的深情赞歌。",
            "**AI 常见同质化缺陷**：容易滑向卡通化扁平宣传画、疲软无力的现代插画人物，或充斥商业插画轻飘飘的柔美，丧失木刻版画刀砍斧凿的雄强筋骨。",
            "**本 Skill 矫正法则**：\n  1. **新兴木刻刀痕刻线 (Woodcut gouge lines)**：结构边缘展现强劲有力的刀锋切面与黑白阴阳交错的粗犷木刻肌理。\n  2. **红光亮与英雄仰视视角**：人物身材挺拔结实，目光坚毅昂首望向前方，45度仰视形成崇高的力量感。\n  3. **重工业与大地质感**：聚焦钢铁铸造、麦穗齿轮、高耸烟囱与夯实泥土，杜绝一切轻佻的马卡龙与装饰发光线条。"
        ],
        "palette": [
            "- 革命朱砂红 (Revolutionary Vermilion Red): `#C91B1B` (旗帜与核心力量符号, 占40%)",
            "- 晨曦工业黄 (Dawn Industrial Ochre Yellow): `#F6BA13` (朝阳曙光与麦穗齿轮, 占25%)",
            "- 鞍钢机械冷灰 (Furnace Machine Iron Gray): `#3E444A` (机械铸铁与建筑骨架, 占25%)",
            "- 延安木刻暖褐 (Woodblock Warm Earth Brown): `#5E3A24` (木刻阴影与土地原色, 占10%)"
        ],
        "materials": [
            "- 延安新兴木刻油墨拓印粗糙纹理 (Woodcut relief block ink texture and rough wood grain)",
            "- 未经漂白的重磅牛皮纸与再生工业印刷纸 (Unbleached kraft paper with raw fibrous specks)",
            "- 生铁铸造机械与冷轧钢材哑光切面 (Matte cast iron machinery and hot-rolled steel plate)",
            "- 粗布劳动工作服与工装帆布质地 (Heavy cotton canvas and coarse denim workwear)"
        ],
        "optics": [
            "- 地平线破晓喷薄而出的金色朝阳烈光 (Blazing golden sunrise breaking over industrial horizon)",
            "- 45度高对比度仰角侧逆光，硬朗勾勒工农兵面部骨骼轮廓。",
            "- 严禁柔光箱平光与毫无明暗力量的无影散漫光。"
        ],
        "grid": [
            "- 构图：强烈的对角线透视构图（Dynamic Diagonal Axis），主体自左下向右上昂扬冲刺。",
            "- 空间：饱满而极具压迫感的构图，英雄主体占据画面中央大半幅，背景以几何齿轮与烟囱阵列呼应。"
        ],
        "forbidden": [
            "NO pastel colors, NO cute anime characters, NO soft romantic floral elements",
            "NO decadent capitalist luxury, NO corporate slick minimalism",
            "NO soft airbrush gradients, NO shiny glitter textures",
            "NO downward timid looking figures, NO weak frail physiques"
        ],
        "positive_prompt": "Heroic Socialist Realism and revolutionary woodcut propaganda poster art, 1950s Chinese industrial aesthetic. Strong heroic steelworker low-angle shot gazing towards the socialist dawn horizon, background filled with towering blast furnaces, giant interlocking mechanical gears, and bold fluttering red banners `#C91B1B`. Dramatic chisel blade carved woodblock print texture, bold graphic lines, high contrast black ink gouging, golden morning sunlight `#F6BA13` illuminating resolute jawline, rough kraft paper background, monumental scale and immense revolutionary strength.",
        "negative_prompt": "cute cartoon, soft 3d render, anime style, pastel colors, Western corporate minimalism, timid posture, blurry details, soft focus, weak lighting, luxury glitter.",
        "typography": [
            "- **标语口号**：手绘刚劲铁线黑体、老式宣传画实心粗黑体，全部实心无投影。",
            "- **书刊题字**：刚健有力的毛体书法或木刻大字，字字千钧。"
        ],
        "voice_match": "`voice-luxun`（冷峻硬骨体）或 `voice-wieden-kennedy`（存在主义极限史诗）。"
    },
    "style-neo-guochao": {
        "name": "style-neo-guochao",
        "description": "新国潮与东方赛博机能 Skill。将汉字偏旁解构、传统战甲马面裙与数码机能美学、高反差朱砂黑科技深度重构，打破庸俗剪纸古风。",
        "version": "1.0.0",
        "tags": ["neo-guochao", "cyber-orientalism", "techwear", "streetwear", "graphic-design", "anti-homogenization"],
        "title": "新国潮与东方赛博机能 (Neo-Chinese Guochao & Techwear)",
        "chapter": "第一篇第4章",
        "soul": [
            "**核心哲学**：传统古老图腾（山海经异兽、青铜饕餮、道家符箓、汉字偏旁部首）与硬核赛博机能（Techwear）、3D数码异化艺术的强力杂交。它不是复古，而是东方文化在未来数字时空中的强势降临。",
            "**AI 常见同质化缺陷**：滥用俗气金色祥云剪纸贴图、廉价影楼汉服插画、毫无设计感的荧光蓝紫赛博雨夜，堆砌空洞符号。",
            "**本 Skill 矫正法则**：\n  1. **汉字结构异化与工业解构**：将楷书隶书笔画强行金属机械化、加入榫卯式战术卡扣断笔与穿孔排版。\n  2. **朱砂红与机能黑的极度反差**：以纯粹暗黑碳纤机能为底色，单点暴烈朱砂赤红与冷凝玉石色形成高能脉冲。\n  3. **战术马面裙与机能装配**：融合百褶马面裙硬挺剪裁、战术织带、防水压胶工艺与哑光钛合金配件。"
        ],
        "palette": [
            "- 淬火朱砂赤 (Cinnabar Pulse Red): `#D9251D` (警戒线条与能量核心, 占20%)",
            "- 战术机能暗黑 (Tactical Stealth Black): `#121214` (主基底与战术机能外骨骼, 占60%)",
            "- 冷淬玉石青 (Cyan Jade Cryo): `#00FFB2` (微光数码符箓与发光回路, 占10%)",
            "- 钛合金哑光灰 (Matte Titanium Slate): `#8A8F99` (机械卡扣与结构线条, 占10%)"
        ],
        "materials": [
            "- 哑光防撕裂尼龙与压胶防水面料 (Matte ripstop Cordura nylon and seam-taped technical fabric)",
            "- 激光镂空哑光钛合金与碳纤维结构件 (Laser-cut titanium hardware and matte dry carbon fiber)",
            "- 半透明磨砂工程亚克力与导光带 (Semi-translucent frosted acrylic and subtle light guides)",
            "- 天然冷翡翠与硬核金属异化镶嵌 (Raw cold jadeite set into brutalist mechanical frames)"
        ],
        "optics": [
            "- 隐秘阴郁的环境暗部，局域投射超细朱砂红或冰青色激光准星线。",
            "- 哑光表面极弱的漫反射高光，杜绝油腻次表面散射与泛滥光晕。"
        ],
        "grid": [
            "- 构图：战术模块化HUD卡片网格系统，参数标签与中文警告标识紧密排布在四周边缘。",
            "- 排版：超大异化汉字纵贯画面一侧，与精密数据条、机能警示斜纹形成密度悬殊对比。"
        ],
        "forbidden": [
            "NO traditional red lantern kitsch, NO cheesy paper-cut patterns",
            "NO cute chibi characters, NO soft watercolor fairy aesthetics",
            "NO cheap purple cyberpunk gradients, NO generic medieval fantasy armor",
            "NO messy blurry strokes, NO nostalgic sepia vintage filters"
        ],
        "positive_prompt": "Avant-garde Neo-Chinese techwear streetwear concept design, cyber-orientalism fashion editorial. Subject wearing asymmetric matte black tactical Mamianqun pleats made of heavy Cordura `#121214`, paired with structural dry carbon armor plates and cinnabar red pulse cables `#D9251D`. Intricate typography with deconstructed de-formed Chinese ideograms printed across matte chest harness, subtle cryo jade micro-glow `#00FFB2`, dark minimalist brutalist concrete backdrop, cinematic moody rim light, high-tech industrial hardware, sharp hyper-detailed texture, 8k resolution, Hasselblad lens.",
        "negative_prompt": "traditional paper cut, cheap red lanterns, fantasy dragon, generic cyberpunk purple, low poly, oversaturated, cute, anime, messy composition, blurry, oily shiny 3d.",
        "typography": [
            "- **主视觉汉字**：极度加粗的无衬线几何断笔黑体、机械拆卸部首定制字型。",
            "- **数据与标签**：等宽英文字体（JetBrains Mono / DIN Next）与竖排微型警示标语组合。"
        ],
        "voice_match": "`voice-yemaozhong`（铁锤冲突穿透体）或 `voice-jobs-clarity`（激进清澈体）。"
    },
    "style-wabi-sabi": {
        "name": "style-wabi-sabi",
        "description": "日本物哀、侘寂与原白美学 Skill。探寻风化残缺、无釉粗陶、阴翳礼赞与极低照度素白，拒绝网红日系泛白滤镜。",
        "version": "1.0.0",
        "tags": ["wabi-sabi", "mono-no-aware", "japanese-aesthetics", "minimalism", "anti-homogenization"],
        "title": "日本物哀、侘寂与原白 (Wabi-Sabi, Mono no Aware & Shiroi)",
        "chapter": "第二篇第5章",
        "soul": [
            "**核心哲学**：物哀（对瞬息万物盛极必衰之悲悯）与侘寂（在简朴、粗粝、不对称、岁月斑驳风化中见不完美之美）。遵循原研哉“原白”的虚无容纳力与谷崎润一郎《阴翳礼赞》的暗处微光。",
            "**AI 常见同质化缺陷**：生成油光水滑的浅木色网红无印风民宿、过曝的惨白空气日系糖水片，失去千锤百炼的岁月包浆与苍凉阴翳之感。",
            "**本 Skill 矫正法则**：\n  1. **风化裂痕与物理残缺**：画面聚焦无釉粗陶器微孔(Unglazed pottery)、粗粝砂石、风化开裂的老木头与金缮(Kintsugi)修补痕迹。\n  2. **低照度阴翳幽暗**：让大面积画面沉浸在深沉温暖的幽暗中，光线仅作为暗处轻拂微物的显形介质。\n  3. **去中心极端空虚**：留出广袤未开垦的负空间，物体偏安一隅，流露无常飘零的叹息。"
        ],
        "palette": [
            "- 阴翳玄墨黑 (Shadow Inei Charcoal): `#1F1E1C` (深邃阴暗基底, 占50%)",
            "- 风化老木褐 (Weathered Cedar Brown): `#5A4D41` (主体残物与枯枝, 占30%)",
            "- 枯山水砂灰 (Karesansui Gravel Gray): `#8C877D` (砂石耙纹, 占15%)",
            "- 素白生麻米 (Shiroi Raw Linen): `#E8E6E1` (和纸与微光投射面, 占5%)"
        ],
        "materials": [
            "- 柴烧粗陶表面未打磨的气孔与微小裂纹 (Unglazed wood-fired stoneware with raw porous cracks)",
            "- 百年老杉木日晒雨淋后的灰白风化木纹 (Century-old weathered cedar wood with deep grain fractures)",
            "- 手工抄造楮皮和纸的粗纤维透光肌理 (Handmade kozo washi paper with uneven raw plant fibers)",
            "- 枯山水白砂细致耙梳的波纹波浪 (Raked granite white gravel in delicate meditation ripples)"
        ],
        "optics": [
            "- 晨昏穿过纸拉门 (Shoji) 的极度微弱柔和漫射天光 (Subtle ambient daylight filtered through paper screen)",
            "- 深沉无光泽的慢快门氛围，极深暗部中保留极高微观质感层次。",
            "- 严禁任何硬光直射与现代高饱和彩色滤镜。"
        ],
        "grid": [
            "- 留白率：≥70%，偏居一角（Bottom-corner or extreme asymmetric offset）。",
            "- 排版：极少文字，单列竖排无衬线或极细明朝体，如落叶轻飘在纸面边际。"
        ],
        "forbidden": [
            "NO glossy polished surfaces, NO bright overexposed sunny rooms",
            "NO modern plastic furniture, NO colorful floral arrangements",
            "NO high contrast pop gradients, NO flashy luxury gold foils",
            "NO perfectly symmetrical framing, NO crowded cluttered elements"
        ],
        "positive_prompt": "Masterpiece of Wabi-sabi and Mono no aware Japanese aesthetic, architectural still life. A single rustic cracked unglazed stoneware vase `#5A4D41` repaired with subtle gold lacquer kintsugi line, resting on an aged weathered charred cedar wood floor `#1F1E1C`. Behind it, a single dried wild grass stem casts a faint delicate shadow across a raw handmade washi screen `#E8E6E1`. Extreme low-light atmosphere, praising shadows in the manner of Jun'ichiro Tanizaki, deep quietude, poetic melancholy, exquisite tactile macro textures, 8k resolution, shot on medium format film.",
        "negative_prompt": "bright, overexposed, cheerful, glossy surfaces, neon, modern interior, colorful, symmetrical, crowded, plastic, studio light, vivid colors.",
        "typography": [
            "- **字体选择**：极细日照明朝体 (Mincho Light) 或 游明朝体，字号极小，字距开阔。",
            "- **排版原则**：单行竖排靠左下角，不设任何底色块与图标装饰。"
        ],
        "voice_match": "`voice-japanese-restraint`（日系日常节制絮语）或 `voice-proust`（微观心理通感）。"
    },
    "style-tropical-modernism": {
        "name": "style-tropical-modernism",
        "description": "拉美热带现代主义 Skill。以巴拉甘与尼迈耶的狂烈原色实墙、雕塑般混凝土曲面与热带光影为核心，驱散西欧玻璃盒子的冰冷沉闷。",
        "version": "1.0.0",
        "tags": ["tropical-modernism", "barragan", "niemeyer", "latin-architecture", "vibrant-color", "anti-homogenization"],
        "title": "拉美热带现代主义 (Latin American Tropical Modernism)",
        "chapter": "第二篇第6章",
        "soul": [
            "**核心哲学**：拒斥欧洲功能主义那种冰冷、苍白的玻璃盒子。认为建筑必须应对热带暴烈的日照与暴雨，唤醒阿兹特克、玛雅古文明对阳光与大地的敬畏，追求充满肉身激情的雕塑感与形而上学光影。",
            "**AI 常见同质化缺陷**：生成千篇一律的度假村棕榈树与千篇一律的泳池蓝水花，缺乏巴拉甘式的深邃形而上学沉思与纯粹大体量实墙。",
            "**本 Skill 矫正法则**：\n  1. **大体量纯色实墙 (Solid Monolithic Walls)**：绝无琐碎小窗格与繁杂金属框架，大块面的建筑高墙构成空间切割。\n  2. **高纯度烈日原色撞色**：采用墨西哥粉红、深钴蓝与铬黄的狂野撞色，在烈日下爆发极高能量。\n  3. **刀切般硬阴影与静止水镜**：暴烈正午阳光投射出边缘绝对锋利的深黑阴影，水面如黑色玄武岩般凝固倒映粉墙。"
        ],
        "palette": [
            "- 墨西哥狂艳粉 (Mexican Vibrant Pink): `#E03576` (主立面巨墙, 占40%)",
            "- 暴烈深钴蓝 (Deep Violent Cobalt Blue): `#1338BE` (对撞墙体与深远阴影面, 占25%)",
            "- 烈日铬黄 (Chrome Sun Yellow): `#FDB813` (光线折射面与端景, 占15%)",
            "- 玄武岩深冷灰 (Volcanic Basalt Ash): `#323232` (地面基座与石阶, 占20%)"
        ],
        "materials": [
            "- 传统手工抹灰粗拉毛水泥灰浆 (Rough hand-troweled stucco plaster with visible tactile ridges)",
            "- 墨西哥黑色火山玄武岩碎石与石阶 (Dark porous volcanic basalt stone pavers)",
            "- 镜面般完全静止的浅水池 (Pristine mirror-flat still water reflecting pure solid color)",
            "- 雕塑般高耸挺拔的独生巨大仙人掌 (Solitary giant saguaro and sculptural blue agave)"
        ],
        "optics": [
            "- 正午炽烈垂直顶光 (Intense harsh overhead midday tropical sunlight)",
            "- 投影边缘如剃刀般锋利分明的深邃几何黑色硬投影 (Razor-sharp brutalist geometric cast shadows)",
            "- 严禁任何雾化柔光、多云阴天漫射光或现代冷淡白光。"
        ],
        "grid": [
            "- 构图：巨幅单色几何色块对撞，横向与纵向实墙将画面切分成蒙德里安式的三维空间。",
            "- 留白：纯净无云的钴蓝天空作为天然色块，画面纯度极高。"
        ],
        "forbidden": [
            "NO modern European glass curtain wall skyscrapers, NO cluttered balconies",
            "NO desaturated muted filters, NO cloudy overcast flat lighting",
            "NO tourist beach umbrellas and deck chairs, NO soft pastel watercolor hues",
            "NO chaotic textures, NO fake plastic foliage"
        ],
        "positive_prompt": "Architectural photography of Luis Barragán inspired modernist courtyard in Mexico, massive high monolithic stucco walls painted in vibrant Mexican pink `#E03576` and deep cobalt blue `#1338BE`, a solitary giant sculptural saguaro cactus growing from black volcanic lava gravel `#323232`, pristine reflective still water pond creating sharp geometric reflections, intense brutal overhead tropical sunlight casting razor-sharp architectural shadows, pure blue clear sky, tactile rough plaster texture, 70mm architectural lens perspective, cinematic stillness.",
        "negative_prompt": "clouds, overcast light, soft shadows, glass skyscraper, European classical ornaments, muted pastel colors, grainy noise, cluttered interior, blurry details, tourists.",
        "typography": [
            "- **主标题**：几何无衬线大写英文字体（Futura Bold / Gotham），字符间距拉大，稳重厚实。",
            "- **排版原则**：文字紧贴画面边缘实墙色块对齐，保持建筑立面的纯粹几何感。"
        ],
        "voice_match": "`voice-wieden-kennedy`（存在主义生命意志）或 `voice-hemingway`（冰山极简电报体）。"
    },
    "style-islamic-geometric": {
        "name": "style-islamic-geometric",
        "description": "伊斯兰现代几何与当代书写 Skill。以八角星轮无尽自相似拓扑、镂空木屏风微气候光影与库法体现代涂鸦书写为核心，破除庸俗阿拉丁滤镜。",
        "version": "1.0.0",
        "tags": ["islamic-geometry", "mashrabiya", "kufic", "calligraffiti", "architecture", "anti-homogenization"],
        "title": "伊斯兰现代几何与当代书写 (Islamic Geometric Modernism & Calligraffiti)",
        "chapter": "第二篇第7章",
        "soul": [
            "**核心哲学**：因宗教严禁偶像崇拜，艺术家将对真主宇宙神圣秩序的崇敬，全部升华为无穷无尽的几何星轮数学演算法（Girih）与对阿拉伯书写文字造型极限的探索。让·努维尔阿布扎比卢浮宫“光雨”为其当代巅峰。",
            "**AI 常见同质化缺陷**：无脑生成好莱坞阿拉丁神灯式金色葱头顶城堡、廉价土豪金贴图、毫无数学拓扑逻辑的随意乱线花纹。",
            "**本 Skill 矫正法则**：\n  1. **严格数学自相似几何拓扑**：基于八角、十二角星轮与蔓藤花纹（Arabesque）的严密多中心对称算法延展，自成宇宙无限律动。\n  2. **微气候镂空屏风与光之雨**：通过传统 Mashrabiya 镂空构件，将沙漠酷烈日光切割为千万道射入幽暗室内的光柱（光之织造）。\n  3. **当代库法字体解构涂鸦**：融合古老庄严的方形库法体（Kufic）与当代街头 Calligraffiti 先锋狂放笔触。"
        ],
        "palette": [
            "- 绿松石青 (Turquoise Lapis Lazuli): `#00A896` (釉砖核心点缀, 占25%)",
            "- 殿堂真金箔 (Pure Gold Leaf Luster): `#E5A93B` (星轮细线与文字镶边, 占20%)",
            "- 深邃群青蓝 (Deep Ultramarine Cobalt): `#1A237E` (星空穹顶与深邃背景, 占35%)",
            "- 干燥石膏砂白 (Desert Gypsum Sand White): `#FAF8F5` (建筑石壁与镂空构件, 占20%)"
        ],
        "materials": [
            "- 摩洛哥手工切割彩色釉面拼接瓷砖 (Hand-cut glazed Moroccan Zellige mosaic tiles)",
            "- 精密激光切割氧化黄铜与青铜镂空屏风 (Precision laser-cut oxidized brass Mashrabiya screens)",
            "- 未打磨沙漠多孔石灰石大石块 (Unpolished desert porous limestone ashlar blocks)",
            "- 古老皮纸上纯黑苏丹墨与金粉干刷笔锋 (Black Sumi ink and dry brush gold leaf calligraphy strokes)"
        ],
        "optics": [
            "- 强烈日光射穿镂空遮阳顶盖，在地面与墙面投射出波澜壮阔的“几何光雨”（Rain of Light volumetric rays）。",
            "- 局部极高反差，光束在空气微尘中形成清晰的可见光柱。"
        ],
        "grid": [
            "- 构图：严格的多维中心辐射网格与等边自相似平铺，极度严谨对称，如曼陀罗般无限衍生。",
            "- 排版：外框采用多层嵌套几何边界，内部文字紧贴几何框架交织。"
        ],
        "forbidden": [
            "NO cartoon Aladdin fantasy castles, NO cheap Disney magic carpets",
            "NO chaotic messy patterns without geometric logic, NO Western baroque flourishes",
            "NO blurry gradients, NO neon cyberpunk colors, NO human idols or figurative statues"
        ],
        "positive_prompt": "Monumental contemporary Islamic geometric modernism architecture, inspired by Jean Nouvel and I.M. Pei. A grand soaring pavilion with intricate multi-layered octagonal star Mashrabiya latticework roof. Intense desert sunbeams pierce through the geometric metal canopy creating a dramatic 'Rain of Light' volumetric ray effect across unpolished pale limestone floors. Deep turquoise glazed tiles `#00A896` and subtle pure gold leaf inlays `#E5A93B` shimmering on pristine walls, infinite mathematical fractal precision, transcendent sacred tranquility, 8k resolution, architectural wide-angle lens.",
        "negative_prompt": "disney cartoon, aladdin castle, messy doodle, figurative portraits, statues, modern clutter, plastic textures, blurry lines, western rococo ornaments.",
        "typography": [
            "- **主标题**：当代重构几何方形库法体 (Square Kufic) 或锐利流线街头涂鸦书法 (Calligraffiti)。",
            "- **版面编排**：文字完全融入几何网格边框，形成图文无缝咬合的整体建筑感。"
        ],
        "voice_match": "`voice-neilfrench`（傲慢贵族长文）或 `voice-ogilvy-fact`（事实密集流）。"
    },
    "style-arts-crafts": {
        "name": "style-arts-crafts",
        "description": "工艺美术运动 Skill。传承威廉·莫里斯反工业异化哲学，以自然藤蔓交织、手工木雕版油墨印痕与厚材质朴美学，剔除现代数码塑料平铺感。",
        "version": "1.0.0",
        "tags": ["arts-and-crafts", "william-morris", "woodblock", "botanical", "textile-design", "anti-homogenization"],
        "title": "工艺美术运动 (Arts and Crafts Movement)",
        "chapter": "第三篇第8章",
        "soul": [
            "**核心哲学**：19世纪后半叶由约翰·拉斯金与威廉·莫里斯发起。尖锐批判工业革命对工人创造力的异化与流水线产品的粗制滥造，主张回归中世纪手工艺的诚实质朴，从大自然的藤蔓、果实与鸟兽中提取有机生命的交织秩序。",
            "**AI 常见同质化缺陷**：生成千篇一律的现代矢量平铺碎花布、毫无厚度的平滑塑料贴图、机械死板对称的壁纸纹理。",
            "**本 Skill 矫正法则**：\n  1. **手工梨木雕版套印痕迹 (Woodblock printing overlap)**：图案边缘呈现手工版画特有的木纹微缺损与油墨轻度渗透咬痕。\n  2. **繁复交织自然生态网络**：由莨苕叶（Acanthus）、野草莓、柳枝与穿梭其中的画眉鸟构筑紧密有机交缠网络，绝非简单单品平铺。\n  3. **诚实材料与手作温度**：强调厚重手工羊毛提花挂毯、未上光生橡木卯榫与自然矿植物提取色。"
        ],
        "palette": [
            "- 莫里斯深林暗绿 (Morris Forest Green): `#2D4739` (叶脉与主藤蔓背景, 占40%)",
            "- 茜草染料砖红 (Madder Brick Red): `#A63D40` (野草莓果实与花朵, 占25%)",
            "- 鼠尾草灰绿 (Sage Muted Green): `#849974` (次级花叶与卷须, 占20%)",
            "- 纯羊皮纸暖白 (Parchment Warm Cream): `#F3E8D2` (底纸与天然织线, 占15%)"
        ],
        "materials": [
            "- 厚重手工植物染色羊毛提花面料 (Heavy hand-woven vegetable-dyed wool Jacquard tapestry)",
            "- 手工雕刻梨木版多色油墨套印的天然棉布 (Woodblock printed natural unbleached cotton calico)",
            "- 粗颗粒古法手工造纸边缘微毛边 (Coarse handmade deckle-edge rag paper)",
            "- 英国老橡木与胡桃木纯手工雕花实木质感 (Hand-carved solid English oak with natural wax finish)"
        ],
        "optics": [
            "- 英国乡间19世纪大窗边斜照进来的自然漫射天光 (Natural diffused English countryside window daylight)",
            "- 完全无人工高光与现代塑料反光，呈现温润沉着的全哑光吸光质感。"
        ],
        "grid": [
            "- 构图：无限生长连续密铺式图案（All-over pattern），S形主干带动螺旋缠绕次枝蔓。",
            "- 排版：中世纪泥金手抄本排版格局，大首字装饰花体（Illuminated initial），双栏对称布局。"
        ],
        "forbidden": [
            "NO modern digital vector flat floral prints, NO shiny polyester ribbons",
            "NO 3D CGI plastic leaves, NO neon modern colors, NO cold metal glass elements",
            "NO stark sterile white backgrounds, NO repetitive copy-paste stamped look"
        ],
        "positive_prompt": "Authentic Arts and Crafts movement textile and woodblock print design in the style of William Morris, late 19th century. Dense interlocking tapestry pattern featuring deep green acanthus leaves `#2D4739`, tangled wild strawberry vines with ripe madder red berries `#A63D40`, and delicate thrush birds hiding in foliage. Hand-carved pearwood block printing texture with slight natural ink bleeding, muted natural botanical dyes, rough warm parchment cotton background `#F3E8D2`, exquisite organic rhythm, honest craftsmanship, museum archive quality.",
        "negative_prompt": "modern digital vector, seamless plastic wallpaper, 3d render, glossy reflections, neon bright colors, artificial gradient, photorealistic plastic, low quality flat.",
        "typography": [
            "- **主标题**：凯姆斯科特工坊风格中世纪哥特手抄字体（Golden Type / Troy Type），重笔画衬线。",
            "- **正文**：经典粗衬线卡斯隆体 (Caslon) 或 威尼斯老衬线体，搭配精美木刻首字花边。"
        ],
        "voice_match": "`voice-wangzengqi`（民间质朴风物）或 `voice-zhangailing`（世俗繁复工笔）。"
    },
    "style-art-nouveau": {
        "name": "style-art-nouveau",
        "description": "新艺术运动 Skill。以慕夏感性女性、鞭绳曲线、高迪有机熔融锻铁与拜占庭金色马赛克为核心，打破现代冷酷僵硬几何。",
        "version": "1.0.0",
        "tags": ["art-nouveau", "mucha", "gaudi", "whiplash-curve", "stained-glass", "anti-homogenization"],
        "title": "新艺术运动 (Art Nouveau / Jugendstil)",
        "chapter": "第三篇第9章",
        "soul": [
            "**核心哲学**：1890s-1910s 世纪之交以阿尔丰斯·慕夏、安东尼·高迪与埃克托尔·吉马尔为代表。痛恨古典主义的死板对称与工业革命的生硬机械，主张从植物茎蔓的生机勃勃中汲取灵感，用富有强烈弹性的“鞭绳曲线（Whiplash curve）”与拜占庭神性重塑世间万物。",
            "**AI 常见同质化缺陷**：生成迪士尼公主式现代CG芭比脸、油腻金色发丝糊成一团、劣质网游塑料花环。",
            "**本 Skill 矫正法则**：\n  1. **波状鞭绳曲线 (Whiplash dynamic line)**：所有线条均带有由慢变急、宛如抽鞭般收发自如的张力与弹性回弹。\n  2. **浅浮雕轮廓勾线与平涂填色**：遵循日本浮世绘影响下的黑褐利落外轮廓线，内部辅以精妙柔和的平涂色彩阶梯。\n  3. **拜占庭神性与有机材质**：融入金箔马赛克光晕、彩绘铅条镶嵌玻璃(Stained glass)与熔融态锻铁骨架。"
        ],
        "palette": [
            "- 孔雀石幽绿 (Malachite Peacock Green): `#1A535C` (叶蔓与深色衣褶, 占30%)",
            "- 拜占庭古神金 (Byzantine Antique Pale Gold): `#C5A059` (神性光晕与金属边线, 占25%)",
            "- 凋零玫瑰粉 (Faded Rose Petal Pink): `#DDA7A5` (花瓣与女性面颊微晕, 占20%)",
            "- 象牙暖乳白 (Ivory Warm Parchment): `#F8F4E9` (画布底色与肌肤留白, 占25%)"
        ],
        "materials": [
            "- 彩色含铅手工熔铸彩色玻璃与黑色焊铅线条 (Artisan stained glass with dark lead cames)",
            "- 巴黎地铁入口式如植物生长的青铜锻铁 (Fluid organic wrought iron with verdigris patina)",
            "- 珍珠母贝与蛋白石虹彩镶嵌片 (Iridescent mother-of-pearl and fire opal inlays)",
            "- 细密古法石版彩色印刷纸面颗粒 (Antique multi-stone color chromolithograph paper texture)"
        ],
        "optics": [
            "- 黄金时代的落日熔金侧光，透过彩色玻璃滤下斑斓流动的圣洁色光。",
            "- 人物面部保持温润扁平的平光感，依靠线条自身起伏呈现立体，严禁现代硬核阴影。"
        ],
        "grid": [
            "- 构图：上方为半圆形或马蹄拱形神龛画框（Halo arch），人物发丝与衣带向两侧向下如波浪瀑布般倾泻。",
            "- 装饰框：层层嵌套的百合花、鸢尾花或孔雀羽毛交织缠绕边框。"
        ],
        "forbidden": [
            "NO modern 3D CGI glossy dolls, NO anime faces, NO stiff straight geometric grids",
            "NO neon lights, NO harsh photorealistic lens flare, NO plastic glossy materials",
            "NO symmetrical industrial boxes, NO messy digital paint splatters"
        ],
        "positive_prompt": "Masterpiece Art Nouveau decorative poster in the definitive style of Alphonse Mucha, 1900. An ethereal divine muse with cascading long wavy hair intertwined with blooming pale pink water lilies `#DDA7A5` and winding malachite green vines `#1A535C`. Majestic circular Byzantine halo arch behind her head detailed with antique gold leaf mosaic tiles `#C5A059`. Elegant flowing whiplash curves, bold calligraphic dark outlines, flat color lithographic print texture on warm ivory paper `#F8F4E9`, exquisite sensual organic rhythm, Paris Belle Époque exhibition grade.",
        "negative_prompt": "photorealistic 3d render, anime style, modern barbie face, shiny plastic, neon cyberpunk, stiff straight lines, heavy drop shadows, low quality flat.",
        "typography": [
            "- **主标题**：新艺术运动定制流动花体（如 Eckmann-Schrift / Arnold Böcklin），笔画末端如植物卷须微翘。",
            "- **排版原则**：文字顺应拱门或波浪边框呈弧形排列，与插画融为一体。"
        ],
        "voice_match": "`voice-lixinpian`（感官避难所）或 `voice-zhangailing`（繁复工笔苍凉）。"
    },
    "style-constructivism": {
        "name": "style-constructivism",
        "description": "构成主义与风格派 Skill。以利西茨基与蒙德里安的生产主义、纯粹三原色、尖锐对角线力场与工业照相蒙太奇为灵魂，消灭资产阶级矫饰插画。",
        "version": "1.0.0",
        "tags": ["constructivism", "de-stijl", "lissitzky", "mondrian", "avant-garde", "anti-homogenization"],
        "title": "构成主义与风格派 (Constructivism & De Stijl)",
        "chapter": "第三篇第10章",
        "soul": [
            "**核心哲学**：1910s-1930s 俄国十月革命先锋艺术家（利西茨基、罗德琴科、塔特林）与荷兰风格派（蒙德里安、杜斯堡）。宣告纯艺术的死亡，主张设计是社会的“构建工程”（Production Art），以最极限的几何原形、纯粹三原色与对角线力场唤醒工业集体意志。",
            "**AI 常见同质化缺陷**：生成杂乱无章的现代抽象涂鸦色块、带有柔化光影与软圆角、缺乏革命机器般的冷酷工业咬合力。",
            "**本 Skill 矫正法则**：\n  1. **尖锐对角线动力场 (Dynamic diagonal thrust)**：以 30° 或 45° 的巨大红色楔子或几何斜线劈开画面，撕裂静态平衡。\n  2. **绝对纯粹的原色与非色彩**：仅允许纯红、纯黄、纯蓝配合纯黑与白，严禁中间过渡灰阶或渐变。\n  3. **工业照相蒙太奇 (Photomontage)**：高反差黑白工人摄影剪影、工业机床齿轮与粗黑排版实色块硬核穿插拼贴。"
        ],
        "palette": [
            "- 革命先锋烈红 (Vanguard Crimson Red): `#DE2B2B` (对角线楔子与核心标语, 占35%)",
            "- 机械冷轧黑 (Mechanical Cold Rolled Black): `#1B1B1B` (实色结构梁与黑白照片剪影, 占35%)",
            "- 风格派纯原黄 (De Stijl Primary Yellow): `#FFD700` (点缀平衡色块, 占10%)",
            "- 苏联新闻纸砂白 (Soviet Newsprint Off-White): `#F4F4F0` (底纸与负空间切割, 占20%)"
        ],
        "materials": [
            "- 粗糙苏联早期新闻纸与牛皮卡纸纤维 (Coarse Soviet newsprint and raw unbleached cardstock)",
            "- 高反差黑白摄影冲印银盐粗颗粒 (High-contrast coarse grain black and white photomontage silver gelatin)",
            "- 哑光广告平涂水粉油墨边缘硬切面 (Matte flat gouache ink with razor-sharp masked edges)",
            "- 未经油漆涂装的粗钢铁梁与工程螺栓 (Unpainted structural raw black steel beams and bolts)"
        ],
        "optics": [
            "- 绝对平光的二维平面图示与极高反差黑白摄影直出拼贴。",
            "- 彻底剔除三维真实光影、球体渐变球与假高光。"
        ],
        "grid": [
            "- 构图：第三国际纪念塔螺旋式对角线力矩构图，彻底打破水平垂直基线。",
            "- 排版：超大字号实心无衬线字母沿斜线排列，与粗黑分割线、红色三角几何重叠锁定。"
        ],
        "forbidden": [
            "NO soft gradients, NO blurry shadows, NO delicate cursive handwriting",
            "NO floral ornaments, NO sweet pastel colors, NO glossy 3d glass balls",
            "NO centered bourgeois salon composition, NO nostalgic vintage sepia filters"
        ],
        "positive_prompt": "Russian Constructivism and De Stijl avant-garde graphic design poster, inspired by El Lissitzky and Alexander Rodchenko, 1920. Dynamic diagonal composition with a colossal sharp red wedge `#DE2B2B` penetrating a black sphere and structural mechanical grid `#1B1B1B`. High-contrast black and white cut-out photomontage of industrial steel turbine machinery and worker silhouette. Bold stark Cyrillic-inspired typography, pure primary yellow square accent `#FFD700`, aged off-white newsprint paper texture `#F4F4F0`, supreme revolutionary tension, raw geometrical power, historical masterpiece.",
        "negative_prompt": "soft watercolor, modern corporate gradient, soft shadows, 3d glossy render, cute, pastel colors, cursive script, messy splatters, symmetrical classical layout.",
        "typography": [
            "- **标题字体**：极限加粗实心苏式无衬线几何体（如 Rodchenko Grotesk）、重磅工业黑体。",
            "- **排版原则**：文字顺应斜线旋转，字高超长，字距紧锁，字行穿插红色粗实线。"
        ],
        "voice_match": "`voice-luxun`（匕首讽喻硬骨）或 `voice-wieden-kennedy`（存在主义抗争史诗）。"
    },
    "style-bauhaus": {
        "name": "style-bauhaus",
        "description": "包豪斯与功能主义体系 Skill。以“形式追随功能”、无缝镀铬钢管、纯粹几何三原色与严密无衬线字体为准则，杜绝一切非理性浮华装饰。",
        "version": "1.0.0",
        "tags": ["bauhaus", "functionalism", "gropius", "minimalism", "industrial-design", "anti-homogenization"],
        "title": "包豪斯与功能主义体系 (Bauhaus & Functionalism)",
        "chapter": "第三篇第11章",
        "soul": [
            "**核心哲学**：1919-1933 德国包豪斯（格罗佩斯、密斯·凡德罗、拜耶、莫霍利-纳吉）。确立“形式追随功能（Form follows function）”与“艺术与技术的新统一”。主张清除一切无意义的历史复古装饰，以机械化大生产为前提，让材料的真实物理属性与数学纯粹几何直接说话。",
            "**AI 常见同质化缺陷**：随意堆砌红黄蓝浮雕三维球体、滥用圆滑阴影、把理性功能主义误解为儿童积木玩具。",
            "**本 Skill 矫正法则**：\n  1. **理性极简工业构件**：画面必须包含严谨的无缝冷弯镀铬钢管（Tubular steel）、压铸黑色电木或平滑工业平板玻璃。\n  2. **原色几何构成法**：严格限制使用红黄蓝三原色与黑白灰，形体仅采用纯正圆、正方、正三角。\n  3. **绝对无衬线信息层级**：取消所有大写字母层级（拜耶“单一世界体”理念），以绝对线性的横纵坐标构建功能清晰的信息界面。"
        ],
        "palette": [
            "- 包豪斯正红 (Bauhaus Primary Red): `#DE3831` (强调色块与核心几何原形, 占15%)",
            "- 乌尔姆理性蓝 (Rational Bauhaus Blue): `#0055A5` (结构平衡色块, 占15%)",
            "- 工业指示黄 (Industrial Primary Yellow): `#FFCC00` (微量导视点睛, 占10%)",
            "- 冷轧镀铬银黑 (Tubular Chrome & Carbon Black): `#111111` (金属管线与主要文字, 占30%)",
            "- 德绍校舍白 (Dessau Plaster White): `#F5F5F3` (主墙面与留白空间, 占30%)"
        ],
        "materials": [
            "- 冷弯无缝冷轧镀铬钢管镜面微光 (Cold-bent seamless tubular chrome steel with crisp mirror highlights)",
            "- 压铸黑色胶木与哑光实木原漆 (Molded black Bakelite and smooth lacquered solid beech wood)",
            "- 纯平工业建筑玻璃与极窄黑铁窗框 (Architectural clear plate glass and slim black steel window sash)",
            "- 哑光无涂布德绍印刷卡纸原色 (Matte uncoated German archival paper cardstock)"
        ],
        "optics": [
            "- 德绍校舍北向落地玻璃幕墙射入的中性清澈天光 (Neutral clean daylight from Bauhaus north-facing glass curtain wall)",
            "- 清晰而收敛的物理硬投影，绝无柔化晕染与浮夸漫反射光晕。"
        ],
        "grid": [
            "- 构图：严格遵循垂直与水平正交网格（Orthogonal Grid），偶有严谨的45度角功能线引入。",
            "- 排版：非对称平衡（Asymmetrical typography），大字号纯小写无衬线文字与色块紧密咬合。"
        ],
        "forbidden": [
            "NO decorative floral patterns, NO baroque carvings, NO classical capitals",
            "NO serif historical fonts, NO blurred pastel colors, NO skeuomorphic glossy bubbles",
            "NO messy chaotic brush strokes, NO frivolous luxury embellishments"
        ],
        "positive_prompt": "Authentic Bauhaus functionalist design exhibition poster and architectural composition, Dessau 1926 style, inspired by Walter Gropius and Herbert Bayer. Pure geometric harmony featuring a cantilevered tubular chrome steel chair `#111111`, framed by solid flat color blocks of primary red `#DE3831` and rational blue `#0055A5`. Clean orthogonal architectural grid, clear industrial plate glass window casting precise geometric shadows on pale plaster wall `#F5F5F3`. Pure sans-serif lowercase typography arranged flush-left, matte uncoated paper texture, ultimate industrial clarity, iconic modernist masterpiece.",
        "negative_prompt": "ornamental flourishes, rococo, serif font, blurred gradient, 3d glossy spheres, soft brush strokes, nostalgic vintage dirty textures, cluttered composition.",
        "typography": [
            "- **排版字体**：Herbert Bayer 纯几何小写 Universal 体、Futura Medium、Akzidenz-Grotesk。",
            "- **编排原则**：坚决左对齐，强制字号跳跃（如 72pt 与 10pt 的直接对撞），消灭修饰线条。"
        ],
        "voice_match": "`voice-jobs-clarity`（激进清澈体）或 `voice-ogilvy-fact`（事实密集流）。"
    },
    "style-art-deco": {
        "name": "style-art-deco",
        "description": "装饰艺术风格 Skill。汲取爵士时代机器奢华、克莱斯勒大厦阶梯金字塔、放射太阳芒与金属拉丝对称，破除俗气婚礼请帖贴片感。",
        "version": "1.0.0",
        "tags": ["art-deco", "roaring-twenties", "chrysler-building", "luxury", "geometric-elegance", "anti-homogenization"],
        "title": "装饰艺术风格 (Art Deco)",
        "chapter": "第三篇第12章",
        "soul": [
            "**核心哲学**：1920s-1940s 爵士时代（Roaring Twenties）对机器时代速度、摩天大楼与古典奢华的交响颂歌。从古埃及图坦卡蒙墓金字塔折线、阿兹特克阶梯神庙汲取几何灵感，结合远洋邮轮流线型与闪烁金属，宣告工业时代属于摩登贵族的昂贵浪漫。",
            "**AI 常见同质化缺陷**：生成俗不可耐的廉价金色线条相框、俗套现代婚庆请帖背景、线条杂乱毫无机械力量感。",
            "**本 Skill 矫正法则**：\n  1. **阶梯退台与太阳光芒 (Ziggurat & Sunburst)**：严格运用金字塔阶梯式向上收分线、放射状机械太阳芒与对称折线。\n  2. **高对比冷冽贵金属质感**：以黑曜石纯黑、深墨绿为坚实基底，拉丝黄铜金与飞艇冷银形成利落高光边缘。\n  3. **流线型对称仪轨 (Streamlined Symmetry)**：遵循中央垂直对称轴，形如远洋客轮船头与克莱斯勒大厦塔尖，充满速度与威严。"
        ],
        "palette": [
            "- 帝国拉丝金 (Chrysler Brushed Gold): `#D4AF37` (主几何金属构架与流线, 占35%)",
            "- 黑曜石深渊黑 (Obsidian Onyx Black): `#0D0D0D` (背景基底与高反差实色面, 占45%)",
            "- 盖茨比祖母绿 (Gatsby Emerald Green): `#095240` (奢华天鹅绒与釉面点缀, 占15%)",
            "- 飞艇镀铬冷银 (Airship Chrome Silver): `#C0C0C0` (边缘锐利反光微雕, 占5%)"
        ],
        "materials": [
            "- 高级拉丝黄铜与精密机械刻线金属板 (Brushed satin brass and precision machined bronze panels)",
            "- 高度抛光黑色大理石与黑曜石深邃镜面 (Polished black Marquina marble with fine white veining)",
            "- 几何拼花热带黑檀木与红木嵌木贴皮 (Geometric marquetry exotic ebony wood veneer)",
            "- 爵士时代磨砂几何浮雕玻璃 (Frosted geometric molded Lalique crystal glass)"
        ],
        "optics": [
            "- 剧院式戏剧化聚光灯 (Theatrical focused beam spotlighting) 勾勒金属锋利切角边缘。",
            "- 沉郁夜景背景中金属与黑曜石的高反差光泽，严禁平庸无层次的日间平光。"
        ],
        "grid": [
            "- 构图：严格的垂直中轴完全对称（Axial Symmetry），自下而上层层收窄的梯形阶梯结构。",
            "- 边框：多层嵌套的几何折角包边框（Stepped Corner Borders）。"
        ],
        "forbidden": [
            "NO cheap glitter sparkles, NO messy hand-drawn scribbles, NO rustic country wood",
            "NO soft cute anime themes, NO casual asymmetrical grunge layouts",
            "NO plastic modern materials, NO dull desaturated flat colors"
        ],
        "positive_prompt": "Definitive 1930s Art Deco luxury masterpiece poster, inspired by Cassandre and the Chrysler Building crown. Heroic vertical symmetrical composition featuring streamlined geometric stepped ziggurat tower and radiating sunburst rays in brushed solid brass `#D4AF37` against a deep obsidian black marble backdrop `#0D0D0D`. Rich emerald green velvet accents `#095240`, crisp metallic silver highlights `#C0C0C0`. Razor-sharp chamfered corners, polished luxury materials, dramatic theatrical lighting, Gatsby-era opulent grandeur, flawless museum exhibition print.",
        "negative_prompt": "cheap wedding template, messy lines, cartoon, blurry, low resolution, rustic vintage dirt, modern flat design, cute illustration, casual doodle.",
        "typography": [
            "- **主标题**：经典的 Art Deco 定制大写字体（如 Bifur / Peignot / Broadway），双线重叠、高腰线特征。",
            "- **排版原则**：全大写排版，居中轴线对称，字母间距大幅扩张（tracking +200）。"
        ],
        "voice_match": "`voice-neilfrench`（傲慢贵族长文）或 `voice-xushunying`（消费符号学）。"
    },
    "style-midcentury-modern": {
        "name": "style-midcentury-modern",
        "description": "中世纪现代主义 (MCM) Skill。以战后原子时代乐观主义、伊姆斯热压曲木、芥末黄橄榄绿调色盘与室内外交融为核心，破除廉价现代北欧塑料感。",
        "version": "1.0.0",
        "tags": ["mid-century-modern", "mcm", "eames", "atomic-age", "interior-design", "anti-homogenization"],
        "title": "中世纪现代主义 (Mid-Century Modern, MCM)",
        "chapter": "第三篇第14章",
        "soul": [
            "**核心哲学**：1940s-1960s 战后原子时代乐观主义（伊姆斯夫妇、埃罗·沙里宁、野口勇、保罗·兰德）。坚信科技能带来民主化的优雅生活。以热压模塑胶合板（Molded plywood）的人机工学曲面打破硬直冰冷，让大面积落地玻璃窗将加州暖阳与室外绿意无缝引纳室内。",
            "**AI 常见同质化缺陷**：生成廉价出租屋式的现代“假北欧宜家风”、泛白塑料家具、毫无岁月温润感与原子时代特定造型趣味。",
            "**本 Skill 矫正法则**：\n  1. **热压曲木与锥形细椅腿**：画面必须呈现伊姆斯躺椅式优雅的胡桃木模压曲面，配以黄铜套靴的细锥形椅腿（Peg legs）。\n  2. **战后特调有机大地色盘**：限定芥末黄、复古牛油果绿、焦糖陶土橙与深核桃木色，浓郁而温润。\n  3. **原子时代几何图腾 (Atomic Age motifs)**：融入野口勇式回旋镖曲线、几何腰子形茶几与放射状星芒原子钟。"
        ],
        "palette": [
            "- 棕榈泉芥末黄 (Palm Springs Mustard Ochre): `#D4A373` (核心织物与色块, 占30%)",
            "- 战后牛油果绿 (Atomic Avocado Olive): `#606C38` (绿植与软包, 占25%)",
            "- 焦糖陶土橙 (Caramel Terracotta Orange): `#BC6C25` (抱枕与点缀色块, 占15%)",
            "- 油饰黑胡桃木褐 (Oiled Walnut Dark Brown): `#3D2619` (曲木家具结构框架, 占30%)"
        ],
        "materials": [
            "- 七层热压成型黑胡桃木模塑胶合板 (Hot-pressed 7-ply molded black walnut plywood)",
            "- 粗花呢羊毛人字纹混纺软包面料 (Coarse woolen tweed herringbone upholstery fabric)",
            "- 落地通透钢框落地玻璃窗与裸露红砖壁炉 (Steel-framed floor-to-ceiling glass and exposed textured red brick)",
            "- 哑光黑色粉末涂层金属管与细黄铜椅靴 (Matte black powder-coated steel wire and brass ferrules)"
        ],
        "optics": [
            "- 加州午后4点穿透整面落地玻璃窗的金色斜阳 (Golden afternoon 4 PM California sunlight pouring through glass wall)",
            "- 室内温暖、明亮而舒适的漫射光，在木质曲面上呈现柔滑的高光反射。"
        ],
        "grid": [
            "- 构图：水平延展的开阔通透格局（Open-plan flow），家具呈现轻盈的漂浮悬挑感。",
            "- 平面排版：保罗·兰德式趣味不对称几何贴片，大色块与俏皮抽象图形相互制衡。"
        ],
        "forbidden": [
            "NO cheap contemporary white plastic furniture, NO cold chrome office cubicles",
            "NO heavy Victorian velvet curtains, NO dark gloomy gothic rooms",
            "NO sterile modern grey minimalism, NO kitschy neon lighting"
        ],
        "positive_prompt": "Mid-Century Modern architectural interior photography, Palm Springs 1958 villa inspired by Richard Neutra and Charles Eames. An iconic molded walnut plywood lounge chair `#3D2619` with black leather upholstery, resting on a coarse mustard yellow wool rug `#D4A373`. Floor-to-ceiling glass wall revealing lush outdoor tropical monsteras and avocado olive garden `#606C38`. Exposed brick fireplace, walnut kidney-shaped coffee table, golden warm late-afternoon sunlight casting long geometric window frame shadows, impeccable vintage warmth, 8k resolution, architectural magazine cover.",
        "negative_prompt": "cheap modern furniture, ikea plastic look, cold grey corporate, gothic darkness, victorian clutter, modern led strip lights, blurry textures, messy room.",
        "typography": [
            "- **主标题**：保罗·兰德式现代趣味字体（如 Cooper Black / Clarendon / Futura Bold）。",
            "- **正文排版**：中等字重无衬线体，搭配纯色有机腰子形底色块。"
        ],
        "voice_match": "`voice-wangzengqi`（民间日常白描）或 `voice-jobs-clarity`（激进清澈体）。"
    },
    "style-pop-psychedelic": {
        "name": "style-pop-psychedelic",
        "description": "波普与迷幻艺术 Skill。以安迪·沃霍尔大众消费品崇拜、本戴点网印、荧光撞色与迷幻熔岩融化字体为核心，破除无脑现代渐变彩色图。",
        "version": "1.0.0",
        "tags": ["pop-art", "psychedelic", "warhol", "lichtenstein", "screen-print", "anti-homogenization"],
        "title": "波普与迷幻艺术 (Pop Art & Psychedelic)",
        "chapter": "第三篇第15章",
        "soul": [
            "**核心哲学**：1960s-1970s 安迪·沃霍尔、罗伊·利希滕斯坦与旧金山摇滚海报教父韦斯·威尔逊（Wes Wilson）。消解精英艺术与大众消费品的森严壁垒，将罐头、可乐、漫画与摇滚乐推上神坛。通过丝网印刷的机械复制错版与视网膜高频荧光撞色，释放反叛狂欢。",
            "**AI 常见同质化缺陷**：生成毫无机械感的手绘彩色乱涂、平滑现代数码平滑渐变，缺少丝网印刷特有的网点粗糙感与油墨错位漏印。",
            "**本 Skill 矫正法则**：\n  1. **利希滕斯坦本戴点 (Ben-Day dots)**：阴影与中间调完全由机械排列的均匀圆点阵列构成。\n  2. **丝网印刷错位重影 (Misregistration)**：油墨色块边缘出现轻微套印不准的偏移错位，流露工业批量印制的粗粝机械魅力。\n  3. **荧光强撞色与熔岩字体 (Melting lava lettering)**：电光粉、酸性黄与天青色的高频对冲，文字如流动融化的岩浆紧密填满缝隙。"
        ],
        "palette": [
            "- 沃霍尔荧光粉 (Warhol Shocking Hot Pink): `#FF007F` (高能背景与冲击色块, 占35%)",
            "- 漫画电光柠檬黄 (Comic Electric Lemon Yellow): `#FFF01F` (高光与文字主体, 占30%)",
            "- 利希滕斯坦纯青 (Lichtenstein Vivid Cyan): `#00D2FF` (阴影与对比网点, 占25%)",
            "- 丝网印刷重墨黑 (Screenprint Carbon Ink Black): `#050505` (粗重外轮廓与网点, 占10%)"
        ],
        "materials": [
            "- 粗网目丝网油墨印刷平涂覆盖 (Coarse mesh silkscreen flat ink with subtle pinhole imperfections)",
            "- 廉价彩色漫画新闻纸上的粗糙本戴点阵 (Pulp comic book newsprint paper with visible mechanical dot matrix)",
            "- 波普时代充气乙烯基PVC塑料光泽 (Inflatable high-gloss PVC vinyl plastic reflections)",
            "- 摇滚音乐节荧光颜料在黑光灯下的发光质地 (Fluorescent day-glo pigment paper poster finish)"
        ],
        "optics": [
            "- 极高强度的平光无影商业闪光灯直射 (Flat high-intensity paparazzi strobe flash illumination)。",
            "- 色彩饱和度直冲视网膜极限，彻底消灭细腻灰调与柔和阴影过渡。"
        ],
        "grid": [
            "- 构图：4格或9格等分网格序列重复（Warholian grid matrix），或向心旋转的迷幻同心圆波浪排布。",
            "- 排版：反重力膨胀，文字形同流体填满一切负空间。"
        ],
        "forbidden": [
            "NO quiet muted earthy tones, NO soft pastel watercolor blends",
            "NO realistic classical oil painting rendering, NO gothic dark gloom",
            "NO sleek minimalist white spaces, NO dull corporate blue grids"
        ],
        "positive_prompt": "Classic 1960s Pop Art and psychedelic concert poster aesthetic, in the combined style of Andy Warhol and Roy Lichtenstein. Giant bold consumer icon presented in a 4-panel silkscreen grid with vibrant colorway variations: shocking hot pink `#FF007F`, electric lemon yellow `#FFF01F`, and vivid cyan `#00D2FF`. Prominent coarse mechanical Ben-Day dot shading patterns, deliberate slight screen-printing ink registration misalignment, heavy solid black ink outlines `#050505`. High saturation, flat strobe light illumination, vintage comic book newsprint paper texture, electrifying counterculture pop masterpiece.",
        "negative_prompt": "muted colors, soft watercolor gradient, realistic classical painting, 3d render, dark moody lighting, minimalist beige, dull grey, blurry details.",
        "typography": [
            "- **主标题**：迷幻融化流动字体（Psychedelic Art Nouveau lettering）、波普加粗肥皂泡泡体。",
            "- **编排原则**：字体重叠膨胀，字母内部填充本戴点或反差荧光色。"
        ],
        "voice_match": "`voice-xushunying`（消费符号学）或 `voice-yemaozhong`（冲突认知穿透体）。"
    },
    "style-brutalist": {
        "name": "style-brutalist",
        "description": "粗野主义与反设计 Skill。以柯布西耶原始清水混凝土(Béton Brut)、未打磨重工业骨架、反美学单宽等宽代码排版为灵魂，消灭虚伪精致的资产阶级滤镜。",
        "version": "1.0.0",
        "tags": ["brutalism", "anti-design", "raw-concrete", "monospace", "le-corbusier", "anti-homogenization"],
        "title": "粗野主义与反设计 (Brutalism & Anti-Design)",
        "chapter": "第三篇第16章",
        "soul": [
            "**核心哲学**：二战后柯布西耶在马赛公寓提出“Béton Brut（原始粗糙混凝土）”，延续至伦敦巴比肯中心。拒绝资产阶级虚伪轻佻的粉刷精修，让建筑的承重骨架、脱模木纹与管道裸露于世。数字时代演化为反设计（Anti-Design）：用未修饰的单宽字体与粗暴色块撕碎过度包装的商业UI。",
            "**AI 常见同质化缺陷**：生成打磨精致光洁的“网红灰色咖啡馆水泥墙”、加上温馨柔光绿植过度修饰，彻底丧失粗野主义震撼的巨碑压迫感与原始攻击性。",
            "**本 Skill 矫正法则**：\n  1. **原始木模板清水混凝土 (Raw board-marked concrete)**：表面清晰可见杉木模板拼缝、木纹反印、气孔蜂窝与粗粝砂石沉淀。\n  2. **巨碑式悬挑几何体量 (Monolithic Cantilever)**：粗重的几何混凝土块体违抗视觉习惯，形成沉重而威严的压迫感。\n  3. **数字反排版度规**：单宽打字机字体（Monospace）、超粗1px/2px纯黑边框、坚决不设渐变阴影与圆角。"
        ],
        "palette": [
            "- 原始木模水泥灰 (Raw Board Concrete Gray): `#7A8288` (主体立面与粗糙表面, 占55%)",
            "- 暴露型钢深炭灰 (Exposed Structural Steel Ash): `#3F4347` (阴影与沉重基座, 占30%)",
            "- 工地警示强酸黄 (Construction Warning Yellow): `#FFCC00` (高反差警告色块, 占10%)",
            "- 原始终端纯白 (Raw Terminal White): `#FFFFFF` (极简等宽文本与标识, 占5%)"
        ],
        "materials": [
            "- 粗糙松木木模板翻打的清水混凝土气孔接缝 (Rough board-formed poured concrete with raw seams and honeycombing)",
            "- 未经防锈精抛的重型冷轧工字钢梁 (Unfinished hot-rolled structural steel I-beams with raw mill scale)",
            "- 无涂层粗糙石棉水泥板与粗砂抹面 (Raw textured fibrous cement board and roughcast aggregate)",
            "- 数字端：原生未加样式的标准 HTML 元素质感 (Unstyled default browser aesthetics and raw code tables)"
        ],
        "optics": [
            "- 阴冷浓郁的北欧工业阴天平光 (Cold overcast overcast industrial sky skylight)，绝对杜绝浪漫夕阳与暖调柔光。",
            "- 几何悬挑在建筑立面上投下深重硬朗的冷灰色深阴影。"
        ],
        "grid": [
            "- 构图：重体量巨碑式倾斜与悬挑（Monumental Cantilever Mass），打破常规轻盈感。",
            "- 平面排版：极端密集的网格系统，文字满格铺排到底，粗黑实线表格互相穿插。"
        ],
        "forbidden": [
            "NO smooth polished boutique cafe plaster, NO cute houseplants and cozy rugs",
            "NO warm romantic golden sunset light, NO soft round corners and drop shadows",
            "NO cursive scripts, NO luxury gold trims, NO clean corporate glass facades"
        ],
        "positive_prompt": "Monumental Brutalist architecture and raw anti-design poster concept, inspired by Le Corbusier's Béton Brut and the Barbican estate. Colossal cantilevered concrete monolithic towers `#7A8288` with highly detailed rough board-marked timber grain textures and deep casting seams. Dramatic overcast cold grey sky, stark heavy geometric shadows. Bold functionalist graphic overlay with warning yellow stripes `#FFCC00` and stark white monospace technical typography `#FFFFFF`. Raw unpolished power, honest architectural materiality, 8k resolution, captured on Hasselblad wide-angle lens.",
        "negative_prompt": "polished luxury interior, cozy cafe, soft shadows, warm sunset, golden light, cute flowers, rounded corners, corporate smooth gradient, blurry textures, weak structure.",
        "typography": [
            "- **排版字体**：Courier New / OCR-A / Space Mono 等宽字体、或重磅未打磨无衬线黑体。",
            "- **排版原则**：全大写，带实黑边框的表格线切割，杜绝任何对齐补偿与优美圆角。"
        ],
        "voice_match": "`voice-luxun`（冷峻匕首体）或 `voice-neilfrench`（傲慢冷酷长文）。"
    },
    "style-memphis": {
        "name": "style-memphis",
        "description": "后现代主义与孟菲斯风格 Skill。以“少就是无聊 (Less is a bore)”、塑料水磨石、黑色波浪线、糖果撞色拼贴为灵魂，解构严肃包豪斯的冰冷刻板。",
        "version": "1.0.0",
        "tags": ["memphis", "postmodernism", "sottsass", "1980s", "radical-design", "anti-homogenization"],
        "title": "后现代主义与孟菲斯风格 (Postmodernism & Memphis Group)",
        "chapter": "第三篇第17章",
        "soul": [
            "**核心哲学**：1981年意大利米兰埃托·索特萨斯（Ettore Sottsass）成立孟菲斯集团，打出“Less is a bore（少就是无聊）”旗号。反叛现代主义包豪斯长达半个世纪的严肃、理性与功能教条。以廉价的塑料层压板、五彩水磨石、波浪纹与戏谑几何，宣告后现代大众狂欢与设计自由。",
            "**AI 常见同质化缺陷**：生成杂乱无章的幼儿园儿童涂鸦插画、平滑现代渐变色块、丧失80年代孟菲斯特定的大师级积木结构与质感对比。",
            "**本 Skill 矫正法则**：\n  1. **索特萨斯经典纹样 (Bacterio & Terrazzo)**：必须引入黑色微型细菌状波浪短线纹理（Bacterio pattern）与彩色树脂碎片水磨石。\n  2. **戏谑非理性几何积木拼装**：圆柱体、纯黄三角锥、斑马斜条纹与波浪曲线的大胆悬浮咬合，违抗传统重力逻辑。\n  3. **高饱和波普糖果撞色**：柠檬黄、珊瑚粉、绿松石蓝与电光紫的高烈度并置，边缘锐利无渐变。"
        ],
        "palette": [
            "- 孟菲斯柠檬黄 (Memphis Radical Lemon Yellow): `#FFE800` (几何构件与背景重点, 占30%)",
            "- 戏谑珊瑚粉 (Cheeky Coral Pop Pink): `#FF6F7D` (圆柱与波浪板, 占25%)",
            "- 绿松石薄荷蓝 (Turquoise Mint Cyan): `#4DEEEA` (平衡基座色块, 占20%)",
            "- 细菌斑马黑白 (Bacterio Zebra Black & White): `#000000/#FFFFFF` (波浪条纹与水磨石底纹, 占25%)"
        ],
        "materials": [
            "- 印有索特萨斯细菌纹的哑光塑料层压板 (Matte plastic laminate with custom Sottsass Bacterio squiggles)",
            "- 彩色大理石与玻璃碎块人造水磨石板 (Polished terrazzo composite with bright pastel aggregate chips)",
            "- 亮光烤漆弯曲金属圆管与彩色积木实木 (Glossy lacquered bent steel tubing and painted wooden geometric solids)",
            "- 80年代无光泽印刷涂料实色印刷面 (Solid screen-printed silkscreen ink blocks)"
        ],
        "optics": [
            "- 1980年代商业摄影棚无影高调摄影 (High-key 1980s studio strobe lighting)，无环境暗部，色彩极致纯粹明艳。",
            "- 几何阴影短小干脆，带有玩具般的戏剧性趣味。"
        ],
        "grid": [
            "- 构图：几何碎片倾斜拼贴（Dynamic Postmodern Collage），斜向30度悬浮，打破水平垂直基准线。",
            "- 排版：波浪线条自由穿插于标题与几何块之间，反规则跳跃式排版。"
        ],
        "forbidden": [
            "NO sterile grey corporate minimalism, NO traditional wood antique carvings",
            "NO soft romantic floral gradients, NO rustic distressed textures",
            "NO dark gloomy noir shadows, NO serious functionalist grid conformity"
        ],
        "positive_prompt": "Iconic Memphis Group postmodern design masterpiece, in the distinct style of Ettore Sottsass, Milan 1981. Playful sculptural furniture and graphic arrangement featuring a vibrant lemon yellow pyramid `#FFE800`, a coral pink curved column `#FF6F7D`, and turquoise floating geometric blocks `#4DEEEA`. Prominent black and white squiggly Bacterio pattern laminate surfaces, colorful terrazzo texture base. Sharp 1980s studio strobe flash lighting, zero gradient, crisp joyful irony, avant-garde radical design explosion, 8k resolution, exhibition catalog photography.",
        "negative_prompt": "dull corporate grey, serious bauhaus grid, classical vintage oil, rustic wood, soft gradient, dark gloomy lighting, messy scribbles, cheap modern flat vector.",
        "typography": [
            "- **主标题**：80年代先锋几何粗体（如 Memphis / Futura Bold / Broadway 解构版）。",
            "- **排版原则**：文字沿波浪线或斜线排布，字母填色互相撞色，充满戏谑幽默。"
        ],
        "voice_match": "`voice-xushunying`（消费符号学）或 `voice-lixinpian`（感官蒙太奇避难所）。"
    },
    "style-grunge-acid": {
        "name": "style-grunge-acid",
        "description": "垃圾排版与解构酸性设计 Skill。以大卫·卡森《Ray Gun》反可读性排版、3D流动液态铬合金、尖锐拉伸哥特体与复印机噪点为灵魂，粉碎平庸工整。",
        "version": "1.0.0",
        "tags": ["grunge", "acid-graphics", "david-carson", "liquid-metal", "cyber-rave", "anti-homogenization"],
        "title": "垃圾排版与解构酸性设计 (Grunge Typography & Acid Graphics)",
        "chapter": "第三篇第18章",
        "soul": [
            "**核心哲学**：1990年代大卫·卡森（David Carson）在《Ray Gun》杂志开创的垃圾排版（Grunge Typography），以及当代电子乐地下 Rave 派对中复兴的酸性平面（Acid Graphics）。主张“不要把可读性误认为是沟通”，以撕裂的复印机噪点、过度垂直拉伸的尖锐哥特体与3D融化液态金属触手，向一切循规蹈矩的学院派网格宣战。",
            "**AI 常见同质化缺陷**：生成千篇一律的无脑赛博霓虹蓝紫光晕、字体依然老老实实居中规整、毫无真实的物理撕裂破坏力与视网膜冲击感。",
            "**本 Skill 矫正法则**：\n  1. **3D流体液态金属 (Liquid chrome molten chrome)**：在深黑空间中扭曲穿梭的高反射流动水银触手与锐利倒钩。\n  2. **黑白复印机撕裂噪点 (Xerox photocopier texture)**：大量粗糙颗粒高对比扫描噪波、边缘撕裂半色调杂质与物理胶带反光贴片。\n  3. **反可读性极端拉伸哥特体**：字体纵向拉伸200%以上、尖端如手术刀般锐利、层层交错堆叠破坏视线连续性。"
        ],
        "palette": [
            "- 熔融水银冷铬银 (Liquid Molten Chrome Silver): `#D8D8D8` (3D液态金属触手与核心几何, 占35%)",
            "- 毒性酸性荧光黄绿 (Toxic Acid Neon Lime): `#DFFF00` (撕裂字体与微观数据标签, 占25%)",
            "- 视网膜电光深紫 (Retina Cyber Violet): `#5D00FF` (次级高能光泽与背景渐晕, 占15%)",
            "- 地下虚无黑 (Underground Void Carbon Black): `#0A0A0A` (深邃高反差基底, 占25%)"
        ],
        "materials": [
            "- 3D流动熔融高反光液态铬合金 (3D raytraced liquid mercury chrome metal with sharp HDRI reflections)",
            "- 廉价黑白复印机多次翻印的高反差撕裂噪波 (Distorted Xerox photocopier texture with paper tears and high-contrast threshold grit)",
            "- 镭射全息烫印彩虹膜反射 (Iridescent holographic foil refraction highlights)",
            "- 透明工业包装封箱胶带与撕裂标签 (Transparent packing tape with air bubbles and torn paper stickers)"
        ],
        "optics": [
            "- 极高反差地下俱乐部点光源在水银金属表面激发的锐利刺眼高光 (Harsh point-source specular highlights on chrome surfaces)。",
            "- 画面局部出现扫描仪拉动造成的数码条纹与拖影失真。"
        ],
        "grid": [
            "- 构图：彻底粉碎网格（Anti-Grid / Deconstructed Grid），多图层超高密度暴力堆叠碰撞。",
            "- 排版：文字被截断、重叠、垂直倒置、横跨画面，视网膜信息超载。"
        ],
        "forbidden": [
            "NO polite balanced Swiss grid typography, NO clean corporate minimalism",
            "NO soft cute pastel colors, NO calm classical serif layouts",
            "NO sterile white backgrounds, NO traditional legible newspaper alignment"
        ],
        "positive_prompt": "Avant-garde Acid Graphics and 90s Grunge typography poster masterpiece, inspired by David Carson Ray Gun era and contemporary underground cyber-rave visual culture. Central twisting 3D liquid chrome molten spikes `#D8D8D8` with extreme razor-sharp reflections against a void black background `#0A0A0A`. Violently stretched Gothic typography in toxic neon acid lime `#DFFF00` overlapping chaotic Xerox photocopier grain texture, torn paper edges, transparent packaging tape stickers, deep violet chromatic aberration `#5D00FF`. Extreme visual tension, deconstructed anti-grid rebellion, masterwork.",
        "negative_prompt": "neat swiss grid, clean corporate layout, legible aligned text, pastel cute colors, soft focus, plain white background, boring business template.",
        "typography": [
            "- **排版字体**：重度拉伸先锋哥特体（Extended Blackletter）、破坏性像素点阵字与工业危险警示无衬线。",
            "- **排版原则**：字母间距紧贴（Tracking -50）或极度拉大，图文强行穿插遮挡。"
        ],
        "voice_match": "`voice-wangjiawei`（时空疏离体）或 `voice-xushunying`（后现代符号解构）。"
    },
    "style-ui-waves": {
        "name": "style-ui-waves",
        "description": "数字交互三次浪潮 Skill。系统解析拟物化(皮革/金属高光) -> 纯色扁平化(极速响应) -> 空间玻璃拟态(多维深度/Backdrop-blur)的度规法则，杜绝混乱劣质UI。",
        "version": "1.0.0",
        "tags": ["ui-design", "skeuomorphism", "flat-design", "glassmorphism", "spatial-ui", "anti-homogenization"],
        "title": "数字交互三次浪潮 (UI Evolution: Skeuomorphic, Flat & Spatial Glassmorphism)",
        "chapter": "第三篇第19章",
        "soul": [
            "**核心哲学**：自2007年初代iPhone至今人机交互界面的三次深刻审美跃迁：1. 拟物化（Skeuomorphism, 建立人机信任的皮革缝线与真实玻璃反光）；2. 扁平化（Flat Design, 移动互联网爆发期的效率优先与纯色无阴影）；3. 空间计算玻璃拟态（Spatial Glassmorphism / visionOS, 空间维度中具有真实物理光学厚度与景深微模糊的多维悬浮面板）。",
            "**AI 常见同质化缺陷**：生成混乱无逻辑的假发光UI按钮、脏乱的渐变马卡龙色块、缺乏圆角连续性（Squircle）与基线对齐的漂浮文字。",
            "**本 Skill 矫正法则**：\n  1. **空间多维物理玻璃拟态 (Spatial Glass Optics)**：背景毛玻璃实时模糊（Backdrop-filter: blur 30px）、精细 1px 半透明内描边高光（Inner border highlight 0.5px rgba(255,255,255,0.2)）。\n  2. **精确的 8pt 空间网格度规**：所有外边距、内边距与组件高度均严格倍乘于 8px/4px 黄金模度。\n  3. **超高动态多层弥散投影**：多层透明度深度衰减微投影（0 10px 40px rgba(0,0,0,0.08)），构建克制通透的悬浮空间层级。"
        ],
        "palette": [
            "- 空间深空灰黑 (Spatial Dark Obsidian): `#1C1C1E` (高维空间操作界面背景, 占50%)",
            "- 苹果纯透玻璃白 (Frosted Crystal Glass White): `rgba(255,255,255,0.65)` (悬浮多维卡片基座, 占30%)",
            "- 系统电光聚焦蓝 (System Electric Focus Blue): `#007AFF` (主行动按钮与状态指示, 占10%)",
            "- 次级层级微光灰 (Subtle Interface Slate): `#8E8E93` (次级辅助信息与分割基线, 占10%)"
        ],
        "materials": [
            "- 精细喷砂物理亚克力与半透明多层光学毛玻璃 (Fine-sandblasted translucent optical frosted glass with real-time dynamic refraction)",
            "- 边缘极细高光倒角切面 (Precision 1px inner border specular highlight edge chamfer)",
            "- 空间深度微多层弥散空气阴影 (Multi-layered ultra-soft spatial ambient occlusion shadows)",
            "- 超清视网膜高像素点对点显示面板 (Retina crystal display precision with vector subpixel rendering)"
        ],
        "optics": [
            "- 悬浮于虚空中的环境漫射全色域天光，透过半透卡片显现后方背景微妙的色相折射与景深虚化 (Depth-of-field blur)。",
            "- 严禁刺眼的人工荧光外发光球与油腻廉价的塑料高光。"
        ],
        "grid": [
            "- 构图：严格 8pt 柱状网格系统，圆角采用苹果连续曲率超椭圆（Continuous Squircle Corner Radius 24px/32px）。",
            "- 排版：SF Pro Display / Inter 字体体系，严格 110%/130% 基线网格（Baseline rhythm）。"
        ],
        "forbidden": [
            "NO messy random button gradients, NO arbitrary irregular corner radiuses",
            "NO heavy muddy black drop shadows, NO unaligned floating text elements",
            "NO outdated 90s web bevel emboss, NO unreadable neon text without contrast"
        ],
        "positive_prompt": "Ultra-premium Spatial Operating System Glassmorphism UI dashboard concept, inspired by Apple visionOS and modern spatial interfaces. Floating multi-layered translucent frosted glass cards with authentic optical backdrop blur (30px blur), crisp 1px subtle white inner border highlight `rgba(255,255,255,0.2)`. Deep space obsidian backdrop `#1C1C1E` with subtle ambient light refraction. Elegant system blue `#007AFF` action toggles, perfectly aligned typographic hierarchy in San Francisco Pro font. Flawless 8pt grid structure, continuous smooth squircle corners, pristine digital clarity, 8k UI/UX portfolio presentation.",
        "negative_prompt": "messy ui, ugly gradients, bad typography, heavy black drop shadow, blurry icons, 90s bevel, skeuomorphic fake leather, misaligned buttons, low resolution.",
        "typography": [
            "- **主标题与数字**：SF Pro Rounded / Inter SemiBold，极大字阶形成强烈的数字仪表盘视觉锚点。",
            "- **正文与微标签**：SF Pro Text Regular 13pt / 11pt 等宽数字，字距紧致整洁。"
        ],
        "voice_match": "`voice-jobs-clarity`（激进清澈体）或 `voice-ogilvy-fact`（事实密集流）。"
    },
    "style-y2k-cyberpunk": {
        "name": "style-y2k-cyberpunk",
        "description": "千禧未来与赛博谱系 Skill。整合1999千禧危机未来乐观(果冻透彩iMac/充气糖果)与硬核赛博朋克(雨夜霓虹柏油/机械义体伺服)，消灭千篇一律的廉价蓝紫。",
        "version": "1.0.0",
        "tags": ["y2k", "cyberpunk", "futurism", "translucent-plastic", "blade-runner", "anti-homogenization"],
        "title": "千禧未来与赛博谱系 (Y2K Aesthetics & Cyberpunk Spectrum)",
        "chapter": "第三篇第20章",
        "soul": [
            "**核心哲学**：融合两个极具张力的时代切面：1. Y2K（1999-2002 千禧年前后对数码科技爆发的极致未来乐观主义，初代半透彩色 iMac G3、充气透明糖果PVC外壳、金属银与数码矩阵）；2. 硬核赛博朋克（Cyberpunk, “高科技，低生活”，九龙城寨与东京新宿雨夜、湿漉沥青倒影、外露线缆与神经机械义体）。",
            "**AI 常见同质化缺陷**：满屏幕糊成一团的蓝紫色赛博霓虹大平光、毫无机械物理逻辑的贴图假装义体、毫无质感塑料感廉价CG。",
            "**本 Skill 矫正法则**：\n  1. **半透明多彩工程聚碳酸酯 (Translucent Polycarbonate)**：重现初代iMac果冻机壳般的半透磨砂质感，肉眼可见内部复杂的精密电路板芯片与螺钉结构。\n  2. **潮湿雨夜柏油与真实光学霓虹倒影**：必须有真实的黑色潮湿沥青路面积水坑，霓虹灯光在水面呈油污斑驳反射，绝非空气中虚无的全局泛光。\n  3. **精密机械伺服铰链与线缆**：人体机械义体接缝清晰，包含真实的伺服电机、散热鳍片与编制绝缘线束。"
        ],
        "palette": [
            "- 千禧充气电光青 (Y2K Electric Cyan): `#00E5FF` (果冻外壳与数码抬头显示, 占30%)",
            "- 赛博极光高能紫 (Cyberpunk High-Volt Magenta): `#BD00FF` (招牌灯影与能量回路, 占25%)",
            "- 机械警戒铬黄 (Machinery Caution Amber): `#FF5500` (伺服关节与危险标识, 占15%)",
            "- 雨夜潮湿沥青黑 (Rain-soaked Asphalt Black): `#0D0E15` (基底深色夜景与机械骨架, 占30%)"
        ],
        "materials": [
            "- 半透明多彩果冻磨砂聚碳酸酯塑料外壳 (Translucent jelly frosted polycarbonate casing revealing micro-circuitry)",
            "- 雨夜带油污与雨滴反光的粗糙柏油路面 (Rain-slicked dark asphalt street with iridescent oil slicks)",
            "- 磨砂钛合金与碳化钨哑光机械骨骼 (Matte brushed titanium and tungsten carbide mechanical prosthetics)",
            "- 90年代末低清凸面CRT阴极射线管显示器扫描线纹理 (Retro CRT monitor scanlines with glass bulb phosphor glow)"
        ],
        "optics": [
            "- 湿漉漉的地面漫射倒影，局域锐利的霓虹招牌反光，夜雨中微弱的水汽丁达尔效应。",
            "- 镜头偶带有鱼眼广角微畸变 (Fisheye wide-angle lens characteristic of 2000s music videos)。"
        ],
        "grid": [
            "- 构图：倾斜动态视角，密集重叠的HUD抬头显示数据框，多窗口重叠界面（Multi-window desktop）。",
            "- 排版：粗椭圆气泡形标签框与极细科技等宽英文字符紧密共存。"
        ],
        "forbidden": [
            "NO generic flat purple haze without contrast, NO boring modern corporate office",
            "NO smooth featureless 3d robot dolls, NO dull grey low-contrast daylight",
            "NO historical vintage beige, NO clean empty minimalist hospital rooms"
        ],
        "positive_prompt": "Cinematic Y2K futuristic and Cyberpunk spectrum masterpiece, blending 1999 optimistic tech with dystopian rain-slicked atmosphere. A sleek mechanical android figure with translucent cyan polycarbonate casing `#00E5FF` exposing internal intricate brass servos and fiber optic cables, standing in a dense neon-drenched Tokyo rain alley. Deep asphalt black street `#0D0E15` reflecting puddles of vibrant high-volt magenta `#BD00FF` and caution amber warning lights `#FF5500`. Y2K chrome floating data icons, retro CRT scanline texture, authentic anamorphic lens flare, sharp rain drops, hyper-detailed 8k resolution.",
        "negative_prompt": "generic purple fog, low quality cgi, flat cartoon, boring daylight, clean minimalist room, blurry details, soft focus, plastic doll skin without seams.",
        "typography": [
            "- **主标题**：千禧流动充气泡泡数码字（Y2K Blob / Liquid Vector font）或拉伸等宽微机代码体。",
            "- **排版原则**：带有银色立体金属描边，附带技术版本号（如 v2.000 / SYSTEM READY）标签。"
        ],
        "voice_match": "`voice-wangjiawei`（时空延宕疏离体）或 `voice-jobs-clarity`（激进清澈体）。"
    }
}

def generate_visual_skill(skill_id, data):
    output_dir = os.path.join("skills", "visual", skill_id)
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "SKILL.md")
    
    tags_str = ", ".join([f'"{t}"' for t in data["tags"]])
    soul_str = "\n".join([f"- {s}" for s in data["soul"]])
    palette_str = "\n".join([f"  {p}" for p in data["palette"]])
    materials_str = "\n".join([f"  {m}" for m in data["materials"]])
    optics_str = "\n".join([f"  {o}" for o in data["optics"]])
    grid_str = "\n".join([f"  {g}" for g in data["grid"]])
    forbidden_str = "\n".join([f"- {f}" for f in data["forbidden"]])
    typography_str = "\n".join([f"{t}" for t in data["typography"]])
    
    content = f"""---
name: "{data['name']}"
description: "{data['description']}"
version: "{data['version']}"
tags: [{tags_str}]
---

# 风格定义：{data['title']}

> 源自《全球近现代设计美学全景图谱》{data['chapter']}。

## 1. 风格灵魂与反同质化主张 (Soul & Anti-Homogenization)
{soul_str}

## 2. 视觉 DNA 参数表 (Visual Parameter Matrix)
- **调色盘 (Restricted Palette)**:
{palette_str}
- **材质微观肌理 (Materials & Textures)**:
{materials_str}
- **光学系统与镜头 (Lighting & Optics)**:
{optics_str}
- **版式系统与构图网格 (Composition & Grid)**:
{grid_str}

## 3. 负向禁忌词库 (Negative Prompt & Anti-Patterns)
`FORBIDDEN`:
{forbidden_str}

## 4. 图像生成提示词注入模板 (Prompt Engine)
- **Positive Prompt**:
  > {data['positive_prompt']}
- **Negative Prompt**:
  > {data['negative_prompt']}

## 5. 平面与排版指南 (Graphic Layout Rules)
{typography_str}

## 6. 配套文字修辞推荐 (Harmonized Copywriting Voice)
- 协同 Skill：{data['voice_match']}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated visual skill: {skill_id} -> {file_path}")

if __name__ == "__main__":
    for skill_id, data in VISUAL_SKILLS.items():
        generate_visual_skill(skill_id, data)
    print(f"Successfully generated all {len(VISUAL_SKILLS)} visual skills!")
