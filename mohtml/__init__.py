from bs4 import BeautifulSoup

html_tags = ['a', 'p','h1','h2','h3','h4','h5','h6','div','span','pre','blockquote','q','ul','ol','li','dl','dt','dd','table','thead','tbody','tfoot','tr','th','td','caption','form','label','select','option','textarea','button','fieldset','legend','article','section','nav','aside','header','footer','main','figure','figcaption','strong','em','mark','code','samp','kbd','var','time','abbr','dfn','sub','sup','audio','video','picture','canvas','details','summary','dialog','script','noscript','template','style','html','head','body']

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
        elem = f"<{class_name}>" if class_name in html_tags else f"<{class_name}/>"
        if self.kwargs:
            kwargs_str = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in self.kwargs.items())
            elem = f"<{class_name} {kwargs_str}>"
        for arg in self.args:
            elem += f"\n   {arg}"
        if class_name in html_tags: 
            elem += f"\n</{class_name}>"
        return BeautifulSoup(elem, features="html.parser").prettify()

    return __repr__

def mk_docstring(class_name): 
    return f"""Object that represents `<{class_name}>` HTML element."""

for class_name in html_tags + self_closing_tags:
    new_class = type(class_name, (), {
        '__init__': mk_init(class_name),
        '__repr__': mk_repr(class_name),
        '__doc__': mk_docstring(class_name), 
        '__str__': mk_repr(class_name)
    })

    globals()[class_name] = new_class