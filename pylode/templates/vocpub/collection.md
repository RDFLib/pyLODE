### {{ default_prefLabel }}
Property | Value
--- | ---
URI | `{{ uri }}`
{%- if prefLabels|length > 0 %}
Preferred Labels | {%- for prefLabel in prefLabels %}{{ prefLabel[0] }} ({{ prefLabel[1] }})<br />{%- endfor %}
{%- endif %}
{%- if altLabels|length > 0 %}
Alternate Labels | {%- for altLabel in altLabels %}{{ altLabel[0] }} ({{ altLabel[1] }})<br />{%- endfor %}
{%- endif %}
{%- if descriptions|length > 0 %}
Description | {%- for description in descriptions %}{{ description[0] }} ({{ description[1] }})<br />{%- endfor %}
{%- endif %}
{%- if scopeNotes|length > 0 %}
Scope Notes | {%- for scopeNote in scopeNotes %}{{ scopeNote[0] }} ({{ scopeNote[1] }})<br />{%- endfor %}
{%- endif %}
{%- if source is not none %}
Source | {{ source }}
{%- endif %}
{%- if members|length > 0 %}
Members | {%- for member in members %}{{ member }}<br />{%- endfor %}
{%- endif %}

