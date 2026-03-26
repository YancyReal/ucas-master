#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "Img" / "porting"
FONT_FAMILY = "Songti SC, STSong, Noto Serif CJK SC, serif"


def svg_header(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "  <defs>",
        '    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="userSpaceOnUse">',
        '      <path d="M0,0 L12,6 L0,12 z" fill="#666666"/>',
        "    </marker>",
        "  </defs>",
        '  <rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>',
    ]


def svg_footer(lines: list[str]) -> str:
    return "\n".join(lines + ["</svg>", ""])


def add_rect(
    lines: list[str],
    x: float,
    y: float,
    w: float,
    h: float,
    fill: str = "#ffffff",
    stroke: str = "#888888",
    stroke_width: float = 1.6,
    radius: float = 10,
) -> None:
    lines.append(
        f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" ry="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
    )


def add_line(
    lines: list[str],
    points: list[tuple[float, float]],
    stroke: str = "#666666",
    stroke_width: float = 2.0,
    arrow: bool = True,
) -> None:
    point_text = " ".join(f"{x},{y}" for x, y in points)
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    lines.append(
        f'  <polyline points="{point_text}" fill="none" stroke="{stroke}" '
        f'stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"{marker}/>'
    )


def add_path(
    lines: list[str],
    d: str,
    stroke: str = "#666666",
    stroke_width: float = 2.0,
    arrow: bool = True,
) -> None:
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    lines.append(
        f'  <path d="{d}" fill="none" stroke="{stroke}" stroke-width="{stroke_width}" '
        f'stroke-linecap="round" stroke-linejoin="round"{marker}/>'
    )


def add_text(
    lines: list[str],
    x: float,
    y: float,
    content: str,
    size: int = 24,
    weight: str = "400",
    anchor: str = "middle",
    fill: str = "#333333",
    line_gap: float | None = None,
) -> None:
    parts = content.split("\n")
    gap = line_gap if line_gap is not None else size * 1.35
    start_y = y - gap * (len(parts) - 1) / 2.0
    lines.append(
        f'  <text x="{x}" y="{start_y}" font-family="{FONT_FAMILY}" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">'
    )
    for idx, part in enumerate(parts):
        dy = 0 if idx == 0 else gap
        lines.append(f'    <tspan x="{x}" dy="{dy}">{escape(part)}</tspan>')
    lines.append("  </text>")


def add_badge(lines: list[str], x: float, y: float, label: str) -> None:
    lines.append(
        f'  <circle cx="{x}" cy="{y}" r="22" fill="#d9d9d9" stroke="#777777" stroke-width="1.6"/>'
    )
    add_text(lines, x, y + 1, label, size=22, weight="700")


def add_box(
    lines: list[str],
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    subtitle: str = "",
    fill: str = "#ffffff",
    stroke: str = "#8a8a8a",
    title_size: int = 25,
    subtitle_size: int = 18,
) -> None:
    add_rect(lines, x, y, w, h, fill=fill, stroke=stroke)
    if subtitle:
        add_text(lines, x + w / 2.0, y + h * 0.36, title, size=title_size, weight="700")
        add_text(lines, x + w / 2.0, y + h * 0.70, subtitle, size=subtitle_size, fill="#555555")
    else:
        add_text(lines, x + w / 2.0, y + h / 2.0, title, size=title_size, weight="700")


def write_file(name: str, svg: str) -> Path:
    path = OUT_DIR / f"{name}.svg"
    path.write_text(svg, encoding="utf-8")
    return path


def render(svg_path: Path) -> None:
    pdf_path = svg_path.with_suffix(".pdf")
    png_path = svg_path.with_suffix(".png")
    subprocess.run(
        ["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", str(pdf_path), str(svg_path)],
        check=True,
    )
    subprocess.run(
        [
            "/opt/homebrew/bin/rsvg-convert",
            "-f",
            "png",
            "-w",
            "2200",
            "-o",
            str(png_path),
            str(svg_path),
        ],
        check=True,
    )


