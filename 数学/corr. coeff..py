import math
import re

fmt = """
\\begin{{center}}
\\resizebox{{\\columnwidth-4.6em}}{{!}}{{%
    \\begin{{tabular}}{{|c|c|c|c|c|}}
    \\hline
    $x_i$       & $y_i$       & $x_i^2$       & $y_i^2$       & $x_iy_i$       \\\\
    \\hline
    {}\\\\
    \\hline
    \\hline
    $\\sum{{x_i}}$ & $\\sum{{y_i}}$ & $\\sum{{x_i^2}}$ & $\\sum{{y_i^2}}$ & $\\sum{{x_iy_i}}$ \\\\
    \\hline
    {}        \\\\
    \\hline
    \\end{{tabular}}
}}
\\end{{center}}
\\begin{{flalign*}}
\\bar{{x}} & = \\frac{{{xi}}}{{{n}}} = {barx} \\\\
\\bar{{y}} & = \\frac{{{yi}}}{{{n}}} = {bary} \\\\
r & = \\frac{{\\frac{{{xiyi}}}{{{n}}} - {barx} \\times {bary}}}{{\\sqrt{{\\left(\\frac{{{x2i}}}{{{n}}} 
- {barx}^2\\right)\\left(\\frac{{{y2i}}}{{{n}}} - {bary}^2\\right)}}}} & \\\\
    & = {ans}
\\end{{flalign*}}
"""

raw = """
82      & 59    \\
              79      & 63    \\
              76      & 99    \\
              63      & 67    \\
              56      & 61    \\
              67      & 88    \\
              69      & 82    \\
              81      & 77    \\
              77      & 75    \\
              73      & 74    \\
              58      & 67    \\
              64      & 79    \\
              68      & 75    \\
              72      & 65    \\
              75      & 64    \\
              80      & 66    \\
"""

data = [list(map(int, i.split("&")))
        for i in [i for i in re.sub(r"\s", "", raw).split("\\") if i]]
data = [[i, j, i**2, j**2, i * j] for i, j in data]

xi, yi, x2i, y2i, xiyi = [sum(i) for i in list(zip(*data))]

n = len(data)
barx, bary = xi / n, yi / n

r = (xiyi / n - barx * bary) / \
    math.sqrt((x2i / n - barx**2) * (y2i / n - bary**2))

print(
    fmt.format(
        " \\\\\n".join(" & ".join(map(lambda i: str(round(i, 2)), i))
                       for i in data),
        " & ".join(map(lambda i: str(round(i, 2)), [xi, yi, x2i, y2i, xiyi])),
        xi=round(xi, 2),
        yi=round(yi, 2),
        x2i=round(x2i, 2),
        y2i=round(y2i, 2),
        xiyi=round(xiyi, 2),
        n=n,
        barx=round(barx, 2),
        bary=round(bary, 2),
        ans=round(r, 4),
    )
)
