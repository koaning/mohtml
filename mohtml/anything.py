from mohtml import mk_init, mk_repr, mk_docstring

def __getattr__(class_name):
    class_name = class_name.replace("_", "-")
    new_class = type(class_name, (), {
        '__init__': mk_init(class_name),
        '__repr__': mk_repr(class_name),
        '__doc__': mk_docstring(class_name), 
        '__str__': mk_repr(class_name),
        '_repr_html_': mk_repr(class_name),
    })

    return new_class
