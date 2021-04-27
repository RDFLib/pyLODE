Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# The RDF Schema vocabulary (RDFS)

## Metadata
* **URI**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **Ontology RDF**
  * RDF ([rdfs.ttl](turtle))

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Class](#Class),
[Container](#Container),
[ContainerMembershipProperty](#ContainerMembershipProperty),
[Datatype](#Datatype),
[Literal](#Literal),
[Resource](#Resource),
### Class
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#Class`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | <p>The class of classes.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Sub-classes |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
In domain of |[rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf)<br />
In range of |[rdfs:range](http://www.w3.org/2000/01/rdf-schema#range)<br />[rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain)<br />[rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf)<br />
Has members |[rdfs:Container](http://www.w3.org/2000/01/rdf-schema#Container)<br />[rdfs:ContainerMembershipProperty](http://www.w3.org/2000/01/rdf-schema#ContainerMembershipProperty)<br />[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class)<br />[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal)<br />[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype)<br />[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource)<br />
### Container
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#Container`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | <p>The class of RDF containers.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
### ContainerMembershipProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#ContainerMembershipProperty`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | <p>The class of container membership properties, rdf:_1, rdf:_2, ...,                     all of which are sub-properties of 'member'.</p>
Super-classes |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
### Datatype
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#Datatype`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | <p>The class of RDF datatypes.</p>
Super-classes |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
### Literal
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#Literal`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | <p>The class of literal values, eg. textual strings and integers.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In range of |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />[rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment)<br />
### Resource
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#Resource`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | <p>The class resource, everything.</p>
Sub-classes |[rdfs:Container](http://www.w3.org/2000/01/rdf-schema#Container) (c)<br />[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
In domain of |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />[rdfs:member](http://www.w3.org/2000/01/rdf-schema#member)<br />[rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment)<br />[rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso)<br />[rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy)<br />
In range of |[rdfs:member](http://www.w3.org/2000/01/rdf-schema#member)<br />[rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy)<br />[rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso)<br />

## Properties
[comment](#comment),
[domain](#domain),
[isDefinedBy](#isDefinedBy),
[label](#label),
[member](#member),
[range](#range),
[seeAlso](#seeAlso),
[subClassOf](#subClassOf),
[subPropertyOf](#subPropertyOf),
[](comment)
### comment
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#comment`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | A description of the subject resource.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](domain)
### domain
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#domain`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | A domain of the subject property.
Domain(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](isDefinedBy)
### isDefinedBy
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#isDefinedBy`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | The defininition of the subject resource.
Super-properties |[rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso)<br />
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](label)
### label
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#label`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | A human-readable name for the subject.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](member)
### member
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#member`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | A member of the subject resource.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](range)
### range
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#range`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | A range of the subject property.
Domain(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](seeAlso)
### seeAlso
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#seeAlso`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | Further information about the subject resource.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](subClassOf)
### subClassOf
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#subClassOf`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | The subject is a subclass of a class.
Domain(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](subPropertyOf)
### subPropertyOf
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#subPropertyOf`
Is Defined By | http://www.w3.org/2000/01/rdf-schema#
Description | The subject is a subproperty of a property.
Domain(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Range(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />

## Named Individuals
## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
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