### {{ title }} <sup>c</sup>
Property | Value
--- | ---
URI | `{{ uri }}`
{%- if is_defined_by is not none %}
Is Defined By | {{ is_defined_by }}
{%- endif %}
{%- if classes|length > 0 %}
* **Class(es)**
{%- for class in classes %}
  * {{ class }}
{%- endfor %}
{%- endif %}
{%- if source is not none %}
Source | {{ source }}
{%- endif %}
{%- if description is not none %}
Description | {{ description }}
{%- endif %}
{%- if see_also is not none %}
See Also | {{ see_also }}
{%- endif %}
{%- if same_as is not none %}
Same As | {{ same_as }}
{%- endif %}
