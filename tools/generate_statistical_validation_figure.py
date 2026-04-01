#!/usr/bin/env python3

from __future__ import annotations

import math
import statistics
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "Img" / "mybenchmark"
SVG_PATH = OUT_DIR / "statistical-validation-stripplot.svg"
PDF_PATH = OUT_DIR / "statistical-validation-stripplot.pdf"
PNG_PATH = OUT_DIR / "statistical-validation-stripplot.png"

FONT = "Arial, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif"
SERIF = "Times New Roman, Georgia, Songti SC, STSong, serif"

COLORS = {
    "bg": "#ffffff",
    "panel": "#fbfbfb",
    "grid": "#e4e4e4",
    "border": "#cfcfcf",
    "text": "#333333",
    "muted": "#666666",
    "baseline": "#6c757d",
    "scheme1": "#d17a22",
    "scheme3": "#2b8a5a",
    "tag_blue_fill": "#edf4ff",
    "tag_blue_stroke": "#7aa2dd",
    "tag_green_fill": "#e8f6ee",
    "tag_green_stroke": "#74b28c",
}


def svg_header(width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "  <defs>",
        "    <filter id=\"shadow\" x=\"-20%\" y=\"-20%\" width=\"140%\" height=\"140%\">",
        "      <feDropShadow dx=\"0\" dy=\"1.5\" stdDeviation=\"2\" flood-color=\"#000000\" flood-opacity=\"0.08\"/>",
        "    </filter>",
        "  </defs>",
        f'  <rect width="{width}" height="{height}" fill="{COLORS["bg"]}"/>',
    ]


def svg_footer(lines: list[str]) -> str:
    return "\n".join(lines + ["</svg>", ""])


def add_rect(
    lines: list[str],
    x: float,
    y: float,
    w: float,
    h: float,
    *,
    fill: str,
    stroke: str,
    stroke_width: float = 1.4,
    radius: float = 12,
    extra: str = "",
) -> None:
    lines.append(
        f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" ry="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" {extra}/>'
    )


def add_line(
    lines: list[str],
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    stroke: str,
    stroke_width: float = 1.6,
    dash: str | None = None,
) -> None:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    lines.append(
        f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
        f'stroke-width="{stroke_width}"{dash_attr}/>'
    )


def add_circle(
    lines: list[str],
    cx: float,
    cy: float,
    r: float,
    *,
    fill: str,
    stroke: str = "#ffffff",
    stroke_width: float = 1.2,
) -> None:
    lines.append(
        f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
    )


def add_text(
    lines: list[str],
    x: float,
    y: float,
    content: str,
    *,
    size: int = 16,
    family: str = FONT,
    weight: str = "400",
    fill: str = COLORS["text"],
    anchor: str = "start",
) -> None:
    lines.append(
        f'  <text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" fill="{fill}">{escape(content)}</text>'
    )


def add_rotated_text(
    lines: list[str],
    x: float,
    y: float,
    content: str,
    *,
    size: int = 15,
    family: str = FONT,
    fill: str = COLORS["muted"],
) -> None:
    lines.append(
        f'  <text x="{x}" y="{y}" transform="rotate(-90 {x} {y})" '
        f'font-family="{family}" font-size="{size}" text-anchor="middle" fill="{fill}">{escape(content)}</text>'
    )


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def stddev(values: list[float]) -> float:
    return statistics.stdev(values)


class Panel:
    def __init__(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        title: str,
        ylabel: str,
        y_min: float,
        y_max: float,
        y_ticks: list[float],
        note: str,
        note_fill: str,
        note_stroke: str,
    ) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.title = title
        self.ylabel = ylabel
        self.y_min = y_min
        self.y_max = y_max
        self.y_ticks = y_ticks
        self.note = note
        self.note_fill = note_fill
        self.note_stroke = note_stroke

        self.plot_x = x + 76
        self.plot_y = y + 68
        self.plot_w = w - 108
        self.plot_h = h - 126

    def scale_y(self, value: float) -> float:
        ratio = (value - self.y_min) / (self.y_max - self.y_min)
        return self.plot_y + self.plot_h - ratio * self.plot_h


