# Enter `mohtml`

This project is all about a DSL to write HTML in Python. 

> This work is *heavily* inspired by [FastHTML](https://fastht.ml/). I mainly made this to see if I could reimplement it easily and if I might be able to hack together a lightweight variant of the idea for Marimo. If you feel like giving folks credit, feel free to join the FastHTML Discord and give them a high-five first. 

## Installation

You can install this project via uv/pip: 

```python
uv pip install mohtml
```

## Quick demo

With that out of the way, let's have a quick look what what the DSL is like.

```python
# You can import any HTML element this way
from mohtml import a, p, div, script, h1

div(
    script(src="https://cdn.tailwindcss.com"),
    h1("welcome to my blog", klass="font-bold text-xl"),
    p("my name is vincent", klass="text-gray-500 text-sm"),
    a("please check my site", href="https://calmcode.io", klass="underline")
)
```

This code will generate the following HTML:

```html
<div>
 <script src="https://cdn.tailwindcss.com">
 </script>
 <h1 class="font-bold text-xl">
  welcome to my blog
 </h1>
 <p class="text-gray-500 text-sm">
  my name is vincent
 </p>
 <a class="underline" href="https://calmcode.io">
  please check my site
 </a>
</div>
```

You can also render this HTML nicely from Marimo via: 

```python
myhtml = div(...)
mo.Html(f"{myhtml}")
```

## From here?

This is already pretty cool on it's own, but there are a few directions here. 

1. Maybe we can use this tool to make representations of objects nicer in Marimo.
2. Maybe we can come up with a nice way to turn these HTML objects into something reactive.
3. Maybe we can use this as an alternative for Jinja templates in some dases. Could be nice to make some simple dashboard-y UI components here.
