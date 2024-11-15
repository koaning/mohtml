import marimo

__generated_with = "0.9.20"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md(
        """
        # Enter `mohtml`

        This project is all about a DSL to write HTML in Python. 

        > This work is *heavily* inspired by [FastHTML](https://fastht.ml/). I mainly made this to see if I could reimplement it easily and if I might be able to hack together a lightweight variant of the idea for Marimo. If you feel like giving folks credit, feel free to join the FastHTML Discord and give them a high-five first. 

        With that out of the way, let's have a quick look what what the DSL is like.
        """
    )
    return


@app.cell
def __(a, div, h1, p, script):
    myhtml = div(
        script(src="https://cdn.tailwindcss.com"),
        h1("welcome to my blog", klass="font-bold text-xl"),
        p("my name is vincent", klass="text-gray-500 text-sm"),
        a("please check my site", href="https://calmcode.io", klass="underline")
    )

    myhtml
    return (myhtml,)


@app.cell
def __(mo):
    mo.md(
        """
        Notice the syntax here. 

        1. Each function call represents an HTML element. 
        2. Each function call can define `**kwargs` which are passed unto the HTML element as you might expect. 
        3. You can add children to the elements via `*args`. Errors will be raised when you try to add children to elements that do not support that like `<br/>`.
        """
    )
    return


@app.cell
def __(mo, myhtml):
    mo.iframe(f"{myhtml}", height=130)
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    from mohtml import a, div, p, h1, script
    return a, div, h1, p, script


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
