# Records Authority Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/ra`
* **Creators(s)**
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@surroundaustralia.com></a>) of [SURROUND Australia Pty Ltd](https://surroundaustralia.com)
* **Contributor(s)**
  * National Archives of Australia, Information Governance Section
    (<information.governance@naa.gov.au></a>)
* **Created**
  * 2019-08-05
* **Modified**
  * 2019-08-06
* **Ontology RDF**
  * RDF ([ra.ttl](turtle))
### Description
<p>This ontology is an <a href="https://www.w3.org/OWL/">OWL</a> interpretation of elements of the <a href="http://naa.gov.au">National Archives of Australia (NAA)</a>'s Records Authorty documents and some of their corresponding NAA database elements. It is dependent on the <a href="http://linked.data.gov.au/def/crs">CRS Ontology</a> for overall context regarding Agency/Record associations and just models the additional RA elements the CRS ontology doesn't.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Disposal Action](#DisposalAction),
[Function](#Function),
[Numbered Subclass](#NumberedSubclass),
[RA Class](#RAClass),
[Record](#Record),
[Records Authorty](#RecordsAuthorty),
### Record
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agr#Record`
Description | <p>The Archiving of Government Records Ontology's Record class.</p>
### Function
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Function`
Description | <p>The Commonwealth Record Series Ontology's Function class.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
### Disposal Action
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/ra#DisposalAction`
Description | <p>A Disposal Action is an instruction to carry out the disposal (retention or descruction) of a government Record. In addition to being a skos:Concept since it acts as a classifier, a Disposal Action is also a Provenance Ontology Plan meaning it instructs a course of action - how to dispose of a record.</p>
Super-classes |[prov:Plan](http://www.w3.org/ns/prov#Plan) (c)<br />[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[requires](requires) (op)<br />
### Numbered Subclass
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/ra#NumberedSubclass`
Description | <p>A numbered subclass is a finer-grained Record categorisation concept than an RA Class within a Records Authority. Numbeed Subclasses are idnetified in Records Authorities with an entry number and relate directly to Disposal Actions.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In domain of |[requires](requires) (op)<br />
### RA Class
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/ra#RaClass`
Description | <p>An RA Class is a categorisation concept for collections of Records within a Records Authority. An RA class is equivalent to the CRS Ontology's Function records categorisation.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
### Records Authorty
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/ra#RecordsAuthority`
Description | <p>A Records Authority is a document that identifies minimum retention periods for Records and authorises the destruction of Records as required by Section 24 of the Archives Act 1983.</p>
<pre><code>                      A Records Authority individual, as represented in this ontology, contains a collection of RA Classes and Numbered Subclasses used to categorise Records in order for them to be assiged Disposal Actions.
</code></pre>
Super-classes |[skos:ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme) (c)<br />[owl:NamedIndividual](http://www.w3.org/2002/07/owl#NamedIndividual) (c)<br />

## Object Properties
[requires](#requires),
[](requires)
### requires
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/ra#requires`
Description | A Numbered Subclass categorisation of a Record requires a particular Disposal Action assignment (categorisation) for that record.
Usage Note | Many Numbered Subclasses map to a few Disposal Actions
Domain(s) |[NumberedSubclass](NumberedSubclass) (c)<br />
Range(s) |[DisposalAction](DisposalAction) (c)<br />

## Named Individuals
## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/ra#`
* **:**
  * `http://linked.data.gov.au/def/ra#`
* **agr**
  * `http://linked.data.gov.au/def/agr#`
* **crs**
  * `http://linked.data.gov.au/def/crs#`
* **dct**
  * `http://purl.org/dc/terms/`
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