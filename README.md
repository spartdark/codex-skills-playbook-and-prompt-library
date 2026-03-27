# Codex Skills Playbook and Prompt Library

Biblioteca pública e instalable de skills para Codex, pensada para clonar, versionar, compartir y publicar como releases de GitHub.

Este repositorio organiza cada skill como una unidad distribuible con:

- `SKILL.md` como punto de entrada operativo.
- `prompt.md` con enfoque, tono y guardrails.
- `skill.json` con metadatos instalables.
- `README.md` y `CHANGELOG.md` propios.
- ejemplos y assets reutilizables.

## Version actual

La versión inicial del repositorio es `0.1.0`.

## Skills incluidas

- `skill-git-github-expert`: buenas prácticas de Git, ramas, PRs, commits y releases.
- `skill-rag-research`: diseño y ejecución de investigación RAG con grounding y citas verificables.
- `skill-sdd-architect`: desarrollo guiado por especificaciones, criterios de aceptación y trazabilidad.

## Estructura principal

```text
.
├── catalog.json
├── docs/
├── install/
├── skills/
│   ├── skill-git-github-expert/
│   ├── skill-rag-research/
│   └── skill-sdd-architect/
└── templates/
    └── skill-template/
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
