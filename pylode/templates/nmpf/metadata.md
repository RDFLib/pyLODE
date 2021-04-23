# {{ title }}

## Metadata
* **URI**
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
* **Version URI**
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
{%- if source is not none %}
* **Source**
  * {{ source }}
{%- endif %}
* **Ontology RDF**
  * {{ ont_rdf }}
{%- if repository is not none %}
* **Code Repository**
  * {{ repository }}
{%- endif %}

{%- if description is not none %}
### Description
{{ description }}
{%- endif %}
{%- if historyNote is not none %}
* **History Note:** {{ historyNote }}
{%- endif %}

## Table of Contents
{%- if has_classes %}
1. [Classes](#classes)
{%- endif %}
{%- if has_ops %}
1. [Object Properties](#objectproperties)
{%- endif %}
{%- if has_fps %}
1. [Functional Properties](#functionalproperties)
{%- endif %}
{%- if has_dps %}
1. [Datatype Properties](#datatypeproperties)
{%- endif %}
{%- if has_aps %}
1. [Annotation Properties](#annotationproperties)
{%- endif %}
{%- if has_ps %}
1. [Properties](#properties)
{%- endif %}
{%- if has_nis %}
1. [Named Individuals](#namedindividuals)
{%- endif %}
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
