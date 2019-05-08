
# Trick to generate ls patterns

Useful way to include curly braces when generating list commands

```
{% if HOURS | length > 1 %}
    ls global_{{ '{' + HOURS | join(',') + '}' }}.nc
{% else %}
    ls global_{{ HOURS | join(',') }}.nc
{% endif %}
```

In the case where the list is longer than a single entry, the following
code is generated

```
ls global_{1,2,3}.nc
```

If there is only a single item to process the other branch of the if statement
is processed

```
ls global_1.nc
```

