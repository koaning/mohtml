from mohtml import span

def highlight(*content, color="yellow"):
    colors = {
        "yellow": "rgba(255, 249, 85, 0.6)",
        "green": "rgba(102, 255, 102, 0.6)",
        "blue": "rgba(102, 102, 255, 0.6)",
        "red": "rgba(255, 102, 102, 0.6)",
    }
    style = f"background-image: linear-gradient(to right, {colors[color]} 0%, {colors[color]} 5%, {colors[color]} 95%, {colors[color]} 100%); padding: 0 4px; border-radius: 3px; display: inline-block; transform: rotate(-0.5deg);"
    
    return span(*content, style=style)

