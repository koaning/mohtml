from bs4 import BeautifulSoup

html_tags = ['a', 'p', 'i', 'b', 'h1','h2','h3','h4','h5','h6','div','span','pre','blockquote','q','ul','ol','li','dl','dt','dd','table','thead','tbody','tfoot','tr','th','td','caption','form','label','select','option','textarea','button','fieldset','legend','article','section','nav','aside','header','footer','main','figure','figcaption','strong','em','mark','code','samp','kbd','var','time','abbr','dfn','sub','sup','audio','video','picture','canvas','details','summary','dialog','script','noscript','template','style','html','head','body']

self_closing_tags = ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']


def mk_init(class_name): 
    def __init__(self, *args, **kwargs):
        self.html_name = class_name
        self.args = args
        if self.args and class_name in self_closing_tags:
            raise RuntimeError(f"{class_name} element cannot have *args because it represents self closing html tag.")
        self.kwargs = kwargs
        if "klass" in self.kwargs:
            self.kwargs["class"] = self.kwargs["klass"]
            del self.kwargs["klass"]

    return __init__

def mk_repr(class_name):
    def __repr__(self):
        elem = f"<{class_name}>" if class_name not in self_closing_tags else f"<{class_name}/>"
        if self.kwargs:
            kwargs_str = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in self.kwargs.items())
            elem = f"<{class_name} {kwargs_str}>"
        for arg in self.args:
            elem += f"{arg}"
        if class_name not in self_closing_tags: 
            elem += f"</{class_name}>"
        return elem

    return __repr__

def mk_docstring(class_name): 
    return f"""Object that represents `<{class_name}>` HTML element."""

for class_name in html_tags + self_closing_tags:
    new_class = type(class_name, (), {
        '__init__': mk_init(class_name),
        '__repr__': mk_repr(class_name),
        '__doc__': mk_docstring(class_name), 
        '__str__': mk_repr(class_name),
        '_repr_html_': mk_repr(class_name),
    })

    globals()[class_name] = new_class

def tailwind_css():
    return script(src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio,line-clamp,container-queries")

def surreal_js():
    return script(src="https://cdn.jsdelivr.net/gh/gnat/surreal@main/surreal.js")

def bootstrap_css():
    return link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC", crossorigin="anonymous")

def alpine_js():
    return script(src="https://cdn.jsdelivr.net/npm/alpinejs@3.14.8/dist/cdn.min.js")


def pretty_print(thing):
    print(BeautifulSoup(str(thing), features="html.parser").prettify())