## Classes
{%- for fid in fids %}
[{{ fid[0] }}]({{ fid[1] }}), 
{%- endfor %}
{%- for class in classes %}
{{ class|safe }}
{%- endfor %}
