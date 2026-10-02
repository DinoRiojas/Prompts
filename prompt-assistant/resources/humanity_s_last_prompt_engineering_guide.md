# Humanity’s Last Prompt Engineering Guide

**By Matthew Berman & Nick Wentz**  
*Forward Future (FF) — Learn faster. Work smarter.*

---

## Overview

Most guides on prompt engineering either overcomplicate the basics or give you vague tips that don’t hold up when you actually try to use them.

This one’s different.

We’ve done the homework for you—gathering best practices from OpenAI, Google, Anthropic, and real-world testing—and broken it all down into something you can actually use. Whether you’re in sales, operations, marketing, or leadership, this guide will show you how to get dramatically better results from ChatGPT, Claude, Gemini, and other chat-based AI tools.

---

## How to Use This Guide

This guide is designed to help you become dramatically more effective at using AI tools like ChatGPT, Claude, and Gemini—whether you’re just getting started or already using them in your daily work.

### Structured for Action
* **Section 1:** Introduces how prompting works and why it matters.
* **Section 2:** Explains what makes a prompt work—and how models think.
* **Section 3:** Helps you diagnose and fix bad prompts fast.
* **Section 4:** Breaks down 11 foundational prompting techniques with real examples.
* **Section 5:** Gives ready-to-use templates for common business roles.
* **Section 6:** Includes a scorecard and worksheet to refine and evaluate your prompts.
* **Section 7:** Offers a glossary of key terms for beginners and pros alike.

### How to Use It
* Skim the techniques—then go deep on the ones most relevant to your workflows.
* Use the diagnostic section (Section 3) any time the AI gives poor or vague results.
* Return to the scorecard when refining a prompt for better consistency or results.

### Who It’s For
This guide is for professionals—in marketing, sales, operations, leadership, and beyond—who want to get better results from AI without needing technical expertise.

### What You’ll Learn
* How prompts actually work behind the scenes
* Proven techniques to improve accuracy and creativity
* Ready-to-use templates for common business roles
* Common mistakes to avoid

---

## Section 1: Introduction to Prompt Engineering

Prompting isn't about tricking AI—it’s about teaching it to think clearly. Large language models (LLMs) like ChatGPT, Claude, and Gemini are fundamentally prediction engines. Given an input (your prompt), they generate the most likely next word based on patterns learned from massive amounts of text. That makes your prompt the blueprint.

A vague request will produce vague output. But a clear, well-structured prompt? That’s how you get useful, specific, and often surprisingly intelligent responses.

### Why Prompt Engineering Matters
Prompt engineering is the skill of designing effective instructions for AI. It doesn’t require coding, ML knowledge, or advanced technical skills. What it does require is the ability to be clear, specific, and intentional with your inputs.

A good prompt tells the model:
* **Who it is:** (`"You are a product strategist..."`)
* **What to do:** (`"Summarize this in 3 bullet points."`)
* **What it’s working with:** (`Input: text, table, scenario, etc.`)
* **How to respond:** (`e.g., bullet list, JSON, tone, word count`)

Once you learn how to structure that input—and iterate when things go sideways—you can:
* Summarize complex documents in seconds
* Brainstorm new product ideas or messaging
* Analyze data, extract patterns, or generate insights
* Role-play expert conversations
* Automate repetitive writing and analysis tasks

### Prompting Is a Leverage Skill
The better you prompt, the more productive and valuable AI becomes in your workflows. It’s not just a shortcut—it’s a force multiplier.

> **Key Takeaway:**  
> In most cases where AI gives poor output, the issue isn’t the model. **It’s the prompt.**  
> That’s why prompt engineering is one of the most valuable skills in the AI era.

You don't need to become a "prompt hacker." You just need to learn how to speak the model's language.

---

## Section 2: What Makes a Prompt Work?

Think of it like giving a highly capable assistant a task: if you don’t explain what you want, how you want it, and why it matters, the results may be vague, verbose, or just flat-out wrong.

Prompts are affected by more than just what you type:

| Factor | Why It Matters |
| :--- | :--- |
| **Model** | Each LLM has unique strengths, capabilities, and quirks. |
| **Context** | Input quality (documents, examples) impacts reasoning and accuracy. |
| **Structure** | Clear formatting improves output consistency and usefulness. |
| **Style + Tone** | You can control formality, voice, or persona. |
| **Model Settings** | Output length, temperature, and sampling all influence creativity vs. precision. |