def draw_error_bar(lines: list[str], cx: float, y_mean: float, y_top: float, y_bottom: float, color: str) -> None:
    add_line(lines, cx, y_top, cx, y_bottom, stroke=color, stroke_width=2.6)
    add_line(lines, cx - 10, y_top, cx + 10, y_top, stroke=color, stroke_width=2.6)
    add_line(lines, cx - 10, y_bottom, cx + 10, y_bottom, stroke=color, stroke_width=2.6)
    add_circle(lines, cx, y_mean, 5.2, fill=color)


def draw_panel(
    lines: list[str],
    panel: Panel,
    groups: list[dict[str, object]],
    *,
    highlight_index: int,
) -> None:
    add_rect(
        lines,
        panel.x,
        panel.y,
        panel.w,
        panel.h,
        fill=COLORS["panel"],
        stroke=COLORS["border"],
        extra='filter="url(#shadow)"',
    )
    add_text(lines, panel.x + 26, panel.y + 34, panel.title, size=22, family=SERIF, weight="700")
    add_rotated_text(
        lines,
        panel.x + 22,
        panel.y + panel.h / 2 + 10,
        panel.ylabel,
    )

    tag_w = 176 if len(panel.note) > 22 else 152
    add_rect(
        lines,
        panel.x + panel.w - tag_w - 22,
        panel.y + 18,
        tag_w,
        28,
        fill=panel.note_fill,
        stroke=panel.note_stroke,
        stroke_width=1.2,
        radius=14,
    )
    add_text(
        lines,
        panel.x + panel.w - tag_w / 2 - 22,
        panel.y + 37,
        panel.note,
        size=13,
        family=FONT,
        weight="700",
        fill=panel.note_stroke,
        anchor="middle",
    )

    # Grid, ticks, axes.
    for tick in panel.y_ticks:
        y = panel.scale_y(tick)
        add_line(lines, panel.plot_x, y, panel.plot_x + panel.plot_w, y, stroke=COLORS["grid"], stroke_width=1.1)
        tick_label = f"{int(tick)}" if math.isclose(tick, round(tick)) else f"{tick:.2f}"
        add_text(lines, panel.plot_x - 12, y + 5, tick_label, size=13, fill=COLORS["muted"], anchor="end")

    add_line(lines, panel.plot_x, panel.plot_y, panel.plot_x, panel.plot_y + panel.plot_h, stroke="#b8b8b8", stroke_width=1.6)
    add_line(
        lines,
        panel.plot_x,
        panel.plot_y + panel.plot_h,
        panel.plot_x + panel.plot_w,
        panel.plot_y + panel.plot_h,
        stroke="#b8b8b8",
        stroke_width=1.6,
    )

    centers = [
        panel.plot_x + panel.plot_w * 0.31,
        panel.plot_x + panel.plot_w * 0.73,
    ]
    jitters = (-14, 0, 14)

    for idx, group in enumerate(groups):
        values = group["values"]
        group_mean = mean(values)
        group_std = stddev(values)
        color = group["color"]
        center = centers[idx]

        for value, jitter in zip(values, jitters):
            add_circle(lines, center + jitter, panel.scale_y(value), 6.2, fill=color)

        y_mean = panel.scale_y(group_mean)
        y_top = panel.scale_y(group_mean + group_std)
        y_bottom = panel.scale_y(group_mean - group_std)
        draw_error_bar(lines, center, y_mean, y_top, y_bottom, color)
        add_line(lines, center - 18, y_mean, center + 18, y_mean, stroke=color, stroke_width=3.0)

        add_text(lines, center, panel.plot_y + panel.plot_h + 28, group["label"], size=14, weight="700", anchor="middle")
        add_text(lines, center, panel.plot_y + panel.plot_h + 48, "n = 3", size=12, fill=COLORS["muted"], anchor="middle")

        if idx == highlight_index:
            label = group["std_label"]
            if abs(y_top - y_mean) < 18:
                sd_y = max(panel.plot_y + 18, y_top - 14)
                mean_y = min(panel.plot_y + panel.plot_h - 12, y_mean + 26)
            else:
                sd_y = y_top - 10 if y_top > panel.plot_y + 18 else panel.plot_y + 18
                mean_y = y_mean - 14
            add_text(lines, center, sd_y, label, size=13, weight="700", fill=color, anchor="middle")
            add_text(lines, center, mean_y, group["mean_label"], size=12, fill=color, anchor="middle")


