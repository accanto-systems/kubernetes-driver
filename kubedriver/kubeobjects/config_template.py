import jinja2 as jinja
from pathlib import Path
from .config_doc import ObjectConfigurationDocument

class ObjectConfigurationTemplate:

    @staticmethod
    def from_file(self, path):
        path = Path(path)
        with open(self.path, 'r') as f:
            content = f.read()
        return ObjectConfigurationTemplate(content)

    def __init__(self, template_content):
        self.template_content = template_content

    def render(self, input_properties):
        jinja_env = jinja.Environment(loader=jinja.BaseLoader)
        rendered_template_content = jinja_env.from_string(self.template_content).render(input_properties)
        return ObjectConfigurationDocument(rendered_template_content)