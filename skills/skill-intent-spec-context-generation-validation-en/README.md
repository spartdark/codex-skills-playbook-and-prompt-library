# Intent Spec Context Generation Validation

Public English-language skill for turning ambiguous AI-first product ideas into structured, validated, buildable PRDs.

## What It Covers

- intent engineering and JTBD;
- structured PRDs with traceability;
- context, RAG, and memory framing;
- generation guardrails and evaluation logic;
- validation planning with hypotheses, experiments, and falsification;
- AI-first architecture and risk identification.

## Example Use Cases

- "Turn this AI product idea into a serious PRD."
- "Help me validate whether this assistant should exist before we build it."
- "Define the context, retrieval, and validation model for this workflow."

## Installation

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-intent-spec-context-generation-validation-en "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Contents

- `SKILL.md`: workflow, gates, and guardrails.
- `prompt.md`: role, principles, and expected outcomes.
- `skill.json`: installable metadata.
- `examples/`: example prompt.
- `assets/`: review checklist.
