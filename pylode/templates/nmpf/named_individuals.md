## Named Individuals
{%- for fid in fids %}
[{{ fid[1] }}](#{{ fid[0] }}), 
{%- endfor %}
{%- for ni in named_individuals %}
{{ ni|safe }}
{%- endfor %}
