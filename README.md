# Kamalesh Canva Agent

An all-in-one creative assistant with a primary specialization in professional presentations.

## Targets

- **Claude Code plugin:** skills, commands, agent definition, and remote Canva MCP configuration.
- **Claude Desktop:** project-instructions pack that reuses the same skills and brand profiles alongside Claude's Canva remote integration.

## Core behavior

Ask → understand → plan → obtain approval → inspect tools → execute → verify → refine → deliver.

## Included skills

1. Design Director
2. Brand System
3. Presentation Studio
4. Social Content Studio
5. Carousel Generator
6. Campaign Workflow

## Install in Claude Code

1. Extract this folder.
2. In VS Code, open the extracted `kamalesh-canva-agent` folder.
3. Ensure Claude Code is installed and available.
4. Test locally:

   ```bash
   claude --plugin-dir .
   ```

5. In Claude Code, inspect `/help` and try `/presentation` or `/design-review`.
6. Confirm Canva MCP is connected and authorized. If the remote server does not connect automatically, follow the current Claude Code MCP setup instructions and add the endpoint from `.mcp.json` using the supported remote HTTP transport.

## Set up Claude Desktop

Follow `desktop/CLAUDE_DESKTOP_SETUP.md`. Use `desktop/CLAUDE_DESKTOP_PROJECT_INSTRUCTIONS.md` as the Project Instructions and add the skill/brand-profile files as project knowledge.

## Canva MCP

The project references Canva's hosted remote MCP endpoint:

`https://mcp.canva.com/mcp`

Canva MCP capabilities and plan restrictions can change. The agent must inspect live tools before acting. Brand-template and resize operations may be plan-gated; do not assume every Canva account has every capability.

## Brand profiles

The included Kamalesh profile is a **draft**. The K mark and exact serif heading font require approval. Use `brand-profiles/README.md` for the versioning convention.

## Validation

Run:

```bash
python scripts/validate_project.py
```

This validates JSON, skill frontmatter, required files, and key folder structure. It does not test live Canva authentication or actual design operations.

## Known limitations

- Claude Code plugins and Claude Desktop extensions are different packaging systems.
- A `.mcpb` package bundles a local MCP server; Canva's hosted remote MCP is configured as a remote service. This project therefore does not pretend to provide a local Canva MCP server.
- Claude Desktop does not automatically load Claude Code slash commands or plugin skills. Use the provided Project Instructions and project knowledge files.
- Canva tool availability depends on authorization, account plan, and the live MCP tool list.

## License

MIT. See `LICENSE`.
