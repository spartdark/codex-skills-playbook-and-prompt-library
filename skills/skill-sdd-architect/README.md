# SDD Architect

Skill pública para convertir ideas vagas o features complejas en especificaciones, planes técnicos y trabajo ejecutable.

## Qué cubre

- problem framing;
- objetivos y alcance;
- requisitos funcionales y no funcionales;
- criterios de aceptación;
- plan técnico por fases;
- revisión de alineación entre requisitos e implementación.

## Casos de uso

- "Convierte esta idea en una especificación publicable".
- "Necesito un plan técnico con riesgos y tareas".
- "Revisa si lo implementado realmente cumple el PRD".

## Instalación

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-sdd-architect "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Contenido

- `SKILL.md`: flujo base y activadores.
- `prompt.md`: principios de facilitación.
- `skill.json`: metadata instalable.
- `examples/`: ejemplo práctico.
- `assets/`: checklist para revisar especificaciones.
