from mohtml import style

def chord_css():
    """
    Adds css classes for <fret-board> and <string-note> elements. j

    Based on these demos: 
    https://dev.to/madsstoumann/guitar-chords-in-css-3hk8?utm_source=cassidoo&utm_medium=email&utm_campaign=birds-born-in-a-cage-think-flying-is-an-illness
    https://codepen.io/stoumann/pen/qEEKJYq
    """
    return style("""
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
