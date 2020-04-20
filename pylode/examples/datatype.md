# Datatypes
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/datatype`
* **Creators(s)**
  * None
* **Created**
  * 2019-03-25
* **Modified**
  * 2019-10-03
* **Imports**
  * [http://www.w3.org/ns/prov-o#](http://www.w3.org/ns/prov-o#)
  * [http://purl.org/dc/elements/1.1/](http://purl.org/dc/elements/1.1/)
  * [http://usefulinc.com/ns/doap](http://usefulinc.com/ns/doap)
  * [http://topbraid.org/schema/](http://topbraid.org/schema/)
* **License**
  * [http://creativecommons.org/publicdomain/zero/1.0/](http://creativecommons.org/publicdomain/zero/1.0/)
* **Ontology RDF**
  * RDF ([datatype.ttl](turtle))
* **Code Repository**
  * <[https://github.com/AGLDWG/datatype-ont](https://github.com/AGLDWG/datatype-ont)>
### Description
<p>A set of classes representing data-types. 
These may be used for observation results, or for the range of specific properties in other applications where scaled numbers, ranges, percents etc are required. </p>
* **History Note:** Originally developed for use as the value of an observation result (sosa:hasResult) in the context of the TERN-plot ontology. 

However, objects from these classes may appear in many contexts. 

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Boolean](#Boolean),
[Concept](#Concept),
[Count](#Count),
[Percent](#Percent),
[Percent range](#Percentrange),
[Quantitative Measure](#QuantitativeMeasure),
[Quantitative Range](#QuantitativeRange),
[Text](#Text),
### Boolean
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/Boolean`
Description | <p>Class to encapsulate a true-or-false value</p>
Restrictions |[data:value](datavalue) (dp) **exactly** 1<br />[data:value](datavalue) (dp) **only** [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />
### Concept
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/Concept`
Description | <p>Class to encapsulate a classifier, usually a values from a controlled vocabulary</p>
Restrictions |[data:vocabulary](vocabulary) (op) **exactly** 1<br />[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value) **only** [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value) **exactly** 1<br />
### Count
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/Count`
Description | <p>Class to encapsulate an integer value</p>
Restrictions |[data:uncertainty](datauncertainty) (dp) **max** 1<br />[data:value](datavalue) (dp) **exactly** 1<br />[data:value](datavalue) (dp) **only** [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
### Percent
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/Percent`
Description | <p>Class to encapsulate a quantitative measure expressed as a percent value</p>
Super-classes |[data:QuantitativeMeasure](QuantitativeMeasure) (c)<br />
Restrictions |[data:uncertainty](datauncertainty) (dp) **max** 1<br />[data:unit](unitofmeasure) (op) **value** [http://qudt.org/vocab/unit/PERCENT](http://qudt.org/vocab/unit/PERCENT) (c)<br />
### Percent range
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/PercentRange`
Description | <p>Class to encapsulate a quantitative range expressed as in percent values</p>
Super-classes |[data:QuantitativeRange](QuantitativeRange) (c)<br />
Restrictions |[data:unit](unitofmeasure) (op) **value** [http://qudt.org/vocab/unit/PERCENT](http://qudt.org/vocab/unit/PERCENT) (c)<br />[data:uncertainty](datauncertainty) (dp) **max** 1<br />
### Quantitative Measure
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/QuantitativeMeasure`
Description | <p>Class to encapsulate a quantitative measure value</p>
Restrictions |[data:uncertainty](datauncertainty) (dp) **max** 1<br />[data:value](datavalue) (dp) **exactly** 1<br />[data:unit](unitofmeasure) (op) **exactly** 1<br />[data:value](datavalue) (dp) **only** [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
Sub-classes |[data:Percent](Percent) (c)<br />
### Quantitative Range
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/QuantitativeRange`
Description | <p>Class to encapsulate a quantitative range </p>
Restrictions |[data:min](dataminimum) (dp) **exactly** 1<br />[data:unit](unitofmeasure) (op) **exactly** 1<br />[data:uncertainty](datauncertainty) (dp) **max** 1<br />[data:max](datamaximum) (dp) **exactly** 1<br />
Sub-classes |[data:PercentRange](Percentrange) (c)<br />
### Text
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/Text`
Description | <p>Class to encapsulate a textual value</p>
Restrictions |[data:value](datavalue) (dp) **only** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />[data:value](datavalue) (dp) **exactly** 1<br />

## Object Properties
[data standard](#datastandard),
[unit of measure](#unitofmeasure),
[vocabulary](#vocabulary),
[](datastandard)
### data standard
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/standard`
[](unitofmeasure)
### unit of measure
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/unit`
Super-properties |[data:standard](datastandard) (op)<br />
[](vocabulary)
### vocabulary
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/vocabulary`
Super-properties |[data:standard](datastandard) (op)<br />
Range(s) |[skos:ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme) (c)<br />[skos:Collection](http://www.w3.org/2004/02/skos/core#Collection) (c)<br />[owl:Ontology](http://www.w3.org/2002/07/owl#Ontology) (c)<br />

## Datatype Properties
[data maximum](#datamaximum),
[data minimum](#dataminimum),
[data uncertainty](#datauncertainty),
[data value](#datavalue),
[](datamaximum)
### data maximum
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/max`
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
[](dataminimum)
### data minimum
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/min`
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
[](datauncertainty)
### data uncertainty
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/uncertainty`
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
[](datavalue)
### data value
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/datatype/value`
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />

## Named Individuals
## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/datatype/`
* **data**
  * `http://linked.data.gov.au/def/datatype/`
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
  * `http://schema.org/`
* **sdo1**
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