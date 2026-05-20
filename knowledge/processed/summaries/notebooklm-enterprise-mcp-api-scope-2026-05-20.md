# NotebookLM Enterprise MCP API Scope

- source type: web
- source URLs:
  - https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks
  - https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources
  - https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-audio-overview
  - https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api
  - https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview
- captured date: 2026-05-20
- confidence: verified
- project relevance: Defines the safe integration boundary for a local NotebookLM MCP server.

## Summary

Google documents public REST endpoints for NotebookLM Enterprise through Discovery Engine. The documented surface covers creating, retrieving, listing recently viewed, deleting, and sharing notebooks; adding text, web, YouTube, Google Docs, Google Slides, and uploaded file sources; creating and deleting notebook audio overviews; and generating standalone podcasts.

The personal NotebookLM product at `https://notebooklm.google.com/` is described separately from NotebookLM Enterprise. The implementation in `services/notebooklm-mcp` should therefore target the official Enterprise/Discovery Engine API surface and avoid reverse engineered personal web app calls.

## Implementation Decision

Create an MCP server that authenticates with Google Cloud OAuth credentials and exposes explicit tools for the documented API methods. Do not expose a notebook chat/query MCP tool until Google documents a stable endpoint for that use case.

## Evidence Pointers

- Notebook management API page: create, get, list recently viewed, delete, and share methods.
- Sources API page: batch source creation, local file upload, source retrieval, and deletion.
- Audio overview API page: one audio overview per notebook, create and delete methods.
- Podcast API page: standalone API, context inputs, operation result, download endpoint, allowlist note.
- Overview page: personal NotebookLM and NotebookLM Enterprise are separate products and interfaces.
