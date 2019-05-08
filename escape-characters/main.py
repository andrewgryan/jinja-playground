import jinja2

syntax = """
{% if HOURS | length > 1 %}
ls global_{{ '{' + HOURS | join(',') + '}' }}.nc
{% else %}
ls global_{{ HOURS | join(',') }}.nc
{% endif %}
"""

print(jinja2.Template(syntax).render(HOURS=[1, 2, 3]))
print(jinja2.Template(syntax).render(HOURS=[1,]))
