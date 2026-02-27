from fastmcp import FastMCP
from fastmcp.utilities.types import Image
import io
import matplotlib.pyplot as plt

app = FastMCP()

@app.tool
def add(n1: int, n2: int) ->int:
    """Add two numbers together."""

    return n1 + n2

@app.tool
def draw_pie_chart(numbers: list[int]) -> Image:
    """Draw a pie chart from a list of numbers."""
    plt.pie(numbers)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    
    return Image(data=buffer.getvalue(), format='png')
