import jinja2


syntax = """
{% set HOURS=[] %}
{% for I in range(N) %}
    {% do HOURS.append(ITEMS[I::N]) %}
{% endfor %}
{% for I in range(N) %}
    task_{{ '%02d' % I }}
    HOURS={{ HOURS[I] | join(' ') }}
{% endfor %}
"""

environment = jinja2.Environment(extensions=['jinja2.ext.do'])
items = ["A", "B", "C", "D", "E", "F", "G"]
N = 3
print(environment.from_string(syntax).render(
    N=N,
    ITEMS=items))
