from mohtml import div, p

def test_basic_div_p():
    assert str(div(p("hello"))) == "<div><p>hello</p></div>"
