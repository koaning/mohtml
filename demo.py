import marimo

__generated_with = "0.12.8"
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
    return a, div, h1, p, pretty_print, script


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
    return CoolCat, img, span


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
    return elem, surreal_js, tailwind_css


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
    return (yes_really_anything,)


@app.cell
def _():
    from mohtml.parser import CustomHTMLParser
    from mohtml.components import terminal 

    parser = CustomHTMLParser()

    # You would normally use this as a decorator. May change this. 
    parser.register("terminal")(terminal)
    return CustomHTMLParser, parser, terminal


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
    return i, item, items, out, test_str


@app.cell
def _(p):
    from mohtml.components import highlight
    from mohtml import b

    p("I want to say", highlight("hello ", b("world"), color="yellow"), "to all of you", style="font-size: 30px;")
    return b, highlight


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
    return editor, start_value


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Style only components 

        This is inspired by [this blogpost](https://codepen.io/stoumann/pen/qEEKJYq).
        """
    )
    return


@app.cell(hide_code=True)
def _():
    from mohtml import style 

    chord_css = style("""
    fret-board {
    	--fret-board-bg: light-dark(#EEE, #333);
    	--fret-board-fret-c: light-dark(#000, #FFF);
    	--fret-board-fret-w: clamp(0.0625rem, 0.03125rem + 0.5cqi, 0.5rem);
    	--fret-board-string-c: light-dark(#0008, #FFF8);
    	--fret-board-string-w: clamp(0.0625rem, 0.03125rem + 0.5cqi, 0.125rem);

    	/* private consts */
    	--_frets: attr(frets type(<number>), 4);
    	--_strings: attr(strings type(<number>), 6);

    	aspect-ratio: 1 / 1;
    	background-color: var(--fret-board-bg);
    	border-radius: var(--fret-board-bdrs, .5rem);
    	box-sizing: border-box;
    	container-type: inline-size;
    	display: grid;
    	font-family: var(--fret-board-ff, inherit);
    	grid-template-columns: repeat(calc(var(--_strings) * 2), 1fr);
    	grid-template-rows:
    		var(--fret-board-top-row-h, 12%)
    		repeat(calc(var(--_frets)), 1fr)
    		var(--fret-board-bottom-row-h, 15%);
    	place-items: center;

    	/* Grid Lines (frets and strings) */
    	&::before {
    		background-color: var(--fret-board-fret-bg, #0000);
    		background-image:
    			linear-gradient(90deg, var(--fret-board-string-c) var(--fret-board-string-w), #0000 0 var(--fret-board-string-w)),
    			linear-gradient(180deg,  var(--fret-board-fret-c) var(--fret-board-fret-w), #0000 0 var(--fret-board-fret-w));
    		background-position: 0 var(--fret-board-fret-w), 0 0;
    		background-repeat: repeat-x, repeat-y;
    		background-size:
    			calc(100% / (var(--_strings) - 1) - (var(--fret-board-string-w) / var(--_strings))) calc(100% - (2 * var(--fret-board-fret-w))),
    			100% calc(100% / var(--_frets) - (var(--fret-board-fret-w) / var(--_frets)));
    		box-shadow: 0 calc(0px - var(--fred-board-fret-bbsw, 1.5cqi)) 0 0 var(--fret-board-fret-c);
    		content: '';
    		display: block;
    		grid-area: 2 / 2 / calc(var(--_frets) + 2) / calc(var(--_strings) * 2);
    		height: 100%;
    		width: 100%;
    	}
    	/* Chord Name */
    	&::after {
    		color: var(--fret-board-chord-c, light-dark(#222, #FFF));
    		content: attr(chord);
    		font-size: var(--fret-board-chord-fs, 7.5cqi);
    		font-weight: var(--fret-board-chord-fw, 500);
    		grid-column: 2 / span calc((var(--_strings) * 2) - 2);
    		grid-row: calc(var(--_frets) + 2);
    		text-align: center;
    		width: 100%;
    	}

    	/* Fret Number (optional). Set <li value="[number]"> to set fret offset */
    	ol {
    		align-items: center;
    		display: grid;
    		font-size: var(--fret-board-fret-number-fs, 5cqi);
    		font-weight: var(--fret-board-fret-number-fw, 400);
    		grid-column: 1;
    		grid-row: 2 / span var(--_frets);
    		grid-template-rows: repeat(var(--_frets), 1fr);
    		height: 100%;
    		list-style-position: inside;
    		padding: 0;
    	}
    }

    string-note {
    	--string-note-h: 12cqi;
    	--string-note-open-mute-h: 5cqi;

    	/* from attr() */
    	--barre: attr(barre type(<number>), 1);
    	--fret:  attr(fret type(<number>), 0);
    	--string:  attr(string type(<number>), 0);

    	aspect-ratio: 1;
    	background-color: var(--string-note-bg, currentColor);
    	border-radius: 50%; 
    	box-sizing: border-box;
    	display: grid;
    	grid-column: calc((var(--_strings) * 2) - (var(--string) * 2 - 1)) / span calc(var(--barre) * 2);
    	grid-row: calc(var(--fret) + 1);
    	height: var(--string-note-h);
    	isolation: isolate;
    	list-style: none;
    	place-content: center;

    	&::after {
    		color: var(--string-note-c, light-dark(#FFF, #222));
    		content: attr(finger);
    		font-size: var(--string-note-fs, 7cqi);
    		font-weight: var(--string-note-fw, 500);
    		text-box: cap alphabetic;
    	}
    	&[barre] {
    		aspect-ratio: unset;
    		border-radius: var(--string-note-h);
    		opacity: var(--string-note-barre-o, .6);
    		width: 100%;
    	}
    	&[mute], &[open] {
    		background-color: var(--string-note-mute-open-c, light-dark(#222, #FFF));
    		height: var(--string-note-open-mute-h);
    		width: var(--string-note-open-mute-h);
    	}
    	&[mute] {
    		border-image: conic-gradient(var(--fret-board-bg) 0 0) 50%/calc(50% - 0.25cqi);
    		rotate: 45deg;
    	}
    	&[open] {
    		border-radius: 50%;
    		mask: radial-gradient(circle farthest-side at center, #0000 calc(100% - 1cqi), #000 calc(100% - 1cqi + 1px));
    	}
    }""")

    chord_css
    return chord_css, style


@app.cell
def _(div):
    from mohtml.anything import fret_board, string_note

    div(
        fret_board(
            string_note(string="6", open=...),
            string_note(string="5", fret="2", finger="2"),
            string_note(string="4", fret="2", finger="3"),
            string_note(string="3", fret="1", finger="1"),
            string_note(string="2", open=...),
            string_note(string="1", open=...),
            frets="4", strings="6", chord="E Major"
        )
        , style="width: 300px;"
    )
    return fret_board, string_note


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We can do svg with this library too!""")
    return


@app.cell
def _():
    from mohtml import svg, circle

    svg(
        circle(cx=50, cy=50, r=40),
        circle(cx=150, cy=50, r=4),
        svg(
            circle(cx=5, cy=5, r=4),
            viewBox="0 0 10 10",
            x=200,
            width=100,
        ),
        viewBox="0 0 300 100",
        xmlns="http://www.w3.org/2000/svg",
        stroke="red",
        fill="grey",
    )
    return circle, svg


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
