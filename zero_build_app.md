# App Specification: [Your App Name]

## 1. Tech Stack & Architecture Constraints (Zero-Build / No Node.js)
- **Strict Requirement:** Build a purely client-side, static web application using **vanilla HTML5, CSS3, and ES6+ JavaScript**.
- **No Build Step:** Do NOT use React, Vite, Webpack, TypeScript, Node.js, or `package.json` / `npm install` dependencies.
- **Standalone Execution:** The app must run immediately when opening `index.html` directly in a browser (via `file://` or any static web server) with zero compilation or bundling.
- **External Libraries (if needed):** Load any third-party libraries (e.g., Tailwind CSS, Lucide icons, Chart.js) strictly via standard `<script>` or `<link>` CDN tags in `index.html`, or native browser ES module CDN imports (`https://esm.sh/...`).

## 2. File Structure
Keep the project flat and minimal:
- `index.html` — Semantic markup, layout structure, and CDN imports.
- `styles.css` — Custom styling, CSS variables, and responsive grid/flexbox layouts.
- `app.js` — All application state, DOM manipulation, event listeners, and logic.

## 3. Core Purpose & User Flow
- **Overview:** [1–2 sentences describing what the app does and who it is for.]
- **Primary Workflow:**
  1. [Step 1: e.g., User enters text or uploads a local file.]
  2. [Step 2: e.g., App processes the input and updates the interactive view.]
  3. [Step 3: e.g., User exports/downloads the result or saves progress.]

## 4. Key Features & UI Components
- **[Feature 1 Name]:** [Specific behavior, inputs, and expected output.]
- **[Feature 2 Name]:** [Specific behavior, inputs, and expected output.]
- **[Feature 3 Name]:** [Specific behavior, inputs, and expected output.]

## 5. Data Persistence & API Integration
- **Local Storage:** Persist user settings and session data in browser `localStorage` (with a button to clear/reset data).
- **Gemini API Integration (Optional — remove if not needed):**
  - Provide a clean UI input modal/drawer where the user pastes their own Gemini API key (stored in `sessionStorage` or `localStorage`).
  - Make direct browser `fetch()` calls to the Gemini REST API (`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent`) rather than using a Node.js backend SDK.

## 6. Visual Design & UX
- **Style:** [e.g., Clean, minimalist, high-contrast dashboard / dark mode / editorial layout.]
- **Responsiveness:** Must adapt cleanly to both desktop and mobile viewports.
- **Feedback States:** Include clear empty states, loading spinners during async actions, and inline error alerts.