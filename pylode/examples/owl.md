Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# The OWL 2 Schema vocabulary (OWL 2)

## Metadata
* **URI**
  * `http://www.w3.org/2002/07/owl`
* **Version Information**
  * $Date: 2009/11/15 10:54:12 $
* **Version URI**
  * [http://www.w3.org/2002/07/owl](http://www.w3.org/2002/07/owl)
* **Imports**
  * [http://www.w3.org/2000/01/rdf-schema](http://www.w3.org/2000/01/rdf-schema)
* **Ontology RDF**
  * RDF ([owl.ttl](turtle))
### Description
<p>This ontology partially describes the built-in classes and
  properties that together form the basis of the RDF/XML syntax of OWL 2.
  The content of this ontology is based on Tables 6.1 and 6.2
  in Section 6.4 of the OWL 2 RDF-Based Semantics specification,
  available at http://www.w3.org/TR/owl2-rdf-based-semantics/.
  Please note that those tables do not include the different annotations
  (labels, comments and rdfs:isDefinedBy links) used in this file.
  Also note that the descriptions provided in this ontology do not
  provide a complete and correct formal description of either the syntax
  or the semantics of the introduced terms (please see the OWL 2
  recommendations for the complete and normative specifications).
  Furthermore, the information provided by this ontology may be
  misleading if not used with care. This ontology SHOULD NOT be imported
  into OWL ontologies. Importing this file into an OWL 2 DL ontology
  will cause it to become an OWL 2 Full ontology and may have other,
  unexpected, consequences.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[AllDifferent](#AllDifferent),
[AllDisjointClasses](#AllDisjointClasses),
[AllDisjointProperties](#AllDisjointProperties),
[Annotation](#Annotation),
[AnnotationProperty](#AnnotationProperty),
[AsymmetricProperty](#AsymmetricProperty),
[Axiom](#Axiom),
[Class](#Class),
[DataRange](#DataRange),
[DatatypeProperty](#DatatypeProperty),
[DeprecatedClass](#DeprecatedClass),
[DeprecatedProperty](#DeprecatedProperty),
[FunctionalProperty](#FunctionalProperty),
[InverseFunctionalProperty](#InverseFunctionalProperty),
[IrreflexiveProperty](#IrreflexiveProperty),
[NamedIndividual](#NamedIndividual),
[NegativePropertyAssertion](#NegativePropertyAssertion),
[Nothing](#Nothing),
[ObjectProperty](#ObjectProperty),
[Ontology](#Ontology),
[OntologyProperty](#OntologyProperty),
[ReflexiveProperty](#ReflexiveProperty),
[Restriction](#Restriction),
[SymmetricProperty](#SymmetricProperty),
[Thing](#Thing),
[TransitiveProperty](#TransitiveProperty),
### AllDifferent
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#AllDifferent`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of collections of pairwise different individuals.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In domain of |[owl:distinctMembers](distinctMembers)<br />
### AllDisjointClasses
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#AllDisjointClasses`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of collections of pairwise disjoint classes.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
### AllDisjointProperties
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#AllDisjointProperties`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of collections of pairwise disjoint properties.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
### Annotation
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#Annotation`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of annotated annotations for which the RDF serialization consists of an annotated subject, predicate and object.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
### AnnotationProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#AnnotationProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of annotation properties.</p>
Super-classes |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Has members |[owl:versionInfo](versionInfo) (ap)<br />[owl:deprecated](deprecated) (ap)<br />[owl:incompatibleWith](incompatibleWith) (ap)<br />[owl:backwardCompatibleWith](backwardCompatibleWith) (ap)<br />[owl:priorVersion](priorVersion) (ap)<br />
### AsymmetricProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#AsymmetricProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of asymmetric properties.</p>
Super-classes |[owl:ObjectProperty](ObjectProperty) (c)<br />
### Axiom
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#Axiom`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of annotated axioms for which the RDF serialization consists of an annotated subject, predicate and object.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
### Class
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#Class`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of OWL classes.</p>
Super-classes |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
Sub-classes |[owl:Restriction](Restriction) (c)<br />
In domain of |[owl:disjointWith](disjointWith)<br />[owl:hasKey](hasKey)<br />[owl:disjointUnionOf](disjointUnionOf)<br />[owl:complementOf](complementOf)<br />
In range of |[owl:disjointWith](disjointWith)<br />[owl:onClass](onClass)<br />[owl:complementOf](complementOf)<br />
Has members |[owl:Thing](Thing)<br />[owl:Nothing](Nothing)<br />
### DataRange
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#DataRange`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of OWL data ranges, which are special kinds of datatypes. Note: The use of the IRI owl:DataRange has been deprecated as of OWL 2. The IRI rdfs:Datatype SHOULD be used instead.</p>
Super-classes |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
### DatatypeProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#DatatypeProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of data properties.</p>
Super-classes |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Has members |[owl:topDataProperty](topDataProperty) (dp)<br />[owl:bottomDataProperty](bottomDataProperty) (dp)<br />
### DeprecatedClass
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#DeprecatedClass`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of deprecated classes.</p>
Super-classes |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
### DeprecatedProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#DeprecatedProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of deprecated properties.</p>
Super-classes |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
### FunctionalProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#FunctionalProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of functional properties.</p>
Super-classes |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
### InverseFunctionalProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#InverseFunctionalProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of inverse-functional properties.</p>
Super-classes |[owl:ObjectProperty](ObjectProperty) (c)<br />
### IrreflexiveProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#IrreflexiveProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of irreflexive properties.</p>
Super-classes |[owl:ObjectProperty](ObjectProperty) (c)<br />
### NamedIndividual
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#NamedIndividual`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of named individuals.</p>
Super-classes |[owl:Thing](Thing) (c)<br />
### NegativePropertyAssertion
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#NegativePropertyAssertion`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of negative property assertions.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In domain of |[owl:targetValue](targetValue)<br />[owl:sourceIndividual](sourceIndividual)<br />[owl:targetIndividual](targetIndividual)<br />[owl:assertionProperty](assertionProperty)<br />
### Nothing
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#Nothing`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>This is the empty class.</p>
Super-classes |[owl:Thing](Thing) (c)<br />
### ObjectProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#ObjectProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of object properties.</p>
Super-classes |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Sub-classes |[owl:InverseFunctionalProperty](InverseFunctionalProperty) (c)<br />[owl:TransitiveProperty](TransitiveProperty) (c)<br />[owl:AsymmetricProperty](AsymmetricProperty) (c)<br />[owl:ReflexiveProperty](ReflexiveProperty) (c)<br />[owl:SymmetricProperty](SymmetricProperty) (c)<br />[owl:IrreflexiveProperty](IrreflexiveProperty) (c)<br />
In domain of |[owl:inverseOf](inverseOf)<br />[owl:propertyChainAxiom](propertyChainAxiom)<br />
In range of |[owl:inverseOf](inverseOf)<br />
Has members |[owl:topObjectProperty](topObjectProperty) (op)<br />[owl:bottomObjectProperty](bottomObjectProperty) (op)<br />
### Ontology
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#Ontology`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of ontologies.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In domain of |[owl:versionIRI](http://www.w3.org/2002/07/owl#versionIRI)<br />[owl:backwardCompatibleWith](backwardCompatibleWith) (ap)<br />[owl:imports](http://www.w3.org/2002/07/owl#imports)<br />[owl:priorVersion](priorVersion) (ap)<br />[owl:incompatibleWith](incompatibleWith) (ap)<br />
In range of |[owl:backwardCompatibleWith](backwardCompatibleWith) (ap)<br />[owl:versionIRI](http://www.w3.org/2002/07/owl#versionIRI)<br />[owl:incompatibleWith](incompatibleWith) (ap)<br />[owl:priorVersion](priorVersion) (ap)<br />[owl:imports](http://www.w3.org/2002/07/owl#imports)<br />
Has members |[http://www.w3.org/2002/07/owl](http://www.w3.org/2002/07/owl)<br />
### OntologyProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#OntologyProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of ontology properties.</p>
Super-classes |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Has members |[owl:imports](http://www.w3.org/2002/07/owl#imports)<br />[owl:incompatibleWith](incompatibleWith) (ap)<br />[owl:priorVersion](priorVersion) (ap)<br />[owl:versionIRI](http://www.w3.org/2002/07/owl#versionIRI)<br />[owl:backwardCompatibleWith](backwardCompatibleWith) (ap)<br />
### ReflexiveProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#ReflexiveProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of reflexive properties.</p>
Super-classes |[owl:ObjectProperty](ObjectProperty) (c)<br />
### Restriction
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#Restriction`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of property restrictions.</p>
Super-classes |[owl:Class](Class) (c)<br />
In domain of |[owl:allValuesFrom](allValuesFrom)<br />[owl:maxCardinality](maxCardinality)<br />[owl:hasValue](hasValue)<br />[owl:hasSelf](hasSelf)<br />[owl:onClass](onClass)<br />[owl:minCardinality](minCardinality)<br />[owl:onProperties](onProperties)<br />[owl:minQualifiedCardinality](minQualifiedCardinality)<br />[owl:onDataRange](onDataRange)<br />[owl:onProperty](onProperty)<br />[owl:qualifiedCardinality](qualifiedCardinality)<br />[owl:maxQualifiedCardinality](maxQualifiedCardinality)<br />[owl:cardinality](cardinality)<br />[owl:someValuesFrom](someValuesFrom)<br />
### SymmetricProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#SymmetricProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of symmetric properties.</p>
Super-classes |[owl:ObjectProperty](ObjectProperty) (c)<br />
### Thing
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#Thing`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of OWL individuals.</p>
Sub-classes |[owl:NamedIndividual](NamedIndividual) (c)<br />[owl:Nothing](Nothing) (c)<br />
In domain of |[owl:bottomDataProperty](bottomDataProperty) (dp)<br />[owl:differentFrom](differentFrom)<br />[owl:sameAs](sameAs)<br />[owl:topDataProperty](topDataProperty) (dp)<br />[owl:bottomObjectProperty](bottomObjectProperty) (op)<br />[owl:topObjectProperty](topObjectProperty) (op)<br />
In range of |[owl:differentFrom](differentFrom)<br />[owl:sameAs](sameAs)<br />[owl:targetIndividual](targetIndividual)<br />[owl:topObjectProperty](topObjectProperty) (op)<br />[owl:sourceIndividual](sourceIndividual)<br />[owl:bottomObjectProperty](bottomObjectProperty) (op)<br />
### TransitiveProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#TransitiveProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | <p>The class of transitive properties.</p>
Super-classes |[owl:ObjectProperty](ObjectProperty) (c)<br />

## Object Properties
[bottomObjectProperty](#bottomObjectProperty),
[topObjectProperty](#topObjectProperty),
[](bottomObjectProperty)
### bottomObjectProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#bottomObjectProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The object property that does not relate any two individuals.
Domain(s) |[owl:Thing](Thing) (c)<br />
Range(s) |[owl:Thing](Thing) (c)<br />
[](topObjectProperty)
### topObjectProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#topObjectProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The object property that relates every two individuals.
Domain(s) |[owl:Thing](Thing) (c)<br />
Range(s) |[owl:Thing](Thing) (c)<br />

## Datatype Properties
[bottomDataProperty](#bottomDataProperty),
[topDataProperty](#topDataProperty),
[](bottomDataProperty)
### bottomDataProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#bottomDataProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The data property that does not relate any individual to any data value.
Domain(s) |[owl:Thing](Thing) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](topDataProperty)
### topDataProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#topDataProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The data property that relates every individual to every data value.
Domain(s) |[owl:Thing](Thing) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />

## Annotation Properties
[backwardCompatibleWith](#backwardCompatibleWith),
[deprecated](#deprecated),
[incompatibleWith](#incompatibleWith),
[priorVersion](#priorVersion),
[versionInfo](#versionInfo),
[](backwardCompatibleWith)
### backwardCompatibleWith
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#backwardCompatibleWith`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The annotation property that indicates that a given ontology is backward compatible with another ontology.
Domain(s) |[owl:Ontology](Ontology) (c)<br />
Range(s) |[owl:Ontology](Ontology) (c)<br />
[](deprecated)
### deprecated
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#deprecated`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The annotation property that indicates that a given entity has been deprecated.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](incompatibleWith)
### incompatibleWith
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#incompatibleWith`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The annotation property that indicates that a given ontology is incompatible with another ontology.
Domain(s) |[owl:Ontology](Ontology) (c)<br />
Range(s) |[owl:Ontology](Ontology) (c)<br />
[](priorVersion)
### priorVersion
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#priorVersion`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The annotation property that indicates the predecessor ontology of a given ontology.
Domain(s) |[owl:Ontology](Ontology) (c)<br />
Range(s) |[owl:Ontology](Ontology) (c)<br />
[](versionInfo)
### versionInfo
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#versionInfo`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The annotation property that provides version information for an ontology or another OWL construct.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />

## Properties
[allValuesFrom](#allValuesFrom),
[annotatedProperty](#annotatedProperty),
[annotatedSource](#annotatedSource),
[annotatedTarget](#annotatedTarget),
[assertionProperty](#assertionProperty),
[cardinality](#cardinality),
[complementOf](#complementOf),
[datatypeComplementOf](#datatypeComplementOf),
[differentFrom](#differentFrom),
[disjointUnionOf](#disjointUnionOf),
[disjointWith](#disjointWith),
[distinctMembers](#distinctMembers),
[equivalentClass](#equivalentClass),
[equivalentProperty](#equivalentProperty),
[hasKey](#hasKey),
[hasSelf](#hasSelf),
[hasValue](#hasValue),
[intersectionOf](#intersectionOf),
[inverseOf](#inverseOf),
[maxCardinality](#maxCardinality),
[maxQualifiedCardinality](#maxQualifiedCardinality),
[members](#members),
[minCardinality](#minCardinality),
[minQualifiedCardinality](#minQualifiedCardinality),
[onClass](#onClass),
[onDataRange](#onDataRange),
[onDatatype](#onDatatype),
[onProperties](#onProperties),
[onProperty](#onProperty),
[oneOf](#oneOf),
[propertyChainAxiom](#propertyChainAxiom),
[propertyDisjointWith](#propertyDisjointWith),
[qualifiedCardinality](#qualifiedCardinality),
[sameAs](#sameAs),
[someValuesFrom](#someValuesFrom),
[sourceIndividual](#sourceIndividual),
[targetIndividual](#targetIndividual),
[targetValue](#targetValue),
[unionOf](#unionOf),
[withRestrictions](#withRestrictions),
[](allValuesFrom)
### allValuesFrom
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#allValuesFrom`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the class that a universal property restriction refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](annotatedProperty)
### annotatedProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#annotatedProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the predicate of an annotated axiom or annotated annotation.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](annotatedSource)
### annotatedSource
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#annotatedSource`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the subject of an annotated axiom or annotated annotation.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](annotatedTarget)
### annotatedTarget
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#annotatedTarget`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the object of an annotated axiom or annotated annotation.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](assertionProperty)
### assertionProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#assertionProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the predicate of a negative property assertion.
Domain(s) |[owl:NegativePropertyAssertion](NegativePropertyAssertion) (c)<br />
Range(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
[](cardinality)
### cardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#cardinality`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the cardinality of an exact cardinality restriction.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[xsd:nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) (c)<br />
[](complementOf)
### complementOf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#complementOf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that a given class is the complement of another class.
Domain(s) |[owl:Class](Class) (c)<br />
Range(s) |[owl:Class](Class) (c)<br />
[](datatypeComplementOf)
### datatypeComplementOf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#datatypeComplementOf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that a given data range is the complement of another data range with respect to the data domain.
Domain(s) |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
Range(s) |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
[](differentFrom)
### differentFrom
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#differentFrom`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that two given individuals are different.
Domain(s) |[owl:Thing](Thing) (c)<br />
Range(s) |[owl:Thing](Thing) (c)<br />
[](disjointUnionOf)
### disjointUnionOf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#disjointUnionOf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that a given class is equivalent to the disjoint union of a collection of other classes.
Domain(s) |[owl:Class](Class) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](disjointWith)
### disjointWith
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#disjointWith`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that two given classes are disjoint.
Domain(s) |[owl:Class](Class) (c)<br />
Range(s) |[owl:Class](Class) (c)<br />
[](distinctMembers)
### distinctMembers
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#distinctMembers`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the collection of pairwise different individuals in a owl:AllDifferent axiom.
Domain(s) |[owl:AllDifferent](AllDifferent) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](equivalentClass)
### equivalentClass
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#equivalentClass`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that two given classes are equivalent, and that is used to specify datatype definitions.
Domain(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](equivalentProperty)
### equivalentProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#equivalentProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that two given properties are equivalent.
Domain(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Range(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
[](hasKey)
### hasKey
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#hasKey`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the collection of properties that jointly build a key.
Domain(s) |[owl:Class](Class) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](hasSelf)
### hasSelf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#hasSelf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the property that a self restriction refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](hasValue)
### hasValue
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#hasValue`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the individual that a has-value restriction refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](intersectionOf)
### intersectionOf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#intersectionOf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the collection of classes or data ranges that build an intersection.
Domain(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](inverseOf)
### inverseOf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#inverseOf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that two given properties are inverse.
Domain(s) |[owl:ObjectProperty](ObjectProperty) (c)<br />
Range(s) |[owl:ObjectProperty](ObjectProperty) (c)<br />
[](maxCardinality)
### maxCardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#maxCardinality`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the cardinality of a maximum cardinality restriction.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[xsd:nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) (c)<br />
[](maxQualifiedCardinality)
### maxQualifiedCardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#maxQualifiedCardinality`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the cardinality of a maximum qualified cardinality restriction.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[xsd:nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) (c)<br />
[](members)
### members
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#members`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the collection of members in either a owl:AllDifferent, owl:AllDisjointClasses or owl:AllDisjointProperties axiom.
Domain(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](minCardinality)
### minCardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#minCardinality`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the cardinality of a minimum cardinality restriction.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[xsd:nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) (c)<br />
[](minQualifiedCardinality)
### minQualifiedCardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#minQualifiedCardinality`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the cardinality of a minimum qualified cardinality restriction.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[xsd:nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) (c)<br />
[](onClass)
### onClass
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#onClass`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the class that a qualified object cardinality restriction refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[owl:Class](Class) (c)<br />
[](onDataRange)
### onDataRange
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#onDataRange`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the data range that a qualified data cardinality restriction refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
[](onDatatype)
### onDatatype
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#onDatatype`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the datatype that a datatype restriction refers to.
Domain(s) |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
Range(s) |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
[](onProperties)
### onProperties
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#onProperties`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the n-tuple of properties that a property restriction on an n-ary data range refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](onProperty)
### onProperty
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#onProperty`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the property that a property restriction refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
[](oneOf)
### oneOf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#oneOf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the collection of individuals or data values that build an enumeration.
Domain(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](propertyChainAxiom)
### propertyChainAxiom
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#propertyChainAxiom`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the n-tuple of properties that build a sub property chain of a given property.
Domain(s) |[owl:ObjectProperty](ObjectProperty) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](propertyDisjointWith)
### propertyDisjointWith
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#propertyDisjointWith`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that two given properties are disjoint.
Domain(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
Range(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
[](qualifiedCardinality)
### qualifiedCardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#qualifiedCardinality`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the cardinality of an exact qualified cardinality restriction.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[xsd:nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) (c)<br />
[](sameAs)
### sameAs
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#sameAs`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines that two given individuals are equal.
Domain(s) |[owl:Thing](Thing) (c)<br />
Range(s) |[owl:Thing](Thing) (c)<br />
[](someValuesFrom)
### someValuesFrom
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#someValuesFrom`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the class that an existential property restriction refers to.
Domain(s) |[owl:Restriction](Restriction) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](sourceIndividual)
### sourceIndividual
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#sourceIndividual`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the subject of a negative property assertion.
Domain(s) |[owl:NegativePropertyAssertion](NegativePropertyAssertion) (c)<br />
Range(s) |[owl:Thing](Thing) (c)<br />
[](targetIndividual)
### targetIndividual
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#targetIndividual`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the object of a negative object property assertion.
Domain(s) |[owl:NegativePropertyAssertion](NegativePropertyAssertion) (c)<br />
Range(s) |[owl:Thing](Thing) (c)<br />
[](targetValue)
### targetValue
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#targetValue`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the value of a negative data property assertion.
Domain(s) |[owl:NegativePropertyAssertion](NegativePropertyAssertion) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](unionOf)
### unionOf
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#unionOf`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the collection of classes or data ranges that build a union.
Domain(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />
[](withRestrictions)
### withRestrictions
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#withRestrictions`
Is Defined By | http://www.w3.org/2002/07/owl#
Description | The property that determines the collection of facet-value pairs that define a datatype restriction.
Domain(s) |[rdfs:Datatype](http://www.w3.org/2000/01/rdf-schema#Datatype) (c)<br />
Range(s) |[rdf:List](http://www.w3.org/1999/02/22-rdf-syntax-ns#List) (c)<br />

## Named Individuals
## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **grddl**
  * `http://www.w3.org/2003/g/data-view#`
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