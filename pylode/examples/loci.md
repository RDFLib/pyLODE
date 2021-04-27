Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# LOC-I Ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/loci`
* **Publisher(s)**
  * [CSIRO](http://catalogue.linked.data.gov.au/org/csiro)
* **Creators(s)**
  * [Nicholas Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@csiro.au></a>) of [CSIRO](http://catalogue.linked.data.gov.au/def/csiro)
* **Created**
  * 2018-10-29
* **Modified**
  * 2018-11-09
* **Version Information**
  * Beta version
* **Version URI**
  * [http://linked.data.gov.au/def/loci/1.0](http://linked.data.gov.au/def/loci/1.0)
* **Imports**
  * [dcat:](http://www.w3.org/ns/dcat#)
  * [http://purl.org/linked-data/registry](http://purl.org/linked-data/registry)
  * [owl:](http://www.w3.org/2002/07/owl#)
  * [rdf:](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
* **License &amp; Rights**
  * [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
  * &copy; 2019 CSIRO
* **Ontology RDF**
  * RDF ([loci.ttl](turtle))
### Description
<p>A profile of several ontologies implemented to govern Linked Data resources published within the LOC-I project.</p>
<p>This is a profile of the <a href="http://www.opengeospatial.org/standards/geosparql">GeoSPARQL</a> and <a href="https://www.w3.org/TR/vocab-dcat-2/">DCAT v2</a> &amp; <a href="http://www.w3.org/TR/void/">VOID</a> that require certain properties defined by those ontologies be present for several classes of resource that are of particular importance to the <a href="https://confluence.csiro.au/display/DIPAAnalyticHubs/Location+Integration+Capability+Loc-I">LOC-I</a> project.</p>
<p>This ontology constrains both normative instruction on what constitutes LOC-I objects and supplies executable constraints to validate instances.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Annotation Properties](#annotationproperties)
1. [Named Individuals](#namedindividuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[LOCI Data Publishers](#LOCIDataPublishers),
[LOCI Dataset](#LOCIDataset),
[LOCI Dataset Linking Statement](#LOCIDatasetLinkingStatement),
[LOCI Feature](#LOCIFeature),
[LOCI Linkset](#LOCILinkset),
[Statement](#Statement),
### LOCI Data Publishers
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#DataPublisher`
Description | <p>The set of all approved publishers of LOCI data, all of whom are known</p>
Super-classes |[foaf:Group](http://xmlns.com/foaf/0.1/Group) (c)<br />
### LOCI Dataset
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#Dataset`
Description | <p>A LOCI Dataset is a DCAT and VOID Dataset that has been accepted by the LOCI Registry Manager.</p>
Super-classes |[void:Dataset](http://rdfs.org/ns/void#Dataset) (c)<br />[dcat:Dataset](http://www.w3.org/ns/dcat#Dataset) (c)<br />
Restrictions |[dct:modified](http://purl.org/dc/terms/modified) **exactly** 1<br />[dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint) **min** 1<br />[dct:publisher](http://purl.org/dc/terms/publisher) **exactly** 1 [foaf:Organization](http://xmlns.com/foaf/0.1/Organization) (c)<br />[dct:title](http://purl.org/dc/terms/title) **exactly** 1<br />[dct:issued](http://purl.org/dc/terms/issued) **exactly** 1<br />
Sub-classes |[http://linked.data.gov.au/def/loci#Linkset](http://linked.data.gov.au/def/loci#Linkset) (c)<br />
Has members |[http://linked.data.gov.au/dataset/gnaf](http://linked.data.gov.au/dataset/gnaf)<br />[http://linked.data.gov.au/dataset/asgs](http://linked.data.gov.au/dataset/asgs)<br />[http://linked.data.gov.au/dataset/geofabric](http://linked.data.gov.au/dataset/geofabric)<br />
### LOCI Dataset Linking Statement
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#DatasetLinkingStatement`
Description | <p>An RDF Statement (Subject, Predicate, Object + additional metadata) that links class instances in one LOCI Dataset with class instances in another</p>
Super-classes |[rdf:Statement](http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement) (c)<br />
Restrictions |[rdf:object](http://www.w3.org/1999/02/22-rdf-syntax-ns#object) **exactly** 1 [http://linked.data.gov.au/def/loci#Feature](http://linked.data.gov.au/def/loci#Feature) (c)<br />[http://linked.data.gov.au/def/loci#hadGenerationMethod](http://linked.data.gov.au/def/loci#hadGenerationMethod) (op) **exactly** 1 [prov:Plan](http://www.w3.org/ns/prov#Plan) (c)<br />[http://purl.org/linked-data/registryregister](http://purl.org/linked-data/registryregister) **exactly** 1 [http://linked.data.gov.au/def/loci#Linkset](http://linked.data.gov.au/def/loci#Linkset) (c)<br />[rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject) **exactly** 1 [http://linked.data.gov.au/def/loci#Feature](http://linked.data.gov.au/def/loci#Feature) (c)<br />
### LOCI Feature
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#Feature`
Super-classes |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### LOCI Linkset
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#Linkset`
Description | <p>A LOCI Linkset is a specialised form of a VOID Linkset that requires the void:subjectsTarget &amp; void:objectsTarget indicate LOCI Datasets</p>
Super-classes |[http://linked.data.gov.au/def/loci#Dataset](http://linked.data.gov.au/def/loci#Dataset) (c)<br />[void:Linkset](http://rdfs.org/ns/void#Linkset) (c)<br />
Has members |[http://linked.data.gov.au/def/loci#AddressesCatchments](http://linked.data.gov.au/def/loci#AddressesCatchments)<br />
### Statement
Property | Value
--- | ---
URI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement`
Sub-classes |[http://linked.data.gov.au/def/loci#DatasetLinkingStatement](http://linked.data.gov.au/def/loci#DatasetLinkingStatement) (c)<br />

## Object Properties
[had generation method](#hadgenerationmethod),
[](hadgenerationmethod)
### had generation method
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#hadGenerationMethod`
Description | The LOCI Dataset Linking Statement had a Method that was used to generate it
Range(s) |[prov:Plan](http://www.w3.org/ns/prov#Plan) (c)<br />

## Annotation Properties
[minQualifiedCardinality](#minQualifiedCardinality),
[qualifiedCardinality](#qualifiedCardinality),
[member](#member),
[](minQualifiedCardinality)
### minQualifiedCardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#minQualifiedCardinality`
[](qualifiedCardinality)
### qualifiedCardinality
Property | Value
--- | ---
URI | `http://www.w3.org/2002/07/owl#qualifiedCardinality`
[](member)
### member
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#member`

## Named Individuals
[ASGS Dataset](#ASGSDataset),
[Addresses Catchments Linkset](#AddressesCatchmentsLinkset),
[Australian Bureau of Statistics](#AustralianBureauofStatistics),
[CSIRO](#CSIRO),
[GNAF Dataset](#GNAFDataset),
[Geofabric Dataset](#GeofabricDataset),
[Geoscience Australia](#GeoscienceAustralia),
[LOCI Data Publishers](#LOCIDataPublishers),
[PSMA Australia](#PSMAAustralia),
### CSIRO <sup>c</sup>
Property | Value
--- | ---
URI | `http://catalogue.linked.data.gov.au/org/O-000886`
* **Contributor(s)**
  * [foaf:Organization](http://xmlns.com/foaf/0.1/Organization)
### Geoscience Australia <sup>c</sup>
Property | Value
--- | ---
URI | `http://catalogue.linked.data.gov.au/org/O-000887`
* **Contributor(s)**
  * [foaf:Organization](http://xmlns.com/foaf/0.1/Organization)
### Australian Bureau of Statistics <sup>c</sup>
Property | Value
--- | ---
URI | `http://catalogue.linked.data.gov.au/org/O-000928`
* **Contributor(s)**
  * [foaf:Organization](http://xmlns.com/foaf/0.1/Organization)
### PSMA Australia <sup>c</sup>
Property | Value
--- | ---
URI | `http://catalogue.linked.data.gov.au/org/psma`
* **Contributor(s)**
  * [foaf:Organization](http://xmlns.com/foaf/0.1/Organization)
### ASGS Dataset <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/dataset/asgs`
* **Contributor(s)**
  * [http://linked.data.gov.au/def/loci#Dataset](http://linked.data.gov.au/def/loci#Dataset)
### Geofabric Dataset <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/dataset/geofabric`
* **Contributor(s)**
  * [http://linked.data.gov.au/def/loci#Dataset](http://linked.data.gov.au/def/loci#Dataset)
### GNAF Dataset <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/dataset/gnaf`
* **Contributor(s)**
  * [http://linked.data.gov.au/def/loci#Dataset](http://linked.data.gov.au/def/loci#Dataset)
### Addresses Catchments Linkset <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#AddressesCatchments`
* **Contributor(s)**
  * [http://linked.data.gov.au/def/loci#Linkset](http://linked.data.gov.au/def/loci#Linkset)
### LOCI Data Publishers <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/loci#DataPublisher`
* **Contributor(s)**
  * [owl:Class](http://www.w3.org/2002/07/owl#Class)
  * [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class)
Description | The set of all approved publishers of LOCI data, all of whom are known
## Namespaces
* **dcat**
  * `http://www.w3.org/ns/dcat#`
* **dct**
  * `http://purl.org/dc/terms/`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
* **geosparql**
  * `http://www.opengis.net/ont/geosparql#`
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
* **void**
  * `http://rdfs.org/ns/void#`
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