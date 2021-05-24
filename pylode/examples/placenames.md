Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Place Names Profile

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/placenames`
* **Publisher(s)**
  * [Geoscience Australia](http://catalogue.linked.data.gov.au/org/ga)
* **Creators(s)**
  * [Nicholas Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@csiro.au></a>) of [CSIRO](http://catalogue.linked.data.gov.au/def/csiro)
* **Contributor(s)**
  * Armin Haller
  * Irina Bastrakova
* **Created**
  * 2018-08-02
* **Modified**
  * 2019-06-01
* **Version Information**
  * 2
* **Rights**
  * &copy; Commonwealth of Australia (Geoscience Australia) 2019
* **Ontology RDF**
  * RDF ([placenames.ttl](turtle))
### Description
<p>This is an ontology that profiles several other ontologies. It describes Place Names that are used in the Place Names Gazetteer of Australia. Place Names are names given to natural and artificial geospatial features, such as administrative areas, political regions, mountain ranges, rivers, bays etc. Place Names are assigned and managed by multiple Jurisdictions around Australia and may have varying status: official, historical etc. This ontology provides a meta model to bring Place Name data together in one Semantic Web data collection.</p>
* **History Note:** <p>This version of this ontology, 2, covers the same conceptual territory of the original ontology (see placenames-original.ttl) but is aligned with:</p>
<pre><code>* GeoSPARQL ontology - Features &amp; Geometries
* ISA Programme Location Core Vocabulary (locn) - Location class
* ASGS Ontology - ASGS Features
* GNAF Ontology - Addresses
* schema.org - Agent subclasses and some Place Name annotations
* Time Ontology in OWL - for temporal extents
</code></pre>
<p>The first version of this Place Names ontology is archived online at https://github.com/GeoscienceAustralia/Place-Names.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Named Individuals](#namedindividuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[ASGS Feature](#ASGSFeature),
[Address](#Address),
[Agent](#Agent),
[Concept](#Concept),
[ContractedCatchment](#ContractedCatchment),
[Feature](#Feature),
[Gazetteer](#Gazetteer),
[Geometry](#Geometry),
[Identifier](#Identifier),
[Jurisdiction](#Jurisdiction),
[Organisation](#Organisation),
[Place](#Place),
[Place Name](#PlaceName),
[Place Name Formality](#PlaceNameFormality),
[Place Type](#PlaceType),
[Point of Interest](#PointofInterest),
[Region](#Region),
[Register](#Register),
[Registered Item](#RegisteredItem),
[Registry Status](#RegistryStatus),
[State or Territory](#StateorTerritory),
[Temporal Entity](#TemporalEntity),
[string](#string),
### ASGS Feature
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/asgs#Feature`
Description | <p>The ASGS Ontology's Feature Class</p>
Super-classes |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### State or Territory
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/asgs#StateOrTerritory`
Super-classes |[http://linked.data.gov.au/def/placenames/Jurisdiction](http://linked.data.gov.au/def/placenames/Jurisdiction) (c)<br />
### Address
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/gnaf#Address`
Description | <p>The GNAF Ontology's Address Class</p>
Super-classes |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### ContractedCatchment
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/ContractedCatchment`
Super-classes |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### Gazetteer
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/Gazetteer`
Description | <p>A Gazetteer is a Register of Place Names created by a Jurisdiction</p>
Super-classes |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Restrictions |[http://purl.org/linked-data/registry#containedItemClass](http://purl.org/linked-data/registry#containedItemClass) (op) **value** [http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />
### Jurisdiction
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/Jurisdiction`
Description | <p>A Jurisdiction is an Organisation that has authority to make choices within its allocated domain.</p> <p>In the context of the Place Names Profile, Jurisdictions may select Place Names for Features within their allocated area - Australian state, local government area etc.</p>
Super-classes |[sdo:Organization](https://schema.org/Organization) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/asgs#StateOrTerritory](http://linked.data.gov.au/def/asgs#StateOrTerritory) (c)<br />
In range of |[http://linked.data.gov.au/def/placenames/hasPlaceNamingAuthority](http://linked.data.gov.au/def/placenames/hasPlaceNamingAuthority) (op)<br />[http://linked.data.gov.au/def/placenames/wasNamedBy](http://linked.data.gov.au/def/placenames/wasNamedBy) (op)<br />
### Place
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/Place`
Description | <p>An identifiable geographic Place as defined by the Composite Gazetteer of Australia.</p>
Super-classes |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Restrictions |[http://linked.data.gov.au/def/placenames/register](http://linked.data.gov.au/def/placenames/register) (op) **some** [http://linked.data.gov.au/def/placenames/Gazetteer](http://linked.data.gov.au/def/placenames/Gazetteer) (c)<br />[http://linked.data.gov.au/def/placenames/hasFeatureClassification](http://linked.data.gov.au/def/placenames/hasFeatureClassification) (op) **only** [http://linked.data.gov.au/def/placenames/PlaceType](http://linked.data.gov.au/def/placenames/PlaceType) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/placenames/Region](http://linked.data.gov.au/def/placenames/Region) (c)<br />[http://linked.data.gov.au/def/placenames/PointOfInterest](http://linked.data.gov.au/def/placenames/PointOfInterest) (c)<br />
In domain of |[http://linked.data.gov.au/def/placenames/hasFeatureClassification](http://linked.data.gov.au/def/placenames/hasFeatureClassification) (op)<br />
### Place Name
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/PlaceName`
Description | <p>The name of a place, assigned by an official naming authority in the Place Names Gazeteer of Australia.</p>
Super-classes |[http://purl.org/linked-data/registry#RegisteredItem](http://purl.org/linked-data/registry#RegisteredItem) (c)<br />
Restrictions |[https://www.w3.org/ns/adms#identifier](https://www.w3.org/ns/adms#identifier) (op) **some** [https://www.w3.org/ns/adms#Identifier](https://www.w3.org/ns/adms#Identifier) (c)<br />[http://linked.data.gov.au/def/placenames/register](http://linked.data.gov.au/def/placenames/register) (op) **some** [http://linked.data.gov.au/def/placenames/Gazetteer](http://linked.data.gov.au/def/placenames/Gazetteer) (c)<br />[http://linked.data.gov.au/def/placenames/wasNamedBy](http://linked.data.gov.au/def/placenames/wasNamedBy) (op) **some** [http://linked.data.gov.au/def/placenames/Jurisdiction](http://linked.data.gov.au/def/placenames/Jurisdiction) (c)<br />[http://purl.org/linked-data/registry#status](http://purl.org/linked-data/registry#status) (op) **some** [http://purl.org/linked-data/registry#Status](http://purl.org/linked-data/registry#Status) (c)<br />[http://linked.data.gov.au/def/placenames/hasPronunciation](http://linked.data.gov.au/def/placenames/hasPronunciation) (op) **some** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
In domain of |[http://linked.data.gov.au/def/placenames/hasPlaceNameFormality](http://linked.data.gov.au/def/placenames/hasPlaceNameFormality) (op)<br />[http://linked.data.gov.au/def/placenames/wasNamedBy](http://linked.data.gov.au/def/placenames/wasNamedBy) (op)<br />[http://linked.data.gov.au/def/placenames/hasPronunciation](http://linked.data.gov.au/def/placenames/hasPronunciation) (op)<br />[http://linked.data.gov.au/def/placenames/hasPlaceNamingAuthority](http://linked.data.gov.au/def/placenames/hasPlaceNamingAuthority) (op)<br />
### Place Name Formality
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/PlaceNameFormality`
Description | <p>The formality of a Place Name: is it official, historical, colloquilal one?</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[http://linked.data.gov.au/def/placenames/hasPlaceNameFormality](http://linked.data.gov.au/def/placenames/hasPlaceNameFormality) (op)<br />
### Place Type
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/PlaceType`
Description | <p>The Place Type classification as of the ICSM Permanent Committee on Place Names classification scheme.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[http://linked.data.gov.au/def/placenames/hasFeatureClassification](http://linked.data.gov.au/def/placenames/hasFeatureClassification) (op)<br />
### Point of Interest
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/PointOfInterest`
Description | <p>A specific point Location that someone may find useful or interesting.</p>
Super-classes |[http://linked.data.gov.au/def/placenames/Place](http://linked.data.gov.au/def/placenames/Place) (c)<br />
Restrictions |[http://linked.data.gov.au/def/placenames/wasNamedBy](http://linked.data.gov.au/def/placenames/wasNamedBy) (op) **only** [prov:Agent](http://www.w3.org/ns/prov#Agent) (c)<br />
### Region
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/Region`
Description | <p>A Region is an area of land that has common features.</p>
Super-classes |[http://linked.data.gov.au/def/placenames/Place](http://linked.data.gov.au/def/placenames/Place) (c)<br />
### Register
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#Register`
Sub-classes |[http://linked.data.gov.au/def/placenames/Gazetteer](http://linked.data.gov.au/def/placenames/Gazetteer) (c)<br />
### Registered Item
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#RegisteredItem`
Sub-classes |[http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />
### Registry Status
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#Status`
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[http://purl.org/linked-data/registry#status](http://purl.org/linked-data/registry#status) (op)<br />
### Feature
Property | Value
--- | ---
URI | `http://www.opengis.net/ont/geosparql#Feature`
Description | <p>The GeoSPARQL Ontology's Feature Class</p>
Restrictions |[http://linked.data.gov.au/def/placenames/hasPlaceName](http://linked.data.gov.au/def/placenames/hasPlaceName) (op) **some** [http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/gnaf#Address](http://linked.data.gov.au/def/gnaf#Address) (c)<br />[http://linked.data.gov.au/def/placenames/Place](http://linked.data.gov.au/def/placenames/Place) (c)<br />[http://linked.data.gov.au/def/placenames/ContractedCatchment](http://linked.data.gov.au/def/placenames/ContractedCatchment) (c)<br />[http://linked.data.gov.au/def/asgs#Feature](http://linked.data.gov.au/def/asgs#Feature) (c)<br />
In domain of |[geosparql:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) (op)<br />[http://linked.data.gov.au/def/placenames/hasPlaceName](http://linked.data.gov.au/def/placenames/hasPlaceName) (op)<br />
### Geometry
Property | Value
--- | ---
URI | `http://www.opengis.net/ont/geosparql#Geometry`
Description | <p>The GeoSPARQL Ontology's Geometry Class</p>
In range of |[geosparql:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) (op)<br />
### string
Property | Value
--- | ---
URI | `http://www.w3.org/2001/XMLSchema#string`
### Concept
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#Concept`
Sub-classes |[http://purl.org/linked-data/registry#Status](http://purl.org/linked-data/registry#Status) (c)<br />[http://linked.data.gov.au/def/placenames/PlaceNameFormality](http://linked.data.gov.au/def/placenames/PlaceNameFormality) (c)<br />[http://linked.data.gov.au/def/placenames/PlaceType](http://linked.data.gov.au/def/placenames/PlaceType) (c)<br />
### Temporal Entity
Property | Value
--- | ---
URI | `http://www.w3.org/2006/time#TemporalEntity`
### Agent
Property | Value
--- | ---
URI | `http://www.w3.org/ns/prov#Agent`
Description | <p>The Provenance Ontology's Agent Class</p>
Sub-classes |[sdo:Organization](https://schema.org/Organization) (c)<br />
### Organisation
Property | Value
--- | ---
URI | `https://schema.org/Organization`
Description | <p>Schema.org's Organization Class</p>
Super-classes |[prov:Agent](http://www.w3.org/ns/prov#Agent) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/placenames/Jurisdiction](http://linked.data.gov.au/def/placenames/Jurisdiction) (c)<br />
### Identifier
Property | Value
--- | ---
URI | `https://www.w3.org/ns/adms#Identifier`

## Object Properties
[has feature classification](#hasfeatureclassification),
[hasGeometry](#hasGeometry),
[has place name](#hasplacename),
[has place name formality](#hasplacenameformality),
[has place naming authority](#hasplacenamingauthority),
[pronunciation](#pronunciation),
[place name of](#placenameof),
[register](#register),
[was named by](#wasnamedby),
[containedItemClass](#containedItemClass),
[has status](#hasstatus),
[has geometry](#hasgeometry),
[notation](#notation),
[has time](#hastime),
[theme](#theme),
[wasAttributedTo](#wasAttributedTo),
[identifier](#identifier1),
[](hasfeatureclassification)
### has feature classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/hasFeatureClassification`
Description | A relation between a Feature and a classification of its real world phenomena.
Super-properties |[dcat:theme](http://www.w3.org/ns/dcat#theme) (op)<br />
Domain(s) |[http://linked.data.gov.au/def/placenames/Place](http://linked.data.gov.au/def/placenames/Place) (c)<br />
Range(s) |[http://linked.data.gov.au/def/placenames/PlaceType](http://linked.data.gov.au/def/placenames/PlaceType) (c)<br />
[](hasGeometry)
### hasGeometry
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/hasGeometry`
[](hasplacename)
### has place name
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/hasPlaceName`
Description | The Feature has a place name (label) assigned to it
Scope Notes | All PlaceName objects names indicated by hasPlaceName should have the role of the name indicated with a Name Type
Domain(s) |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Range(s) |[http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](hasplacenameformality)
### has place name formality
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/hasPlaceNameFormality`
Description | The formality of a Place Name
Scope Notes | Values for this property must be selected from the Place Name Formality vocabulary
Domain(s) |[http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />
Range(s) |[http://linked.data.gov.au/def/placenames/PlaceNameFormality](http://linked.data.gov.au/def/placenames/PlaceNameFormality) (c)<br />
[](hasplacenamingauthority)
### has place naming authority
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/hasPlaceNamingAuthority`
Description | A relation definining the Naming Authority responsible for the naming of a Place.
Domain(s) |[http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />
Range(s) |[http://linked.data.gov.au/def/placenames/Jurisdiction](http://linked.data.gov.au/def/placenames/Jurisdiction) (c)<br />
[](pronunciation)
### pronunciation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/hasPronunciation`
Description | The pronunciation of a Place Name, indicated by means of a phonetic alphabet string
Super-properties |[skos:notation](http://www.w3.org/2004/02/skos/core#notation) (op)<br />
Domain(s) |[http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />
[](placenameof)
### place name of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/placeNameOf`
[](register)
### register
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/register`
[](wasnamedby)
### was named by
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/wasNamedBy`
Description | A relation that states the Jurisdiction that named a Feature
Super-properties |[prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo) (op)<br />
Domain(s) |[http://linked.data.gov.au/def/placenames/PlaceName](http://linked.data.gov.au/def/placenames/PlaceName) (c)<br />
Range(s) |[http://linked.data.gov.au/def/placenames/Jurisdiction](http://linked.data.gov.au/def/placenames/Jurisdiction) (c)<br />
[](containedItemClass)
### containedItemClass
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#containedItemClass`
[](hasstatus)
### has status
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#status`
Scope Notes | This property is the generic Registry Ontology status property indicating the status of a RegisteredItem in a Registry but in this ontology it is used to indicate only the status of a Place Name in a Gazetteer.
Range(s) |[http://purl.org/linked-data/registry#Status](http://purl.org/linked-data/registry#Status) (c)<br />
[](hasgeometry)
### has geometry
Property | Value
--- | ---
URI | `http://www.opengis.net/ont/geosparql#hasGeometry`
Description | GeoSPARQL Ontology's hasGeometry property
Domain(s) |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Range(s) |[geosparql:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
[](notation)
### notation
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#notation`
[](hastime)
### has time
Property | Value
--- | ---
URI | `http://www.w3.org/2006/time#hastime`
[](theme)
### theme
Property | Value
--- | ---
URI | `http://www.w3.org/ns/dcat#theme`
[](wasAttributedTo)
### wasAttributedTo
Property | Value
--- | ---
URI | `http://www.w3.org/ns/prov#wasAttributedTo`
[](identifier1)
### identifier
Property | Value
--- | ---
URI | `https://www.w3.org/ns/adms#identifier`

## Datatype Properties
[string](#string),
[identifier](#identifier),
[](string)
### string
Property | Value
--- | ---
URI | `http://www.w3.org/2001/XMLSchema#string`
[](identifier)
### identifier
Property | Value
--- | ---
URI | `https://schema.org/identifier`

## Annotation Properties
[scopeNote](#scopeNote),
[name](#name),
[](scopeNote)
### scopeNote
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#scopeNote`
[](name)
### name
Property | Value
--- | ---
URI | `https://schema.org/name`

## Named Individuals
[Place Name](#PlaceName),
### Place Name <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/placenames/PlaceName`
* **Contributor(s)**
  * [owl:Class](http://www.w3.org/2002/07/owl#Class)
  * [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class)
Description | The name of a place, assigned by an official naming authority in the Place Names Gazeteer of Australia.
## Namespaces
* **dcat**
  * `http://www.w3.org/ns/dcat#`
* **dct**
  * `http://purl.org/dc/terms/`
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
* **time**
  * `http://www.w3.org/2006/time#`
* **vann**
  * `http://purl.org/vocab/vann/`
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