{%- if url is not none -%}
    [{{ name }}]({{ url }})
{%- else -%}
    {{ name }}
{%- endif %}
{%- if orcid %}
    {{ orcid }}
{%- endif %}
{%- if email is not none %}
    [{{ email }}]({{ email }})
{%- endif %}
