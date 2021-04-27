[]({{ fid }})
### {{ title }}
Property | Value
--- | ---
URI | `{{ uri }}`
{%- if is_defined_by is not none %}
Is Defined By | {{ is_defined_by }}
{%- endif %}
{%- if source is not none %}
Source | {{ source }}
{%- endif %}
{%- if description is not none %}
Description | {{ description }}
{%- endif %}
{%- if scopeNote is not none %}
Scope Notes | {{ scopeNote }}
{%- endif %}
{%- if example is not none %}
Example | ```{{ example|safe }}```
{%- endif %}
{%- if supers|length > 0 %}
Super-properties | {%- for super in supers %}{{ super }}<br />{%- endfor %}
{%- endif %}
{%- if domains|length > 0 or domainIncludes|length > 0 %}
Domain(s) | {%- if domains|length > 0 %}{%- for domain in domains %}{{ domain }}<br />{%- endfor %}
{%- endif %}
{%- if domainIncludes|length > 0 %}
([sdo:domainIncludes](https://schema.org/domainIncludes))<br />{%- for domainInclude in domainIncludes %}{{ domainInclude }}<br />{%- endfor %}
{%- endif %}
{%- endif %}
{%- if ranges|length > 0 or rangeIncludes|length > 0 %}
Range(s) | {%- if ranges|length > 0 %}{%- for range in ranges %}{{ range }}<br />{%- endfor %}
{%- endif %}
{%- if rangeIncludes|length > 0 %}
([sdo:rangeIncludes](https://schema.org/domainIncludes)){%- for rangeInclude in rangeIncludes %}{{ rangeInclude }}{%- endfor %}
{%- endif %}
{%- endif %}
