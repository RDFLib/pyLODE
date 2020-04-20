# The PLOT ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/plot/`
* **Creators(s)**
  * None
* **Created**
  * 2019-03-25
* **Modified**
  * 2019-06-11
* **Imports**
  * [http://purl.org/dc/elements/1.1/](http://purl.org/dc/elements/1.1/)
  * [ssn:ext](http://www.w3.org/ns/ssn/ext)
* **License**
  * [http://creativecommons.org/publicdomain/zero/1.0/](http://creativecommons.org/publicdomain/zero/1.0/)
* **Ontology RDF**
  * RDF ([plot.ttl](turtle))
### Description
<p>This vocabulary provides a set of classes to support capture of plot- and site-based ecological survey data. It is primary related to vegetation surveys, following the methdologies outlined in the Australian Soil and Land Survey Field Handbook.</p>
<p>PLOT is technically an extension to the W3C SSN/SOSA vocabulary, and also uses elements from the SSN-EXT ontology.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Ecological Community](#EcologicalCommunity),
[Ecology Observation](#EcologyObservation),
[Environmental continuant](#Environmentalcontinuant),
[Environmental region defined primarily by its function and membership](#Environmentalregiondefinedprimarilybyitsfunctionandmembership),
[Environmental region defined primarily by its location and extent](#Environmentalregiondefinedprimarilybyitslocationandextent),
[Flux tower](#Fluxtower),
[Location](#Location),
[Location of study](#Locationofstudy),
[Organism Occurrence ](#OrganismOccurrence),
[Organism assemblage](#Organismassemblage),
[Single taxon community](#Singletaxoncommunity),
[Single taxon community](#SiteTaxon),
[Site or location](#Siteorlocation),
[Survey](#Survey),
[Taxon assignment observation](#Taxonassignmentobservation),
[Vegetation strata classification ](#Vegetationstrataclassification),
[Vegetation stratum](#Vegetationstratum),
[Visit to a site](#Visittoasite),
[Visit to a study location](#Visittoastudylocation),
### Location
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/Location`
Super-classes |[dcterms:Location](http://purl.org/dc/terms/Location) (c)<br />
Restrictions |[locn:geometry](http://www.w3.org/ns/locn#geometry) **some** [w3cgeo:Point](http://www.w3.org/2003/01/geo/wgs84_pos#Point) (c)<br />[plot:mapsheetNumber](http://linked.data.gov.au/def/plot/mapsheetNumber) (dp) **max** 1<br />[plot:mapScale](http://linked.data.gov.au/def/plot/mapScale) (op) **max** 1<br />[plot:mapsheetName](http://linked.data.gov.au/def/plot/mapsheetName) (dp) **max** 1<br />
In domain of |[plot-x:isLocationOf](http://linked.data.gov.au/def/plot/x/isLocationOf) (op)<br />
### Organism Occurrence 
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/OrganismOccurence`
Description | <ol>
<li>sub-class of Sample because observations of an organism occurrence are primarily interesting if they represents a commuity or assemblage</li>
<li>sub-class of SpatialObject because it is bound to a specified location</li>
<li>sub-class of TemporalEntity because it is bound to a specified time</li>
</ol>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />[http://www.w3.org/2006/time#TemporalEntity](http://www.w3.org/2006/time#TemporalEntity) (c)<br />[geosparql:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Restrictions |[geosparql:defaultGeometry](http://www.opengis.net/ont/geosparql#defaultGeometry) **only** [w3cgeo:Point](http://www.w3.org/2003/01/geo/wgs84_pos#Point) (c)<br />[geosparql:defaultGeometry](http://www.opengis.net/ont/geosparql#defaultGeometry) **exactly** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** [plot-x:EcologicalCommunity](http://linked.data.gov.au/def/plot/x/EcologicalCommunity) (c)<br />
### Site or location
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/Site`
Description | <p>Location where observations may be made
May be a plot, quadrat, transect, trap etc</p>
Super-classes |[geosparql:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />
Restrictions |[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** ([plot-x:EnvironmentalSystem](http://linked.data.gov.au/def/plot/x/EnvironmentalSystem) (c) or [plot-x:EnvironmentalZone](http://linked.data.gov.au/def/plot/x/EnvironmentalZone) (c))<br />[sosa:isResultOf](http://www.w3.org/ns/sosa/isResultOf) **only** [plot:SiteVisit](http://linked.data.gov.au/def/plot/SiteVisit) (c)<br />[dcterms:hasPart](http://purl.org/dc/terms/hasPart) **only** [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[locn:location](http://www.w3.org/ns/locn#location) **only** [plot:Location](http://linked.data.gov.au/def/plot/Location) (c)<br />[plot:siteDescription](http://linked.data.gov.au/def/plot/siteDescription) (op) **min** 1<br />[dcterms:created](http://purl.org/dc/terms/created) **exactly** 1<br />[dcterms:isPartOf](http://purl.org/dc/terms/isPartOf) **only** [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) **only** [prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />[dcterms:relation](http://purl.org/dc/terms/relation) **some** [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
In domain of |[plot-x:floristics](http://linked.data.gov.au/def/plot/x/floristics) (op)<br />[plot-x:sampleLevel](http://linked.data.gov.au/def/plot/x/sampleLevel) (op)<br />[plot:siteDescription](http://linked.data.gov.au/def/plot/siteDescription) (op)<br />[plot-x:sampleType](http://linked.data.gov.au/def/plot/x/sampleType) (op)<br />
### Vegetation stratum
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/SiteStratum`
Description | <p>Structural element covering a recognisable height range in vegetation ecosystem occurring at an observation site</p>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />
Restrictions |[plot:stratum](http://linked.data.gov.au/def/plot/stratum) (op) **exactly** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **only** [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
### Single taxon community
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/SiteStratumTaxon`
Description | <p>Community of a single taxon in an identified stratum in a vegetation ecosystem occurring at an observation site</p>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />
Restrictions |[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** [plot:SiteTaxon](http://linked.data.gov.au/def/plot/SiteTaxon) (c)<br />[plot:stratum](http://linked.data.gov.au/def/plot/stratum) (op) **exactly** 1<br />[sosa:isFeatureOfInterestOf](http://www.w3.org/ns/sosa/isFeatureOfInterestOf) **min** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** [plot:SiteStratum](http://linked.data.gov.au/def/plot/SiteStratum) (c)<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **min** 1 [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[plot:taxon](http://linked.data.gov.au/def/plot/taxon) (op) **exactly** 1<br />
### Single taxon community
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/SiteTaxon`
Description | <p>Data corresponding to an individual of this class would usually be derived from observations relating to a set of SiteStratumTaxon at the same site on the same taxon</p>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />
Restrictions |[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **only** [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[plot:taxon](http://linked.data.gov.au/def/plot/taxon) (op) **exactly** 1<br />
### Visit to a site
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/SiteVisit`
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Restrictions |[plot:hadSubActivity](http://linked.data.gov.au/def/plot/hadSubActivity) (op) **some** ([sosa:Sampling](http://www.w3.org/ns/sosa/Sampling) (c) or [sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c) or [ssn-ext:ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c))<br />[plot:wasSubActivityOf](http://linked.data.gov.au/def/plot/wasSubActivityOf) (op) **some** [plot-x:Survey](http://linked.data.gov.au/def/plot/x/Survey) (c)<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **only** [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
### Vegetation strata classification 
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/Stratum`
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
### Organism assemblage
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/Assemblage`
Super-classes |[plot-x:EcologicalCommunity](http://linked.data.gov.au/def/plot/x/EcologicalCommunity) (c)<br />
### Ecological Community
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/EcologicalCommunity`
Super-classes |[plot-x:EnvironmentalSystem](http://linked.data.gov.au/def/plot/x/EnvironmentalSystem) (c)<br />
Sub-classes |[plot-x:Assemblage](http://linked.data.gov.au/def/plot/x/Assemblage) (c)<br />
### Environmental continuant
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant`
Description | <p>Union of environmental system, environmental zone, and ecological community?</p>
Super-classes |[sosa:FeatureOfInterest](http://www.w3.org/ns/sosa/FeatureOfInterest) (c)<br />
Sub-classes |[plot-x:EnvironmentalSystem](http://linked.data.gov.au/def/plot/x/EnvironmentalSystem) (c)<br />[plot-x:EnvironmentalZone](http://linked.data.gov.au/def/plot/x/EnvironmentalZone) (c)<br />
### Environmental region defined primarily by its function and membership
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/EnvironmentalSystem`
Super-classes |[plot-x:EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c)<br />[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Sub-classes |[plot-x:EcologicalCommunity](http://linked.data.gov.au/def/plot/x/EcologicalCommunity) (c)<br />
### Environmental region defined primarily by its location and extent
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/EnvironmentalZone`
Super-classes |[plot-x:EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c)<br />[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
### Flux tower
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/FluxTower`
Super-classes |[sosa:Platform](http://www.w3.org/ns/sosa/Platform) (c)<br />
Restrictions |[sosa:hosts](http://www.w3.org/ns/sosa/hosts) **min** 1 [sosa:Sensor](http://www.w3.org/ns/sosa/Sensor) (c)<br />[locn:location](http://www.w3.org/ns/locn#location) **min** 1<br />
### Ecology Observation
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/Observation`
Super-classes |[sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c)<br />
Restrictions |[ssn-ext:hasUltimateFeatureOfInterest](http://www.w3.org/ns/ssn/ext/hasUltimateFeatureOfInterest) **only** ([plot:Site](http://linked.data.gov.au/def/plot/Site) (c) or [plot:OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c) or [plot-x:EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c) or [plot:OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c))<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **only** ([plot:Site](http://linked.data.gov.au/def/plot/Site) (c) or [plot:OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c) or [plot-x:EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c) or [plot:OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c))<br />
### Location of study
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/StudyLocation`
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
### Visit to a study location
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/StudyLocationVisit`
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Restrictions |[prov:used](http://www.w3.org/ns/prov#used) **some** [plot-x:StudyLocation](http://linked.data.gov.au/def/plot/x/StudyLocation) (c)<br />
### Survey
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/Survey`
Description | <p>Survey is composed of a set of Observations and ObservationCollections, which may have a site as its feature-of-interest
In this context the value of feature-of-interest is expected to be the value of the chain   (ssn-ext:hasMember)+/sosa:hasFeatureOfInterest</p>
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Restrictions |[dcterms:title](http://purl.org/dc/terms/title) **exactly** 1<br />[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith) **some** [prov:Organization](http://www.w3.org/ns/prov#Organization) (c)<br />[http://purl.org/dc/elements/1.1/creator](http://purl.org/dc/elements/1.1/creator) **min** 1<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **min** 1 [plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[dcterms:accessRights](http://purl.org/dc/terms/accessRights) **exactly** 1 [http://www.w3.org/ns/odrl/2/Permission](http://www.w3.org/ns/odrl/2/Permission) (c)<br />[locn:location](http://www.w3.org/ns/locn#location) **only** [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />[dcterms:license](http://purl.org/dc/terms/license) **exactly** 1 [http://www.w3.org/ns/odrl/2/Policy](http://www.w3.org/ns/odrl/2/Policy) (c)<br />
### Taxon assignment observation
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/TaxonAssignment`
Super-classes |[sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c)<br />
Restrictions |[sosa:observedProperty](http://www.w3.org/ns/sosa/observedProperty) **value** [op:Taxon-identity](http://www.tern.org.au/cv/op/Taxon-identity) (c)<br />

## Object Properties
[pointer to child activity](#pointertochildactivity),
[Map scale](#Mapscale),
[siteDescription](#siteDescription),
[stratum classification](#stratumclassification),
[taxon classification](#taxonclassification),
[pointer to parent activity](#pointertoparentactivity),
[Site floristics classification](#Sitefloristicsclassification),
[Quality of individual or related observation results](#Qualityofindividualorrelatedobservationresults),
[describes the location of](#describesthelocationof),
[Observer](#Observer),
[sample level classification](#samplelevelclassification),
[sample type classification](#sampletypeclassification),
[Sampler](#Sampler),
[Site visitor](#Sitevisitor),
[is member of](#ismemberof),
[](pointertochildactivity)
### pointer to child activity
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/hadSubActivity`
Description | To allow links between observations or site-visits and projects, programs and initiatives, between observations and site-visits, etc
Domain(s) |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Range(s) |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
[](Mapscale)
### Map scale
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/mapScale`
[](siteDescription)
### siteDescription
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/siteDescription`
Super-properties |[sosa:isFeatureOfInterestOf](http://www.w3.org/ns/sosa/isFeatureOfInterestOf)<br />
Domain(s) |[plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[ssn-ext:ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c)<br />
[](stratumclassification)
### stratum classification
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/stratum`
Super-properties |[dcterms:type](http://purl.org/dc/terms/type)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](taxonclassification)
### taxon classification
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/taxon`
Super-properties |[dcterms:type](http://purl.org/dc/terms/type)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](pointertoparentactivity)
### pointer to parent activity
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/wasSubActivityOf`
Super-properties |[prov:wasInformedBy](http://www.w3.org/ns/prov#wasInformedBy)<br />
[](Sitefloristicsclassification)
### Site floristics classification
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/floristics`
Super-properties |[dcterms:type](http://purl.org/dc/terms/type)<br />
Domain(s) |[plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](Qualityofindividualorrelatedobservationresults)
### Quality of individual or related observation results
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/hasResultQuality`
Description | this property allows an indication of the quality of the data to be provided at the level of either an individual observation or a thematic group. This is commonly done by some kind of description of the method, protocol, sensor, observer, etc. 
Domain(s) |([sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c) or [ssn-ext:ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c))<br />
[](describesthelocationof)
### describes the location of
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/isLocationOf`
Description | Links an individual location description to the resource (e.g. a plot:Site) that it relates to
Domain(s) |[plot:Location](http://linked.data.gov.au/def/plot/Location) (c)<br />
[](Observer)
### Observer
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/observer`
Super-properties |[sosa:madeBySensor](http://www.w3.org/ns/sosa/madeBySensor)<br />[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />
[](samplelevelclassification)
### sample level classification
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/sampleLevel`
Super-properties |[dcterms:type](http://purl.org/dc/terms/type)<br />
Domain(s) |[plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](sampletypeclassification)
### sample type classification
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/sampleType`
Description | The site's plot shape description, e.g. square, circle, etc.
Super-properties |[dcterms:type](http://purl.org/dc/terms/type)<br />
Domain(s) |[plot:Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](Sampler)
### Sampler
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/sampler`
Super-properties |[sosa:madeBySampler](http://www.w3.org/ns/sosa/madeBySampler)<br />[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />
[](Sitevisitor)
### Site visitor
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/x/visitor`
Super-properties |[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />
[](ismemberof)
### is member of
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/ssn/ext/isMemberOf`
Description | indicates a collection of which the context resource is a member
Super-properties |[plot:wasSubActivityOf](http://linked.data.gov.au/def/plot/wasSubActivityOf) (op)<br />
Domain(s) |([sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c) or [ssn-ext:ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c))<br />
Range(s) |[ssn-ext:ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c)<br />

## Datatype Properties
[Mapsheet](#Mapsheet),
[Mapsheet](#mapsheetNumber),
[](Mapsheet)
### Mapsheet
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/mapsheetName`
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](mapsheetNumber)
### Mapsheet
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/plot/mapsheetNumber`
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

## Named Individuals
## Namespaces
* **dcterms**
  * `http://purl.org/dc/terms/`
* **geosparql**
  * `http://www.opengis.net/ont/geosparql#`
* **locn**
  * `http://www.w3.org/ns/locn#`
* **op**
  * `http://www.tern.org.au/cv/op/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **plot**
  * `http://linked.data.gov.au/def/plot/`
* **plot-x**
  * `http://linked.data.gov.au/def/plot/x/`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `http://schema.org/`
* **sdo1**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **sosa**
  * `http://www.w3.org/ns/sosa/`
* **ssn**
  * `http://www.w3.org/ns/ssn/`
* **ssn-ext**
  * `http://www.w3.org/ns/ssn/ext/`
* **w3cgeo**
  * `http://www.w3.org/2003/01/geo/wgs84_pos#`
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