Prompt engineering is not a one-and-done process—it’s iterative. You’ll often need to test, tweak, and refine to get the best results.

### Behind the Scenes: How Language Models Think
LLMs are prediction engines. They don't think like humans—they generate the next most likely word (token) based on the sequence you give them, plus everything they’ve seen during training.

That means your prompt is effectively setting the stage: you’re steering the model's attention, telling it what type of answer to aim for, and how to structure its response. Small changes in how you phrase your prompt can lead to radically different outputs.

### LLM Output Configuration (What You Can Control)
Most AI platforms (like ChatGPT, Claude, Gemini) let you adjust settings that affect how responses are generated:

| Setting | What It Does |
| :--- | :--- |
| **Temperature** | Controls randomness. Lower = more focused, higher = more creative. |
| **Max tokens** | Caps the length of the response. Prevents run-ons. |
| **Top-p / Top-k** | Controls which words the model can choose from when generating responses. |

> **Pro Tip:**  
> For predictable, factual responses, set temperature to **$0 - 0.3$**.  
> For creativity, **$0.7 - 1.0$** is better.

---

## Section 3: Fixing Bad Prompts — Common Mistakes & How to Improve Them

Poor results often come from unclear, vague, or under-specified prompts. Below are common weak prompts and their improved versions:

| Problem | Weak Prompt | Improved Prompt |
| :--- | :--- | :--- |
| **Too vague** | *Write a summary.* | Summarize the article below in 3 bullet points. Focus on key findings, avoid repeating the introduction. |
| **No audience specified** | *Rewrite this for clarity.* | Rewrite this for a busy executive audience. Use short sentences and strip out nonessential background. |
| **Missing role/context** | *Help me with this draft.* | You are a brand copywriter. Improve the tone of this draft to make it more confident and modern. |
| **No format instruction** | *What's a good alternative?* | Suggest 3 alternatives in a numbered list. Include 1-2 sentence explanations for each. |
| **No reasoning requested** | *What's the best option here?* | Evaluate these 3 options. List pros and cons for each, then recommend one with a short rationale. |
| **Unclear intent** | *Turn this into a message.* | Convert the following into a 3-line Slack message that is clear, friendly, and includes a call to action. |
| **Lacks structure** | *Help me improve this.* | Rewrite this performance review to follow this structure: achievements, challenges, and next steps. |

### How to Improve a Prompt: A Simple Checklist
Use this as a quick diagnostic when a model gives poor output:
1. **Am I being too vague?** Be specific about the task and expectations.
2. **Did I include a role or point of view?** Adding `"You are a..."` sets the tone and mindset.
3. **Is the input complete and relevant?** Include all necessary information for the model to reason effectively.
4. **Have I requested a clear format?** Specify if you want bullets, a paragraph, JSON, etc.
5. **Am I asking for reasoning?** If judgment is involved, ask the model to "think step by step" or explain its logic.
6. **Have I broken the task into smaller parts if needed?** Split complex requests into multiple, focused steps.

---

## Section 4: Prompting Techniques

These eleven foundational techniques will help you structure clearer instructions, improve model performance, and adapt to different use cases across business and technical workflows.

---

### 1. Zero-Shot Prompting
* **What it is:** A single instruction without any examples.
* **When to use it:** For simple or well-understood tasks where context is obvious.
* **Core Example:**  
  `"Summarize this customer support ticket in 3 bullet points."`
* **More Examples:**
  * Summarize the following transcript into a one-paragraph executive briefing suitable for a board meeting.
  * Generate 3 headline options for a homepage that emphasizes speed, simplicity, and trust.
  * Based on the meeting notes below, write an email recap with next steps and responsible owners.
  * Extract and rank the top 3 objections raised in this sales call transcript.
* **Tips:**
  * *Beginner:* Start with simple, clear instructions using action verbs like "Summarize," "List," or "Write." Avoid vague words like "help" or "explain."
  * *Intermediate:* Add a format instruction (e.g., "in 3 bullet points" or "as a table") to shape the output and reduce ambiguity.
  * *Advanced:* Combine multiple directives in a single sentence to pack precision (e.g., "Summarize in 3 bullets, each under 10 words, focusing on customer pain points.").

---

