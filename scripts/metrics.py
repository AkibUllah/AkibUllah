"""Render a profile metrics card (dark + light SVG) from public GitHub data.

Usage: GITHUB_TOKEN=... python scripts/metrics.py <login> <out_dir>
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from collections import Counter
from html import escape

API = "https://api.github.com/graphql"
SKIP_LANGS = {"HTML", "CSS", "Dockerfile", "Makefile", "Jinja", "Procfile", "Mako", "Smarty", "Batchfile"}
SKIP_REPOS = {".github"}
PALETTE = ["#22d3ee", "#a78bfa", "#34d399", "#f472b6", "#fbbf24", "#60a5fa", "#94a3b8"]


def gql(query: str, variables: dict, token: str) -> dict:
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.load(resp)
    if body.get("errors"):
        raise RuntimeError(body["errors"])
    return body["data"]


REPOS = """
query($login: String!, $after: String) {
  user(login: $login) {
    contributionsCollection { contributionCalendar { totalContributions } }
    repositories(first: 100, after: $after, privacy: PUBLIC, isFork: false, ownerAffiliations: OWNER) {
      pageInfo { hasNextPage endCursor }
      nodes {
        name
        releases { totalCount }
        languages(first: 12, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } }
      }
    }
  }
}
"""

PRS = """
query($q: String!) { search(query: $q, type: ISSUE, first: 1) { issueCount } }
"""


def collect(login: str, token: str) -> dict:
    repos, after, contributions = [], None, 0
    while True:
        data = gql(REPOS, {"login": login, "after": after}, token)["user"]
        contributions = data["contributionsCollection"]["contributionCalendar"]["totalContributions"]
        page = data["repositories"]
        repos += [r for r in page["nodes"] if r["name"] not in SKIP_REPOS and r["name"] != login]
        if not page["pageInfo"]["hasNextPage"]:
            break
        after = page["pageInfo"]["endCursor"]
    langs: Counter[str] = Counter()
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            if edge["node"]["name"] not in SKIP_LANGS:
                langs[edge["node"]["name"]] += edge["size"]
    merged = gql(PRS, {"q": f"author:{login} is:pr is:merged"}, token)["search"]["issueCount"]
    external = gql(PRS, {"q": f"author:{login} is:pr -user:{login}"}, token)["search"]["issueCount"]
    return {
        "projects": len(repos),
        "releases": sum(r["releases"]["totalCount"] for r in repos),
        "merged_prs": merged,
        "oss_prs": external,
        "contributions": contributions,
        "languages": langs.most_common(),
    }


def render(m: dict, dark: bool) -> str:
    bg0, bg1 = ("#070b14", "#0b1222") if dark else ("#f7f9ff", "#eef3ff")
    fg, sub, border, tile = (
        ("#e8eefc", "#9aa7c0", "#24324f", "#0e1729") if dark else ("#0f172a", "#475569", "#d4dcf0", "#ffffff")
    )
    stats = [
        ("Projects", m["projects"]),
        ("Releases", m["releases"]),
        ("Merged PRs", m["merged_prs"]),
        ("PRs to other repos", m["oss_prs"]),
        ("Contributions (1y)", m["contributions"]),
    ]
    w, gap, x0 = 1200, 16, 40
    tile_w = (w - 2 * x0 - gap * (len(stats) - 1)) / len(stats)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="250" viewBox="0 0 {w} 250" role="img" aria-label="GitHub metrics">',
        '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>'
        '<linearGradient id="acc" x1="0" x2="1"><stop offset="0" stop-color="#22d3ee"/><stop offset="1" stop-color="#a78bfa"/></linearGradient></defs>',
        "<style>.n{animation:up .9s ease-out both}@keyframes up{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}"
        "@media (prefers-reduced-motion: reduce){.n{animation:none}}</style>",
        f'<rect x=".5" y=".5" width="{w - 1}" height="249" rx="18" fill="url(#bg)" stroke="{border}"/>',
        '<g font-family="Segoe UI, Inter, Helvetica, Arial, sans-serif">',
    ]
    for i, (label, value) in enumerate(stats):
        x = x0 + i * (tile_w + gap)
        parts.append(
            f'<g class="n" style="animation-delay:{i * 0.12:.2f}s">'
            f'<rect x="{x:.1f}" y="28" width="{tile_w:.1f}" height="96" rx="12" fill="{tile}" stroke="{border}"/>'
            f'<rect x="{x + 18:.1f}" y="44" width="28" height="3" rx="1.5" fill="url(#acc)"/>'
            f'<text x="{x + 18:.1f}" y="88" font-size="34" font-weight="700" fill="{fg}">{value:,}</text>'
            f'<text x="{x + 18:.1f}" y="110" font-size="14" fill="{sub}">{escape(label)}</text></g>'
        )
    total = sum(s for _, s in m["languages"]) or 1
    top = m["languages"][:6]
    rest = total - sum(s for _, s in top)
    segs = [(n, s) for n, s in top] + ([("Other", rest)] if rest > 0 else [])
    bar_x, bar_w, y = 40, w - 80, 156
    parts.append(f'<text x="{bar_x}" y="{y - 8}" font-size="14" fill="{sub}">Languages across public projects</text>')
    parts.append(f'<clipPath id="bar"><rect x="{bar_x}" y="{y}" width="{bar_w}" height="12" rx="6"/></clipPath><g clip-path="url(#bar)">')
    cx = bar_x
    for i, (name, size) in enumerate(segs):
        seg = bar_w * size / total
        parts.append(f'<rect x="{cx:.1f}" y="{y}" width="{seg + 0.5:.1f}" height="12" fill="{PALETTE[i % len(PALETTE)]}"/>')
        cx += seg
    parts.append("</g>")
    lx = bar_x
    for i, (name, size) in enumerate(segs):
        label = f"{name} {100 * size / total:.1f}%"
        parts.append(
            f'<circle cx="{lx + 6}" cy="{y + 40}" r="6" fill="{PALETTE[i % len(PALETTE)]}"/>'
            f'<text x="{lx + 18}" y="{y + 45}" font-size="14" fill="{fg}">{escape(label)}</text>'
        )
        lx += 30 + 8.2 * len(label)
    parts.append(f'<text x="{w - 40}" y="234" font-size="12" fill="{sub}" text-anchor="end">updated daily from public GitHub data</text>')
    parts.append("</g></svg>")
    return "".join(parts)


def main() -> None:
    login, out = sys.argv[1], sys.argv[2]
    token = os.environ["GITHUB_TOKEN"]
    metrics = collect(login, token)
    os.makedirs(out, exist_ok=True)
    for dark in (True, False):
        with open(os.path.join(out, f"metrics-{'dark' if dark else 'light'}.svg"), "w", encoding="utf-8") as fh:
            fh.write(render(metrics, dark))
    print(json.dumps({k: v for k, v in metrics.items() if k != "languages"}), metrics["languages"][:6])


if __name__ == "__main__":
    main()
