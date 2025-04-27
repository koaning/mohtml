from mohtml.components import terminal
from mohtml import span, b

def test_terminal_nesting():
    out = str(terminal(span("> hello there")))
    assert "<span>" in out
    assert "> hello there" in out
    out = str(terminal(b("> hello there")))
    assert "<b>" in out
    assert "> hello there" in out
