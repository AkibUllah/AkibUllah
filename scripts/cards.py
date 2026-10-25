"""Render the flagship project cards (dark + light SVG) used in the profile README."""

from __future__ import annotations

import os
import sys
import textwrap
from html import escape

CARDS = [
    ("saas-starter-kit", "SaaS Starter Kit", "Multi-tenant SaaS foundation: orgs, roles, invites, API keys, plan limits and billing on FastAPI + Next.js 14.", ["FastAPI", "Next.js", "PostgreSQL", "Redis"], "#22d3ee"),
    ("rag-eval-lab", "RAG Eval Lab", "Bilingual English/Bangla retrieval with a measured comparison of chunkers and retrievers. Live in-browser demo.", ["Python", "RAG", "BM25", "pgvector"], "#a78bfa"),
    ("ai-support-agent", "AI Support Agent", "Tool-calling agent that refunds within policy, with guardrails, injection screening and a 53-scenario eval suite.", ["Agents", "FastAPI", "React", "Evals"], "#f472b6"),
    ("fastapi-payment-gateway", "Payment Gateway", "One API over bKash, SSLCommerz and Stripe: idempotency keys, a strict state machine, signed webhooks, settlement.", ["FastAPI", "FinTech", "SQLAlchemy", "Docker"], "#34d399"),
    ("webhook-relay", "Webhook Relay", "Reliable delivery with backoff, circuit breakers, dead letters and SKIP LOCKED workers that scale horizontally.", ["FastAPI", "PostgreSQL", "asyncio", "HMAC"], "#fbbf24"),
    ("go-api-gateway", "Go API Gateway", "Reverse-proxy gateway in Go: JWT/JWKS, rate limiting, health-checked load balancing, hot reload, Prometheus.", ["Go", "net/http", "Redis", "Prometheus"], "#60a5fa"),
]


def card(name: str, title: str, desc: str, tags: list[str], accent: str, dark: bool) -> str:
    bg0, bg1 = ("#0b1222", "#0e1729") if dark else ("#ffffff", "#f5f8ff")
    fg, sub, border, chip = (
        ("#e8eefc", "#9aa7c0", "#24324f", "#14203a") if dark else ("#0f172a", "#475569", "#d4dcf0", "#eef3ff")
    )
    lines = textwrap.wrap(desc, 62)
    if len(lines) > 2:
        raise ValueError(f"description for {name} needs {len(lines)} lines; keep it to two")
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="580" height="190" viewBox="0 0 580 190" role="img"',
        f' aria-label="{escape(title)}: {escape(desc)}">',
        f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>',
        f'<clipPath id="r"><rect width="580" height="190" rx="16"/></clipPath><radialGradient id="glow"><stop offset="0" stop-color="{accent}" stop-opacity="{0.22 if dark else 0.14}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>',
        f'<rect x=".5" y=".5" width="579" height="189" rx="16" fill="url(#bg)" stroke="{border}"/>',
        '<circle cx="540" cy="20" r="150" fill="url(#glow)" clip-path="url(#r)"/>',
        f'<rect x="24" y="26" width="34" height="4" rx="2" fill="{accent}"/>',
        '<g font-family="Segoe UI, Inter, Helvetica, Arial, sans-serif">',
        f'<text x="24" y="62" font-size="23" font-weight="700" fill="{fg}">{escape(title)}</text>',
        f'<text x="556" y="62" font-size="13" fill="{sub}" text-anchor="end">↗ {escape(name)}</text>',
    ]
    for i, line in enumerate(lines):
        out.append(f'<text x="24" y="{96 + i * 22}" font-size="15" fill="{sub}">{escape(line)}</text>')
    x = 24
    for tag in tags:
        width = max(44.0, 20 + 7.4 * len(tag))
        out.append(
            f'<rect x="{x:.1f}" y="148" width="{width:.1f}" height="24" rx="12" fill="{chip}" stroke="{border}"/>'
            f'<text x="{x + width / 2:.1f}" y="164.5" font-size="12.5" fill="{fg}" text-anchor="middle">{escape(tag)}</text>'
        )
        x += width + 8
    out.append("</g></svg>")
    return "".join(out)


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "assets/cards"
    os.makedirs(out, exist_ok=True)
    for name, title, desc, tags, accent in CARDS:
        for dark in (True, False):
            path = os.path.join(out, f"{name}-{'dark' if dark else 'light'}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(card(name, title, desc, tags, accent, dark))
    print(f"wrote {len(CARDS) * 2} cards to {out}")


if __name__ == "__main__":
    main()
