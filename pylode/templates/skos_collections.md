## Collections
{%- for collection in collections %}
* [{{ collection[0] }}](#{{ collection[1] }})   
{%- endfor %}
{%- for collection in collections %}
{{ collection[2]|safe }}
{%- endfor %}
