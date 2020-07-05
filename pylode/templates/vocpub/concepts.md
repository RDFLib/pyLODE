## Concepts
{%- if concept_hierarchy is not none %}
{{ concept_hierarchy|safe }}
{%- endif %}
{%- for concept in concepts %}
{{ concept[2]|safe }}
{%- endfor %}
