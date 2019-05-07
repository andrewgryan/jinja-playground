import jinja2


syntax = """
{% set CHUNKS=[] %}
{% for I in range(N) %}
    {% do CHUNKS.append(ITEMS[I::N]) %}
{% endfor %}
{% for I in range(N) %}
    [[task_{{ '%02d' % I }}]]
        [[[environment]]]
            HOURS={{ CHUNKS[I] | join(' ') }}
{% endfor %}
"""

environment = jinja2.Environment(extensions=['jinja2.ext.do'])
items = [1, 2, 3, 4, 5]
N = 2
print(environment.from_string(syntax).render(
    N=N,
    ITEMS=items))
