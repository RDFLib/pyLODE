### {{ default_prefLabel }}
Property | Value
--- | ---
URI | `{{ uri }}`
{%- if prefLabels|length > 0 %}
Preferred Labels | {%- for prefLabel in prefLabels %}{{ prefLabel[0] }} ({{ prefLabel[1] }})<br />{%- endfor %}
{%- endif %}
{%- if altLabels|length > 0 %}
Alternate Labels | {%- for altLabel in altLabels %}{{ altLabel }}<br />{%- endfor %}
{%- endif %}
{%- if definitions|length > 0 %}
Definitions | {%- for definition in definitions %}{{ definition }}<br />{%- endfor %}
{%- endif %}
{%- if scopeNotes|length > 0 %}
Scope Notes | {%- for scopeNote in scopeNotes %}{{ scopeNote }}<br />{%- endfor %}
{%- endif %}
{%- if examples|length > 0 %}
Examples | {%- for example in examples %}{{ example }}<br />{%- endfor %}
{%- endif %}
{%- if source is not none %}
Source | {{ source }}
{%- endif %}
{%- if broaders|length > 0 %}
Broader Concepts | {%- for broader in broaders %}{{ broader }}<br />{%- endfor %}
{%- endif %}
{%- if narrowers|length > 0 %}
Narrower Concepts | {%- for narrower in narrowers %}{{ narrower }}<br />{%- endfor %}
{%- endif %}
{%- if exactMatches|length > 0 %}
Exact Matches | {%- for exactMatch in exactMatches %}{{ exactMatch }}<br />{%- endfor %}
{%- endif %}
{%- if closeMatches|length > 0 %}
Exact Matches | {%- for closeMatch in closeMatches %}{{ closeMatch }}<br />{%- endfor %}
{%- endif %}
{%- if broadMatches|length > 0 %}
Broad Matches | {%- for broadMatch in broadMatches %}{{ broadMatch }}<br />{%- endfor %}
{%- endif %}
{%- if narrowMatches|length > 0 %}
Narrow Matches | {%- for narrowMatch in narrowMatches %}{{ narrowMatch }}<br />{%- endfor %}
{%- endif %}
