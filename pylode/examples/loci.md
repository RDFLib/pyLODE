# LOC-I Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
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
* **Version IRI**
  * [http://linked.data.gov.au/def/loci/1.0](http://linked.data.gov.au/def/loci/1.0)
* **Imports**
  * [http://purl.org/linked-data/registry](http://purl.org/linked-data/registry)
  * [owl:](http://www.w3.org/2002/07/owl#)
  * [rdf:](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
  * [dcat:](http://www.w3.org/ns/dcat#)
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
IRI | `http://linked.data.gov.au/def/loci#DataPublisher`
Description | <p>The set of all approved publishers of LOCI data, all of whom are known</p>
Super-classes |[http://xmlns.com/foaf/0.1/Group](http://xmlns.com/foaf/0.1/Group) (c)<br />
### LOCI Dataset
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/loci#Dataset`
Description | <p>A LOCI Dataset is a DCAT and VOID Dataset that has been accepted by the LOCI Registry Manager.</p>
Super-classes |[dcat:Dataset](http://www.w3.org/ns/dcat#Dataset) (c)<br />[http://rdfs.org/ns/void#Dataset](http://rdfs.org/ns/void#Dataset) (c)<br />
Restrictions |[dct:issued](http://purl.org/dc/terms/issued) **exactly** 1<br />[dct:publisher](http://purl.org/dc/terms/publisher) **exactly** 1 [http://xmlns.com/foaf/0.1/Organization](http://xmlns.com/foaf/0.1/Organization) (c)<br />[dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint) **min** 1<br />[dct:title](http://purl.org/dc/terms/title) **exactly** 1<br />[dct:modified](http://purl.org/dc/terms/modified) **exactly** 1<br />
Sub-classes |[Linkset](LOCILinkset) (c)<br />
### LOCI Dataset Linking Statement
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/loci#DatasetLinkingStatement`
Description | <p>An RDF Statement (Subject, Predicate, Object + additional metadata) that links class instances in one LOCI Dataset with class instances in another</p>
Super-classes |[rdf:Statement](http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement) (c)<br />
Restrictions |[rdf:object](http://www.w3.org/1999/02/22-rdf-syntax-ns#object) **exactly** 1 [Feature](LOCIFeature) (c)<br />[http://purl.org/linked-data/registryregister](http://purl.org/linked-data/registryregister) **exactly** 1 [Linkset](LOCILinkset) (c)<br />[rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject) **exactly** 1 [Feature](LOCIFeature) (c)<br />[hadGenerationMethod](hadgenerationmethod) (op) **exactly** 1 [prov:Plan](http://www.w3.org/ns/prov#Plan) (c)<br />
### LOCI Feature
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/loci#Feature`
Super-classes |[http://www.opengis.net/ont/geosparql#Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### LOCI Linkset
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/loci#Linkset`
Description | <p>A LOCI Linkset is a specialised form of a VOID Linkset that requires the void:subjectsTarget &amp; void:objectsTarget indicate LOCI Datasets</p>
Super-classes |[http://rdfs.org/ns/void#Linkset](http://rdfs.org/ns/void#Linkset) (c)<br />[Dataset](LOCIDataset) (c)<br />
### Statement
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement`
Sub-classes |[DatasetLinkingStatement](LOCIDatasetLinkingStatement) (c)<br />

## Object Properties
[had generation method](#hadgenerationmethod),
[](hadgenerationmethod)
### had generation method
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/loci#hadGenerationMethod`
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
IRI | `http://www.w3.org/2002/07/owl#minQualifiedCardinality`
[](qualifiedCardinality)
### qualifiedCardinality
Property | Value
--- | ---
IRI | `http://www.w3.org/2002/07/owl#qualifiedCardinality`
[](member)
### member
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#member`

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
IRI | `http://catalogue.linked.data.gov.au/org/O-000886`
* **Contributor(s)**
  * [http://xmlns.com/foaf/0.1/Organization](http://xmlns.com/foaf/0.1/Organization)
### Geoscience Australia <sup>c</sup>
Property | Value
--- | ---
IRI | `http://catalogue.linked.data.gov.au/org/O-000887`
* **Contributor(s)**
  * [http://xmlns.com/foaf/0.1/Organization](http://xmlns.com/foaf/0.1/Organization)
### Australian Bureau of Statistics <sup>c</sup>
Property | Value
--- | ---
IRI | `http://catalogue.linked.data.gov.au/org/O-000928`
* **Contributor(s)**
  * [http://xmlns.com/foaf/0.1/Organization](http://xmlns.com/foaf/0.1/Organization)
### PSMA Australia <sup>c</sup>
Property | Value
--- | ---
IRI | `http://catalogue.linked.data.gov.au/org/psma`
* **Contributor(s)**
  * [http://xmlns.com/foaf/0.1/Organization](http://xmlns.com/foaf/0.1/Organization)
### ASGS Dataset <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/dataset/asgs`
* **Contributor(s)**
  * [Dataset](http://linked.data.gov.au/def/loci#Dataset)
### Geofabric Dataset <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/dataset/geofabric`
* **Contributor(s)**
  * [Dataset](http://linked.data.gov.au/def/loci#Dataset)
### GNAF Dataset <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/dataset/gnaf`
* **Contributor(s)**
  * [Dataset](http://linked.data.gov.au/def/loci#Dataset)
### Addresses Catchments Linkset <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/loci#AddressesCatchments`
* **Contributor(s)**
  * [Linkset](http://linked.data.gov.au/def/loci#Linkset)
### LOCI Data Publishers <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/loci#DataPublisher`
* **Contributor(s)**
  * [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class)
  * [owl:Class](http://www.w3.org/2002/07/owl#Class)
Description | The set of all approved publishers of LOCI data, all of whom are known
## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/loci#`
* **:**
  * `http://linked.data.gov.au/def/loci#`
* **dcat**
  * `http://www.w3.org/ns/dcat#`
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
* **reg**
  * `http://purl.org/linked-data/registry`
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