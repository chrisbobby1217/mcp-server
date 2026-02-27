from fastmcp import FastMCP
app = FastMCP()

@app.tool
def add(n1: int, n2: int) ->int:
    """Add two numbers together."""
    return n1 + n2
