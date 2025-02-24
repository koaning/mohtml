import marimo

__generated_with = "0.11.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from mohtml import a, p, div, script, h1

    print(
        div(
            script(src="https://cdn.tailwindcss.com"),
            h1("welcome to my blog", klass="font-bold text-xl"),
            p("my name is vincent", klass="text-gray-500 text-sm"),
            a("please check my site", href="https://calmcode.io", klass="underline")
        )
    )
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
        )
    ])
    return CoolCat, img, span


@app.cell
def _(div):
    from mohtml import link

    def boostrap_css():
        return link(
            rel="stylesheet", 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        )

    def horizontal_spacing(*args):
        return div(
            div(*[div(a, klass="col") for a in args], 
                klass="row"
            ), 
            klass="container"
        )

    # You can uncomment the line below to make the lower cell look nicer, but it conflicts with the tailwind css that we loaded earlier. 
    # boostrap_css()
    return boostrap_css, horizontal_spacing, link


@app.cell
def _(CoolCat, horizontal_spacing):
    horizontal_spacing(
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
        CoolCat(
            name="joy", 
            nickname="the lazy one", 
            desc="totally quits all the time", 
            avatar="https://placecats.com/louie/200/200"
        )
    )
    return


@app.cell
def _(div, mo, script):
    from mohtml import surreal_js, tailwind_css

    mo.iframe(str(div(
        surreal_js(), 
        tailwind_css(),
        div(
            "My background changes when you click me.",
            script("""me().on("click", ev => { me(ev).classToggle('bg-gray-200') })""")
        )
    )))
    return surreal_js, tailwind_css


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


if __name__ == "__main__":
    app.run()
