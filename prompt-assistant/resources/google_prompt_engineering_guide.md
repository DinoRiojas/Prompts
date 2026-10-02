# Prompt Engineering: Principles, Techniques, and Best Practices

*Based on the Google Whitepaper by Lee Boonstra (February 2025)*

---

## 1. Introduction & Overview

Large Language Models (LLMs) operate as next-token prediction engines. When provided sequential text as input, the model predicts the subsequent token based on statistical patterns learned during pretraining. 

**Prompt engineering** is the disciplined practice of designing and refining inputs to guide LLMs toward accurate, contextually relevant, and properly formatted outputs. While any user can interact with LLM interfaces, maximizing output quality requires understanding:
- Model architectures and training baselines.
- Runtime sampling hyperparameters.
- Structured prompting strategies.
- Iterative evaluation and testing workflows.

---

## 2. LLM Output Configuration & Hyperparameters

Configuring inference parameters is critical to controlling token selection and output length.

### Output Length (`max_output_tokens`)
- Dictates the maximum number of tokens generated before generation halts.
- **Key Insight:** Reducing token limits cuts off generation; it does *not* inherently make the model's writing style more concise. Stylistic brevity must be instructed via the prompt itself.
- Limiting tokens helps avoid excessive compute usage, latency, and costs, and prevents unbounded output loops in agent frameworks (e.g., ReAct).

### Sampling Controls

Token generation relies on probability distributions over vocabulary tokens. Three key parameters dictate this selection:

| Parameter | Function | Low Values | High Values | Recommended Baseline |
| :--- | :--- | :--- | :--- | :--- |
| **Temperature** ($T$) | Scales the probability logits (analogous to softmax temperature). | Near $0$: Deterministic, greedy decoding, predictable. | $0.8 - 1.0+$: Diverse, creative, higher variance. | $0.0$ for math/logic; $0.2$ for factual tasks; $0.9$ for creative writing. |
| **Top-K** | Limits token selection to the top $K$ most probable candidates. | $1$: Pure greedy decoding. | $40+$: Broader pool of candidate tokens. | $20 - 40$ |
| **Top-P** (Nucleus) | Selects candidates dynamically from the smallest set whose cumulative probability reaches threshold $P$. | Low ($<0.5$): Highly focused on dominant tokens. | Close to $1.0$: Retains almost all non-zero probability tokens. | $0.9 - 0.95$ |

#### Parameter Interactions & Boundary Behaviors
- **$T = 0$:** Overrides Top-K and Top-P, enforcing greedy selection.
- **Top-K = 1:** Disables the effect of Temperature and Top-P.
- **Repetition Loop Bug:** Can occur at both extremes. At very low temperatures, models may get stuck in repetitive deterministic loops. At very high temperatures, random selections can cycle back into previously seen phrases.

---

## 3. Core Prompting Techniques

### 3.1 Zero-Shot Prompting
Provides only task instructions and context without demonstrations.

```text
Goal: Classify movie review sentiment.
Model: gemini-pro | Temp: 0.1 | Max Tokens: 5

Prompt:
Classify movie reviews as POSITIVE, NEUTRAL, or NEGATIVE.
Review: "Her" is a disturbing study revealing the direction humanity is headed if AI is allowed to keep evolving, unchecked. I wish there were more movies like this masterpiece.
Sentiment:

Expected Output:
POSITIVE
```

### 3.2 Few-Shot Prompting
Provides one or more input-output demonstrations to establish structural, formatting, or semantic patterns before the actual task.

```text
Goal: Parse pizza orders into valid JSON.
Model: gemini-pro | Temp: 0.1 | Max Tokens: 250

Prompt:
Parse a customer's pizza order into valid JSON:

EXAMPLE:
Order: Can I get a large pizza with tomato sauce, basil and mozzarella
JSON Response:
{
  "size": "large",
  "type": "normal",
  "ingredients": [["tomato sauce", "basil", "mozzarella"]]
}

TASK:
Order: Now, I would like a large pizza, with the first half cheese and mozzarella. And the other tomato sauce, ham and pineapple.
JSON Response:
```

*Rule of Thumb:* Use 3–5 diverse examples covering representative edge cases.

---

### 3.3 System, Role, and Contextual Prompting

These three prompt dimensions serve distinct functions:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. SYSTEM PROMPT                                            │
│    Establishes core boundaries, tools, and output format    │
│    (e.g., "Always respond in JSON. Follow strict safety.")  │
├─────────────────────────────────────────────────────────────┤
│ 2. ROLE PROMPT                                              │
│    Shapes perspective, voice, and stylistic persona         │
│    (e.g., "Act as an experienced travel journalist.")       │
├─────────────────────────────────────────────────────────────┤
│ 3. CONTEXTUAL PROMPT                                        │
│    Provides dynamic, situational background data            │
│    (e.g., "The target audience is parents with toddlers.")  │
└─────────────────────────────────────────────────────────────┘
```

#### JSON Output Enforcement
Enforcing JSON via system schemas limits hallucination and produces parseable responses:

```text
Goal: Extract entities into structured JSON.
Model: gemini-pro | Temp: 0.1 | Max Tokens: 512

Prompt:
Extract movie reviews into JSON conforming to the schema below.

Schema:
{
  "name": String,
  "sentiment": "POSITIVE" | "NEGATIVE" | "NEUTRAL"
}