def build_overview() -> str:
    width, height = 1200, 790
    lines = svg_header(width, height)

    add_rect(lines, 40, 35, 1120, 118, fill="#fafafa", stroke="#b5b5b5")
    add_rect(lines, 40, 185, 525, 260, fill="#fafafa", stroke="#b5b5b5")
    add_rect(lines, 595, 185, 565, 260, fill="#fafafa", stroke="#b5b5b5")
    add_rect(lines, 40, 480, 1120, 112, fill="#fafafa", stroke="#b5b5b5")
    add_rect(lines, 40, 630, 1120, 72, fill="#e9e9e9", stroke="#9a9a9a")

    add_text(lines, 72, 62, "外部工具与执行入口", size=24, weight="700", anchor="start")
    add_text(lines, 72, 212, "编译器侧（art/compiler）", size=24, weight="700", anchor="start")
    add_text(lines, 627, 212, "运行时侧（art/runtime）", size=24, weight="700", anchor="start")
    add_text(lines, 72, 507, "公共支撑库与工件层", size=24, weight="700", anchor="start")

    add_box(lines, 90, 82, 210, 52, "dex2oat", fill="#ffffff", title_size=22)
    add_box(lines, 470, 82, 280, 52, "app_process / dalvikvm", fill="#ffffff", title_size=22)
    add_box(lines, 845, 82, 230, 52, "profman / artd", fill="#ffffff", title_size=22)

    add_box(lines, 90, 250, 195, 78, "后端汇编与\n代码生成", fill="#dddddd", title_size=24)
    add_box(lines, 315, 250, 195, 78, "Optimizing\nCompiler", fill="#dddddd", title_size=24)
    add_box(lines, 90, 348, 195, 68, "Driver / Linker", fill="#ffffff", title_size=21)
    add_box(lines, 315, 348, 195, 68, "JNI Compiler", fill="#dddddd", title_size=22)

    add_box(lines, 645, 250, 205, 78, "C++ 解释器\n与 Nterp", fill="#dddddd", title_size=24)
    add_box(lines, 890, 250, 205, 78, "JIT 与\n运行时协同", fill="#dddddd", title_size=24)
    add_box(lines, 645, 348, 205, 68, "Quick EntryPoints", fill="#dddddd", title_size=21)
    add_box(lines, 890, 348, 205, 68, "ClassLinker / GC\nThread / JNI", fill="#ffffff", title_size=20)

    add_box(lines, 110, 525, 290, 50, "libdexfile / libartbase", fill="#ffffff", title_size=21)
    add_box(lines, 455, 525, 290, 50, "OAT / ELF / CFI", fill="#ffffff", title_size=21)
    add_box(lines, 800, 525, 290, 50, "profile / native bridge", fill="#ffffff", title_size=21)

    add_text(
        lines,
        600,
        667,
        "LoongArch64 ISA / ABI / Linux-Android 系统环境",
        size=28,
        weight="700",
    )

    add_line(lines, [(195, 134), (195, 185)])
    add_line(lines, [(610, 134), (610, 185)])
    add_line(lines, [(960, 134), (960, 185)])
    add_line(lines, [(565, 316), (595, 316)])
    add_text(lines, 580, 292, "编译结果 / 入口协同", size=16, fill="#666666")
    add_line(lines, [(302, 445), (302, 480)])
    add_line(lines, [(877, 445), (877, 480)])
    add_line(lines, [(600, 592), (600, 630)])

    add_rect(lines, 70, 728, 22, 22, fill="#dddddd", stroke="#777777", stroke_width=1.2, radius=3)
    add_text(lines, 110, 739, "阴影框表示本文直接适配或补齐的核心模块", size=18, anchor="start")

    return svg_footer(lines)


