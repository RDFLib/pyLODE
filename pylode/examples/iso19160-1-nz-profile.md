Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# ISO19160-1:2015 Address ontology - NZ Profile

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/iso19160-1-address-nz-profile`
* **Publisher(s)**
  * [Australian Government Linked Data Working Group](http://linked.data.gov.au/org/agldwg)
* **Creators(s)**
  * Tristan W. Reed
    (<tristan.reed@curtin.edu.au></a>) of [Curtin University](https://www.curtin.edu.au/)
* **Contributor(s)**
  * [Nicholas J. Car](https://orcid.org/0000-0002-8742-7730)
    [[ORCID]](https://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@surroundaustralia.com></a>) of [SURROUND Australia Pty Ltd](https://surroundaustralia.com)
* **Created**
  * 2017-12-02
* **Modified**
  * 2017-10-24
* **Version URI**
  * [http://linked.data.gov.au/def/iso19160-1-address-nz-profile/1.1](http://linked.data.gov.au/def/iso19160-1-address-nz-profile/1.1)
* **Imports**
  * [http://linked.data.gov.au/def/iso19160-1-address](http://linked.data.gov.au/def/iso19160-1-address)
* **Source**
  * [http://standards.iso.org/iso/19160/-1/NZ%20Profile%20Specification%2020151203.pdf](http://standards.iso.org/iso/19160/-1/NZ%20Profile%20Specification%2020151203.pdf)
* **Ontology RDF**
  * RDF ([iso19160-1-nz-profile.ttl](turtle))
* **Code Repository**
  * [https://github.com/AGLDWG/iso19160-1-address-ont](https://github.com/AGLDWG/iso19160-1-address-ont)
### Description
<p>This ontology is an OWL ontology version of the New Zealand Profile of ISO 19160-1:2015 Addressing.</p>

## Table of Contents
1. [Classes](#classes)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Address Alias](#AddressAlias),
[Address Component](#AddressComponent),
[Address Period](#AddressPeriod),
[Addressable Object](#AddressableObject),
### Address Alias
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/iso19160-1-address-nz-profile#AddressAlias`
Description | <p>ISO 19160 Address Alias class with the additional restrictions of requiring Address Alias lifecycle stage properties to have Address Lifecycle Stage class object and Address Alias lifespan to have Lifespan class objects as their range values.</p>
Super-classes |[http://linked.data.gov.au/def/iso19160-1-address#AddressAlias](http://linked.data.gov.au/def/iso19160-1-address#AddressAlias) (c)<br />
Restrictions |[http://linked.data.gov.au/def/iso19160-1-address#AddressAlias.lifespan](http://linked.data.gov.au/def/iso19160-1-address#AddressAlias.lifespan) **only** [http://linked.data.gov.au/def/iso19160-1-address#Lifespan](http://linked.data.gov.au/def/iso19160-1-address#Lifespan) (c)<br />[http://linked.data.gov.au/def/iso19160-1-address#AddressAlias.lifecycleStage](http://linked.data.gov.au/def/iso19160-1-address#AddressAlias.lifecycleStage) **only** [http://linked.data.gov.au/def/iso19160-1-address#AddressLifecycleStage](http://linked.data.gov.au/def/iso19160-1-address#AddressLifecycleStage) (c)<br />
### Address Component
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/iso19160-1-address-nz-profile#AddressComponent`
Description | <p>ISO 19160 Address Component class with the additional restrictions of requiring one and only one Address lifespan, Address provenance, Address Component lifecycle stage and an Address Component Value locale  properties</p>
Super-classes |[http://linked.data.gov.au/def/iso19160-1-address#AddressComponent](http://linked.data.gov.au/def/iso19160-1-address#AddressComponent) (c)<br />
Restrictions |[http://linked.data.gov.au/def/iso19160-1-address#AddressComponentValue.locale](http://linked.data.gov.au/def/iso19160-1-address#AddressComponentValue.locale) **exactly** 0<br />[http://linked.data.gov.au/def/iso19160-1-address#Address.lifespan](http://linked.data.gov.au/def/iso19160-1-address#Address.lifespan) **exactly** 1<br />[http://linked.data.gov.au/def/iso19160-1-address#Address.provenance](http://linked.data.gov.au/def/iso19160-1-address#Address.provenance) **exactly** 1<br />[http://linked.data.gov.au/def/iso19160-1-address#AddressComponent.lifecycleStage](http://linked.data.gov.au/def/iso19160-1-address#AddressComponent.lifecycleStage) **exactly** 1<br />
### Addressable Object
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/iso19160-1-address-nz-profile#AddressableObject`
Description | <p>ISO 19160 Addressable Object class with the additional restrictions of requiring one and only one Address Component lifespan, Address Component position and an Address Component lifecycle stage properties.</p>
Super-classes |[http://linked.data.gov.au/def/iso19160-1-address#AddressableObject](http://linked.data.gov.au/def/iso19160-1-address#AddressableObject) (c)<br />
Restrictions |[http://linked.data.gov.au/def/iso19160-1-address#AddressComponent.lifecycleStage](http://linked.data.gov.au/def/iso19160-1-address#AddressComponent.lifecycleStage) **exactly** 1<br />[http://linked.data.gov.au/def/iso19160-1-address#Address.position](http://linked.data.gov.au/def/iso19160-1-address#Address.position) **exactly** 0<br />[http://linked.data.gov.au/def/iso19160-1-address#Address.lifespan](http://linked.data.gov.au/def/iso19160-1-address#Address.lifespan) **exactly** 1<br />
### Address Period
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/iso19160-1-address-nz-profile#AddressedPeriod`
Description | <p>ISO 19160 Addressed Period class with the additional restriction of requiring at most one Address provenance properties.</p>
Super-classes |[http://linked.data.gov.au/def/iso19160-1-address#AddressedPeriod](http://linked.data.gov.au/def/iso19160-1-address#AddressedPeriod) (c)<br />
Restrictions |[http://linked.data.gov.au/def/iso19160-1-address#Address.provenance](http://linked.data.gov.au/def/iso19160-1-address#Address.provenance) **max** 1<br />[http://linked.data.gov.au/def/iso19160-1-address#Address.provenance](http://linked.data.gov.au/def/iso19160-1-address#Address.provenance) **only** [http://linked.data.gov.au/def/iso19160-1-address#AddressProvenance](http://linked.data.gov.au/def/iso19160-1-address#AddressProvenance) (c)<br />

## Named Individuals
## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prof**
  * `http://www.w3.org/ns/dx/prof/`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Classes: c
* Object Properties: op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: dp
* Properties: p
* Named Individuals: ni