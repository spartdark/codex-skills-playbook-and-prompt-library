# Quickstart

## Instalar una skill en menos de dos minutos

```bash
git clone https://github.com/spartdark/codex-skills-playbook-and-prompt-library.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R codex-skills-playbook-and-prompt-library/skills/skill-sdd-architect \
  "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Elegir la skill correcta

- Usa `skill-git-github-expert` si vas a trabajar con ramas, PRs, releases o hygiene de historial.
- Usa `skill-rag-research` si necesitas grounding, evaluación de fuentes o respuestas con citas.
- Usa `skill-sdd-architect` si vas a convertir una idea difusa en PRD, plan técnico y tareas ejecutables.

## Primer uso sugerido

- Git & GitHub Expert: "Prepárame una estrategia segura para abrir un PR limpio".
- RAG Research: "Diseña un pipeline RAG con fuentes privadas y citas verificables".
- SDD Architect: "Convierte esta idea en especificación, plan y checklist de entrega".
