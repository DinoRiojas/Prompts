---
name: morningstar-url
description: "Generates Morningstar.com direct HTTPS URLs for security tickers covering portfolio, quote, performance, risk, strategy, and price tabs. Outputs each HTTPS URL separately with an empty line between every URL. Use when the user asks for Morningstar links, URLs, pages, or tabs for specific ticker symbols, mutual funds, ETFs, or stocks."
---
# Morningstar URL Generator

Generate exact HTTPS URLs for Morningstar tabs across fund and ETF tickers, listing each URL separately with a blank line between every link.

## When to Use

- When the user asks for Morningstar URLs or direct web links for one or more tickers.
- When generating direct links for Morningstar tabs.

## Tab Order

Output links in this exact order:
1. `portfolio`
2. `quote`
3. `performance`
4. `risk`
5. `strategy`
6. `price`

## URL Structure

- **Mutual Funds** (e.g., `vtsax`, `fxaix`):
  `https://www.morningstar.com/funds/xnas/{ticker}/{tab}`
- **ETFs** (e.g., `voo`, `spy`, `vtip`):
  Use the appropriate exchange slug, such as:
  `https://www.morningstar.com/etfs/arcx/{ticker}/{tab}` or `https://www.morningstar.com/etfs/xnas/{ticker}/{tab}`

## Output Formatting Rules

- Output ONLY the raw `https://` URLs.
- Do NOT output bullet points, labels, bold text, markdown headers, or descriptive text.
- Every single URL must be separated by an empty blank line (double newline).
- Ticker symbols must be lowercase in the URL slug.
