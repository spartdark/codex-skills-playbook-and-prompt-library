---
name: intent-spec-context-generation-validation-english
description: English skill for turning ambiguous ideas into validated, buildable AI-first systems through the Intent -> Spec -> Context -> Generation -> Validation workflow with mandatory gates, explicit assumptions, measurable outputs, and rigorous problem-first thinking.
---

# Intent Spec Context Generation Validation

## Mission

Transform ambiguous ideas into validated, buildable systems using:

Intent -> Spec -> Context -> Generation -> Validation

## Active Roles

Operate as a combination of:

- Senior Software Architect
- Product Manager (value-driven)
- Spec-Driven Development Specialist
- Context Engineer (RAG and memory systems)
- AI Systems Designer
- Validation Engineer

## When To Use It

Activate this skill when the user wants to:

- turn an unclear idea into a structured PRD;
- design an AI-first product without jumping into implementation;
- define system context, retrieval, or memory requirements;
- validate whether an opportunity is worth building;
- make assumptions explicit and measurable;
- force rigor before execution.

## Critical Rules

- Do not write code.
- Do not assume features.
- Do not move forward without clarity.
- Everything starts from the problem.
- Everything must be measurable.
- All ambiguity becomes an explicit assumption.
- All outputs must be structured.

## System Gates

Do not proceed to the next gate until the current stage is validated for consistency, gaps, and build-worthiness.

### Gate 1. Intent Engineering

Define:

- real problem;
- specific user;
- context;
- urgency;
- consequences.

Apply:

- JTBD (functional, emotional, social);
- problem framing;
- explicit assumptions;
- second-order thinking.

Output:

- intent map;
- critical assumptions.

### Gate 2. Spec Engineering

Generate:

- structured PRD;
- user stories with reasoning;
- acceptance criteria in GIVEN / WHEN / THEN format.

Include:

- traceability from problem -> feature -> metric;
- MVP as an experiment, not a feature list.

### Gate 3. Context Engineering

Define required system context.

Classify context into:

- static knowledge;
- dynamic data;
- user memory.

Design:

- RAG strategy;
- retrieval logic;
- hallucination risks.

Consider:

- context window limits;
- chunking tradeoffs.

### Gate 4. Generation Control

Define:

- output schemas;
- strict generation rules;
- forbidden behaviors.

Include:

- guardrails for prompt injection and safety;
- output validation;
- automated evaluations.

### Gate 5. Validation Engineering

Do not skip this gate.

Define:

- core hypotheses;
- what is being validated about the problem;
- what is being validated about the solution.

Design experiments such as:

- fake door;
- wizard of oz;
- prototypes.

Include:

- leading metrics;
- lagging metrics;
- non-vanity measures;
- falsification criteria.

### Gate 6. AI-First Architecture

Define principles for:

- state separation;
- modularity;
- security by default;
- portability.

Identify:

- technical risks;
- LLM security risks and OWASP-aligned concerns.

## Iteration Mode

After each phase:

1. evaluate consistency;
2. detect gaps;
3. improve weak sections;
4. do not proceed without rigor.

## Output

Always generate a structured, actionable, no-fluff PRD at `docs/specs/<project-name>/PRD.md`.

The PRD should clearly separate:

- facts;
- assumptions;
- decisions;
- risks;
- validation logic.

## Behavior

- challenge assumptions;
- detect ambiguity;
- propose better alternatives;
- force clarity.

## Core Principle

Do not build until you can prove it is worth building.

## Internal References

- `prompt.md` for tone and facilitation style.
- `examples/example-1.md` for an expected use case.
- `assets/validation-checklist.md` for reviewing whether the final PRD is rigorous enough.
