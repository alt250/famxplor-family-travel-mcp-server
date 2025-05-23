# famxplor-family-travel-mcp-server

The first MCP server dedicated to families who travel with their kids. 
Find activities tested by families worldwide from [Famxplor](https://famxplor.com)

## API Key

See [Famxplor Family Travel API](https://famxplor.com/api) to get an API key

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

For MCP clients supporting remote streamable-http servers, configuration looks like:

```json
{
  "mcpServers": {
    "famxplor": {
      "url": "https://mcp.famxplor.com/mcp/"
    }
  }
}
```

## Run the server manually

```shell
FAMXPLOR_API_KEY="<your Famxplor API key>" uv run server.py
```