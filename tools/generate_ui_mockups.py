from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "design" / "ui"
OUT.mkdir(parents=True, exist_ok=True)


FONT = "'Segoe UI Variable','Microsoft YaHei UI','Segoe UI',sans-serif"


def svg_shell(width: int, height: int, body: str, defs: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<defs>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="18" stdDeviation="30" flood-color="#0F172A" flood-opacity=".18"/></filter>
  <filter id="shadowSmall" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#0F172A" flood-opacity=".16"/></filter>
  <filter id="blur"><feGaussianBlur stdDeviation="42"/></filter>
  <linearGradient id="wallpaper" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#DBEAFE"/><stop offset=".52" stop-color="#F8FAFC"/><stop offset="1" stop-color="#D1FAE5"/></linearGradient>
  <linearGradient id="blueSoft" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#EFF6FF"/><stop offset="1" stop-color="#DBEAFE"/></linearGradient>
  <style>
    text {{ font-family: {FONT}; fill: #172033; }}
    .muted {{ fill:#64748B; }} .subtle {{ fill:#94A3B8; }} .white {{ fill:#FFFFFF; }}
    .h1 {{ font-size:30px; font-weight:650; }} .h2 {{ font-size:22px; font-weight:650; }}
    .body {{ font-size:15px; }} .small {{ font-size:13px; }} .label {{ font-size:12px; font-weight:600; letter-spacing:.7px; }}
    .mono {{ font-family:'Cascadia Mono','Microsoft YaHei UI',monospace; }}
  </style>
  {defs}
</defs>
{body}
</svg>'''


def icon(kind: str, x: float, y: float, size: float = 22, color: str = "#64748B", sw: float = 1.8) -> str:
    # Small, deliberately simple Fluent-like line icons.
    paths = {
        "home": '<path d="M4 10.5 12 4l8 6.5V20h-6v-6h-4v6H4z"/>',
        "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4M17 3v4M3 10h18"/>',
        "users": '<circle cx="9" cy="8" r="3"/><path d="M3.5 20c.7-4 2.4-6 5.5-6s4.8 2 5.5 6M16 5.5a3 3 0 0 1 0 5.8M16 14c2.7.2 4.2 2.1 4.7 5"/>',
        "duty": '<path d="M6 4h12v17H6zM9 4V2h6v2M9 9h6M9 13h6M9 17h4"/>',
        "bell": '<path d="M18 9a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9M9 21h6"/>',
        "bolt": '<path d="m13 2-8 12h7l-1 8 8-12h-7z"/>',
        "palette": '<path d="M12 3a9 9 0 1 0 0 18h1.2a2.3 2.3 0 0 0 0-4.6h-.8a1.5 1.5 0 0 1 0-3h2A6.6 6.6 0 0 0 21 6.8C18.8 4.4 15.6 3 12 3z"/><circle cx="7.5" cy="10" r=".8"/><circle cx="10" cy="6.8" r=".8"/><circle cx="15" cy="7" r=".8"/>',
        "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9 7 7M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/>',
        "shield": '<path d="M12 3 20 6v5c0 5.2-3.2 8.7-8 10-4.8-1.3-8-4.8-8-10V6z"/><path d="m8.5 12 2.2 2.2 4.8-5"/>',
        "dice": '<rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8" cy="8" r="1" fill="currentColor"/><circle cx="16" cy="8" r="1" fill="currentColor"/><circle cx="12" cy="12" r="1" fill="currentColor"/><circle cx="8" cy="16" r="1" fill="currentColor"/><circle cx="16" cy="16" r="1" fill="currentColor"/>',
        "close": '<path d="M5 5l14 14M19 5 5 19"/>',
        "board": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 22h8M12 18v4M7 9h10M7 13h6"/>',
        "arrow": '<path d="M5 12h14M14 7l5 5-5 5"/>',
        "check": '<path d="m5 12 4 4L19 6"/>',
    }
    p = paths[kind]
    return f'<g transform="translate({x},{y}) scale({size/24})" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="color:{color}">{p}</g>'


def management() -> str:
    nav = [
        ("home", "概览", True), ("calendar", "今日与课程表", False), ("users", "学生与小组", False),
        ("duty", "值日与岗位", False), ("bell", "提醒与自动化", False), ("bolt", "快捷操作与热键", False),
        ("palette", "外观与窗口", False), ("gear", "系统与启动", False),
    ]
    nav_items = []
    y = 182
    for ic, label, active in nav:
        if active:
            nav_items.append(f'<rect x="112" y="{y-15}" width="224" height="46" rx="7" fill="#E7F0FF"/>')
            nav_items.append('<rect x="112" y="%s" width="3" height="24" rx="1.5" fill="#2563EB"/>' % (y-4))
        nav_items.append(icon(ic, 132, y-5, 20, "#2563EB" if active else "#64748B"))
        nav_items.append(f'<text x="166" y="{y+11}" font-size="14" font-weight="{650 if active else 500}" fill="{"#1D4ED8" if active else "#475569"}">{label}</text>')
        y += 54

    schedule = []
    courses = [("08:00", "语文", "进行中", "#2563EB"), ("09:00", "数学", "下一节", "#0D9488"), ("10:10", "英语", "", "#7C3AED"), ("11:10", "物理", "", "#D97706"), ("14:00", "班会", "", "#E11D48")]
    x = 446
    for i, (tm, subject, state, color) in enumerate(courses):
        w = 140 if i else 174
        fill = "#EFF6FF" if i == 0 else "#FFFFFF"
        stroke = "#BFDBFE" if i == 0 else "#E2E8F0"
        schedule.append(f'<rect x="{x}" y="478" width="{w}" height="100" rx="8" fill="{fill}" stroke="{stroke}"/>')
        schedule.append(f'<rect x="{x}" y="478" width="4" height="100" rx="2" fill="{color}"/>')
        schedule.append(f'<text x="{x+18}" y="504" class="small muted">{tm}</text>')
        schedule.append(f'<text x="{x+18}" y="540" font-size="22" font-weight="650">{subject}</text>')
        if state:
            schedule.append(f'<text x="{x+18}" y="562" font-size="12" fill="{color}">{state}</text>')
        x += w + 12

    body = f'''
<rect width="1600" height="1000" fill="#E8EDF3"/>
<circle cx="1450" cy="90" r="220" fill="#DCE7F5"/><circle cx="80" cy="930" r="250" fill="#E5EFEA"/>
<g filter="url(#shadow)">
  <rect x="80" y="50" width="1440" height="900" rx="18" fill="#F8FAFC"/>
  <path d="M98 50h1404a18 18 0 0 1 18 18v42H80V68a18 18 0 0 1 18-18z" fill="#FFFFFF"/>
</g>
<circle cx="110" cy="80" r="9" fill="#2563EB"/><path d="m106 80 4-6 4 6-4 6z" fill="#fff"/>
<text x="130" y="86" font-size="15" font-weight="650">EvoClass</text><text x="208" y="86" class="small muted">教室助手</text>
<line x1="80" y1="110" x2="1520" y2="110" stroke="#E2E8F0"/>
<circle cx="1430" cy="80" r="4" fill="#94A3B8"/><rect x="1466" y="76" width="9" height="9" fill="none" stroke="#64748B"/><path d="m1500 76 9 9m0-9-9 9" stroke="#64748B"/>

<rect x="80" y="110" width="280" height="840" fill="#F3F6F9"/><line x1="360" y1="110" x2="360" y2="950" stroke="#E2E8F0"/>
<text x="112" y="146" class="label muted">工作区</text>
{''.join(nav_items)}
<line x1="112" y1="650" x2="336" y2="650" stroke="#DCE3EA"/>
{icon('shield',132,686,20,'#64748B')}<text x="166" y="702" font-size="14" fill="#475569">数据、日志与关于</text>
<rect x="112" y="866" width="224" height="58" rx="8" fill="#FFFFFF" stroke="#DFE5EC"/>
<circle cx="142" cy="895" r="14" fill="#D1FAE5"/><circle cx="142" cy="895" r="5" fill="#10B981"/>
<text x="166" y="893" class="small" font-weight="650">七年级 2 班</text><text x="166" y="912" font-size="11" class="muted">离线运行 · 数据已保存</text>

<rect x="360" y="110" width="1160" height="840" fill="#FBFCFE"/>
<text x="408" y="165" class="h1">今日概览</text><text x="408" y="192" class="body muted">2026年8月9日，星期日 · 第 3 教学周 / 轮换第 1 周</text>
<rect x="1308" y="143" width="164" height="42" rx="7" fill="#2563EB"/>{icon('board',1327,152,19,'#FFFFFF')}
<text x="1355" y="169" font-size="14" font-weight="600" class="white">预览晨间信息</text>

<rect x="408" y="230" width="724" height="190" rx="10" fill="url(#blueSoft)" stroke="#CFE0F6"/>
<text x="440" y="266" class="label" fill="#1D4ED8">CURRENT CLASS · 当前课程</text>
<text x="440" y="330" font-size="43" font-weight="680">语文</text><text x="440" y="361" class="body muted">第一节 · 张老师 · 08:00—08:45</text>
<rect x="440" y="384" width="506" height="7" rx="3.5" fill="#C9DAF2"/><rect x="440" y="384" width="318" height="7" rx="3.5" fill="#2563EB"/>
<text x="980" y="392" font-size="13" fill="#1D4ED8">剩余 17 分钟</text>
<line x1="1000" y1="264" x2="1000" y2="366" stroke="#C9DAF2"/>
<text x="1034" y="292" class="small muted">下一节</text><text x="1034" y="328" font-size="24" font-weight="650">数学</text><text x="1034" y="354" class="small muted">09:00 开始</text>

<rect x="1156" y="230" width="316" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>
<text x="1184" y="267" class="h2">今日岗位</text><text x="1438" y="267" class="small" fill="#2563EB">编辑</text>
<line x1="1184" y1="286" x2="1444" y2="286" stroke="#E7ECF1"/>
<circle cx="1196" cy="315" r="5" fill="#0D9488"/><text x="1212" y="320" class="body muted">值日</text><text x="1438" y="320" class="body" text-anchor="end" font-weight="600">陈一诺、周嘉言</text>
<circle cx="1196" cy="351" r="5" fill="#D97706"/><text x="1212" y="356" class="body muted">擦黑板</text><text x="1438" y="356" class="body" text-anchor="end" font-weight="600">林语桐</text>
<circle cx="1196" cy="387" r="5" fill="#7C3AED"/><text x="1212" y="392" class="body muted">讲台整理</text><text x="1438" y="392" class="body" text-anchor="end" font-weight="600">第 3 小组</text>

<text x="408" y="462" class="h2">今日课程</text><text x="1098" y="462" class="small" fill="#2563EB" text-anchor="end">查看完整课表  →</text>
{''.join(schedule)}

<text x="408" y="636" class="h2">快捷操作</text>
<g>
  <rect x="408" y="660" width="214" height="88" rx="9" fill="#FFFFFF" stroke="#E2E8F0"/>{icon('calendar',432,682,24,'#2563EB')}
  <text x="472" y="694" font-size="15" font-weight="650">临时换课</text><text x="472" y="718" class="small muted">只影响指定日期</text>
  <rect x="638" y="660" width="214" height="88" rx="9" fill="#FFFFFF" stroke="#E2E8F0"/>{icon('users',662,682,24,'#0D9488')}
  <text x="702" y="694" font-size="15" font-weight="650">替换人员</text><text x="702" y="718" class="small muted">不改变基础轮换</text>
  <rect x="868" y="660" width="214" height="88" rx="9" fill="#FFFFFF" stroke="#E2E8F0"/>{icon('dice',892,682,24,'#7C3AED')}
  <text x="932" y="694" font-size="15" font-weight="650">随机抽人</text><text x="932" y="718" class="small muted">当前剩余 24 人</text>
</g>
<rect x="1156" y="620" width="316" height="128" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>
<text x="1184" y="656" class="h2">运行状态</text><circle cx="1190" cy="687" r="5" fill="#10B981"/><text x="1206" y="692" class="small">调度器运行正常</text>
<circle cx="1190" cy="720" r="5" fill="#10B981"/><text x="1206" y="725" class="small">今日数据已校验</text><text x="1440" y="725" class="small muted" text-anchor="end">刚刚</text>

<rect x="408" y="790" width="1064" height="104" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>
<text x="436" y="827" class="h2">最近提醒</text><rect x="436" y="850" width="72" height="24" rx="12" fill="#ECFDF5"/><text x="472" y="867" font-size="12" fill="#047857" text-anchor="middle">已完成</text>
<text x="524" y="867" class="body">08:00 早读开始提醒</text><text x="1438" y="867" class="small muted" text-anchor="end">展示 12 秒 · 未抢占焦点</text>
<text x="1410" y="925" font-size="11" class="subtle" text-anchor="end">EvoClass 管理主窗口 · 概览页概念稿</text>
'''
    return svg_shell(1600, 1000, body)


def quick_panel() -> str:
    items = [
        ("duty", "显示今日值日", "Ctrl + Alt + D", "#0D9488"),
        ("dice", "随机抽人", "Ctrl + Alt + R", "#7C3AED"),
        ("calendar", "当前课程与课表", "Ctrl + Alt + C", "#2563EB"),
        ("shield", "救援中心", "Ctrl + Alt + Q", "#DC2626"),
        ("gear", "打开管理窗口", "", "#64748B"),
    ]
    rows=[]
    y=286
    for i,(ic,label,key,color) in enumerate(items):
        if i==1:
            rows.append(f'<rect x="136" y="{y-18}" width="330" height="66" rx="8" fill="#EEF2FF"/>')
        rows.append(f'<circle cx="168" cy="{y+15}" r="19" fill="{color}" opacity=".11"/>')
        rows.append(icon(ic,156,y+3,24,color))
        rows.append(f'<text x="204" y="{y+20}" font-size="16" font-weight="{650 if i==1 else 540}">{label}</text>')
        if key: rows.append(f'<text x="442" y="{y+20}" class="small muted" text-anchor="end">{key}</text>')
        y+=72
    body=f'''
<rect width="1600" height="900" fill="url(#wallpaper)"/>
<g filter="url(#blur)" opacity=".52"><circle cx="1280" cy="160" r="190" fill="#93C5FD"/><circle cx="1020" cy="720" r="250" fill="#A7F3D0"/><circle cx="280" cy="780" r="160" fill="#C4B5FD"/></g>
<path d="M0 760 C360 650 600 860 900 740s470-70 700-190V900H0z" fill="#FFFFFF" opacity=".35"/>
<text x="1120" y="166" font-size="64" font-weight="220" fill="#334155" opacity=".56">08:32</text><text x="1124" y="200" font-size="18" fill="#475569" opacity=".68">8月9日  星期日</text>

<!-- quick panel -->
<g filter="url(#shadow)"><rect x="112" y="158" width="378" height="564" rx="16" fill="#FFFFFF" fill-opacity=".93" stroke="#FFFFFF"/></g>
<text x="144" y="207" class="h2">快捷操作</text><text x="144" y="236" class="small muted">七年级 2 班 · 当前为第一节课</text>
<circle cx="443" cy="204" r="18" fill="#F1F5F9"/>{icon('close',433,194,20,'#64748B')}
<line x1="136" y1="258" x2="466" y2="258" stroke="#E2E8F0"/>
{''.join(rows)}
<line x1="136" y1="646" x2="466" y2="646" stroke="#E2E8F0"/>
<circle cx="151" cy="679" r="5" fill="#10B981"/><text x="166" y="684" class="small muted">常驻中 · 自动隐藏已开启</text><text x="454" y="684" class="small" fill="#2563EB" text-anchor="end">固定面板</text>

<!-- floating entry -->
<g filter="url(#shadowSmall)"><rect x="12" y="382" width="68" height="136" rx="24" fill="#172033" fill-opacity=".90"/></g>
<circle cx="46" cy="421" r="20" fill="#2563EB"/><path d="m39 421 7-10 7 10-7 10z" fill="#fff"/>
<line x1="28" y1="458" x2="64" y2="458" stroke="#475569"/>
{icon('dice',34,476,24,'#FFFFFF')}
<text x="512" y="420" font-size="13" fill="#334155" opacity=".70">悬浮入口展开后，菜单保持在触发侧并避开屏幕边缘</text>
<path d="M498 428H420" stroke="#334155" stroke-opacity=".35" stroke-dasharray="5 5"/>

<!-- quiet class status pill -->
<g filter="url(#shadowSmall)"><rect x="1080" y="750" width="418" height="76" rx="14" fill="#FFFFFF" fill-opacity=".90"/></g>
<rect x="1100" y="771" width="5" height="34" rx="2.5" fill="#2563EB"/><text x="1122" y="784" class="small muted">当前课程</text><text x="1122" y="806" font-size="18" font-weight="650">语文 · 剩余 17 分钟</text>
<text x="1468" y="791" font-size="13" fill="#2563EB" text-anchor="end">下一节 数学 09:00</text>
<text x="1550" y="870" font-size="11" class="muted" text-anchor="end">EvoClass 桌面常驻界面 · 悬浮入口与快捷菜单</text>
'''
    return svg_shell(1600,900,body)


def random_overlay() -> str:
    body=f'''
<rect width="1600" height="900" fill="url(#wallpaper)"/>
<g filter="url(#blur)" opacity=".5"><circle cx="240" cy="180" r="220" fill="#BFDBFE"/><circle cx="1390" cy="770" r="300" fill="#A7F3D0"/></g>
<!-- de-emphasized lesson background -->
<rect x="0" y="0" width="1600" height="900" fill="#0F172A" opacity=".30"/>
<g opacity=".4"><rect x="90" y="94" width="460" height="620" rx="12" fill="#fff"/><rect x="112" y="126" width="190" height="18" rx="9" fill="#CBD5E1"/><rect x="112" y="178" width="408" height="220" rx="8" fill="#E2E8F0"/><rect x="112" y="426" width="320" height="14" rx="7" fill="#CBD5E1"/><rect x="112" y="458" width="380" height="14" rx="7" fill="#CBD5E1"/></g>

<g filter="url(#shadow)"><rect x="322" y="176" width="956" height="548" rx="22" fill="#FBFDFF" fill-opacity=".965" stroke="#FFFFFF"/></g>
<rect x="322" y="176" width="956" height="8" rx="4" fill="#7C3AED"/>
{icon('dice',370,218,30,'#7C3AED')}<text x="414" y="245" class="h2">随机抽人</text><text x="414" y="272" class="small muted">七年级 2 班 · 本轮不重复</text>
<circle cx="1222" cy="235" r="20" fill="#F1F5F9"/>{icon('close',1211,224,22,'#64748B')}
<line x1="370" y1="302" x2="1230" y2="302" stroke="#E2E8F0"/>

<text x="800" y="350" class="label muted" text-anchor="middle">SELECTED STUDENT · 抽取结果</text>
<text x="800" y="458" font-size="76" font-weight="690" text-anchor="middle">林语桐</text>
<rect x="660" y="484" width="112" height="34" rx="17" fill="#EDE9FE"/><text x="716" y="507" font-size="14" fill="#6D28D9" text-anchor="middle" font-weight="600">第 3 小组</text>
<rect x="786" y="484" width="154" height="34" rx="17" fill="#F1F5F9"/><text x="863" y="507" font-size="14" class="muted" text-anchor="middle">本轮剩余 24 人</text>

<line x1="370" y1="562" x2="1230" y2="562" stroke="#E2E8F0"/>
<text x="395" y="603" class="small muted">刚才经过：</text>
<text x="488" y="603" font-size="14" fill="#94A3B8">周嘉言</text><text x="574" y="603" font-size="14" fill="#94A3B8">陈一诺</text><text x="660" y="603" font-size="14" fill="#94A3B8">许知夏</text>
<rect x="842" y="584" width="112" height="48" rx="8" fill="#FFFFFF" stroke="#CBD5E1"/>{icon('users',860,596,22,'#64748B')}<text x="892" y="614" font-size="14" font-weight="600">标记缺席</text>
<rect x="970" y="584" width="122" height="48" rx="8" fill="#7C3AED"/>{icon('dice',989,596,22,'#FFFFFF')}<text x="1020" y="614" font-size="14" font-weight="650" class="white">再抽一人</text>
<rect x="1108" y="584" width="96" height="48" rx="8" fill="#F1F5F9"/><text x="1156" y="614" font-size="14" font-weight="600" text-anchor="middle">结束</text>
<text x="800" y="684" font-size="12" class="muted" text-anchor="middle">按 Space 再抽一人 · 按 Esc 结束 · 动画已在结果计算后播放</text>

<!-- floating entry remains available -->
<g filter="url(#shadowSmall)"><rect x="12" y="376" width="64" height="124" rx="23" fill="#172033" fill-opacity=".88"/></g>
<circle cx="44" cy="414" r="19" fill="#7C3AED"/>{icon('dice',32,402,24,'#FFFFFF')}
<line x1="28" y1="450" x2="60" y2="450" stroke="#475569"/>{icon('close',34,466,20,'#FFFFFF')}
<text x="1550" y="870" font-size="11" fill="#E2E8F0" text-anchor="end">EvoClass 中央展示层 · 随机抽人结果态</text>
'''
    return svg_shell(1600,900,body)


def morning_overlay() -> str:
    # A second presentation state proves the overlay shell can host non-random content.
    slots=[("08:00","语文","#2563EB"),("09:00","数学","#0D9488"),("10:10","英语","#7C3AED"),("11:10","物理","#D97706"),("14:00","班会","#E11D48")]
    rows=[]
    y=390
    for i,(tm,sub,color) in enumerate(slots):
        rows.append(f'<text x="830" y="{y}" class="small muted">{tm}</text><rect x="886" y="{y-18}" width="4" height="26" rx="2" fill="{color}"/><text x="905" y="{y}" font-size="16" font-weight="600">{sub}</text>')
        if i<4: rows.append(f'<line x1="830" y1="{y+18}" x2="1132" y2="{y+18}" stroke="#E8EDF2"/>')
        y+=52
    body=f'''
<rect width="1600" height="900" fill="url(#wallpaper)"/><g filter="url(#blur)" opacity=".45"><circle cx="190" cy="760" r="260" fill="#A7F3D0"/><circle cx="1400" cy="170" r="250" fill="#BFDBFE"/></g>
<rect width="1600" height="900" fill="#0F172A" opacity=".16"/>
<g filter="url(#shadow)"><rect x="224" y="116" width="1152" height="668" rx="22" fill="#FBFDFF" fill-opacity=".97"/></g>
<rect x="224" y="116" width="1152" height="7" rx="3.5" fill="#2563EB"/>
<text x="278" y="177" class="label" fill="#2563EB">GOOD MORNING · 晨间信息</text><text x="278" y="229" font-size="32" font-weight="670">早上好，七年级 2 班</text>
<text x="278" y="261" class="body muted">2026年8月9日 星期日 · 第 3 教学周 · 轮换第 1 周</text>
<circle cx="1318" cy="168" r="20" fill="#F1F5F9"/>{icon('close',1307,157,22,'#64748B')}
<line x1="278" y1="292" x2="1322" y2="292" stroke="#E2E8F0"/>

<text x="278" y="337" class="h2">今日岗位</text>
<rect x="278" y="364" width="456" height="84" rx="9" fill="#ECFDF5"/><circle cx="314" cy="406" r="18" fill="#0D9488" opacity=".12"/>{icon('duty',302,394,24,'#0D9488')}
<text x="348" y="397" class="small muted">值日</text><text x="348" y="425" font-size="19" font-weight="650">陈一诺、周嘉言</text>
<rect x="278" y="464" width="456" height="84" rx="9" fill="#FFFBEB"/><circle cx="314" cy="506" r="18" fill="#D97706" opacity=".12"/>{icon('board',302,494,24,'#D97706')}
<text x="348" y="497" class="small muted">擦黑板</text><text x="348" y="525" font-size="19" font-weight="650">林语桐</text>
<rect x="278" y="564" width="456" height="84" rx="9" fill="#F5F3FF"/><circle cx="314" cy="606" r="18" fill="#7C3AED" opacity=".12"/>{icon('users',302,594,24,'#7C3AED')}
<text x="348" y="597" class="small muted">讲台整理</text><text x="348" y="625" font-size="19" font-weight="650">第 3 小组</text>

<line x1="780" y1="326" x2="780" y2="660" stroke="#E2E8F0"/>
<text x="830" y="337" class="h2">今日课表</text>{''.join(rows)}
<rect x="830" y="616" width="302" height="44" rx="8" fill="#EFF6FF"/><text x="850" y="643" class="small" fill="#1D4ED8">第一节 08:00 开始 · 语文</text>
<line x1="278" y1="690" x2="1322" y2="690" stroke="#E2E8F0"/>
<circle cx="288" cy="732" r="4" fill="#2563EB"/><text x="304" y="737" class="small muted">今日无临时换课</text><text x="1318" y="737" class="small muted" text-anchor="end">将在 18 秒后自动收起 · 鼠标移入暂停</text>
<rect x="278" y="756" width="1040" height="4" rx="2" fill="#E2E8F0"/><rect x="278" y="756" width="612" height="4" rx="2" fill="#2563EB"/>
<text x="1550" y="870" font-size="11" fill="#E2E8F0" text-anchor="end">EvoClass 中央展示层 · 晨间信息</text>
'''
    return svg_shell(1600,900,body)


def board() -> str:
    # Contact sheet referencing the three core modes without depending on raster embedding.
    body='''
<rect width="1920" height="1320" fill="#E9EEF4"/>
<text x="84" y="88" font-size="36" font-weight="700">EvoClass UI Concept</text><text x="84" y="122" font-size="16" class="muted">Windows classroom assistant · Quiet Fluent · Independent visual direction</text>
<rect x="1540" y="66" width="290" height="42" rx="21" fill="#FFFFFF"/><circle cx="1570" cy="87" r="7" fill="#10B981"/><text x="1590" y="93" font-size="14" font-weight="600">MVP interface system / v0.1</text>
<g filter="url(#shadowSmall)"><rect x="84" y="172" width="1120" height="700" rx="18" fill="#FFFFFF"/></g>
<rect x="108" y="196" width="1072" height="652" rx="10" fill="#F8FAFC"/><rect x="108" y="196" width="230" height="652" rx="10" fill="#F1F5F9"/>
<circle cx="144" cy="234" r="10" fill="#2563EB"/><text x="164" y="240" font-size="16" font-weight="650">EvoClass</text>
<rect x="128" y="288" width="190" height="42" rx="7" fill="#E7F0FF"/><text x="164" y="314" font-size="14" fill="#1D4ED8" font-weight="650">概览</text>
<text x="372" y="252" font-size="26" font-weight="650">今日概览</text><text x="372" y="280" class="small muted">第 3 教学周 / 轮换第 1 周</text>
<rect x="372" y="326" width="508" height="176" rx="10" fill="url(#blueSoft)" stroke="#CFE0F6"/><text x="402" y="364" class="label" fill="#1D4ED8">CURRENT CLASS</text><text x="402" y="424" font-size="44" font-weight="680">语文</text><text x="402" y="458" class="body muted">第一节 · 剩余 17 分钟</text>
<rect x="906" y="326" width="242" height="176" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/><text x="932" y="365" class="h2">今日岗位</text><text x="932" y="410" class="small muted">值日</text><text x="1124" y="410" class="small" font-weight="600" text-anchor="end">陈一诺、周嘉言</text><text x="932" y="452" class="small muted">擦黑板</text><text x="1124" y="452" class="small" font-weight="600" text-anchor="end">林语桐</text>
<text x="372" y="554" class="h2">今日课程</text><rect x="372" y="582" width="154" height="94" rx="8" fill="#EFF6FF" stroke="#BFDBFE"/><text x="392" y="610" class="small muted">08:00</text><text x="392" y="650" font-size="22" font-weight="650">语文</text><rect x="540" y="582" width="138" height="94" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/><text x="560" y="610" class="small muted">09:00</text><text x="560" y="650" font-size="22" font-weight="650">数学</text><rect x="692" y="582" width="138" height="94" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/><text x="712" y="610" class="small muted">10:10</text><text x="712" y="650" font-size="22" font-weight="650">英语</text>
<text x="108" y="914" class="label muted">01 / MANAGEMENT WINDOW</text><text x="108" y="944" font-size="20" font-weight="650">管理配置清晰、稳定，不把课堂操作藏进设置</text>

<g filter="url(#shadowSmall)"><rect x="1260" y="172" width="576" height="444" rx="18" fill="url(#wallpaper)"/></g>
<rect x="1300" y="226" width="262" height="336" rx="14" fill="#FFFFFF" fill-opacity=".95"/><text x="1324" y="264" font-size="18" font-weight="650">快捷操作</text><line x1="1324" y1="284" x2="1538" y2="284" stroke="#E2E8F0"/><text x="1356" y="326" class="body">显示今日值日</text><rect x="1316" y="346" width="230" height="52" rx="8" fill="#EEF2FF"/><text x="1356" y="379" class="body" font-weight="650">随机抽人</text><text x="1356" y="432" class="body">当前课程与课表</text><text x="1356" y="485" class="body">救援中心</text><text x="1356" y="538" class="body">打开管理窗口</text>
<rect x="1268" y="320" width="46" height="108" rx="20" fill="#172033"/><circle cx="1291" cy="350" r="15" fill="#2563EB"/>
<text x="1284" y="660" class="label muted">02 / FLOATING ENTRY</text><text x="1284" y="690" font-size="20" font-weight="650">一步触达，高频而不打扰</text>

<g filter="url(#shadowSmall)"><rect x="1260" y="760" width="576" height="420" rx="18" fill="#526072"/></g>
<rect x="1310" y="824" width="476" height="290" rx="16" fill="#FFFFFF"/><rect x="1310" y="824" width="476" height="6" rx="3" fill="#7C3AED"/><text x="1342" y="870" font-size="18" font-weight="650">随机抽人</text><line x1="1342" y1="892" x2="1754" y2="892" stroke="#E2E8F0"/><text x="1548" y="970" font-size="48" font-weight="690" text-anchor="middle">林语桐</text><rect x="1465" y="994" width="84" height="28" rx="14" fill="#EDE9FE"/><text x="1507" y="1013" font-size="12" fill="#6D28D9" text-anchor="middle">第3小组</text><rect x="1560" y="994" width="112" height="28" rx="14" fill="#F1F5F9"/><text x="1616" y="1013" font-size="12" class="muted" text-anchor="middle">剩余24人</text><rect x="1628" y="1050" width="110" height="42" rx="7" fill="#7C3AED"/><text x="1683" y="1076" font-size="13" class="white" font-weight="650" text-anchor="middle">再抽一人</text>
<text x="1284" y="1222" class="label muted">03 / PRESENTATION OVERLAY</text><text x="1284" y="1252" font-size="20" font-weight="650">后排可读，自动提醒不抢焦点</text>
<text x="84" y="1272" font-size="13" class="muted">Design principles: quiet / legible / low-distraction / offline-first / keyboard &amp; touch friendly</text>
'''
    return svg_shell(1920,1320,body)


FILES = {
    "evoclass-management-overview.svg": management(),
    "evoclass-floating-quick-panel.svg": quick_panel(),
    "evoclass-random-picker-overlay.svg": random_overlay(),
    "evoclass-morning-overlay.svg": morning_overlay(),
    "evoclass-ui-concept-board.svg": board(),
}


for name, content in FILES.items():
    (OUT / name).write_text(content, encoding="utf-8")
    print(OUT / name)
