# famxplor-family-travel-mcp-server

The first MCP server dedicated to families who travel with their kids. 
Find activities tested by families worldwide from [Famxplor](https://famxplor.com)

## Free to use

Famxplor MCP server is free for personal use, like the [family activities world map](https://famxplor.com/app) of Famxplor.
For commercial use, see the [Famxplor API page](https://famxplor.com/api).

## API Key

Local use and development require an API key, see [Famxplor Family Travel API](https://famxplor.com/api) to get one.

## Development

Setup environment:
```shell
uv sync
```

Run the server with:
```shell
FAMXPLOR_API_KEY="<your Famxplor API key>" uv run server.py
```
