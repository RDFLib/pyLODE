# Decision Provenance ontology (DecPROV)
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://promsns.org/def/decprov`
* **Creators(s)**
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@surroundaustralia.com></a>) of [SURROUND Australia Pty Ltd](https://surroundaustralia.com)
* **Created**
  * 2017-06-28
* **Modified**
  * 2019-08-20
* **Version Information**
  * 2.0
* **Version IRI**
  * [http://promsns.org/def/decprov](http://promsns.org/def/decprov)
* **Imports**
  * [http://www.w3.org/ns/prov-o](http://www.w3.org/ns/prov-o)
* **Ontology RDF**
  * RDF ([decprov.ttl](turtle))
### Description
<p>This ontology is for modelling decisions and thus the causes for actions or the use or generation of things. It allows for a better understanding of <em>why</em> something might have taken place, have been used or produced than the more generic <a href="https://www.w3.org/TR/prov-o/">PROV ontology</a>, on which it is mainly based, does.  </p>
<p>The specialised decision modelling elements of this ontology have been derived from the <a href="https://www.w3.org/2005/Incubator/decision/">W3C Decisions and Decision-Making Incubator Group</a>'s Decision Ontology (DO) which can be found at <a href="https://github.com/nicholascar/decision-o">https://github.com/nicholascar/decision-o</a>. Many DO classes have been aligned with the PROV-O since it is widely recognised that analysing the elements of decisions <em>post hoc</em> is an exercise in provenance.</p>
<p>Unlike the original DO, this ontology cannot be used for <em>normative</em> scenarios: it is only capable of recording decisions that have already been made (so-called <em>data-driven</em> use in the DO). This is because PROV does not have a templating system which can indicate what <em>should</em> occur in future scenarios.</p>
<p>This ontology introduces only one new element for decision modelling over that which was present in the DO: an Agent which allows agency in decision making to be recorded.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Named Individuals](#namedindividuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Answer](#Answer),
[Decision Input Data](#DecisionInputData),
[Decision Logic Expression](#DecisionLogicExpression),
[Decision Making](#DecisionMaking),
[Question](#Question),
[Requirement](#Requirement),
### Decision Input Data
Property | Value
--- | ---
IRI | `http://promsns.org/def/decprov#DecisionInputData`
Description | <p>A Decision Input Data is an Entity that in input to (prov:used by) a DecisionMaking.</p>
Usage Note | Do not use this class to represent decision logic: use DecisionLogicExpression for that.
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
### Decision Logic Expression
Property | Value
--- | ---
IRI | `http://promsns.org/def/decprov#DecisonLogicExpression`
Description | <p>A Decision Logic Expression is a prov:Plan that instructs a course of decision making action.</p>
Usage Note | Use this class to contain decision logic epxpressions in microformats, such as Decision Modelling Notation's FEEL expressions, or as a container entity to hold collections of semantic objects representing decision logic.
Super-classes |[prov:Plan](http://www.w3.org/ns/prov#Plan) (c)<br />
### Answer
Property | Value
--- | ---
IRI | `http://promsns.org/def/do#Answer`
Description | <p>A recorded answer to a Question</p>
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
Restrictions |[prov:wasInfluencedBy](http://www.w3.org/ns/prov#wasInfluencedBy) **some** [do:Question](http://promsns.org/def/do#Question) (c)<br />[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) **some** [do:DecisionMaking](http://promsns.org/def/do#DecisionMaking) (c)<br />
In domain of |[hadQuestion](hadquestion) (op)<br />
### Decision Making
Property | Value
--- | ---
IRI | `http://promsns.org/def/do#DecisionMaking`
Description | <p>A temporal event in which decision processes are undertaken, such as initiating sub-questions for the question to be answered, consideration of options etc.</p>
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
### Question
Property | Value
--- | ---
IRI | `http://promsns.org/def/do#Question`
Description | <p>A recorded question</p>
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
In range of |[hadQuestion](hadquestion) (op)<br />
### Requirement
Property | Value
--- | ---
IRI | `http://promsns.org/def/do#Requirement`
Description | <p>Requirements require something from an OptionSelection Activity. They indicate their requirement with a set (a class) of objects. They are then satisified by the presense of an onject within that class. Multiple Requirements can be intersected to require very specific OptionSelection outcomes.</p>
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />

## Object Properties
[had answer](#hadanswer),
[had question](#hadquestion),
[](hadanswer)
### had answer
Property | Value
--- | ---
IRI | `http://promsns.org/def/decprov#hadAnswer`
Description | Links a Question to an Answer that a DecisionMaking generated for it.
Super-properties |[prov:generated](http://www.w3.org/ns/prov#generated)<br />
[](hadquestion)
### had question
Property | Value
--- | ---
IRI | `http://promsns.org/def/decprov#hadQuestion`
Description | Links an Answer to the Question that motivated a DecisionMaking to generate it.
Super-properties |[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom)<br />
Domain(s) |[do:Answer](http://promsns.org/def/do#Answer) (c)<br />
Range(s) |[do:Question](http://promsns.org/def/do#Question) (c)<br />

## Named Individuals
[DecisionMaker](#DecisionMaker),
### DecisionMaker <sup>c</sup>
Property | Value
--- | ---
IRI | `http://promsns.org/def/do#DecisionMaker`
* **Contributor(s)**
  * [prov:Role](http://www.w3.org/ns/prov#Role)
## Namespaces
* **default (:)**
  * `http://promsns.org/def/decprov#`
* **:**
  * `http://promsns.org/def/decprov#`
* **dct**
  * `http://purl.org/dc/terms/`
* **do**
  * `http://promsns.org/def/do#`
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