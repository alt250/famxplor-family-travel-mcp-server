# famxplor-family-travel-mcp-server

The first MCP server dedicated to families who travel with their kids. 
Find activities tested by families worldwide from [Famxplor](https://famxplor.com)

<a href="https://glama.ai/mcp/servers/@alt250/famxplor-family-travel-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@alt250/famxplor-family-travel-mcp-server/badge" alt="Famxplor Family Travel Activities MCP server" />
</a>

## Free to use

Famxplor MCP server is free for personal use, like the [family activities world map](https://famxplor.com/app) of Famxplor.
For commercial use, see the [Famxplor API page](https://famxplor.com/api).

## API Key

No API key is needed when using the remote MCP server at https://mcp.famxplor.com/mcp/

Local use and development require an API key, see [Famxplor Family Travel API](https://famxplor.com/api) to get one.

## Add to Claude Desktop

Edit `claude_desktop_config.json` and add:

```json
{
  "mcpServers": {
    "famxplor": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.famxplor.com/mcp/"]
    }
  }
}
```

For MCP clients supporting remote streamable-http servers, the configuration looks like:

```json
{
  "mcpServers": {
    "famxplor": {
      "url": "https://mcp.famxplor.com/mcp/"
    }
  }
}
```

## Development

Setup environment:
```shell
uv sync
```

Run the server with:
```shell
FAMXPLOR_API_KEY="<your Famxplor API key>" uv run server.py
```