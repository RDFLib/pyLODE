# {{ label }}
### A Profile

## Metadata
* **URI**
  * `{{ uri }}`
{%- if profiles|length > 0 %}
* **Profile of**
{%- for profile in profiles %}
  * {{ profile }}
{%- endfor %}
{%- endif %}

{%- if publishers|length > 0 %}
* **Publisher(s)**
{%- for publisher in publishers %}
  * {{ publisher }}
{%- endfor %}
{%- endif %}

{%- if creators|length > 0 %}
* **Creators(s)**
{%- for creator in creators %}
  * {{ creator }}
{%- endfor %}
{%- endif %}

{%- if contributors|length > 0 %}
* **Contributor(s)**
{%- for contributor in contributors %}
  * {{ contributor }}
{%- endfor %}
{%- endif %}

{%- if created is not none %}
* **Created**
  * {{ created }}
{%- endif %}
{%- if modified is not none %}
* **Modified**
  * {{ modified }}
{%- endif %}
{%- if issued is not none %}
* **Issued**
  * {{ issued }}
{%- endif %}

{%- if version_info is not none %}
* **Version Information**
  * {{ version_info }}
{%- endif %}
{%- if version_uri is not none %}
* **Version URI**
  * {{ version_uri }}
{%- endif %}

{%- if rights is not none and license is not none %}
* **License &amp; Rights**
  * {{ license }}
  * {{ rights }}
{%- elif rights is not none and license is none %}
* **Rights**
  * {{ rights }}
{%- elif rights is none and license is not none %}
* **License**
  * {{ license }}
{%- endif %}
{%- if source is not none %}
* **Source**
  * {{ source }}  
{%- endif %}
* **Profile RDF**
  * {{ ont_rdf }}

{%- if resource_descriptors|length > 0 %}
* **Has Resource Descriptor(s)**
{%- for rdid, rd in resource_descriptors.items() %}
  * [{{ rd["label"] }}]({{ rdid }})
{%- endfor %}
{%- endif %}
    
{%- if description is not none %}
### Description
{{ description }}
{%- endif %}
