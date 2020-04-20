# Alternates View Profile Schema
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://data.surroundaustralia.com/def/alternates`
* **Creators(s)**
  * [Nicholas J. Car](https://orcid.org/0000-0002-8742-7730)
    [[ORCID]](https://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@surroundaustralia.com></a>) of [SURROUND Australia Pty Ltd](https://surroundaustralia.com)
  * [Rob Atkinson](https://orcid.org/0000-0002-7878-2693)
    [[ORCID]](https://orcid.org/0000-0002-7878-2693)
    (<rob.atkinson@surroundaustralia.com></a>) of [SURROUND Australia Pty Ltd](https://surroundaustralia.com)
* **Created**
  * 2019-10-21
* **Modified**
  * 2019-10-21
* **Imports**
  * [skos:](http://www.w3.org/2004/02/skos/core#)
  * [dct:](http://purl.org/dc/terms/)
* **License**
  * [http://creativecommons.org/licenses/by/4.0](http://creativecommons.org/licenses/by/4.0)
* **Ontology RDF**
  * RDF ([alternates.ttl](turtle))
* **Code Repository**
  * <[https://github.com/nicholascar/alternates-view-profile](https://github.com/nicholascar/alternates-view-profile)>
### Description
<p>An ontology that is a profile of Dublin Core Terms that constrains several of its classes and properties for use and adds a class of its own, all to describe representations of resources. The 'View' and 'Format' classes are based on the Epimorphics' implementation of a Linked Data API (ELDA).</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Properties](#properties)
1. [Named Individuals](#namedindividuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Media Type](#MediaType),
[View](#View),
### View
Property | Value
--- | ---
IRI | `http://data.surroundaustralia.com/def/alternates#View`
Description | <p>A set of properties to show for a resource.</p>
Usage Note | Use this class to represent a 'view' that of representations of a resource conform to.
### Media Type
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/MediaType`
Is Defined By | http://purl.org/dc/terms/
Description | <p>A file format or physical medium.</p>
Usage Note | Use this class to represent instances of Media Types as listed by IANA as the target values for dct:format.
In range of |[dct:format](http://purl.org/dc/terms/format)<br />

## Object Properties
[hasDefaultFormat](#hasDefaultFormat),
[hasDefaultView](#hasDefaultView),
[hasView](#hasView),
[](hasDefaultFormat)
### hasDefaultFormat
Property | Value
--- | ---
IRI | `http://data.surroundaustralia.com/def/alternates#hasDefaultFormat`
Super-properties |[dct:format](http://purl.org/dc/terms/format)<br />
[](hasDefaultView)
### hasDefaultView
Property | Value
--- | ---
IRI | `http://data.surroundaustralia.com/def/alternates#hasDefaultView`
Super-properties |[hasView](hasView) (op)<br />
[](hasView)
### hasView
Property | Value
--- | ---
IRI | `http://data.surroundaustralia.com/def/alternates#hasView`

## Properties
[format](#format),
[](format)
### format
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/format`
Is Defined By | http://purl.org/dc/terms/
Usage Note | Use this property to indicate a dct:MediaType
Range(s) |[dct:MediaType](http://purl.org/dc/terms/MediaType) (c)<br />

## Named Individuals
[None](#None),
### None <sup>c</sup>
Property | Value
--- | ---
IRI | `https://surroundaustralia.com`
* **Contributor(s)**
  * [sdo:Organization](https://schema.org/Organization)
## Namespaces
* **default (:)**
  * `http://data.surroundaustralia.com/def/alternates#`
* **:**
  * `http://data.surroundaustralia.com/def/alternates#`
* **dct**
  * `http://purl.org/dc/terms/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
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
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
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