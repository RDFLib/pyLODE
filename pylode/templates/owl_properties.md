{%- if op_instances|length > 0 %}
## Object Properties
{%- for p in op_instances %}
[{{ p[0] }}](#{{ p[1] }}),
{%- endfor %}
{%- for p in op_instances %}
{{ p[2]|safe }}
{%- endfor %}
{% endif %}
{%- if fp_instances|length > 0 %}
## Functional Properties
{%- for p in fp_instances %}
[{{ p[0] }}](#{{ p[1] }}),
{%- endfor %}
{%- for p in fp_instances %}
{{ p[2]|safe }}
{%- endfor %}
{% endif %}
{%- if dp_instances|length > 0 %}
## Datatype Properties
{%- for p in dp_instances %}
[{{ p[0] }}](#{{ p[1] }}),
{%- endfor %}
{%- for p in dp_instances %}
{{ p[2]|safe }}
{%- endfor %}
{% endif %}
{%- if ap_instances|length > 0 %}
## Annotation Properties
{%- for p in ap_instances %}
[{{ p[0] }}](#{{ p[1] }}),
{%- endfor %}
{%- for p in ap_instances %}
{{ p[2]|safe }}
{%- endfor %}
{% endif %}
{%- if p_instances|length > 0 %}
## Properties
{%- for p in p_instances %}
[{{ p[0] }}](#{{ p[1] }}),
{%- endfor %}
{%- for p in p_instances %}
{{ p[2]|safe }}
{%- endfor %}
{% endif %}
