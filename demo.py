

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from mohtml import a, p, div, script, h1, pretty_print

    _ = div(
        script(src="https://cdn.tailwindcss.com"),
        h1("welcome to my blog", klass="font-bold text-xl"),
        p("my name is vincent", klass="text-gray-500 text-sm"),
        a("please check my site", href="https://calmcode.io", klass="underline")
    )

    pretty_print(_)
    return a, div, h1, p, script


@app.cell
def _(a, div, h1, p, script):
    div(
        script(src="https://cdn.tailwindcss.com"),
        h1("welcome to my blog", klass="font-bold text-4xl"),
        p("my name is vincent", klass="text-gray-500 text-sm"),
        a("please check my site", href="https://calmcode.io", klass="underline")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Fun representations

        It is pretty easy to use this tool to build custom representations of objects. Check the demo below.
        """
    )
    return


@app.cell
def _(div, mo, p):
    from mohtml import img, span 

    class CoolCat: 
        def __init__(self, name, nickname, desc, avatar): 
            self.name = name
            self.nickname = nickname
            self.desc = desc
            self.avatar = avatar

        def _display_(self): 
            return div(
                div(
                    span(self.name, klass="text-xl font-bold text-black"), 
                    span(" - "),
                    span(self.nickname, klass="text-gray-700"), 
                ),
                img(src=self.avatar, klass="rounded-lg"), 
                p(self.desc, klass="text-sm text-gray-900 pt-4"), 
                klass="bg-gray-200 rounded-lg p-4"
            )

        def __str__(self):
            return str(self._display_())


    mo.hstack([
        CoolCat(
            name="tank", 
            nickname="the hunter", 
            desc="takes a blue pill daily", 
            avatar="https://placecats.com/neo/200/200"
        ),
        CoolCat(
            name="neo", 
            nickname="furball", 
            desc="takes a red pill daily", 
            avatar="https://placecats.com/neo_2/200/200"
        ),
        CoolCat(
            name="bella", 
            nickname="the reckless one", 
            desc="will never ever quit", 
            avatar="https://placecats.com/bella/200/200"
        ), 
    ])
    return (span,)


@app.cell(hide_code=True)
def _():
    # from mohtml import link

    # def boostrap_css():
    #     return link(
    #         rel="stylesheet", 
    #         href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    #     )

    # def horizontal_spacing(*args):
    #     return div(
    #         div(*[div(a, klass="col") for a in args], 
    #             klass="row"
    #         ), 
    #         klass="container"
    #     )

    # boostrap_css()
    # horizontal_spacing(
    #     CoolCat(
    #         name="tank", 
    #         nickname="the hunter", 
    #         desc="takes a blue pill daily", 
    #         avatar="https://placecats.com/neo/200/200"
    #     ),
    #     CoolCat(
    #         name="neo", 
    #         nickname="furball", 
    #         desc="takes a red pill daily", 
    #         avatar="https://placecats.com/neo_2/200/200"
    #     ), 
    #     CoolCat(
    #         name="bella", 
    #         nickname="the reckless one", 
    #         desc="will never ever quit", 
    #         avatar="https://placecats.com/bella/200/200"
    #     ), 
    #     CoolCat(
    #         name="joy", 
    #         nickname="the lazy one", 
    #         desc="totally quits all the time", 
    #         avatar="https://placecats.com/louie/200/200"
    #     )
    # )
    return


@app.cell
def _(div, mo, script):
    from mohtml import surreal_js, tailwind_css

    elem = div(
        surreal_js(), 
        tailwind_css(),
        div(
            "My background changes when you click me.",
            script("""me().on("click", ev => { me(ev).classToggle('bg-gray-200') })""")
        )
    )
    mo.iframe(str(elem))
    return


@app.cell
def _(div, p):
    from mohtml.anything import yes_really_anything

    print(
        yes_really_anything(
            div(
                p("hello there")
            ),
            klass="demof"
        )
    )
    return


@app.cell
def _():
    from mohtml.parser import CustomHTMLParser
    from mohtml.components import terminal 

    parser = CustomHTMLParser()

    # You would normally use this as a decorator. May change this. 
    parser.register("terminal")(terminal)
    return parser, terminal


@app.cell
def _(parser):
    test_str = """This returns a generator of `Path` objects. 

    ```python
    Path().glob("*/*.md")
    ```
    """

    items = test_str.split("```")
    out = ""
    for i, item in enumerate(items):
        if i % 2 == 1:
            out += "```" + item + "```"
        else:
            if "terminal" in item:
                out += parser(item)
            else: 
                out += item

    print(out)
    return


@app.cell
def _(mo, template_str):
    from jinja2 import Template 


    class Admonition:
        """
        A simple admonition class for creating note, tip, warning, and danger callouts.
        """
        TYPES = {
            'note': {'icon': 'ℹ️', 'color': '#448aff'},
            'tip': {'icon': '💡', 'color': '#00bfa5'},
            'warning': {'icon': '⚠️', 'color': '#ff9100'},
            'danger': {'icon': '🛑', 'color': '#ff5252'}
        }

        def __init__(self, content, type='note', title=None, collapsible=False):
            """
            Initialize an admonition.

            Args:
                content (str): The main content of the admonition
                type (str): Type of admonition (note, tip, warning, danger)
                title (str, optional): Custom title. Defaults to capitalized type.
                collapsible (bool, optional): Whether the admonition can be collapsed.
            """
            if type not in self.TYPES:
                type = 'note'

            self.type = type
            self.content = content
            self.title = title if title is not None else type.capitalize()
            self.collapsible = collapsible
            self.properties = self.TYPES[type]

        def _display_(self):
            return mo.md(Template(template_str).render(title=self.title, content=self.content, type=self.type))
    return (Admonition,)


@app.cell
def _(Admonition):
    from mohtml import b

    Admonition(b("this is a demo"), title="huh?", type="danger")
    return


@app.cell(hide_code=True)
def _():
    template_str = """
    <div class="admonition {{ type }}">
      <div class="admonition-title">
        {{ title|default(type|capitalize, true) }}
      </div>
      <div class="admonition-content">
        {{ content }}
      </div>
    </div>

    <style>
      /* Base admonition styling */
      .admonition {
        position: relative;
        margin: 1.5625em 0;
        padding: 0 1.2rem 0 1.2rem;
        color: rgba(0, 0, 0, 0.87);
        background-color: #fff;
        border: none;
        border-radius: 0.2rem;
        box-shadow: 0 0.2rem 0.5rem rgba(0, 0, 0, 0.05), 0 0 0.05rem rgba(0, 0, 0, 0.1);
        font-size: 0.8rem;
        overflow: hidden;
      }

      /* Left colored bar using pseudo-element */
      .admonition::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 0.4rem;
        height: 100%;
        background-color: #ccc; /* Default color, will be overridden */
      }

      /* Admonition title styling */
      .admonition .admonition-title {
        position: relative;
        margin: 0 -1.2rem;
        padding: 0.8rem 1.2rem 0.8rem 3.2rem;
        font-weight: 700;
        font-size: 0.8rem;
        line-height: 1.3;
      }

      /* Admonition title icon */
      .admonition .admonition-title::before {
        content: "";
        position: absolute;
        left: 1.2rem;
        top: 50%;
        transform: translateY(-50%);
        width: 1.2rem;
        height: 1.2rem;
        background-position: center;
        background-repeat: no-repeat;
        background-size: contain;
      }

      /* Admonition content styling */
      .admonition .admonition-content {
        margin: 1.25em 0;
        padding: 0;
        line-height: 1.6;
      }

      /* Content spacing */
      .admonition .admonition-content > * {
        margin-top: 0.8em;
        margin-bottom: 0.8em;
      }

      .admonition .admonition-content > *:first-child {
        margin-top: 0;
      }

      .admonition .admonition-content > *:last-child {
        margin-bottom: 0;
      }

      /* Note type */
      .admonition.note::before {
        background-color: #448aff;
      }
      .admonition.note > .admonition-title {
        background-color: rgba(68, 138, 255, 0.1);
        color: #448aff;
      }
      .admonition.note > .admonition-title::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24' fill='%23448aff'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z'/%3E%3C/svg%3E");
      }

      /* Tip type */
      .admonition.tip::before {
        background-color: #00bfa5;
      }
      .admonition.tip > .admonition-title {
        background-color: rgba(0, 191, 165, 0.1);
        color: #00bfa5;
      }
      .admonition.tip > .admonition-title::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24' fill='%2300bfa5'%3E%3Cpath d='M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 0 1 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z'/%3E%3C/svg%3E");
      }

      /* Warning type */
      .admonition.warning::before {
        background-color: #ff9100;
      }
      .admonition.warning > .admonition-title {
        background-color: rgba(255, 145, 0, 0.1);
        color: #ff9100;
      }
      .admonition.warning > .admonition-title::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24' fill='%23ff9100'%3E%3Cpath d='M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z'/%3E%3C/svg%3E");
      }

      /* Danger type */
      .admonition.danger::before {
        background-color: #ff5252;
      }
      .admonition.danger > .admonition-title {
        background-color: rgba(255, 82, 82, 0.1);
        color: #ff5252;
      }
      .admonition.danger > .admonition-title::before {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24' fill='%23ff5252'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z'/%3E%3C/svg%3E");
      }

      /* Nested admonitions */
      .admonition .admonition {
        margin: 1em 0;
      }
    </style>
    """
    return (template_str,)


@app.cell(hide_code=True)
def _(mo):
    start_value = """<terminal theme="dark">
    hello world
    </terminal>"""

    editor = mo.ui.code_editor(language="html", value=start_value)
    editor
    return (editor,)


@app.cell(hide_code=True)
def _(editor, mo, parser):
    mo.md(parser(f"""
    {editor.value}
    """))
    return


@app.cell
def _(span, terminal):
    terminal(span("> hello there"))
    return


if __name__ == "__main__":
    app.run()
