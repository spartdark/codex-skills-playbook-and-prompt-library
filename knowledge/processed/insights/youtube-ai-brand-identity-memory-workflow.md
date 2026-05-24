# Insight: Treat AI Brand Identity as Structured Memory, Not a One-Off Logo Prompt

- Captured: 2026-05-24
- Source pack: `knowledge/raw/youtube/ai-brand-identity-2026-05-24/source-pack-2026-05-24.md`
- Confidence: inferred from multiple sources; Cricut export constraints verified from official help pages.
- Project relevance: reusable workflow for AI-assisted identity systems and future asset generation.

## Claim

For AI-assisted identity work, the durable artifact should be a structured brand memory package, not only generated images. The package should preserve the brief, decisions, tokens, prompt fragments, approved assets, rejected styles, and production rules.

## Evidence

- Lovart-centered sources show the value of a single contextual session that can derive logo, palette, typography, social assets, and merch mockups from the same brand context.
- Midjourney logo sources show fast exploration, but also recurring limitations around text and production readiness.
- AI-ready design system sources argue for structured context, metadata, and token architecture so AI tools can reuse design decisions reliably.
- Cricut official help confirms that vector SVG/DXF uploads behave differently from raster uploads, and that SVG/DXF cannot contain editable text or pattern fills.

## Reusable Recommendation

Create a `brand/` folder for each identity project:

- `brand-brief.md` for strategy and constraints.
- `brand-memory.json` for machine-readable tokens/rules.
- `prompts/` for repeatable prompt recipes.
- `assets/logo/` for source and exported logo variants.
- `assets/cricut/` for cut-ready flat SVGs.
- `decisions/` for why a direction was selected or rejected.

## Production Guardrail

Do not send raw AI-generated raster logos directly to Cricut/vinyl production. First simplify, vectorize/rebuild, outline text, remove gradients/pattern fills for cut files, and test upload in Design Space.

## Promotion Candidate

Potential reusable asset: `templates/brand-ai-memory/` or a future skill for AI-assisted brand identity projects.
