# GNAF ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/gnaf`
* **Publisher(s)**
  * [PSMA Australia](http://catalogue.linked.data.gov.au/org/psma)
* **Creators(s)**
  * [Nicholas Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@csiro.au></a>)
* **Contributor(s)**
  * Joseph Abhayaratna
    (<joseph.abhayaratna@psma.com.au></a>)
* **Created**
  * 2017-12-23
* **Modified**
  * 2019-06-07
* **Version Information**
  * 1.2
* **Version IRI**
  * [http://linked.data.gov.au/def/gnaf/1.2](http://linked.data.gov.au/def/gnaf/1.2)
* **Imports**
  * [http://www.w3.org/ns/prov-o](http://www.w3.org/ns/prov-o)
  * [http://www.opengis.net/ont/geosparql](http://www.opengis.net/ont/geosparql)
* **Source**
  * [https://www.psma.com.au/sites/default/files/g-naf_product_description.pdf](https://www.psma.com.au/sites/default/files/g-naf_product_description.pdf)
* **Ontology RDF**
  * RDF ([gnaf.ttl](turtle))
### Description
<p>An ontology for the content of the PSMA Geocoded National Address File (G-NAF).</p>
<p>The G-NAF is Australia’s authoritative, geocoded address file. It contains more than 13 million Australian physical address records. The records include geocodes which are latitude and longitude map coordinates with coordinate reference system details and other information necissary to prcicely locate addresses on the earth's surface.</p>
<p>The G-NAF does not contain any names or personal information.</p>
<p>The base content of the G-NAF is available freely online at <a href="https://data.gov.au/dataset/geocoded-national-address-file-g-naf">https://data.gov.au/dataset/geocoded-national-address-file-g-naf</a> and also via a Linked Data API that uses this ontology at <a href="http://gnafld.net">http://gnafld.net</a>.</p>
<p>This ontology draws heavily from the OWL ontology version of the ISO19160-1:2015 "Addressing -- Part 1: Conceptual model" standard (see <a href="https://www.iso.org/standard/61710.html">https://www.iso.org/standard/61710.html</a>) which has been created by the ISO TC211, Group for Ontology Management (GOM) and published online by the Australian Government Linked Data Working Group at <a href="http://reference.data.gov.au/def/ont/iso19160-1-address">http://reference.data.gov.au/def/ont/iso19160-1-address</a>.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Named Individuals](#namedindividuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[2011 Mesh Block](#2011MeshBlock),
[2016 Mesh Block](#2016MeshBlock),
[Address](#Address),
[Address Site](#AddressSite),
[Alias](#Alias),
[GNAF Entity](#GNAFEntity),
[ISO19160-1 Address](#ISO19160-1Address),
[Locality](#Locality),
[Location](#Location),
[Mesh Block Match](#MeshBlockMatch),
[Number](#Number),
[Street](#Street),
[Street Locality](#StreetLocality),
### Location
Property | Value
--- | ---
IRI | `http://dbpedia.org/ontology/Location`
Sub-classes |[Locality](Locality) (c)<br />[Address](Address) (c)<br />[Street](Street) (c)<br />
### Address
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#Address`
Super-classes |[dbo:Location](http://dbpedia.org/ontology/Location) (c)<br />[GnafEntity](GNAFEntity) (c)<br />[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />[prov:Location](http://www.w3.org/ns/prov#Location) (c)<br />[http://reference.data.gov.au/def/ont/iso19160-1-address#Address](http://reference.data.gov.au/def/ont/iso19160-1-address#Address) (c)<br />
Restrictions |[hasMeshBlockMatch](hasMeshBlockmatch) (op) **some** [MeshBlockMatch](MeshBlockMatch) (c)<br />[geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) **min** 1 [sf:Point](http://www.opengis.net/ont/sf#Point) (c)<br />[dct:description](http://purl.org/dc/terms/description) **max** 1<br />[hasAlias](hasAlias) (op) **some** [Alias](Alias) (c)<br />[hasLocality](hasLocality) (op) **exactly** 1 [Locality](Locality) (c)<br />[hasPostcode](haspostcode) (dp) **max** 1<br />[hasDateLastModified](hasdatelastmodified) (dp) **exactly** 1<br />[hasStreetLocality](hasStreetLocality) (op) **exactly** 1 [StreetLocality](StreetLocality) (c)<br />[hasNumber](hasNumber) (op) **some** [Number](Number) (c)<br />[hasGnafConfidence](hasGNAFconfidence) (op) **exactly** 1 [GnafConfidence](http://linked.data.gov.au/def/gnaf#GnafConfidence) (c)<br />[hasBuildingName](hasbuildingname) (dp) **max** 1<br />[hasAddressSite](hasAddressSite) (op) **exactly** 1 [AddressSite](AddressSite) (c)<br />
In domain of |[hasMeshBlockMatch](hasMeshBlockmatch) (op)<br />[hasStreetLocality](hasStreetLocality) (op)<br />[hasNumber](hasNumber) (op)<br />[hasAddressSecondary](hasAddressSecondary) (op)<br />[hasAddressSite](hasAddressSite) (op)<br />[hasGnafConfidence](hasGNAFconfidence) (op)<br />[hasGeocode](hasGeocode) (op)<br />
In range of |[hasAlias](hasAlias) (op)<br />[hasAddressSecondary](hasAddressSecondary) (op)<br />
### Address Site
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#AddressSite`
Super-classes |[GnafEntity](GNAFEntity) (c)<br />
Restrictions |[hasName](hasname) (dp) **max** 1<br />
In range of |[hasAddressSite](hasAddressSite) (op)<br />
### Alias
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#Alias`
Super-classes |[GnafEntity](GNAFEntity) (c)<br />
In domain of |[hasAlias](hasAlias) (op)<br />
### GNAF Entity
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#GnafEntity`
Description | <p>Entities (things) that are present as records in the GNAF database. Every GNAF Entity has a data created, date last modified (can be the same) and may have a data retired. These dates indicate the creation, modification &amp; retirement of the representation of the Entity in the GNAF database, not the real-world Entity.</p>
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
Restrictions |[hasDateRetired](hasdateretired) (dp) **max** 1<br />[hasDateCreated](hasdatecreated) (dp) **exactly** 1<br />
Sub-classes |[Alias](Alias) (c)<br />[Street](Street) (c)<br />[Locality](Locality) (c)<br />[Address](Address) (c)<br />[MeshBlockMatch](MeshBlockMatch) (c)<br />[geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />[AddressSite](AddressSite) (c)<br />
### Locality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#Locality`
Super-classes |[GnafEntity](GNAFEntity) (c)<br />[dbo:Location](http://dbpedia.org/ontology/Location) (c)<br />[prov:Location](http://www.w3.org/ns/prov#Location) (c)<br />[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Restrictions |[hasAlias](hasAlias) (op) **some** [Alias](Alias) (c)<br />[hasNeighbour](hasneighbour) (op) **some** [Locality](Locality) (c)<br />[hasPrimaryPostcode](hasprimarypostcode) (dp) **max** 1<br />[geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) **min** 1 [sf:Point](http://www.opengis.net/ont/sf#Point) (c)<br />[hasName](hasname) (dp) **exactly** 1<br />
In domain of |[hasNeighbour](hasneighbour) (op)<br />[hasPrimaryPostcode](hasprimarypostcode) (dp)<br />
In range of |[hasAlias](hasAlias) (op)<br />[hasNeighbour](hasneighbour) (op)<br />[hasLocality](hasLocality) (op)<br />
### 2011 Mesh Block
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#MB2011`
Is Defined By | http://linked.data.gov.au/def/gnaf
Source | G-NAF Data Product Description, November 2017
Description | <p>A Mesh Block from the 2011 census</p>
Super-classes |[asgs:MeshBlock](http://linked.data.gov.au/def/asgs#MeshBlock) (c)<br />
### 2016 Mesh Block
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#MB2016`
Is Defined By | http://linked.data.gov.au/def/gnaf
Source | G-NAF Data Product Description, November 2017
Description | <p>A Mesh Block from the 2016 census</p>
Super-classes |[asgs:MeshBlock](http://linked.data.gov.au/def/asgs#MeshBlock) (c)<br />
### Mesh Block Match
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#MeshBlockMatch`
Super-classes |[GnafEntity](GNAFEntity) (c)<br />
Restrictions |[hasMeshBlock](hasMeshBlock) (op) **exactly** 1 [asgs:MeshBlock](http://linked.data.gov.au/def/asgs#MeshBlock) (c)<br />
In domain of |[hasMeshBlock](hasMeshBlock) (op)<br />
In range of |[hasMeshBlockMatch](hasMeshBlockmatch) (op)<br />
### Number
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#Number`
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
Restrictions |[hasPrefix](hasprefix) (dp) **max** 1<br />[hasSuffix](hassuffix) (dp) **max** 1<br />
In domain of |[hasSuffix](hassuffix) (dp)<br />[hasPrefix](hasprefix) (dp)<br />
In range of |[hasNumber](hasNumber) (op)<br />
### Street
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#Street`
Super-classes |[GnafEntity](GNAFEntity) (c)<br />[dbo:Location](http://dbpedia.org/ontology/Location) (c)<br />[prov:Location](http://www.w3.org/ns/prov#Location) (c)<br />[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Restrictions |[hasAlias](hasAlias) (op) **some** [Alias](Alias) (c)<br />[hasStreetSuffix](hasStreetSuffix) (op) **max** 1 [StreetSuffix](http://linked.data.gov.au/def/gnaf#StreetSuffix) (c)<br />[hasName](hasname) (dp) **exactly** 1<br />
Sub-classes |[StreetLocality](StreetLocality) (c)<br />
In domain of |[hasStreetConfirmation](hasStreetConfirmation) (op)<br />
In range of |[hasAlias](hasAlias) (op)<br />
### Street Locality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#StreetLocality`
Super-classes |[Street](Street) (c)<br />
Restrictions |[hasLocality](hasLocality) (op) **exactly** 1 [Locality](Locality) (c)<br />[hasGnafConfidence](hasGNAFconfidence) (op) **exactly** 1 [GnafConfidence](http://linked.data.gov.au/def/gnaf#GnafConfidence) (c)<br />[geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) **min** 1 [sf:Point](http://www.opengis.net/ont/sf#Point) (c)<br />
In domain of |[hasLocality](hasLocality) (op)<br />[hasStreetSuffix](hasStreetSuffix) (op)<br />
In range of |[hasStreetLocality](hasStreetLocality) (op)<br />
### ISO19160-1 Address
Property | Value
--- | ---
IRI | `http://reference.data.gov.au/def/ont/iso19160-1-address#Address`
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
Sub-classes |[Address](Address) (c)<br />

## Object Properties
[alias of](#aliasof),
[GNAF type](#GNAFtype),
[hasAddressPrimary](#hasAddressPrimary),
[has Address Secondary](#hasAddressSecondary),
[has Address Site](#hasAddressSite),
[has Alias](#hasAlias),
[has Geocode](#hasGeocode),
[has Geocode Reliability](#hasGeocodeReliability),
[has GNAF confidence](#hasGNAFconfidence),
[has Locality](#hasLocality),
[has Mesh Block](#hasMeshBlock),
[has Mesh Block match](#hasMeshBlockmatch),
[has neighbour](#hasneighbour),
[has Number](#hasNumber),
[has State](#hasState),
[has Street Confirmation](#hasStreetConfirmation),
[has Street Locality](#hasStreetLocality),
[has Street Suffix](#hasStreetSuffix),
[](aliasof)
### alias of
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#aliasOf`
[](GNAFtype)
### GNAF type
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#gnafType`
Description | A property to allow for GNAF-specific soft typing of various GNAF classes using code list terms published in the GNAF product guide, for example Locality class instances being soft typed according to the Locality Types list which includes *Alias Only*, *District*, *Gazeted* etc.
[](hasAddressPrimary)
### hasAddressPrimary
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasAddressPrimary`
[](hasAddressSecondary)
### has Address Secondary
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasAddressSecondary`
Domain(s) |[Address](Address) (c)<br />
Range(s) |[Address](Address) (c)<br />
[](hasAddressSite)
### has Address Site
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasAddressSite`
Domain(s) |[Address](Address) (c)<br />
Range(s) |[AddressSite](AddressSite) (c)<br />
[](hasAlias)
### has Alias
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasAlias`
Domain(s) |[Alias](Alias) (c)<br />
Range(s) |[Locality](Locality) (c)<br />[Address](Address) (c)<br />[Street](Street) (c)<br />
[](hasGeocode)
### has Geocode
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasGeocode`
Super-properties |[geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry)<br />
Domain(s) |[Address](Address) (c)<br />
Range(s) |[sf:Point](http://www.opengis.net/ont/sf#Point) (c)<br />
[](hasGeocodeReliability)
### has Geocode Reliability
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasGeocodeReliability`
[](hasGNAFconfidence)
### has GNAF confidence
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasGnafConfidence`
Domain(s) |[Address](Address) (c)<br />
Range(s) |[GnafConfidence](http://linked.data.gov.au/def/gnaf#GnafConfidence) (c)<br />
[](hasLocality)
### has Locality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasLocality`
Super-properties |[geo:sfWithin](http://www.opengis.net/ont/geosparql#sfWithin)<br />
Domain(s) |[StreetLocality](StreetLocality) (c)<br />
Range(s) |[Locality](Locality) (c)<br />
[](hasMeshBlock)
### has Mesh Block
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasMeshBlock`
Domain(s) |[MeshBlockMatch](MeshBlockMatch) (c)<br />
Range(s) |[asgs:MeshBlock](http://linked.data.gov.au/def/asgs#MeshBlock) (c)<br />
[](hasMeshBlockmatch)
### has Mesh Block match
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasMeshBlockMatch`
Domain(s) |[Address](Address) (c)<br />
Range(s) |[MeshBlockMatch](MeshBlockMatch) (c)<br />
[](hasneighbour)
### has neighbour
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasNeighbour`
Domain(s) |[Locality](Locality) (c)<br />
Range(s) |[Locality](Locality) (c)<br />
[](hasNumber)
### has Number
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasNumber`
Domain(s) |[Address](Address) (c)<br />
Range(s) |[Number](Number) (c)<br />
[](hasState)
### has State
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasState`
Super-properties |[geo:sfWithin](http://www.opengis.net/ont/geosparql#sfWithin)<br />
Range(s) |[asgs:StateOrTerritory](http://linked.data.gov.au/def/asgs#StateOrTerritory) (c)<br />
[](hasStreetConfirmation)
### has Street Confirmation
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasStreetConfirmation`
Domain(s) |[Street](Street) (c)<br />
Range(s) |[StreetConfirmation](http://linked.data.gov.au/def/gnaf#StreetConfirmation) (c)<br />
[](hasStreetLocality)
### has Street Locality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasStreetLocality`
Super-properties |[geo:sfWithin](http://www.opengis.net/ont/geosparql#sfWithin)<br />
Domain(s) |[Address](Address) (c)<br />
Range(s) |[StreetLocality](StreetLocality) (c)<br />
[](hasStreetSuffix)
### has Street Suffix
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasStreetSuffix`
Domain(s) |[StreetLocality](StreetLocality) (c)<br />
Range(s) |[StreetSuffix](http://linked.data.gov.au/def/gnaf#StreetSuffix) (c)<br />

## Datatype Properties
[has building name](#hasbuildingname),
[has date created](#hasdatecreated),
[has date last modified](#hasdatelastmodified),
[has date retired](#hasdateretired),
[has description](#hasdescription),
[has legal parcel ID](#haslegalparcelID),
[has name](#hasname),
[has postcode](#haspostcode),
[has prefix](#hasprefix),
[has primary postcode](#hasprimarypostcode),
[has suffix](#hassuffix),
[has private street](#hasprivatestreet),
[](hasbuildingname)
### has building name
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasBuildingName`
[](hasdatecreated)
### has date created
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasDateCreated`
Description | This is the same as prov:wasGeneratedAtTime.
Range(s) |[xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) (c)<br />
[](hasdatelastmodified)
### has date last modified
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasDateLastModified`
Description | This is the same as dct:modified.
[](hasdateretired)
### has date retired
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasDateRetired`
Description | This is the same as prov:wasInvalidatedAtTime.
Range(s) |[xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) (c)<br />
[](hasdescription)
### has description
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasDescription`
Description | This is the same as dct:description.
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](haslegalparcelID)
### has legal parcel ID
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasLegalParcelId`
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](hasname)
### has name
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasName`
Description | This is the same as dct:title.
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](haspostcode)
### has postcode
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasPostcode`
Range(s) |[xsd:int](http://www.w3.org/2001/XMLSchema#int) (c)<br />
[](hasprefix)
### has prefix
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasPrefix`
Domain(s) |[Number](Number) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](hasprimarypostcode)
### has primary postcode
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasPrimaryPostcode`
Domain(s) |[Locality](Locality) (c)<br />
Range(s) |[xsd:int](http://www.w3.org/2001/XMLSchema#int) (c)<br />
[](hassuffix)
### has suffix
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasSuffix`
Domain(s) |[Number](Number) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](hasprivatestreet)
### has private street
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#isPrivateStreet`
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

## Named Individuals
[description](#description),
[has date created](#hasdatecreated),
[has date retired](#hasdateretired),
[has description](#hasdescription),
[has name](#hasname),
[title](#title),
[wasGeneratedAtTime](#wasGeneratedAtTime),
[wasInvalidatedAtTime](#wasInvalidatedAtTime),
### has date created <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasDateCreated`
* **Contributor(s)**
  * [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty)
  * [rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property)
Description | This is the same as prov:wasGeneratedAtTime.
Same As | [prov:wasGeneratedAtTime](http://www.w3.org/ns/prov#wasGeneratedAtTime)
### has date retired <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasDateRetired`
* **Contributor(s)**
  * [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty)
  * [rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property)
Description | This is the same as prov:wasInvalidatedAtTime.
Same As | [prov:wasInvalidatedAtTime](http://www.w3.org/ns/prov#wasInvalidatedAtTime)
### has description <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasDescription`
* **Contributor(s)**
  * [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty)
  * [rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property)
Description | This is the same as dct:description.
Same As | [dct:description](http://purl.org/dc/terms/description)
### has name <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/gnaf#hasName`
* **Contributor(s)**
  * [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty)
  * [rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property)
Description | This is the same as dct:title.
Same As | [dct:title](http://purl.org/dc/terms/title)
### description <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/description`
### title <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/title`
### wasGeneratedAtTime <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/prov#wasGeneratedAtTime`
### wasInvalidatedAtTime <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/prov#wasInvalidatedAtTime`
## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/gnaf#`
* **:**
  * `http://linked.data.gov.au/def/gnaf#`
* **asgs**
  * `http://linked.data.gov.au/def/asgs#`
* **dbo**
  * `http://dbpedia.org/ontology/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **geo**
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
* **sf**
  * `http://www.opengis.net/ont/sf#`
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