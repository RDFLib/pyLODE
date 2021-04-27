Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Geological Administrative Features Ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/geoadminfeatures`
* **Publisher(s)**
  * None
* **Creators(s)**
  * GSQ Informatics Staff
    (<geological_info@dnrme.qld.gov.au></a>)
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@surroundaustralia.com></a>) of [SURROUND Australia Pty Ltd](https://surroundaustralia.com)
* **Created**
  * 2019-12-04
* **Modified**
  * 2019-12-04
* **Imports**
  * [http://www.opengis.net/ont/geosparql](http://www.opengis.net/ont/geosparql)
* **Ontology RDF**
  * RDF ([geoadminfeatures.ttl](turtle))
* **Code Repository**
  * [https://github.com/geological-survey-of-queensland/geological-admininstrative-features-ont](https://github.com/geological-survey-of-queensland/geological-admininstrative-features-ont)
### Description
<p>This ontology describes classes of geospatial feature relevant to the administrative duties of the Geological Survey of Queensland.</p>
<p>As subclasses of the GeoSPARQL Ontology's <code>Feature</code> class, this ontology defines an <code>Administrative Feature</code>. Multiple subclasses of this class are then defined, some with class interrelations.</p>
<p>This ontology is part of the Geological Survey of Queensland's set of <em>component</em> ontologies that together provide definitions for all of GSQ's data. Of particular importance for this ontology is GSQ's Geological Features Profile of SWEET which defined multiple classes of geological feature. It is yet to be published.</p>

## Table of Contents
1. [Classes](#classes)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Administrative feature](#Administrativefeature),
[Block](#Block),
[Permit](#Permit),
[Sub-Block](#Sub-Block),
### Administrative feature
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geoadminfeatures#AdministrativeFeature`
Description | <p>An Administrative Feature is a geo:Feature that is defined by adminstrative processes such as legislation, regulation, policy or procedure.</p>
Super-classes |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/geoadminfeatures#Block](http://linked.data.gov.au/def/geoadminfeatures#Block) (c)<br />[http://linked.data.gov.au/def/geoadminfeatures#Permit](http://linked.data.gov.au/def/geoadminfeatures#Permit) (c)<br />[http://linked.data.gov.au/def/geoadminfeatures#SubBlock](http://linked.data.gov.au/def/geoadminfeatures#SubBlock) (c)<br />
### Block
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geoadminfeatures#Block`
Description | <p>A Block is an administrative division of the State of Queensland that is used for tenure management. A Block is defined as five minutes of latitude by five minutes of longitude. Blocks are grouped by 1:1,000,000 map sheet areas, the names of which provide the containing Blocks with a four letter prefix (e.g. Clermont 1:1,000,000 provides CLER). Each sheet area contains 3456 Blocks, with the Blocks numbered between 1 and 3456 inclusive. A Block is divided into 25 Sub-Blocks.</p>
Super-classes |[http://linked.data.gov.au/def/geoadminfeatures#AdministrativeFeature](http://linked.data.gov.au/def/geoadminfeatures#AdministrativeFeature) (c)<br />
### Permit
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geoadminfeatures#Permit`
Description | <p>Permits are a license granted over a spatial region within the State of Queensland. Permits govern the activities which can be conducted upon them. Activities include exploration, development, and extraction of a specific commodity or commodities.</p>
Super-classes |[http://linked.data.gov.au/def/geoadminfeatures#AdministrativeFeature](http://linked.data.gov.au/def/geoadminfeatures#AdministrativeFeature) (c)<br />
### Sub-Block
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geoadminfeatures#SubBlock`
Description | <p>A Sub-Block is an administrative sub-division of a Block. Each Block is divided into 25 Sub-Blocks. A Sub-Block is defined as one minute of latitude by one minute of longitude. The Sub-Blocks are prefixed with their corresponding Block name and are labelled from A to Z, excluding I. Labels are allocated from left to right, top to bottom, starting from the northwest corner.</p>
Super-classes |[http://linked.data.gov.au/def/geoadminfeatures#AdministrativeFeature](http://linked.data.gov.au/def/geoadminfeatures#AdministrativeFeature) (c)<br />
Restrictions |[geosparql:sfWithin](http://www.opengis.net/ont/geosparql#sfWithin) **exactly** 1 [http://linked.data.gov.au/def/geoadminfeatures#Block](http://linked.data.gov.au/def/geoadminfeatures#Block) (c)<br />

## Named Individuals
## Namespaces
* **dct**
  * `http://purl.org/dc/terms/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
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