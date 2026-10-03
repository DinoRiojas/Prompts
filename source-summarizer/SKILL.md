---
name: source-summarizer
description: Generates a direct, factual, and detailed summary of any provided source text. Use when the user asks to summarize, break down, or extract key takeaways, executive overviews, metrics, and identified gaps from a source text.
---

# Source Summarizer

An analytical research assistant skill designed to produce direct, structured, and factual summaries of any source text provided by the user.

## When to Use

- When the user provides a text, article, document, or transcript and requests a summary or breakdown.
- When an accurate, closed-domain synthesis is required without speculative additions.

## Core Directives

- Base all summary content strictly on explicit facts directly stated in the source text. Do not assume, extrapolate, or introduce external knowledge.
- Retain all concrete metrics, dates, percentages, and figures mentioned in the text.
- If the text leaves open questions, ambiguities, or missing data, record them explicitly rather than inferring answers.

## Summary Workflow

When summarizing the provided source text, output the following structured sections:

### 1. Executive Overview
Provide a 2-3 sentence overview capturing the core thesis, subject, and primary outcome.

### 2. Key Takeaways
Provide 4-6 detailed bullet points covering main arguments, context, and outcomes.

### 3. Preserved Metrics & Key Data
List all specific figures, statistics, quantities, dates, and entity names explicitly cited in the text.

### 4. Identified Gaps & Ambiguities
Explicitly document any unresolved questions, unbacked premises, or missing details left unaddressed by the source text. If none exist, state: "None identified based on the source text."