### 2. Few-Shot Prompting
* **What it is:** You provide one or more examples to guide the model.
* **When to use it:** When the task involves structure, tone, or formatting that the model might not infer on its own.
* **Core Example:**  
  `"Here's one great follow-up email. Now write another based on this new situation..."`
* **More Examples:**
  * `Example: I want a large pizza with mushrooms and basil. JSON: {"size": "large", "toppings": ["mushrooms", "basil"]}. Now convert this: I'd like a small pizza with olives and tomato.`
  * `Here is an ideal product changelog entry: Improved onboarding flow: Faster load times, clearer CTAs, and better mobile UX. Now write one for the feature update described below.`
  * `Here are two customer support responses that defuse frustration with empathy and clarity. Write a third using the same tone and structure.`
  * `Based on these examples of investor update summaries, write one for this month's company performance.`
  * `Here are a few ideal Slack status messages for when someone is heads-down. Create 5 more in the same style.`
* **Tips:**
  * *Beginner:* Copy the structure of one example and change the inputs. This helps you build pattern recognition.
  * *Intermediate:* Provide a range of examples (short/long, formal/casual) to help the model generalize the style or logic.
  * *Advanced:* Fine-tune examples to emphasize edge cases, errors, or style nuances. Use deliberately contrasting examples to teach distinctions.

---

### 3. System Prompting
* **What it is:** Set clear rules for how the model should behave or structure output.
* **When to use it:** To control tone, format, length, or behavior from the beginning.
* **Core Example:**  
  `"Respond only in JSON. Use the format below."`
* **More Examples:**
  * Always answer using the STAR method (Situation, Task, Action, Result). Respond only in bullet points.
  * Only use language that a 10th-grade reader can understand. Avoid technical terms and acronyms.
  * Provide your answer in Markdown format, using headings, subheadings, and bolded key terms.
  * Every time you respond, include a short summary sentence first, followed by your full explanation.
* **Tips:**
  * *Beginner:* Use simple system rules like "Respond in a friendly tone" or "Answer in bullet points."
  * *Intermediate:* Layer constraints like tone, format, and audience all in one system prompt.
  * *Advanced:* Use system prompts to enforce behavior across multiple turns in a chat (e.g., always speak as a mentor, always return Markdown with code blocks, etc.).

---

### 4. Role Prompting
* **What it is:** Assign a persona or point of view.
* **When to use it:** When the model needs to adopt a specific tone, expertise level, or perspective.
* **Core Example:**  
  `"You are a CFO coaching a startup founder on financial risk."`
* **More Examples:**
  * You are a financial advisor. Recommend three strategies for someone with $\$10,000$ to invest and a five-year time horizon.
  * You are a senior PMM at a B2B SaaS company. Write a 3-sentence value proposition for a new AI workflow feature.
  * You are a startup CEO preparing for a pre-seed pitch. Reframe this vision statement to be more investor-friendly.
  * You are a customer success manager. Draft a proactive check-in email for an enterprise client showing early signs of churn.
  * You are a technical recruiter. Review the résumé snippet below and write a 2-line summary of the candidate's profile.
* **Tips:**
  * *Beginner:* Start with "You are a..." followed by a familiar job title (e.g., "You are a content strategist").
  * *Intermediate:* Match the role to the task. Use domain-specific roles (e.g., "You are a data privacy consultant") to shape tone and accuracy.
  * *Advanced:* Combine roles with context and format constraints for nuanced control (e.g., "You are a veteran PMM writing a short memo for legal approval").

---

### 5. Contextual Prompting
* **What it is:** Provide relevant background, data, or a scenario.
* **When to use it:** When task success depends on domain-specific context or past conversation history.
* **Core Example:**  
  `"Here's our brand voice guide. Rewrite this paragraph using that style."`
* **More Examples:**
  * You are writing for a retro gaming blog. Suggest three article ideas based on 1980s arcade culture.
  * Using the customer persona and product description below, write a 2-sentence ad hook that appeals to first-time users.
  * Here's a summary of our brand's tone guidelines. Rewrite the following help center article to match that tone.
  * Given our revenue goals and Q3 priorities, generate 3 OKR options for the sales enablement team.
  * Review this engineering roadmap and suggest a revised timeline, given the team's current velocity and bandwidth constraints.
* **Tips:**
  * *Beginner:* Copy and paste a relevant doc or snippet before the prompt to give the model something to work with.
  * *Intermediate:* Use summaries instead of raw data when the input is long. Pre-frame: "Here's what you need to know..."
  * *Advanced:* Chain multiple inputs (e.g., $\text{persona} + \text{doc} + \text{goals}$), and explicitly state how they relate (e.g., "Given this persona and these product notes...").

