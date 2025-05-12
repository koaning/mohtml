import marimo

__generated_with = "0.13.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from mohtml.components import chord_css
    from mohtml.anything import fret_board, string_note
    from mohtml import div

    chord_css()
    return div, fret_board, mo, string_note


@app.cell
def _(div, fret_board, string_note):
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This function below was generated with an LLM. """)
    return


@app.function(hide_code=True)
def create_guitar_chords_dict():
    guitar_chords = {
        # Major Chords
        "A Major": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "0", "open": True},
                {"string": "4", "fret": "2", "finger": "2"},
                {"string": "3", "fret": "2", "finger": "3"},
                {"string": "2", "fret": "2", "finger": "4"},
                {"string": "1", "fret": "0", "open": True}
            ]
        },
        "B Major": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "2", "finger": "1"},
                {"string": "4", "fret": "4", "finger": "3"},
                {"string": "3", "fret": "4", "finger": "4"},
                {"string": "2", "fret": "4", "finger": "4"},
                {"string": "1", "fret": "2", "finger": "1"}
            ]
        },
        "C Major": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "3", "finger": "3"},
                {"string": "4", "fret": "2", "finger": "2"},
                {"string": "3", "fret": "0", "open": True},
                {"string": "2", "fret": "1", "finger": "1"},
                {"string": "1", "fret": "0", "open": True}
            ]
        },
        "D Major": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "x"},
                {"string": "4", "fret": "0", "open": True},
                {"string": "3", "fret": "2", "finger": "1"},
                {"string": "2", "fret": "3", "finger": "3"},
                {"string": "1", "fret": "2", "finger": "2"}
            ]
        },
        "E Major": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "0", "open": True},
                {"string": "5", "fret": "2", "finger": "2"},
                {"string": "4", "fret": "2", "finger": "3"},
                {"string": "3", "fret": "1", "finger": "1"},
                {"string": "2", "fret": "0", "open": True},
                {"string": "1", "fret": "0", "open": True}
            ]
        },
        "F Major": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "1", "finger": "1"},
                {"string": "5", "fret": "3", "finger": "3"},
                {"string": "4", "fret": "3", "finger": "4"},
                {"string": "3", "fret": "2", "finger": "2"},
                {"string": "2", "fret": "1", "finger": "1"},
                {"string": "1", "fret": "1", "finger": "1"}
            ]
        },
        "G Major": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "3", "finger": "3"},
                {"string": "5", "fret": "2", "finger": "2"},
                {"string": "4", "fret": "0", "open": True},
                {"string": "3", "fret": "0", "open": True},
                {"string": "2", "fret": "0", "open": True},
                {"string": "1", "fret": "3", "finger": "4"}
            ]
        },
        
        # Minor Chords
        "A Minor": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "0", "open": True},
                {"string": "4", "fret": "2", "finger": "2"},
                {"string": "3", "fret": "2", "finger": "3"},
                {"string": "2", "fret": "1", "finger": "1"},
                {"string": "1", "fret": "0", "open": True}
            ]
        },
        "B Minor": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "2", "finger": "1"},
                {"string": "4", "fret": "4", "finger": "3"},
                {"string": "3", "fret": "4", "finger": "4"},
                {"string": "2", "fret": "3", "finger": "2"},
                {"string": "1", "fret": "2", "finger": "1"}
            ]
        },
        "C Minor": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "3", "finger": "1"},
                {"string": "4", "fret": "5", "finger": "3"},
                {"string": "3", "fret": "5", "finger": "4"},
                {"string": "2", "fret": "4", "finger": "2"},
                {"string": "1", "fret": "3", "finger": "1"}
            ]
        },
        "D Minor": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "x"},
                {"string": "5", "fret": "x"},
                {"string": "4", "fret": "0", "open": True},
                {"string": "3", "fret": "2", "finger": "2"},
                {"string": "2", "fret": "3", "finger": "3"},
                {"string": "1", "fret": "1", "finger": "1"}
            ]
        },
        "E Minor": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "0", "open": True},
                {"string": "5", "fret": "2", "finger": "2"},
                {"string": "4", "fret": "2", "finger": "3"},
                {"string": "3", "fret": "0", "open": True},
                {"string": "2", "fret": "0", "open": True},
                {"string": "1", "fret": "0", "open": True}
            ]
        },
        "F Minor": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "1", "finger": "1"},
                {"string": "5", "fret": "3", "finger": "3"},
                {"string": "4", "fret": "3", "finger": "4"},
                {"string": "3", "fret": "1", "finger": "1"},
                {"string": "2", "fret": "1", "finger": "1"},
                {"string": "1", "fret": "1", "finger": "1"}
            ]
        },
        "G Minor": {
            "strings": "6",
            "frets": "5",
            "notes": [
                {"string": "6", "fret": "3", "finger": "2"},
                {"string": "5", "fret": "5", "finger": "4"},
                {"string": "4", "fret": "5", "finger": "4"},
                {"string": "3", "fret": "3", "finger": "1"},
                {"string": "2", "fret": "3", "finger": "1"},
                {"string": "1", "fret": "3", "finger": "1"}
            ]
        }
    }
    
    return guitar_chords


@app.cell
def _(div, fret_board, string_note):
    def render_chord(chord_name, chord_data):
        string_notes = []
    
        for note in chord_data["notes"]:
            if note["fret"] == "x":
                # Don't play this string
                string_notes.append(string_note(string=note["string"], mute=True))
            elif "open" in note and note["open"]:
                # Open string
                string_notes.append(string_note(string=note["string"], open=...))
            else:
                # Fretted note
                string_notes.append(string_note(
                    string=note["string"], 
                    fret=note["fret"], 
                    finger=note["finger"]
                ))
    
        return div(
            fret_board(
                *string_notes,
                frets=chord_data["frets"],
                strings=chord_data["strings"],
                chord=chord_name
            ),
            style="width: 300px; display: inline-block; margin: 10px;"
        )
    return (render_chord,)


@app.cell
def _(mo, render_chord):
    def display_chords(chord_type=None):
        """
        Display guitar chords.
    
        Parameters:
        chord_type (str, optional): Filter chords by type. 
                                   Options: "Major", "Minor", or None for all chords.
        """
        guitar_chords = create_guitar_chords_dict()
    
        chord_elements = []
        for chord_name, chord_data in guitar_chords.items():
            # Filter by chord type if specified
            if chord_type and chord_type not in chord_name:
                continue
            
            chord_elements.append(render_chord(chord_name, chord_data))
    
        return mo.hstack(chord_elements, wrap=True)

    display_chords()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
