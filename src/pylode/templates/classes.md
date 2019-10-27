## Classes
{%- for fid in fids %}
[{{ fid[1] }}](#{{ fid[0] }}), 
{%- endfor %}
{%- for class in classes %}
{{ class|safe }}
{%- endfor %}
