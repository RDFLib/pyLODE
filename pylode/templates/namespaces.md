## Namespaces
* **default ({{ default_namespace_prefix }})**
  * `{{ default_namespace }}`
{%- for key, value in namespaces.items() %}
* **{{ key }}**
  * `{{ value }}`
{%- endfor %}
