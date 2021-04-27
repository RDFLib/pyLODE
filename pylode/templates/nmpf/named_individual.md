### {{ title }} <sup>c</sup>
Property | Value
--- | ---
URI | `{{ uri }}`
{%- if policy_code is not none %}
Policy Code | {{ policy_code }}
{%- endif %}
{%- if is_defined_by is not none %}
Is Defined By | {{ is_defined_by }}
{%- endif %}
{%- if classes|length > 0 %}
* **Contributor(s)**
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
{%- if directs_chapter is not none %}
Directs Chapter Topic Activity Proposals | {{ directs_chapter }}
{%- endif %}
{%- if directs_other is not none %}
Directs Other Proposals in Relation to the Topic Activity | {{ directs_other }}
{%- endif %}
{%- if applies_whole is not none %}
Applies to the Whole Maritime Area | {{ applies_whole }}
{%- endif %}
