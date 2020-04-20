# ASGS Ontology
### A taxonomy

Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)

## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/asgs`
* **Publisher(s)**
  * [Australian Bureau of Statistics](http://linked.data.gov.au/org/abs)
* **Creators(s)**
  * [Laurent Lefort](https://orcid.org/0000-0002-4305-6085)
    [[ORCID]](https://orcid.org/0000-0002-4305-6085) of [Australian Bureau of Statistics](https://www.abs.gov.au)
  * [Simon J.D. Cox](https://orcid.org/0000-0002-3884-3420)
    [[ORCID]](https://orcid.org/0000-0002-3884-3420)
    (<simon.cox@csiro.au></a>) of [CSIRO](https://www.csiro.au)
* **Contributor(s)**
  * [Nicholas J. Car](https://orcid.org/0000-0002-8742-7730)
    [[ORCID]](https://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@surroundaustralia.com></a>) of [SURROUND Australia Pty Ltd](https://surroundaustralia.com)
* **Created**
  * 2018-11-23
* **Modified**
  * 2020-02-03
* **Rights**
  * &copy; 2018 Australian Bureau of Statistics.
* **Source**
  * [https://www.abs.gov.au/websitedbs/D3310114.nsf/home/Australian+Statistical+Geography+Standard+(ASGS)](https://www.abs.gov.au/websitedbs/D3310114.nsf/home/Australian+Statistical+Geography+Standard+(ASGS))
* **Ontology RDF**
  * RDF ([asgs.ttl](turtle))
* **Code Repository**
  * <[https://github.com/AGLDWG/asgs-ont/](https://github.com/AGLDWG/asgs-ont/)>
### Description
<p><a href='https://www.abs.gov.au/websitedbs/D3310114.nsf/home/Australian+Statistical+Geography+Standard+(ASGS)'>Australian Statistical Geography Standard (ASGS)</a> ABS Structures and non-ABS structures</p>

<p>Ontology for the Australian Statistical Geography Standard (ASGS), a framework of statistical areas used by the Australian Bureau of Statistics (ABS) and other organisations to enable the publication of statistics that are comparable and spatially integrated. This ontology contains the definitions for the ABS Structures which are areas that the ABS designs specifically for outputting statistics.</p>

<ul>
  <li>structures: Mesh Block, Statistical Areas (Level 1 to Level 4), Greater Capital City Statistical Areas, State or Territory, Country classes,</li>
  <li>Indigenous structures: Indigenous location, Indigenous area, , Indigenous region classes</li>
  <li>Urban structures: Urban Centre and Locality, Section of State Range, Section of State, and Significant Urban Area classes</li>
</ul>

<p>and for the Non ABS Structures which are not defined or maintained by the ABS but represent administrative areas for which the ABS is committed to providing a range of statistics. The classes defined here corresponds to ABS approximations of spatial areas or regions which are defined elsewhere</p>

<ul>
  <li>Local Government Areas (LGAs)</li>
  <li>Postal Areas (POAs)</li>
  <li>State Suburbs (SSCs)</li>
  <li>Commonwealth Electoral Divisions (CEDs)</li>
  <li>State Electoral Divisions (SEDs)</li>
  <li>Australian Drainage Divisions (ADDs)</li>
  <li>Natural Resource Management Regions (NRMRs)</li>
  <li>Tourism Regions (TRs)</li>
</ul>

<p>The ASGS uses Mesh Blocks as a common building block for all structures. Mesh Blocks are small enough that they can accurately approximate the changing administrative areas maintained by other organisations, without changing themselves.</p>

<p>The publication of the ASGS ontology is part of the Australian Bureau of Statistics contribution to a joint effort to publish authoritative, interconnected spatial products (Location Index project).</p>

<p>The ASGS Ontology is packaged in multiple graphs:</p>

<ul>
    <li>http://linked.data.gov.au/def/asgs (this graph) contains the core classes for ASGS statistical units, and a small number of properties relating to their identity, classification, and containment hierarchy</li>
  <li>http://linked.data.gov.au/def/asgs-cat contains the meshblock classification scheme</li>
  <li>http://linked.data.gov.au/def/asgs-id contains specialised string types for identifiers and labels</li>
  <li>http://linked.data.gov.au/def/asgs-path contains association classes and properties relating to paths between instances of the core classes</li>
  <li>http://linked.data.gov.au/def/asgs-isof (deprecated) contains specialized predicates for containment relationships - this functionality is provided by the generic 'within' and 'contains' relations</li>
  <li>http://linked.data.gov.au/def/asgs-code (deprecated) contains specialised annotation properties for identifiers and labels - this functionality has been superseded by a set of data-types to be used in conjunction with more generic properties</li>
  <li>http://linked.data.gov.au/def/asgs-prop (deprecated) contains specialised ASGS properties for relationships, classifiers, identifiers and labels - this functionality has been superseded by use of types from standardized RDF vocabularies</li>
</u>


## Table of Contents
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes

### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#AustralianDrainageDivision`
Preferred Labels |Australian Drainage Division (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#CommonwealthElectoralDivision`
Preferred Labels |Commonwealth Electoral Division (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#Country`
Preferred Labels |Country (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#DestinationZone`
Preferred Labels |DestinationZone (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#Feature`
Preferred Labels |ASGS Feature (None)<br />
Broader Concepts |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (cp)<br />
Narrower Concepts |[None](MeshBlock) (cp)<br />[None](IndigenousRegion) (cp)<br />[None](StatisticalAreaLevel2) (cp)<br />[None](RemotenessArea) (cp)<br />[None](PostalArea) (cp)<br />[None](UrbanCentreAndLocality) (cp)<br />[None](LocalGovernmentArea) (cp)<br />[None](DestinationZone) (cp)<br />[None](TourismRegion) (cp)<br />[None](GreaterCapitalCityStatisticalArea) (cp)<br />[None](IndigenousLocation) (cp)<br />[None](SignificantUrbanArea) (cp)<br />[None](SectionOfState) (cp)<br />[None](StateOrTerritory) (cp)<br />[None](Country) (cp)<br />[None](StateElectoralDivision) (cp)<br />[None](StatisticalAreaLevel3) (cp)<br />[None](StatisticalAreaLevel4) (cp)<br />[None](CommonwealthElectoralDivision) (cp)<br />[None](StatisticalAreaLevel1) (cp)<br />[None](AustralianDrainageDivision) (cp)<br />[None](IndigenousArea) (cp)<br />[None](StateSuburb) (cp)<br />[None](SectionOfStateRange) (cp)<br />[None](NaturalResourceManagementRegion) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#GreaterCapitalCityStatisticalArea`
Preferred Labels |Greater Capital City Statistical Area (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#IndigenousArea`
Preferred Labels |Indigenous Area (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#IndigenousLocation`
Preferred Labels |Indigenous Location (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#IndigenousRegion`
Preferred Labels |Indigenous Region (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#LocalGovernmentArea`
Preferred Labels |Local Government Area (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#MeshBlock`
Preferred Labels |Mesh Block (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#MeshblockCategory`
Preferred Labels |Meshblock category (None)<br />
Broader Concepts |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#NaturalResourceManagementRegion`
Preferred Labels |Natural Resource Management Region (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#PostalArea`
Preferred Labels |Postal area (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#RemotenessArea`
Preferred Labels |Remoteness Area (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#SectionOfState`
Preferred Labels |Section of State (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#SectionOfStateRange`
Preferred Labels |Section of State Range (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#SignificantUrbanArea`
Preferred Labels |Significant Urban Area (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StateElectoralDivision`
Preferred Labels |State Electoral Division (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StateOrTerritory`
Preferred Labels |StateOrTerritory (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StateSuburb`
Preferred Labels |State Suburb (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StatisticalAreaLevel1`
Preferred Labels |Statistical Area Level 1 (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StatisticalAreaLevel2`
Preferred Labels |Statistical Area Level 2 (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StatisticalAreaLevel3`
Preferred Labels |Statistical Area Level 3 (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#StatisticalAreaLevel4`
Preferred Labels |Statistical Area Level 4 (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#TourismRegion`
Preferred Labels |Tourism Region (None)<br />
Broader Concepts |[None](Feature) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/asgs#UrbanCentreAndLocality`
Preferred Labels |UrbanCentreAndLocality (None)<br />
Broader Concepts |[None](Feature) (cp)<br />

## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/asgs#`
* **asgs**
  * `http://linked.data.gov.au/def/asgs#`
* **cc**
  * `http://creativecommons.org/ns#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dcterms**
  * `http://purl.org/dc/terms/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
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
* **schema**
  * `http://schema.org/`
* **sdo**
  * `https://schema.org/`
* **sf**
  * `http://www.opengis.net/ont/sf#`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **void**
  * `http://rdfs.org/ns/void#`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Collections: cl
* Concepts: cp