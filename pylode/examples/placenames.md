# Place Names Profile
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/placenames`
* **Publisher(s)**
  * [Geoscience Australia](http://catalogue.linked.data.gov.au/org/ga)
* **Creators(s)**
  * [Nicholas Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@csiro.au></a>) of [CSIRO](http://catalogue.linked.data.gov.au/def/csiro)
* **Contributor(s)**
  * Irina Bastrakova
  * Armin Haller
* **Created**
  * 2018-08-02
* **Modified**
  * 2019-06-01
* **Version Information**
  * 2
* **Rights**
  * (c) Commonwealth of Australia (Geoscience Australia) 2019
* **Ontology RDF**
  * RDF ([placenames.ttl](turtle))
### Description
<p>This is an ontology that profiles several other ontologies. It describes Place Names that are used in the Place Names Gazetteer of Australia. Place Names are names given to natural and artificial geospatial features, such as administrative areas, political regions, mountain ranges, rivers, bays etc. Place Names are assigned and managed by multiple Jurisdictions around Australia and may have varying status: official, historical etc. This ontology provides a meta model to bring Place Name data together in one Semantic Web data collection.</p>
* **History Note:** This version of this ontology, 2, covers the same conceptual territory of the original ontology (see placenames-original.ttl) but is aligned with:

    * GeoSPARQL ontology - Features & Geometries
    * ISA Programme Location Core Vocabulary (locn) - Location class
    * ASGS Ontology - ASGS Features
    * GNAF Ontology - Addresses
    * schema.org - Agent subclasses and some Place Name annotations
    * Time Ontology in OWL - for temporal extents

The first version of this Place Names ontology is archived online at https://github.com/GeoscienceAustralia/Place-Names.

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
IRI | `http://linked.data.gov.au/def/asgs#Feature`
Description | <p>The ASGS Ontology's Feature Class</p>
Super-classes |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### State or Territory
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StateOrTerritory`
Super-classes |[Jurisdiction](Jurisdiction) (c)<br />
### Address
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#Address`
Description | <p>The GNAF Ontology's Address Class</p>
Super-classes |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### ContractedCatchment
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/ContractedCatchment`
Super-classes |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
### Gazetteer
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/Gazetteer`
Description | <p>A Gazetteer is a Register of Place Names created by a Jurisdiction</p>
Super-classes |[reg:Register](http://purl.org/linked-data/registry#Register) (c)<br />
Restrictions |[reg:containedItemClass](http://purl.org/linked-data/registry#containedItemClass) (op) **value** [PlaceName](PlaceName) (c)<br />
### Jurisdiction
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/Jurisdiction`
Description | <p>A Jurisdiction is an Organisation that has authority to make choices within its allocated domain.</p>
<p>In the context of the Place Names Profile, Jurisdictions may select Place Names for Features within their allocated area - Australian state, local government area etc.</p>
Super-classes |[sdo:Organization](https://schema.org/Organization) (c)<br />
Sub-classes |[asgs:StateOrTerritory](http://linked.data.gov.au/def/asgs#StateOrTerritory) (c)<br />
In range of |[hasPlaceNamingAuthority](hasplacenamingauthority) (op)<br />[wasNamedBy](wasnamedby) (op)<br />
### Place
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/Place`
Description | <p>An identifiable geographic Place as defined by the Composite Gazetteer of Australia.</p>
Super-classes |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Restrictions |[register](register) (op) **some** [Gazetteer](Gazetteer) (c)<br />[hasFeatureClassification](hasfeatureclassification) (op) **only** [PlaceType](PlaceType) (c)<br />
Sub-classes |[PointOfInterest](PointofInterest) (c)<br />[Region](Region) (c)<br />
In domain of |[hasFeatureClassification](hasfeatureclassification) (op)<br />
### Place Name
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/PlaceName`
Description | <p>The name of a place, assigned by an official naming authority in the Place Names Gazeteer of Australia.</p>
Super-classes |[reg:RegisteredItem](http://purl.org/linked-data/registry#RegisteredItem) (c)<br />
Restrictions |[reg:status](http://purl.org/linked-data/registry#status) (op) **some** [reg:Status](http://purl.org/linked-data/registry#Status) (c)<br />[hasPronunciation](pronunciation) (op) **some** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />[adms:identifier](https://www.w3.org/ns/adms#identifier) (op) **some** [adms:Identifier](https://www.w3.org/ns/adms#Identifier) (c)<br />[register](register) (op) **some** [Gazetteer](Gazetteer) (c)<br />[wasNamedBy](wasnamedby) (op) **some** [Jurisdiction](Jurisdiction) (c)<br />
In domain of |[hasPlaceNamingAuthority](hasplacenamingauthority) (op)<br />[hasPlaceNameFormality](hasplacenameformality) (op)<br />[hasPronunciation](pronunciation) (op)<br />[wasNamedBy](wasnamedby) (op)<br />
### Place Name Formality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/PlaceNameFormality`
Description | <p>The formality of a Place Name: is it official, historical, colloquilal one?</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[hasPlaceNameFormality](hasplacenameformality) (op)<br />
### Place Type
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/PlaceType`
Description | <p>The Place Type classification as of the ICSM Permanent Committee on Place Names classification scheme.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[hasFeatureClassification](hasfeatureclassification) (op)<br />
### Point of Interest
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/PointOfInterest`
Description | <p>A specific point Location that someone may find useful or interesting.</p>
Super-classes |[Place](Place) (c)<br />
Restrictions |[wasNamedBy](wasnamedby) (op) **only** [prov:Agent](http://www.w3.org/ns/prov#Agent) (c)<br />
### Region
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/Region`
Description | <p>A Region is an area of land that has common features.</p>
Super-classes |[Place](Place) (c)<br />
### Register
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#Register`
Sub-classes |[Gazetteer](Gazetteer) (c)<br />
### Registered Item
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#RegisteredItem`
Sub-classes |[PlaceName](PlaceName) (c)<br />
### Registry Status
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#Status`
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[reg:status](http://purl.org/linked-data/registry#status) (op)<br />
### Feature
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#Feature`
Description | <p>The GeoSPARQL Ontology's Feature Class</p>
Restrictions |[hasPlaceName](hasplacename) (op) **some** [PlaceName](PlaceName) (c)<br />
Sub-classes |[ContractedCatchment](ContractedCatchment) (c)<br />[Place](Place) (c)<br />[gnaf:Address](http://linked.data.gov.au/def/gnaf#Address) (c)<br />[asgs:Feature](http://linked.data.gov.au/def/asgs#Feature) (c)<br />
In domain of |[geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) (op)<br />[hasPlaceName](hasplacename) (op)<br />
### Geometry
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#Geometry`
Description | <p>The GeoSPARQL Ontology's Geometry Class</p>
In range of |[geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) (op)<br />
### string
Property | Value
--- | ---
IRI | `http://www.w3.org/2001/XMLSchema#string`
### Concept
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#Concept`
Sub-classes |[PlaceType](PlaceType) (c)<br />[reg:Status](http://purl.org/linked-data/registry#Status) (c)<br />[PlaceNameFormality](PlaceNameFormality) (c)<br />
### Temporal Entity
Property | Value
--- | ---
IRI | `http://www.w3.org/2006/time#TemporalEntity`
### Agent
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/prov#Agent`
Description | <p>The Provenance Ontology's Agent Class</p>
Sub-classes |[sdo:Organization](https://schema.org/Organization) (c)<br />
### Organisation
Property | Value
--- | ---
IRI | `https://schema.org/Organization`
Description | <p>Schema.org's Organization Class</p>
Super-classes |[prov:Agent](http://www.w3.org/ns/prov#Agent) (c)<br />
Sub-classes |[Jurisdiction](Jurisdiction) (c)<br />
### Identifier
Property | Value
--- | ---
IRI | `https://www.w3.org/ns/adms#Identifier`

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
IRI | `http://linked.data.gov.au/def/placenames/hasFeatureClassification`
Description | A relation between a Feature and a classification of its real world phenomena.
Super-properties |[dcat:theme](http://www.w3.org/ns/dcat#theme) (op)<br />
Domain(s) |[Place](Place) (c)<br />
Range(s) |[PlaceType](PlaceType) (c)<br />
[](hasGeometry)
### hasGeometry
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/hasGeometry`
[](hasplacename)
### has place name
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/hasPlaceName`
Description | The Feature has a place name (label) assigned to it
Usage Note | All PlaceName objects names indicated by hasPlaceName should have the role of the name indicated with a Name Type
Domain(s) |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Range(s) |[PlaceName](PlaceName) (c)<br />[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](hasplacenameformality)
### has place name formality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/hasPlaceNameFormality`
Description | The formality of a Place Name
Usage Note | Values for this property must be selected from the Place Name Formality vocabulary
Domain(s) |[PlaceName](PlaceName) (c)<br />
Range(s) |[PlaceNameFormality](PlaceNameFormality) (c)<br />
[](hasplacenamingauthority)
### has place naming authority
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/hasPlaceNamingAuthority`
Description | A relation definining the Naming Authority responsible for the naming of a Place.
Domain(s) |[PlaceName](PlaceName) (c)<br />
Range(s) |[Jurisdiction](Jurisdiction) (c)<br />
[](pronunciation)
### pronunciation
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/hasPronunciation`
Description | The pronunciation of a Place Name, indicated by means of a phonetic alphabet string
Super-properties |[skos:notation](http://www.w3.org/2004/02/skos/core#notation) (op)<br />
Domain(s) |[PlaceName](PlaceName) (c)<br />
[](placenameof)
### place name of
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/placeNameOf`
[](register)
### register
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/register`
[](wasnamedby)
### was named by
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/wasNamedBy`
Description | A relation that states the Jurisdiction that named a Feature
Super-properties |[prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo) (op)<br />
Domain(s) |[PlaceName](PlaceName) (c)<br />
Range(s) |[Jurisdiction](Jurisdiction) (c)<br />
[](containedItemClass)
### containedItemClass
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#containedItemClass`
[](hasstatus)
### has status
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#status`
Usage Note | This property is the generic Registry Ontology status property indicating the status of a RegisteredItem in a Registry but in this ontology it is used to indicate only the status of a Place Name in a Gazetteer.
Range(s) |[reg:Status](http://purl.org/linked-data/registry#Status) (c)<br />
[](hasgeometry)
### has geometry
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#hasGeometry`
Description | GeoSPARQL Ontology's hasGeometry property
Domain(s) |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Range(s) |[geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
[](notation)
### notation
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#notation`
[](hastime)
### has time
Property | Value
--- | ---
IRI | `http://www.w3.org/2006/time#hastime`
[](theme)
### theme
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/dcat#theme`
[](wasAttributedTo)
### wasAttributedTo
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/prov#wasAttributedTo`
[](identifier1)
### identifier
Property | Value
--- | ---
IRI | `https://www.w3.org/ns/adms#identifier`

## Datatype Properties
[string](#string),
[identifier](#identifier),
[](string)
### string
Property | Value
--- | ---
IRI | `http://www.w3.org/2001/XMLSchema#string`
[](identifier)
### identifier
Property | Value
--- | ---
IRI | `https://schema.org/identifier`

## Annotation Properties
[scopeNote](#scopeNote),
[name](#name),
[](scopeNote)
### scopeNote
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#scopeNote`
[](name)
### name
Property | Value
--- | ---
IRI | `https://schema.org/name`

## Named Individuals
[Place Name](#PlaceName),
### Place Name <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/placenames/PlaceName`
* **Contributor(s)**
  * [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class)
  * [owl:Class](http://www.w3.org/2002/07/owl#Class)
Description | The name of a place, assigned by an official naming authority in the Place Names Gazeteer of Australia.
## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/placenames/`
* **:**
  * `http://linked.data.gov.au/def/placenames/`
* **adms**
  * `https://www.w3.org/ns/adms#`
* **asgs**
  * `http://linked.data.gov.au/def/asgs#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dcat**
  * `http://www.w3.org/ns/dcat#`
* **dct**
  * `http://purl.org/dc/terms/`
* **geo**
  * `http://www.opengis.net/ont/geosparql#`
* **gnaf**
  * `http://linked.data.gov.au/def/gnaf#`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **reg**
  * `http://purl.org/linked-data/registry#`
* **sdo**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **time**
  * `http://www.w3.org/2006/time#`
* **vann**
  * `http://purl.org/vocab/vann/`
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