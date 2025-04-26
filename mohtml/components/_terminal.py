from mohtml import div

from jinja2 import Template

template = Template("""
<div style="
    font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
    background-color: {{ theme.bg|default('#2D2D2D') }};
    color: {{ theme.fg|default('#F9F9F9') }};
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    margin: 1em 0;
">
    {# Terminal Title Bar #}
    <div style="
        background-color: {{ theme.title_bg|default('#383838') }};
        padding: 8px 16px;
        position: relative;
        border-bottom: 1px solid rgba(0,0,0,0.1);
    ">
        {# Window Control Dots #}
        <div style="
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            gap: 6px;
        ">
            <div style="
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background-color: #FC625D;
            "></div>
            <div style="
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background-color: #FDBC40;
            "></div>
            <div style="
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background-color: #35CD4B;
            "></div>
        </div>
        
        {# Terminal Title #}
        <div style="
            text-align: center;
            font-size: 13px;
            font-weight: 500;
        ">
            {{ title|default('Terminal') }}
        </div>
    </div>
    
    {# Terminal Content #}
    <div style="
        padding: 8px;
        padding-left: 24px;
        white-space: pre-wrap;
        font-size: 14px;
        line-height: 1.4;
    ">
{{ content }}
    </div>
</div>
""")

def terminal(content, title="terminal", theme="dark"):
    dark_theme = {
        'bg': '#2D2D2D',
        'fg': '#F9F9F9',
        'title_bg': '#383838'
    }
    light_theme = {
        'bg': '#F0F0F0',
        'fg': '#2D2D2D',
        'title_bg': '#E0E0E0'
    }
    context = {
        'content': content,
        'title': title,
        'theme': dark_theme if theme == "dark" else light_theme
    }
    
    return div(template.render(context))