---

### 6. Step-Back Prompting
* **What it is:** Ask the model to solve a general question first, then apply that insight to a specific task.
* **When to use it:** For creative tasks, complex reasoning, or scenario planning.
* **Comparison:**
  * *Prompt Before:* `"Write a level for a new first-person shooter game."`
  * *Step-back Version:* `"What are 5 common environments in great FPS games?"` $\rightarrow$ Then: `"Now write a level based on one."`
* **More Examples:**
  * Before writing the email, list 3 things the recipient likely values based on their role and company. Then write the email using that context.
  * First, outline the characteristics of a high-performing user onboarding flow. Then critique the one below using that framework.
  * Before drafting product positioning, summarize how our top 3 competitors describe themselves. Then write our version to differentiate.
  * Start by identifying the key emotion this campaign should trigger in customers. Then write a subject line that evokes it.
* **Tips:**
  * *Beginner:* Ask a warm-up question before the real task (e.g., "What does the audience care about?" $\rightarrow$ "Now write the email").
  * *Intermediate:* Use it to deconstruct complex decisions or plans (e.g., $\text{goals} \rightarrow \text{actions} \rightarrow \text{message}$).
  * *Advanced:* Use it for self-discovery or creative ideation chains. Ask the model to generate principles first, then apply them to the prompt task.

---

### 7. Chain-of-Thought Prompting (CoT)
* **What it is:** Instruct the model to show its reasoning step by step.
* **When to use it:** For math, logic, planning, or anything that benefits from transparent reasoning.
* **Core Example:**  
  `"When I was 3, my partner was 3x my age. I'm now 20. How old is my partner? Let's think step by step."`
* **More Examples:**
  * Walk through the steps needed to calculate customer acquisition cost (CAC) using the data provided. Then provide the result.
  * Given this list of product issues, identify which could cause the highest drop in NPS, and explain your reasoning.
  * List the steps a support agent should take to de-escalate the situation described in the chat log.
  * Break down the decision-making process for whether to renew or sunset the feature described. Include cost, usage, and team feedback.
* **Tips:**
  * *Beginner:* Add "Explain your reasoning" or "Think step by step" to the end of your prompt.
  * *Intermediate:* Ask the model to list pros and cons, compare options, or walk through logic to justify a recommendation.
  * *Advanced:* Combine with structured outputs (e.g., tables of tradeoffs, multi-step formulas) or nested reasoning paths.

---

### 8. Self-Consistency
* **What it is:** Run the same prompt multiple times and choose the most frequent or consistent result.
* **When to use it:** For high-stakes or ambiguous tasks where accuracy matters.  
  *(Note: Requires a model that supports variability via temperature, e.g., $0.7$ or higher).*
* **Core Example:**  
  `"What's the most likely cause of churn in this case? Run this three times and summarize common themes."`
* **More Examples:**
  * Ask a model to classify an ambiguous email as "important" or "not important" multiple times, then take the majority vote.
  * Classify this review as positive, neutral, or negative five times and return the most frequent label with reasoning.
  * Generate three different explanations for this customer churn event. Then summarize the one that appears most consistently.
  * Write five taglines for this product feature. Then identify the most recurring theme or hook among them.
  * Answer this ambiguous question three times, then decide which version is most likely to align with the user's intent.
* **Tips:**
  * *Beginner:* Run the same prompt a few times and compare results. Choose the best version manually.
  * *Intermediate:* Ask the model to repeat a task 3-5 times and select the most common or consistent answer.
  * *Advanced:* Instruct the model to generate multiple answers, evaluate them for consistency or correctness, and select the best one.

---

### 9. Tree of Thoughts (ToT)
* **What it is:** Explore multiple reasoning paths instead of a single linear answer.
* **When to use it:** For brainstorming, decision-making, or tasks with multiple valid outcomes.  
  *(Note: Often used with agents or frameworks that track branching logic).*
* **Core Example:**  
  `"List three strategies for increasing user retention, with pros and cons for each. Then select the most promising."`
