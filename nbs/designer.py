# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4==4.13.4",
#     "jinja2==3.1.6",
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.12.10"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from jinja2 import Template
    return Template, mo


@app.cell
def _(mo):
    jinja_editor = mo.ui.code_editor(language="html", label="jinja2 template", value="""<b>{{thing}}</b>""")
    html_editor = mo.ui.code_editor(language="html", label="html input", value="""<terminal>
      hello there this is dog <pyfunc thing="foo"></pyfunc><br>
    </terminal>
    """)
    return html_editor, jinja_editor


@app.cell
def _(jinja_editor):
    jinja_editor
    return


@app.cell
def _(html_editor):
    html_editor
    return


@app.cell
def _(pyfunc):
    from mohtml.parser import CustomHTMLParser
    from mohtml.components import terminal

    parser = CustomHTMLParser()
    parser.register("pyfunc")(pyfunc)
    parser.register("terminal")(terminal)
    return CustomHTMLParser, parser, terminal


@app.cell
def _(Template, jinja_editor):
    def pyfunc(*args, **kwargs):
        return Template(jinja_editor.value).render(**kwargs)
    return (pyfunc,)


@app.cell
def _(html_editor, mo, parser):
    mo.iframe(html=parser(html_editor.value))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
