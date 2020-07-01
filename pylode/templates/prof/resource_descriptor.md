### {{ label }}
Property | Value
--- | ---
{%- if uri is not none %}
URI | `{{ uri }}`
{%- endif %}
{%- if comment is not none %}
Description | {{ comment }}
{%- endif %}
{%- if artifact is not none %}
Artifact | {{ artifact }}
{%- endif %}
{%- if roles|length > 0 %}
Roles(s) | {%- for role in roles %}{{ role }} <br />{%- endfor %}
{%- endif %}
{%- if conforms|length > 0 %}
Conforms to | {%- for conform in conforms %}{{ conform }} <br />{%- endfor %}
{%- endif %}
{%- if format is not none %}
Format | {{ format }}
{%- endif %}