* **More Examples:**
  * Explore three different GTM strategies for launching this product in Q4. Then evaluate their tradeoffs and recommend one.
  * Generate 3 unique frameworks for organizing this internal knowledge base. Justify each approach and select the most scalable one.
  * Outline 3 alternative messaging directions for this new feature. Then score them for clarity, originality, and alignment with brand tone.
  * Imagine three distinct customer objections during the onboarding process. For each, propose a mitigation strategy.
* **Tips:**
  * *Beginner:* Ask the model for "3 different ideas" before choosing one.
  * *Intermediate:* Prompt for multiple options, then ask the model to evaluate them for clarity, impact, or feasibility.
  * *Advanced:* Use ToT as a decision-making engine—branch multiple reasoning paths, evaluate tradeoffs, then synthesize the best choice.

---

### 10. ReAct (Reason + Act)
* **What it is:** The model reasons step-by-step and performs actions, such as searching the web or calling a tool.
* **When to use it:** For tool-augmented agents or systems that require external data retrieval or interaction.
* **Core Example:**  
  `"Look up the definition of 'prompt injection' and explain it simply."`
* **More Examples:**
  * Search how many children each member of Metallica has. Sum the total. Output only the final number.
  * Search for this company's most recent funding round. Then write a congratulatory email that references the announcement.
  * Use a code interpreter to calculate the monthly burn rate from this spreadsheet. Then write a plain-English summary.
  * Search for the latest update to the GDPR regulation. Then suggest one change to our current data policy.
  * Find the Glassdoor average rating for this company. Based on the result, write an outreach message addressing potential concerns.
* **Tips:**
  * *Beginner:* Use tools like "Search" or "Calculate" and then manually combine results with AI output.
  * *Intermediate:* Use prompts like "Search for X, then summarize it in 2 lines" to simulate a chain of thought + action.
  * *Advanced:* Combine tool use, reasoning, and generation in one loop (e.g., "Search X $\rightarrow$ Compare Y $\rightarrow$ Generate Z"). Use agents or code interpreter if available.

---

### 11. Automatic Prompt Engineering (APE)
* **What it is:** Use AI to generate and test variations of prompts.
* **When to use it:** When you're designing for scale, training a chatbot, or optimizing prompt performance.
* **Core Example:**  
  `"Give me 10 variations of how someone might order a Metallica T-shirt. Then: test, score, and select the best one."`
* **More Examples:**
  * Write 10 alternate prompts for asking AI to summarize a technical article for a general audience. Then pick the clearest one.
  * Generate 5 prompt variations for helping a user reframe negative self-talk. Rank them from most supportive to most neutral.
  * Create 7 prompt versions that ask users to describe product feedback. Tag each by tone (formal, casual, creative).
  * Produce 5 options for asking ChatGPT to generate campaign ideas for a fintech company. Rate them based on clarity and specificity.
* **Tips:**
  * *Beginner:* Ask the model to rewrite your prompt in 3 clearer variations and choose your favorite.
  * *Intermediate:* Generate 5-10 versions with different tones, formats, or levels of detail—then test them across tasks.
  * *Advanced:* Set up side-by-side testing or use frameworks like PromptLayer, DSPy, or PromptFoo to evaluate performance at scale.

---

## Section 5: Role-Based Prompt Templates

These prompts are designed for everyday use across key business functions. Each one is adaptable—just swap in your input.

### Operations
* **Prompt 1:** You are a process improvement analyst. Review the following workflow and suggest three ways to reduce manual steps.  
  *(Tone: Analytical, concise)*
* **Prompt 2:** You are an operations manager. Based on the data below, identify any scheduling conflicts and recommend an optimized shift plan.  
  *(Tone: Objective, action-oriented)*
* **Prompt 3:** You are a logistics coordinator. Rewrite these internal instructions so they're clear, step-by-step, and easy to follow for new hires.  
  *(Format: Ordered list)*

### Sales
* **Prompt 1:** You are an outbound strategist. Write a LinkedIn message to a VP of Finance at a mid-sized SaaS company. Make it conversational, relevant, and end with a question.  
  *(Tone: Conversational, focused)*
* **Prompt 2:** You are a sales coach. Based on this call transcript, identify three missed opportunities and suggest a better framing of the product's value.  
  *(Tone: Constructive, direct)*
* **Prompt 3:** You are a strategic account executive. Write a follow-up note after a promising discovery call. Include 1 recap line, 2 insights, and 1 CTA.  
  *(Format: Structured email outline)*

