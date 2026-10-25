---
name: qr-code
description: Generates QR codes rendered on an HTML5 canvas for any given URL or text payload. When called with a given URL or text, always immediately execute and generate the canvas QR code using that exact input.
---
# QR Code Generator

This skill guides and executes the generation of client-side, interactive QR codes drawn onto an HTML5 `<canvas>` element for any given URL or text payload.

## Core Execution Rule

- When this skill is invoked with a specific URL or text string, **immediately execute and generate** the HTML canvas QR code tailored to and pre-populated with that exact URL or payload.
- Do not use placeholders or generic defaults when a URL or payload is provided in the prompt; bind the provided URL directly to the canvas initialization.

## Implementation Guidelines

### 1. Default Implementation: Lightweight Canvas Library (`qrious`)

When generating a canvas QR code:
- Initialize the canvas with the exact target URL provided by the user.
- Ensure the canvas size defaults to 256x256 px or larger for clear mobile scanning (300x300 px recommended).
- Set Error Correction to High (`level: 'H'`).
- Provide an interactive control panel:
  - Input field to dynamically update payload/URL.
  - Size adjustments (e.g., 256px to 512px).
  - Error correction level selectors (`L`, `M`, `Q`, `H`).
  - Color palette customization (foreground/background swatches).
  - One-click image download button using `canvas.toDataURL('image/png')`.
- Include tasteful styling (e.g., modern, minimal aesthetic with responsive layouts and clear typography).

### 2. Standalone / Offline Implementation (Zero External Dependencies)

When offline use, security restrictions, or zero CDN dependencies are requested:
- Generate the QR matrix using a pure JavaScript Galois Field GF(2^8) and Reed-Solomon polynomial division module.
- Render modules directly to canvas using standard `ctx.fillRect()` coordinates with a standard 4-module quiet zone.

## Standard Parameters

- **Default Value**: The specific URL or text provided in the user's prompt.
- **Error Correction Level**: `L` (~7%), `M` (~15%), `Q` (~25%), `H` (~30%) (Default: `H`).
- **Quiet Zone / Margin**: Minimum 4 modules.
- **Default Resolution**: Minimum 256x256 px canvas for sharp scanning.
