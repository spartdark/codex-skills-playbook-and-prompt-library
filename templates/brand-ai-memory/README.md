# Brand AI Memory Template

Plantilla portable para copiar una identidad visual AI ready a otro proyecto.

## Instalar En Otro Repo

Copia la carpeta `brand/` al repo destino:

```bash
cp -R templates/brand-ai-memory/brand /path/to/target-repo/
```

Despues:

1. Completa `brand/brand-brief.md`.
2. Completa `brand/brand-memory.json`.
3. Agrega assets aprobados en `brand/assets/logo/`.
4. Agrega exports para corte en `brand/assets/cricut/`.
5. Guarda prompts reutilizables en `brand/prompts/`.
6. Guarda decisiones en `brand/decisions/`.

## Uso Con Codex

Pide a Codex:

```md
Lee `brand/README.md` y usa `brand/brand-memory.json` como fuente de verdad para cualquier pieza de marca. No inventes colores, fuentes o reglas sin marcarlo como propuesta.
```
