{%- if url is not none -%}
    [{{name}}]({{url}})
{%- else -%}
    {{name}}
{%- endif %}
{%- if orcid %}
    [{{orcid}}]({{url}})
{%- endif %}
{%- if email is not none %}
    (<{{email}}></a>)
{%- endif %}
