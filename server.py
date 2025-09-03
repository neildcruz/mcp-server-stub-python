from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("Base MCP Server")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting message in a specified style."""
    styles = {
        "friendly" : "Please write a warm, friendly greeting",
        "formal" : "Please write a formal, professional greeting",
        "casual" : "Please write a casual, laid-back greeting"
    }
    return f"{styles.get(style, styles['friendly'])} for someone named {name}."

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="stdio")