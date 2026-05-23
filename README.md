# Codex Skills Playbook and Prompt Library

Biblioteca pública e instalable de skills para Codex, pensada para clonar, versionar, compartir y publicar como releases de GitHub.

Este repositorio organiza cada skill como una unidad distribuible con:

- `SKILL.md` como punto de entrada operativo.
- `prompt.md` con enfoque, tono y guardrails.
- `skill.json` con metadatos instalables.
- `README.md` y `CHANGELOG.md` propios.
- ejemplos y assets reutilizables.

## Version actual

La version actual del repositorio es `0.5.0`.

## Skills incluidas

- `skill-git-github-expert`: buenas prácticas de Git, ramas, PRs, commits y releases.
- `skill-rag-research`: diseño y ejecución de investigación RAG con grounding y citas verificables.
- `skill-sdd-architect`: desarrollo guiado por especificaciones, criterios de aceptación y trazabilidad.
- `skill-intent-spec-context-generation-validation`: ISCGV++ Product Operating System para pasar de idea ambigua a PRD auditable y validable.
- `skill-intent-spec-context-generation-validation-en`: versión en inglés de ISCGV para convertir ideas ambiguas en PRDs validados y accionables.
- `skill-youtube-transcript`: extracción y normalización de transcripciones públicas de YouTube como fuente trazable.
- `skill-codex-engineering-pre-read`: pre-reads tecnicos con Codex para preparar decisiones, riesgos, gaps de validacion y tareas verificables.

## Plugins incluidos

- `youtube-ai-researcher`: analisis grounded de videos, transcripciones y patrones de YouTube para aprendizajes, ideas, workflows, monetizacion y prompts detectados.
- `reddit-ai-researcher`: analisis grounded de posts y comentarios de Reddit para senales de IA, software, producto, monetizacion, dolores de usuario y mejoras de proceso.

## Estructura principal

```text
.
├── AGENTS.md
├── catalog.json
├── docs/
├── install/
├── plugins/
│   ├── reddit-ai-researcher/
│   └── youtube-ai-researcher/
├── skills/
│   ├── skill-git-github-expert/
│   ├── skill-intent-spec-context-generation-validation/
│   ├── skill-intent-spec-context-generation-validation-en/
│   ├── skill-codex-engineering-pre-read/
│   ├── skill-rag-research/
│   ├── skill-sdd-architect/
│   └── skill-youtube-transcript/
└── templates/
    ├── project-ai-starter/
    └── skill-template/
```

## Inicio rapido para IA

Este repositorio incluye una capa de gobernanza para usarlo como punto de partida en proyectos nuevos o existentes:

- [`AGENTS.md`](AGENTS.md): punto de entrada token-light para Codex y otros agentes.
- [`docs/ai/governance.md`](docs/ai/governance.md): reglas de adopcion, memoria, evidencia y orden de lectura.
- [`templates/project-ai-starter/`](templates/project-ai-starter/): plantilla portable para copiar a otro repo.
- [`knowledge/projects/ia-learning/reuse-backlog.md`](knowledge/projects/ia-learning/reuse-backlog.md): candidatos para convertir knowledge en docs, templates, skills o plugins.

Flujo recomendado para un proyecto nuevo:

1. Copia `templates/project-ai-starter/` al repo destino.
2. Completa `PROJECT_AI_PROFILE.md`.
3. Renombra `knowledge/projects/_template/` a `knowledge/projects/<project-id>/`.
4. Mantén `AGENTS.md` corto y delega el detalle a documentos enlazados.
5. Pide a Codex que lea primero `AGENTS.md` y luego solo los archivos necesarios para la tarea.

Cuando un aprendizaje se repita, promuevelo de forma gradual:

```txt
knowledge -> docs/templates -> skill -> plugin
```

## Instalación rápida

1. Clona el repositorio.
2. Elige la skill que quieras instalar.
3. Copia la carpeta de la skill a tu directorio de skills de Codex.

Ejemplo:

```bash
git clone https://github.com/spartdark/codex-skills-playbook-and-prompt-library.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R codex-skills-playbook-and-prompt-library/skills/skill-git-github-expert \
  "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Guías detalladas:

- [Instalación paso a paso](install/install.md)
- [Quickstart](install/quickstart.md)
- [Compatibilidad](install/compatibility.md)

## Cómo usar una skill

Una vez instalada, la skill puede activarse cuando el prompt del usuario coincide con su propósito o cuando se la menciona por nombre. Consulta el `README.md` de cada skill para ver ejemplos de activación recomendados.

## Catálogo instalable

El archivo [`catalog.json`](catalog.json) describe el inventario público de skills, sus versiones, tags, entrypoints y nivel de estabilidad. Ese catálogo puede consumirse desde herramientas internas, scripts de bootstrap o flujos de publicación.

## Versionado

Este repositorio usa SemVer:

- el repo publica una versión global en [`VERSION`](VERSION);
- cada skill publica su propia versión en `skill.json`;
- los cambios históricos se documentan en [`CHANGELOG.md`](CHANGELOG.md) y en el changelog individual de cada skill.

Consulta:

- [Política de versionado](docs/versioning.md)
- [Convenciones de naming](docs/naming-conventions.md)

## Publicación y releases

El flujo recomendado es:

1. crear cambios en una rama;
2. actualizar `VERSION`, `catalog.json` y changelogs;
3. abrir PR;
4. fusionar a `main`;
5. crear un tag `vX.Y.Z`;
6. publicar release en GitHub.

Más detalle:

- [Publishing](docs/publishing.md)
- [Contributing](CONTRIBUTING.md)

## Licencia

Distribuido bajo licencia [MIT](LICENSE).
