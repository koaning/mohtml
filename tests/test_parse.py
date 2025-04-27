import pytest 
from mohtml.parser import CustomMarkdownParser

parser = CustomMarkdownParser()

@parser.register("red")
def red(content):
    return "<span style=\"color: red\">" + content + "</span>"


@pytest.mark.parametrize("text, expected", [
    ("hello", "hello"),
    ("hello <red>world</red>", "hello <span style=\"color: red\">world</span>"),
    ("hello <red>world</red> hello", "hello <span style=\"color: red\">world</span> hello"),
])
def test_red(text, expected):
    assert parser(text) == expected


def test_code_block1():
    test_str = """
```html
<red>hello</red>
```
"""
    assert parser(test_str) == test_str


def test_code_block2():
    test_str = """
```html
<red>hello</red>
```
<red>hello</red>
"""
    assert parser(test_str) == """
```html
<red>hello</red>
```
<span style=\"color: red\">hello</span>
"""