def build_stages() -> str:
    width, height = 980, 835
    lines = svg_header(width, height)

    stages = [
        ("1", "汇编器与机器描述", "建立最小代码发射能力"),
        ("2", "C++ 解释器闭环", "打通调用、返回与异常传播"),
        ("3", "Nterp 闭环", "建立高效解释执行路径"),
        ("4", "JIT / JNI 与入口点", "建立编译执行与 Java/native 闭环"),
        ("5", "Intrinsic 与热点路径", "形成可验证、可优化的稳定基线"),
    ]
    top = 55
    box_x = 150
    box_w = 700
    box_h = 92
    gap = 58

    for idx, (num, title, subtitle) in enumerate(stages):
        y = top + idx * (box_h + gap)
        add_badge(lines, 95, y + box_h / 2.0, num)
        fill = "#dddddd" if idx in {1, 2, 3} else "#ffffff"
        add_box(lines, box_x, y, box_w, box_h, title, subtitle, fill=fill, title_size=26, subtitle_size=18)
        if idx < len(stages) - 1:
            next_y = y + box_h + gap
            add_line(lines, [(500, y + box_h), (500, next_y)])

    add_rect(lines, 150, 760, 700, 46, fill="#f3f3f3", stroke="#b5b5b5", radius=8)
    add_text(
        lines,
        500,
        783,
        "闭环顺序：可运行 → 可高效解释 → 可编译执行 → 可跨 Java/native → 可支撑热点路径",
        size=18,
    )

    return svg_footer(lines)


def build_runtime_paths() -> str:
    width, height = 1200, 760
    lines = svg_header(width, height)

    add_rect(lines, 40, 45, 250, 620, fill="#fafafa", stroke="#b5b5b5")
    add_rect(lines, 330, 45, 260, 620, fill="#fafafa", stroke="#b5b5b5")
    add_rect(lines, 630, 45, 530, 620, fill="#fafafa", stroke="#b5b5b5")

    add_text(lines, 165, 78, "执行路径", size=24, weight="700")
    add_text(lines, 460, 78, "入口点与桥接层", size=24, weight="700")
    add_text(lines, 895, 78, "运行时服务", size=24, weight="700")

    add_box(lines, 80, 120, 170, 74, "Java 方法 /\nDEX 字节码", fill="#ffffff", title_size=23)
    add_box(lines, 80, 235, 170, 74, "C++ 解释器", fill="#dddddd", title_size=23)
    add_box(lines, 80, 350, 170, 74, "Nterp", fill="#dddddd", title_size=23)
    add_box(lines, 80, 465, 170, 74, "JIT 编译代码", fill="#dddddd", title_size=23)

    add_box(lines, 375, 175, 170, 72, "quick\nentrypoints", fill="#dddddd", title_size=23)
    add_box(lines, 375, 320, 170, 72, "trampolines", fill="#dddddd", title_size=22)
    add_box(lines, 375, 465, 170, 72, "JNI bridge /\nnative stub", fill="#ffffff", title_size=22)

    add_box(lines, 700, 145, 390, 68, "对象分配 / 类解析 / 类型检查", fill="#ffffff", title_size=21)
    add_box(lines, 700, 260, 390, 68, "字段访问 / 字符串辅助", fill="#ffffff", title_size=21)
    add_box(lines, 700, 375, 390, 68, "异常处理 / Deopt / 方法返回修复", fill="#ffffff", title_size=21)
    add_box(lines, 700, 490, 390, 68, "GC / 锁 / 线程 / JNI 支撑", fill="#ffffff", title_size=21)

    add_path(lines, "M 250 157 C 292 160, 332 184, 375 211")
    add_path(lines, "M 250 272 C 292 258, 332 232, 375 211")
    add_path(lines, "M 250 387 C 298 380, 336 368, 375 356")
    add_path(lines, "M 250 488 C 292 470, 332 408, 375 356")
    add_path(lines, "M 250 516 C 298 516, 336 510, 375 501")

    add_path(lines, "M 545 198 C 605 198, 640 184, 700 179")
    add_path(lines, "M 545 224 C 605 232, 640 286, 700 294")
    add_path(lines, "M 545 356 C 605 356, 640 401, 700 409")
    add_path(lines, "M 545 501 C 605 501, 640 520, 700 524")

    add_rect(lines, 80, 594, 1010, 48, fill="#f3f3f3", stroke="#b5b5b5", radius=8)
    add_text(
        lines,
        585,
        618,
        "C++ 解释器更多直接借助运行时辅助；Nterp 与编译代码依赖统一入口点接入主路径",
        size=18,
    )

    return svg_footer(lines)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    figures = {
        "art-porting-overview": build_overview(),
        "art-porting-stages": build_stages(),
        "art-porting-runtime-paths": build_runtime_paths(),
    }
    for name, svg in figures.items():
        svg_path = write_file(name, svg)
        render(svg_path)


if __name__ == "__main__":
    main()
