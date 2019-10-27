# {{ title }}
<sub>metadata by [pyLODE](http://github.com/rdflib/pyLODE)</sub>
## Metadata
* **IRI**
  * `{{ uri }}`
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
{%- if imports|length > 0 %}
{%- if version_uri is not none %}
* **Version IRI**
  * {{ version_uri }}
{%- endif %}
* **Imports**
{%- for import in imports %}
  * {{ import }}  
{%- endfor %}
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
* **Ontology Source**
  * {{ ont_source }}
{%- if repository is not none %}
* **Code Repository**
  * <{{ repository }}>
{%- endif %}

{%- if description is not none %}
### Description
<div id="description">
{{ description }}
{%- endif %}
{%- if historyNote is not none %}
* **History Note:** {{ historyNote }}
{%- endif %}

## Table of Contents
{%- if has_classes %}
* [Classes](#classes)  
{%- endif %}
{%- if has_ops %}
* [Object Properties](#objectproperties)  
{%- endif %}
{%- if has_fps %}
* [Functional Properties](#functionalproperties)  
{%- endif %}
{%- if has_dps %}
* [Datatype Properties](#datatypeproperties)  
{%- endif %}
{%- if has_aps %}
* [Annotation Properties](#annotationproperties)  
{%- endif %}
{%- if has_ps %}
* [Properties](#properties)  
{%- endif %}
{%- if has_nis %}
* [Named Individuals](#namedindividuals)  
{%- endif %}
* [Namespaces](#namespaces)  


## Overview
<img style="width:500px; height:500px; background-color: black;" /><br />
**Figure 1:** Ontology overview  
