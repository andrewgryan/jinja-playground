
# Trick to generate ls patterns

Useful way to include curly braces when generating list commands

```
{% if HOURS | length > 1 %}
    ls global_{{ '{' + HOURS | join(',') + '}' }}.nc
{% else %}
    ls global_{{ HOURS | join(',') }}.nc
{% endif %}
```
