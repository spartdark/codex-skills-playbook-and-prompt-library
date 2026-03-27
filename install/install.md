# Instalación

Esta librería distribuye skills de Codex como carpetas autocontenidas. La instalación consiste en copiar una carpeta de `skills/` al directorio de skills local de Codex.

## Requisitos

- Git para clonar el repositorio.
- Una instalación funcional de Codex.
- Acceso al directorio `${CODEX_HOME:-$HOME/.codex}/skills`.

## Instalación manual de una skill

1. Clona el repositorio:

```bash
git clone https://github.com/spartdark/codex-skills-playbook-and-prompt-library.git
cd codex-skills-playbook-and-prompt-library
```

2. Crea el directorio de skills local si aún no existe:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
```

3. Copia la skill deseada:

```bash
cp -R skills/skill-rag-research "${CODEX_HOME:-$HOME/.codex}/skills/"
```

4. Reinicia tu sesión de Codex o recarga el entorno si tu flujo lo requiere.

## Instalación de varias skills

```bash
cp -R skills/skill-git-github-expert "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/skill-rag-research "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/skill-sdd-architect "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Verificación

Comprueba que la skill quedó instalada:

```bash
ls "${CODEX_HOME:-$HOME/.codex}/skills"
```

Debes ver el slug correspondiente, por ejemplo `skill-rag-research`.

## Actualización

Cuando publiques una nueva release:

1. actualiza tu clon local o descarga la release;
2. revisa `CHANGELOG.md` del repo y de la skill;
3. reemplaza la carpeta instalada por la versión nueva.

## Instalación desde release

Si compartes una release empaquetada:

1. descarga el archivo del release;
2. descomprímelo;
3. copia la carpeta de la skill al directorio local de skills;
4. valida la versión revisando `skill.json`.