### Marketing
* **Prompt 1:** You are a conversion copywriter. Rewrite the following landing page headline to make it more urgent, specific, and benefit-driven. Provide three options.  
  *(Tone: Punchy, persuasive)*
* **Prompt 2:** You are a content strategist. Turn this blog post into a three-post LinkedIn carousel script with a hook, a breakdown, and a CTA.  
  *(Format: Slide-by-slide copy outline)*
* **Prompt 3:** You are a brand voice expert. Review this homepage and suggest two changes to make it more consistent with a warm, authoritative tone.  
  *(Tone: Editorial)*

### Management
* **Prompt 1:** You are a leadership coach. A team lead is struggling with prioritization. Share three frameworks they can use to manage competing requests.  
  *(Tone: Supportive, instructive)*
* **Prompt 2:** You are a department head. Draft a message to your team acknowledging recent tension and outlining next steps to restore alignment.  
  *(Tone: Empathetic, confident)*
* **Prompt 3:** You are an executive preparing for a board update. Summarize your top three metrics, growth levers, and open risks in under 150 words.  
  *(Format: Bulleted or block-style summary)*

### Content Development
* **Prompt 1:** You are a senior editor. Improve the clarity, tone, and structure of this article. Make it more engaging without losing substance.  
  *(Tone: Crisp, confident)*
* **Prompt 2:** You are a content repurposing expert. Turn this long-form article into one tweet thread, one newsletter excerpt, and one TikTok script.  
  *(Format: Multi-output summary)*
* **Prompt 3:** You are a product copywriter. Write three microcopy options for a call-to-action button encouraging users to upgrade.  
  *(Tone: Clear, value-driven)*

### Data Analysis
* **Prompt 1:** You are a business analyst. Interpret the following product usage report and highlight three meaningful trends.  
  *(Tone: Insightful, plain-language)*
* **Prompt 2:** You are a data storyteller. Write a 5-sentence summary of this chart for an executive audience with no technical background.  
  *(Tone: Accessible, high-level)*
* **Prompt 3:** You are a customer insights lead. Based on this NPS feedback dataset, extract two recurring themes and suggest one recommendation.  
  *(Format: Bullet points or numbered summary)*

### Learning & Development
* **Prompt 1:** You are an instructional designer. Turn this onboarding checklist into a simple 5-step training module for new hires.  
  *(Format: Step-by-step breakdown)*
* **Prompt 2:** You are a corporate trainer. Draft a Slack message inviting employees to a new AI literacy workshop. Make it short, clear, and inviting.  
  *(Tone: Friendly, motivating)*
* **Prompt 3:** You are a learning coach. Based on this employee feedback, recommend two personalized learning paths and one potential mentor pairing.  
  *(Tone: Supportive, customized)*

---

## Section 6: Prompt Scorecard & Worksheets

Prompt engineering is an iterative process. The more you test, adjust, and document, the more consistent your results become. Use the following scorecard and worksheet to improve prompt quality, troubleshoot issues, and build a reusable prompt library.

### Prompt Quality Scorecard
Use this 7-point checklist to evaluate the strength of a prompt. For each item, give yourself a score from 1 (no) to 5 (excellent).

| Question | Score (1-5) |
| :--- | :--- |
| 1. Is the task clearly defined? | |
| 2. Did I assign a clear role or persona to the model? | |
| 3. Did I provide the right context or background information? | |
| 4. Did I specify a desired output format (list, paragraph, JSON)? | |
| 5. Did I include instructions for tone, length, or constraints? | |
| 6. If applicable, did I request reasoning or step-by-step thinking? | |
| 7. Is the prompt easy to understand and free of ambiguity? | |

#### Scoring Guide
* **30 – 35:** Strong, high-confidence prompt
* **20 – 29:** Decent, may benefit from revisions
* **Below 20:** Likely to produce inconsistent or unclear outputs

---

### Prompt Refinement Worksheet
Use this template to document and refine your most important prompts over time.

| Field | Notes |
| :--- | :--- |
| **Prompt Name** | *e.g., Weekly Report Summary* |
| **Goal** | *e.g., Summarize usage data into executive-facing bullet points* |
| **Model** | *e.g., ChatGPT-4, Claude 3, Gemini Pro* |
| **Temperature** | *e.g., 0.2 (factual), 0.8 (creative)* |
| **Output Format** | *e.g., JSON, table, three bullet points* |
| **Prompt (Initial)** | *[Paste full prompt]* |
| **Output Sample** | *[Paste or summarize the result]* |
| **What Worked** | *[Note what the model got right]* |
| **What Needs Revision** | *[Note issues: tone, accuracy, structure, hallucination, etc.]* |
| **Final Version** | *[Paste final version after refinement]* |
| **Result Rating** | Strong / Okay / Needs Work |

