Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 

{{ profile|safe }}

{%- if has_collections %}
{{ collections|safe }}
{%- endif %}

{% if has_resource_descriptors %}
## Resource Descriptors
{% for rdid, rd in resource_descriptors.items() %}
{{ rd["html"]|safe }}
{% endfor %}
{% endif %}

{{ namespaces|safe }}