def build_svg() -> str:
    width, height = 1200, 560
    lines = svg_header(width, height)

    add_text(lines, 60, 56, "同日重复测量下的收益稳定性对比", size=28, family=SERIF, weight="700")
    add_text(lines, 60, 82, "原始散点、均值与标准差误差棒共同区分“仅有方向性样本”与“可稳定复现的收益”。", size=15, fill=COLORS["muted"])

    add_rect(lines, 888, 34, 248, 34, fill="#f5f5f5", stroke=COLORS["border"], stroke_width=1.1, radius=17)
    add_text(lines, 1012, 56, "dots = raw runs   whiskers = mean ± 1 std", size=13, fill=COLORS["muted"], anchor="middle")

    left = Panel(
        44,
        108,
        536,
        412,
        "DaCapo / pmd",
        "msec (lower is better)",
        3050,
        3650,
        [3050, 3200, 3350, 3500, 3650],
        "large dispersion in repeated runs",
        COLORS["tag_blue_fill"],
        COLORS["tag_blue_stroke"],
    )
    right = Panel(
        620,
        108,
        536,
        412,
        "SPECjvm2008 / scimark.lu.small",
        "ops/m (higher is better)",
        45,
        72,
        [45, 52, 59, 66, 72],
        "stable gain across repeated runs",
        COLORS["tag_green_fill"],
        COLORS["tag_green_stroke"],
    )

    draw_panel(
        lines,
        left,
        [
            {
                "label": "Baseline",
                "values": [3281.0, 3280.0, 3287.0],
                "color": COLORS["baseline"],
                "std_label": "sd = 3.79",
                "mean_label": "mean = 3282.67",
            },
            {
                "label": "Scheme 1",
                "values": [3180.0, 3611.0, 3183.0],
                "color": COLORS["scheme1"],
                "std_label": "sd = 247.98",
                "mean_label": "mean = 3324.67",
            },
        ],
        highlight_index=1,
    )
    draw_panel(
        lines,
        right,
        [
            {
                "label": "Baseline",
                "values": [47.85, 47.85, 46.19],
                "color": COLORS["baseline"],
                "std_label": "sd = 0.96",
                "mean_label": "mean = 47.30",
            },
            {
                "label": "Scheme 3",
                "values": [69.20, 68.34, 69.20],
                "color": COLORS["scheme3"],
                "std_label": "sd = 0.50",
                "mean_label": "mean = 68.91",
            },
        ],
        highlight_index=1,
    )

    add_rect(lines, 124, 529, 952, 18, fill="#f4f4f4", stroke="#d0d0d0", stroke_width=1.0, radius=9)
    add_text(
        lines,
        600,
        542,
        "左图显示方案一存在正收益样本，但波动显著；右图显示方案三在相邻时间窗口内保持稳定增益。",
        size=13,
        fill=COLORS["muted"],
        anchor="middle",
    )

    return svg_footer(lines)


def render(svg_path: Path) -> None:
    subprocess.run(
        ["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", str(PDF_PATH), str(svg_path)],
        check=True,
    )
    subprocess.run(
        ["/opt/homebrew/bin/rsvg-convert", "-f", "png", "-w", "2200", "-o", str(PNG_PATH), str(svg_path)],
        check=True,
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SVG_PATH.write_text(build_svg(), encoding="utf-8")
    render(SVG_PATH)


if __name__ == "__main__":
    main()
