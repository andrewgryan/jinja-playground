# Chunking tasks

A simple way to spread items across N tasks, first define
a nested list of lists

```
{% set CHUNKS = [] %}
{% for I in range(N) %}
    {% do CHUNKS.append(ITEMS[I::N]) %}
{% endfor %}
```

Then parse the list of lists into a text file

```
{% for I in range(N) %}
    [[task_{{ '%02d' % I }}]]
        [[[environment]]]
            HOURS={{CHUNKS[I] | join(' ')
{% endfor %}
```

For example, given 5 items `ITEMS=[1, 2, 3, 4, 5]` and two tasks `N=2`, the
above template would generate the following text

```
[[task_00]]
    [[[environment]]]
       HOURS=1 3 5

[[task_01]]
    [[[environment]]]
        HOURS=2 4
```

Although the above technique is straight forward, alternative assignments of items to tasks can be tricky
