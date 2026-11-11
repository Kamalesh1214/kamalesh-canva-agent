# Claude Desktop setup

## Important packaging distinction

This project contains a Claude Code plugin and a Claude Desktop usage pack. Claude Code plugins load skills, commands, and agents from `.claude-plugin/plugin.json`. Claude Desktop's `.mcpb` format is for bundling a **local MCP server**. Canva provides a **remote MCP server**, so this project does not create a fake `.mcpb` wrapper around Canva's hosted service.

For Claude Desktop:
1. Connect Canva using Claude's supported Canva integration / remote MCP connection flow.
2. Confirm Canva is authorized and the expected tools are enabled.
3. Open a Claude Project (recommended) and paste the contents of `CLAUDE_DESKTOP_PROJECT_INSTRUCTIONS.md` into Project Instructions.
4. Add the `skills/` directory and `brand-profiles/` directory as project knowledge/files if your Claude Desktop plan and interface support project files.
5. Use the slash-style workflows listed in `COMMANDS.md` as natural-language prompts; Claude Desktop does not automatically install Claude Code plugin slash commands.

Canva MCP endpoint shown in this project's Claude Code configuration:
`https://mcp.canva.com/mcp`

The remote connector's authentication and tool availability are controlled by Canva and Claude. Do not paste access tokens into this repository.
