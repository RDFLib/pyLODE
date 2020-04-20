# The RDF Concepts Vocabulary (RDF)
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **Ontology RDF**
  * RDF ([rdf.ttl](turtle))
### Description
<p>This is the RDF Schema for the RDF vocabulary terms in the RDF Namespace, defined in RDF 1.1 Concepts.</p>

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Alt](#Alt),
[Bag](#Bag),
[List](#List),
[Property](#Property),
[Seq](#Seq),
[Statement](#Statement),
### Alt
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#Alt`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | <p>The class of containers of alternatives.</p>
Super-classes |[rdfs:Container](http://www.w3.org/2000/01/rdf-schema#Container) (c)<br />
### Bag
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#Bag`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | <p>The class of unordered containers.</p>
Super-classes |[rdfs:Container](http://www.w3.org/2000/01/rdf-schema#Container) (c)<br />
### List
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#List`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | <p>The class of RDF Lists.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In domain of |[rdf:rest](http://www.w3.org/1999/02/22-rdf-syntax-ns#rest)<br />[rdf:first](http://www.w3.org/1999/02/22-rdf-syntax-ns#first)<br />
In range of |[rdf:rest](http://www.w3.org/1999/02/22-rdf-syntax-ns#rest)<br />
### Property
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#Property`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | <p>The class of RDF properties.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
### Seq
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#Seq`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | <p>The class of ordered containers.</p>
Super-classes |[rdfs:Container](http://www.w3.org/2000/01/rdf-schema#Container) (c)<br />
### Statement
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | <p>The class of RDF statements.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In domain of |[rdf:predicate](http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate)<br />[rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject)<br />[rdf:object](http://www.w3.org/1999/02/22-rdf-syntax-ns#object)<br />

## Properties
[first](#first),
[object](#object),
[predicate](#predicate),
[rest](#rest),
[subject](#subject),
[type](#type),
[value](#value),
[](first)
### first
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#first`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | The first item in the subject RDF list.
Domain(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](object)
### object
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#object`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | The object of the subject RDF statement.
Domain(s) |[rdf:Statement](http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](predicate)
### predicate
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | The predicate of the subject RDF statement.
Domain(s) |[rdf:Statement](http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](rest)
### rest
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#rest`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | The rest of the subject RDF list after the first item.
Domain(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](subject)
### subject
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#subject`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | The subject of the subject RDF statement.
Domain(s) |[rdf:Statement](http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](type)
### type
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#type`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | The subject is an instance of a class.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](value)
### value
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#value`
Is Defined By | http://www.w3.org/1999/02/22-rdf-syntax-ns#
Description | Idiomatic property used for structured values.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />

## Named Individuals
## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
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