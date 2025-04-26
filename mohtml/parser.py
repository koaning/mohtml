import re
from typing import Callable, Dict, Any, Optional
from functools import wraps
import markdown
from bs4 import BeautifulSoup

class CustomHTMLParser:
    def __init__(self):
        self.components: Dict[str, Callable] = {}
    
    def register(self, tag_name: str):
        """Decorator to register a custom component handler"""
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            self.components[tag_name] = wrapper
            return wrapper
        return decorator
    
    def _parse_attributes(self, tag) -> dict:
        """Convert HTML attributes to Python kwargs"""
        attrs = {}
        for key, value in tag.attrs.items():
            # Try to convert numeric values
            try:
                if value.isdigit():
                    attrs[key] = int(value)
                elif value.replace(".", "").isdigit() and value.count(".") == 1:
                    attrs[key] = float(value)
                else:
                    attrs[key] = value
            except AttributeError:
                # Handle non-string attributes (lists, etc)
                attrs[key] = value
        return attrs
    
    def _process_tag(self, tag) -> str:
        """Process a single tag, handling nested components if necessary"""
        tag_name = tag.name
        
        # If this is a registered component
        if tag_name in self.components:
            # Get the inner content
            inner_content = "".join(str(c) for c in tag.contents)
            
            # Process any nested custom components
            soup = BeautifulSoup(inner_content, 'html.parser')
            for nested_tag in soup.find_all():
                if nested_tag.name in self.components:
                    replacement = self._process_tag(nested_tag)
                    nested_tag.replace_with(BeautifulSoup(replacement, 'html.parser'))
            
            # Get processed inner content
            inner_content = str(soup)
            if len(inner_content) > 0:
                if inner_content[0] == "\n":
                    inner_content = inner_content[1:]
                if inner_content[-1] == "\n":
                    inner_content = inner_content[:-1]
            
            # Get attributes
            attrs = self._parse_attributes(tag)
            
            # Call the registered handler
            return str(self.components[tag_name](inner_content, **attrs))
        
        # If not a custom component, return as is
        return str(tag)
    
    def __call__(self, content) -> str:
        """Parse content and process any custom components"""
        # First check if it's markdown and convert if necessary
        content = str(content)
        if not content.strip().startswith('<'):
            content = markdown.markdown(content)
        
        # Parse the HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Process all custom components
        for tag in soup.find_all():
            if tag.name in self.components:
                replacement = self._process_tag(tag)
                tag.replace_with(BeautifulSoup(replacement, 'html.parser'))
        
        return str(soup)
