Пицца из нашего меню:

{% for entry in catalog -%}
*{{ entry.title }} #{{loop.index}}*
{{ entry.description }}
    {%- for option in entry.options %}
        {{ option.size }} - *{{ option.price }} руб.*
    {%- endfor %}
{% endfor %}