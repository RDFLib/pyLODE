## Collections
{%- for collection in collections %}
[{{ collection[1] }}](#{{ collection[0] }}), 
{%- endfor %}
{%- for collection in collections %}
{{ collection|safe }}
{%- endfor %}
