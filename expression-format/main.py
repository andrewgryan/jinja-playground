import jinja2


syntax = """
{% set ITEMS=[1, 2, 3] %}
{% set STRINGS=[] %}
{% for ITEM in ITEMS %}
{% do STRINGS.append('{:02d}'.format(ITEM)) %}
{% endfor %}
{{ STRINGS }}
"""
environment = jinja2.Environment(extensions=['jinja2.ext.do'])
print(environment.from_string(syntax).render())