---

### Tips for Testing Prompts
* Change one variable at a time (e.g., role, tone, output format).
* Compare multiple outputs with the same prompt using different models.
* Keep a running prompt library to reuse and adapt over time.
* If a prompt fails, isolate why: unclear instruction, missing input, poor formatting?

> **Final Thought:**  
> Prompting isn’t about tricks. It’s about clarity. The better you guide the model, the more valuable it becomes. Once you learn to speak its language, you can do almost anything from strategy to storytelling to automation.  
> This guide is your starting point. Now go make the AI work for you.

---

## Section 7: Glossary of Common Prompt Engineering Terms

| Term | Definition | Example / Context |
| :--- | :--- | :--- |
| **Prompt** | The input or instruction you give to a language model to generate a response. | `"Summarize this article in 3 bullet points."` |
| **LLM (Large Language Model)** | A type of AI trained on vast amounts of text to predict and generate language. Examples include ChatGPT, Claude, and Gemini. | ChatGPT is an LLM developed by OpenAI. |
| **Token** | A chunk of text the model processes, usually a word or word part. Used to count input/output length. | `"summarize"` $= 1\text{ token}$; `"artificial intelligence"` $= 2\text{--}3\text{ tokens}$ |
| **Zero-Shot Prompting** | Giving the model a task without any examples. | `"List 3 benefits of this product."` |
| **Few-Shot Prompting** | Giving the model examples to help it understand how to respond. | *Example:* `"Hi, I'm Alex."` $\rightarrow$ `"Hello Alex, nice to meet you!"` |
| **System Prompt** | A behind-the-scenes instruction that sets the model's behavior or output format. | `"Always respond in JSON."` |
| **Role Prompting** | Telling the model to take on a specific persona or point of view. | `"You are a product manager..."` |
| **Contextual Prompting** | Including relevant background or data to help the model generate better results. | `"Given our brand voice guidelines, write a tweet..."` |
| **Step-Back Prompting** | Asking the model to reflect or solve a broader question before executing the task. | `"What does the user want?"` Then write the message. |
| **Chain-of-Thought (CoT)** | Instructing the model to think through reasoning steps before giving a final answer. | `"Think step by step..."` |
| **Self-Consistency** | Running the same prompt multiple times and selecting the most common or consistent result. | Used for ambiguous or high-stakes tasks. |
| **Tree of Thoughts (ToT)** | Exploring multiple reasoning paths or options before converging on a solution. | `"Explore 3 campaign strategies and evaluate pros and cons."` |
| **ReAct** | A prompting framework where the model reasons and then acts—often used with tools like web search or code interpreters. | `"Search for X" \rightarrow "Summarize" \rightarrow "Recommend Y"` |
| **Automatic Prompt Engineering (APE)** | Using AI to generate, test, and refine multiple versions of a prompt. | `"Write 5 variations of this onboarding prompt and rate them for clarity."` |
| **Temperature** | A setting that controls randomness. Lower = more focused, higher = more creative. | $0.2 =$ precise, $0.8 =$ more varied output |
| **Top-p / Top-k** | Sampling settings that determine which words the model can choose from next—affects diversity in output. | Useful for tuning creativity vs. precision. |
| **Max Tokens** | The maximum length (in tokens) that the model can generate. | Prevents overly long or rambling answers. |
| **Hallucination** | When the model generates false or made-up information that sounds correct. | `"This company raised $50M"` when it actually didn't. |
| **Format Instruction** | A prompt that specifies how the output should be structured (e.g., list, table, paragraph). | `"Respond in JSON"` or `"Use bullet points."` |
| **Persona** | A defined role or identity assigned to the AI in a prompt. | `"You are a friendly customer support agent."` |

---

### About Forward Future
*Helping everyone benefit from AI with timely news & accessible education.*

* **Website:** [forwardfuture.ai](https://forwardfuture.ai)
* **YouTube:** `@matthew_berman`
* **X:** `@forward_future_`

*Thanks for reading!*  
*— Matt, Nick, and the Forward Future Team*