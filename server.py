from mcp.server.fastmcp import FastMCP

print("Starting MCP Server")
mcp = FastMCP("MCP Server 101")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!!!"

# Running the server
if __name__ == "__main__":
    mcp.run()