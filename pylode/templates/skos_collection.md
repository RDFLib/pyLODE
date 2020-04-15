### {{ default_prefLabel }}
Property | Value
--- | ---
IRI | `{{ uri }}`
{%- if prefLabels|length > 0 %}
Preferred Labels | {%- for prefLabel in prefLabels %}{{ prefLabels }}<br />{%- endfor %}
{%- endif %}
{%- if altLabels|length > 0 %}
Alternate Labels | {%- for altLabel in altLabels %}{{ altLabel }}<br />{%- endfor %}
{%- endif %}
{%- if descriptions|length > 0 %}
Description | {%- for description in descriptions %}{{ descriptions }}<br />{%- endfor %}
{%- endif %}
{%- if scopeNotes|length > 0 %}
Scope Notes | {%- for scopeNote in scopeNotes %}{{ scopeNote }}<br />{%- endfor %}
{%- endif %}
{%- if source is not none %}
Source | {{ source }}
{%- endif %}
{%- if members|length > 0 %}
Broader Concepts | {%- for member in members %}{{ members }}<br />{%- endfor %}
{%- endif %}