Review: "Her" is a disturbing study revealing the direction humanity is headed...
JSON Response:
```

---

### 3.4 Step-Back Prompting
Improves domain reasoning by prompting the model to first formulate broader principles or concepts before tackling the specific task.

1. **Step-Back Query:**
   ```text
   Prompt: Based on popular first-person shooter games, what are 5 key environmental settings that make level design engaging and challenging?
   ```
2. **Execution Prompt:**
   ```text
   Context: [Inject the 5 settings generated from step 1]
   Task: Select one setting from above and write a single-paragraph storyline for a new first-person shooter level.
   ```

---

### 3.5 Chain of Thought (CoT) Prompting
Breaks complex problems into sequential reasoning steps prior to generating the final answer. Highly effective for mathematical, algorithmic, and analytical reasoning.

```text
Prompt:
When I was 3 years old, my partner was 3 times my age. Now, I am 20 years old. How old is my partner? Let's think step by step.

Output:
1. When I was 3, my partner was 3 * 3 = 9 years old.
2. The age difference is 9 - 3 = 6 years (partner is older).
3. Now I am 20 years old.
4. My partner's current age is 20 + 6 = 26 years old.
The partner is 26 years old.
```

*CoT Best Practices:*
- Set temperature to `0` for reproducible, greedy deduction.
- Structure output instructions so reasoning steps precede the final extraction token.

---

### 3.6 Self-Consistency
Mitigates errors in linear chain-of-thought generation by:
1. Generating multiple independent reasoning chains using higher temperature ($T \approx 0.7$).
2. Parsing the isolated answer from each path.
3. Applying majority voting to select the final answer.

```
                  ┌── Reasoning Path A ──> Output: "IMPORTANT"
                  │
Prompt (Temp 0.7) ┼── Reasoning Path B ──> Output: "NOT IMPORTANT" ──> Majority Vote: "IMPORTANT"
                  │
                  └── Reasoning Path C ──> Output: "IMPORTANT"
```

---

### 3.7 Tree of Thoughts (ToT)
Extends Chain of Thought into non-linear exploration. Instead of pursuing a single line of deduction, the model generates and evaluates multiple intermediate candidate "thoughts," branching into promising paths and backtracking from dead ends.

---

### 3.8 ReAct (Reason + Act)
Integrates reasoning traces with external execution tools (e.g., search engines, Python REPLs, database APIs) inside an agentic loop:

$$\text{Thought} \longrightarrow \text{Action} \longrightarrow \text{Observation} \longrightarrow \text{Updated Thought} \dots$$

```python
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import VertexAI

llm = VertexAI(temperature=0.1)
tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("How many kids do the band members of Metallica have?")
```

---

### 3.9 Automatic Prompt Engineering (APE)
Automates prompt generation and optimization:
1. **Generation:** An LLM generates candidate prompt variations from a task description.
2. **Evaluation:** Candidate prompts are evaluated across test datasets using automated metrics (e.g., BLEU, ROUGE, execution success rates).
3. **Selection & Refinement:** The highest-performing prompt variant is chosen for production or further refinement.

---

## 4. Code Generation, Explanation, and Review

LLMs can be applied across the entire software development lifecycle:

| Coding Task | Strategy | Example Instruction |
| :--- | :--- | :--- |
| **Generation** | Specific inputs, boundaries, and expected shell/language versions. | "Write a Bash script that takes a directory path and prepends 'draft_' to every file inside." |
| **Explanation** | Provide the snippet without comments; request structured functional breakdowns. | "Explain the step-by-step logic of this script, detailing how errors are caught." |
| **Translation** | Provide source code and target language constraints. | "Translate this Bash script into equivalent, idiomatic Python using `pathlib` and `shutil`." |
| **Review & Debug** | Provide source code along with complete tracebacks. | "This script throws `NameError: name 'toUpperCase' is not defined`. Identify the bug and provide a hardened version." |

---

## 5. Comprehensive Best Practices

1. **Provide High-Quality Examples:** Few-shot prompting remains one of the most reliable steering mechanisms.
2. **Favor Direct Instructions over Negative Constraints:**
   - *Better:* "Include only the console name, manufacturer, release year, and sales figures."
   - *Avoid:* "Do not mention games, accessories, or studio history."
3. **Permute Classification Examples:** When configuring few-shot classification prompts, shuffle example labels to prevent the model from learning spurious ordering biases.
4. **Enforce Rigid Schemas:** For programmatic workflows, supply JSON Schemas for both input payloads and expected outputs.
5. **Implement Output Repair Tools:** When relying on high-volume structured outputs, integrate tools like `json-repair` to handle outputs clipped by token limits.
6. **Decouple Prompts from Application Code:** Keep system prompts, dynamic templates, and few-shot registries in external configuration files or prompt management repositories.

---

## 6. Prompt Iteration Tracking Template

Maintain a structured evaluation ledger to benchmark performance across model versions:

| Field | Description / Value |
| :--- | :--- |
| **Prompt ID / Name** | `sentiment_classifier_v1.2` |
| **Objective** | Extract sentiment class and entities from customer reviews into JSON. |
| **Target Model** | `gemini-pro` (or specific snapshot tag) |
| **Hyperparameters** | `Temp: 0.1` \| `Max Tokens: 512` \| `Top-K: 40` \| `Top-P: 0.8` |
| **Prompt Template** | `You are a data extraction assistant... {input_text}` |
| **Observed Output** | `{"sentiment": "NEGATIVE", "name": "Her"}` |
| **Evaluation Score** | OK / Needs Adjustment / Failed |
| **Reviewer Notes** | JSON valid; correctly resolved conflicting emotional adjectives. |