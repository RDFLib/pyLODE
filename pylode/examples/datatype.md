Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Datatypes

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/datatype`
* **Creators(s)**
  * None
* **Created**
  * 2019-03-25
* **Modified**
  * 2019-10-03
* **Imports**
  * [http://purl.org/dc/elements/1.1/](http://purl.org/dc/elements/1.1/)
  * [http://topbraid.org/schema/](http://topbraid.org/schema/)
  * [http://usefulinc.com/ns/doap](http://usefulinc.com/ns/doap)
  * [http://www.w3.org/ns/prov-o#](http://www.w3.org/ns/prov-o#)
* **License**
  * [http://creativecommons.org/publicdomain/zero/1.0/](http://creativecommons.org/publicdomain/zero/1.0/)
* **Ontology RDF**
  * RDF ([datatype.ttl](turtle))
* **Code Repository**
  * [https://github.com/AGLDWG/datatype-ont](https://github.com/AGLDWG/datatype-ont)
### Description
<p>A set of classes representing data-types. 
These may be used for observation results, or for the range of specific properties in other applications where scaled numbers, ranges, percents etc are required. </p>
* **History Note:** <p>Originally developed for use as the value of an observation result (sosa:hasResult) in the context of the TERN-plot ontology. </p>
<p>However, objects from these classes may appear in many contexts. </p>

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
URI | `http://linked.data.gov.au/def/datatype/Boolean`
Description | <p>Class to encapsulate a true-or-false value</p>
Restrictions |[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **exactly** 1<br />[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **only** [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />
### Concept
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/Concept`
Description | <p>Class to encapsulate a classifier, usually a values from a controlled vocabulary</p>
Restrictions |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value) **only** [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value) **exactly** 1<br />[http://linked.data.gov.au/def/datatype/vocabulary](http://linked.data.gov.au/def/datatype/vocabulary) (op) **exactly** 1<br />
### Count
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/Count`
Description | <p>Class to encapsulate an integer value</p>
Restrictions |[http://linked.data.gov.au/def/datatype/uncertainty](http://linked.data.gov.au/def/datatype/uncertainty) (dp) **max** 1<br />[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **only** [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **exactly** 1<br />
### Percent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/Percent`
Description | <p>Class to encapsulate a quantitative measure expressed as a percent value</p>
Super-classes |[http://linked.data.gov.au/def/datatype/QuantitativeMeasure](http://linked.data.gov.au/def/datatype/QuantitativeMeasure) (c)<br />
Restrictions |[http://linked.data.gov.au/def/datatype/unit](http://linked.data.gov.au/def/datatype/unit) (op) **value** [http://qudt.org/vocab/unit/PERCENT](http://qudt.org/vocab/unit/PERCENT) (c)<br />[http://linked.data.gov.au/def/datatype/uncertainty](http://linked.data.gov.au/def/datatype/uncertainty) (dp) **max** 1<br />
### Percent range
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/PercentRange`
Description | <p>Class to encapsulate a quantitative range expressed as in percent values</p>
Super-classes |[http://linked.data.gov.au/def/datatype/QuantitativeRange](http://linked.data.gov.au/def/datatype/QuantitativeRange) (c)<br />
Restrictions |[http://linked.data.gov.au/def/datatype/uncertainty](http://linked.data.gov.au/def/datatype/uncertainty) (dp) **max** 1<br />[http://linked.data.gov.au/def/datatype/unit](http://linked.data.gov.au/def/datatype/unit) (op) **value** [http://qudt.org/vocab/unit/PERCENT](http://qudt.org/vocab/unit/PERCENT) (c)<br />
### Quantitative Measure
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/QuantitativeMeasure`
Description | <p>Class to encapsulate a quantitative measure value</p>
Restrictions |[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **only** [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />[http://linked.data.gov.au/def/datatype/unit](http://linked.data.gov.au/def/datatype/unit) (op) **exactly** 1<br />[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **exactly** 1<br />[http://linked.data.gov.au/def/datatype/uncertainty](http://linked.data.gov.au/def/datatype/uncertainty) (dp) **max** 1<br />
Sub-classes |[http://linked.data.gov.au/def/datatype/Percent](http://linked.data.gov.au/def/datatype/Percent) (c)<br />
### Quantitative Range
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/QuantitativeRange`
Description | <p>Class to encapsulate a quantitative range </p>
Restrictions |[http://linked.data.gov.au/def/datatype/uncertainty](http://linked.data.gov.au/def/datatype/uncertainty) (dp) **max** 1<br />[http://linked.data.gov.au/def/datatype/unit](http://linked.data.gov.au/def/datatype/unit) (op) **exactly** 1<br />[http://linked.data.gov.au/def/datatype/min](http://linked.data.gov.au/def/datatype/min) (dp) **exactly** 1<br />[http://linked.data.gov.au/def/datatype/max](http://linked.data.gov.au/def/datatype/max) (dp) **exactly** 1<br />
Sub-classes |[http://linked.data.gov.au/def/datatype/PercentRange](http://linked.data.gov.au/def/datatype/PercentRange) (c)<br />
### Text
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/Text`
Description | <p>Class to encapsulate a textual value</p>
Restrictions |[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **exactly** 1<br />[http://linked.data.gov.au/def/datatype/value](http://linked.data.gov.au/def/datatype/value) (dp) **only** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

## Object Properties
[data standard](#datastandard),
[unit of measure](#unitofmeasure),
[vocabulary](#vocabulary),
[](datastandard)
### data standard
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/standard`
Description | Measurement standard, scale, uom, reference system, controlled vocabulary, taxonomy etc
[](unitofmeasure)
### unit of measure
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/unit`
Description | Measurement scale 
Super-properties |[http://linked.data.gov.au/def/datatype/standard](http://linked.data.gov.au/def/datatype/standard) (op)<br />
[](vocabulary)
### vocabulary
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/vocabulary`
Description | controlled vocabulary, taxonomy etc 
Super-properties |[http://linked.data.gov.au/def/datatype/standard](http://linked.data.gov.au/def/datatype/standard) (op)<br />
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
URI | `http://linked.data.gov.au/def/datatype/max`
Description | Maximum value of a range
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
[](dataminimum)
### data minimum
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/min`
Description | Minimum value of range
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
[](datauncertainty)
### data uncertainty
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/uncertainty`
Description | Uncertainty for a quantitative value
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
[](datavalue)
### data value
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/datatype/value`
Description | simple value (a literal)
Super-properties |[rdf:value](http://www.w3.org/1999/02/22-rdf-syntax-ns#value)<br />

## Named Individuals
## Namespaces
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
* **schema**
  * `http://schema.org/`
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