## Namespaces
{%- if default_namespace is not none %}
* **default (:)**
  * `{{ default_namespace }}`
{%- endif %}
{%- for key, value in namespaces.items() %}
* **{{ key }}**
  * `{{ value }}`
{%- endfor %}
