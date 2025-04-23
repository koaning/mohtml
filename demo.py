import marimo

__generated_with = "0.12.8"
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
def _(pl, serialize):
    import srsly
    import anywidget
    import traitlets
    from jinja2 import Template


    def plotty(plot_logic, **kwargs): 
        dataframes = {}
        other = {}
        for k, v in kwargs.items():
            if isinstance(v, pl.DataFrame):
                dataframes[k] = serialize(v, renderer="jsdom")
            else:
                if isinstance(v, str):
                    other[k] = f'"{v}"'
                else:
                    other[k] = v
    
        template_str = """
        import * as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/+esm";
        import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";
        import * as arrow from 'https://cdn.jsdelivr.net/npm/apache-arrow@latest/+esm';
    
        function readPolarsDataFrame(base64Value) {
          // Decode base64 to ArrayBuffer
          const binaryString = atob(base64Value);
          const bytes = new Uint8Array(binaryString.length);
          for (let i = 0; i < binaryString.length; i++) {
            bytes[i] = binaryString.charCodeAt(i);
          }
          const arrayBuffer = bytes.buffer;
      
          // The correct way to create a table from a buffer
          const table = arrow.tableFromIPC(arrayBuffer);
      
          return table;
        }

        function render({ model, el }) {
            {% for key, value in other.items() %}
            const {{ key }} = value;
            {% endfor %}
            {% for key, value in dataframes.items() %}
            const {{ key }} = readPolarsDataFrame("{{ value }}");
            {% endfor %}
            const plot = {{plot_logic}};

            el.append(plot);

        }
        export default { render };
        """
        esm = Template(template_str).render(plot_logic=plot_logic.strip(), dataframes=dataframes, other=other)
        class Widget(anywidget.AnyWidget):
            _esm = esm

        return Widget()

    bls = pl.read_csv("bls-metro-unemployment.csv").with_columns(date=pl.col("date").str.to_date())

    plotty("""
    Plot.plot({
      y: {
        grid: true,
        label: "↑ Unemployment (%)"
      },
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(bls, {x: "date", y: "unemployment", z: "division"})
      ]
    })
    """, bls=bls)
    return Template, anywidget, bls, plotty, srsly, traitlets


@app.cell
def _():
    import base64
    import io
    from datetime import date
    from typing import Any

    import pandas as pd
    import polars as pl


    def serialize(data: Any, renderer: str) -> Any:
        """
        Serialize a data object.

        Parameters
        ----------
        data : Any
            data object to serialize.
        renderer : str
            renderer type.

        Returns
        -------
        Any
            serialized data object.
        """

        # If polars DataFrame, serialize to Arrow IPC
        if isinstance(data, pl.DataFrame):
            value = pl_to_arrow(data)
            if renderer == "jsdom":
                value = base64.standard_b64encode(value).decode("ascii")
            return value
        # If pandas DataFrame, serialize to Arrow IPC
        elif isinstance(data, pd.DataFrame):
            value = pd_to_arrow(data)
            if renderer == "jsdom":
                value = base64.standard_b64encode(value).decode("ascii")
            return value
        # Else, keep as is
        else:
            return data


    def pd_to_arrow(df: pd.DataFrame) -> bytes:
        """
        Convert a pandas DataFrame to Arrow IPC bytes.

        Parameters
        ----------
        df : pd.DataFrame
            pandas DataFrame to convert.

        Returns
        -------
        bytes
            Arrow IPC bytes.
        """
        # Convert dates to timestamps
        for colname in df.columns:
            col = df[colname].dropna()
            if col is not None and isinstance(col[0], date):
                try:
                    df[colname] = pd.to_datetime(df[colname])
                except ValueError:
                    pass
        # Convert timestamps to millisecond units so that
        # Plot will detect them as datetimes
        datetime_columns = df.select_dtypes(include=["datetime64"]).columns
        df[datetime_columns] = df[datetime_columns].astype("datetime64[ms]")

        f = io.BytesIO()
        df.to_feather(f, compression="uncompressed")
        return f.getvalue()


    def pl_to_arrow(df: pl.DataFrame) -> bytes:
        """
        Convert a polars DataFrame to Arrow IPC bytes.

        Parameters
        ----------
        df : pl.DataFrame
            polars DataFrame to convert.

        Returns
        -------
        bytes
            Arrow IPC bytes.
        """

        # Convert dates and datetimes to millisecond units so that
        # Plot will detect them as datetimes
        df = df.with_columns(pl.col(pl.Datetime).cast(pl.Datetime("ms")))
        df = df.with_columns(pl.col(pl.Date).cast(pl.Datetime("ms")))

        f = io.BytesIO()
        df_pd = df.to_pandas()
        df_pd.to_feather(f, compression="uncompressed")
        return f.getvalue()
    return Any, base64, date, io, pd, pd_to_arrow, pl, pl_to_arrow, serialize


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
