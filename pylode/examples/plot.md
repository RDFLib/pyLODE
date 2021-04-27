Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# The PLOT ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/plot/`
* **Creators(s)**
  * None
* **Created**
  * 2019-03-25
* **Modified**
  * 2019-06-11
* **Imports**
  * [dc:](http://purl.org/dc/elements/1.1/)
  * [http://www.w3.org/ns/ssn/ext](http://www.w3.org/ns/ssn/ext)
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
URI | `http://linked.data.gov.au/def/plot/Location`
Super-classes |[dct:Location](http://purl.org/dc/terms/Location) (c)<br />
Restrictions |[http://linked.data.gov.au/def/plot/mapsheetName](http://linked.data.gov.au/def/plot/mapsheetName) (dp) **max** 1<br />[http://linked.data.gov.au/def/plot/mapScale](http://linked.data.gov.au/def/plot/mapScale) (op) **max** 1<br />[http://linked.data.gov.au/def/plot/mapsheetNumber](http://linked.data.gov.au/def/plot/mapsheetNumber) (dp) **max** 1<br />[locn:geometry](http://www.w3.org/ns/locn#geometry) **some** [geo:Point](http://www.w3.org/2003/01/geo/wgs84_pos#Point) (c)<br />
In domain of |[http://linked.data.gov.au/def/plot/x/isLocationOf](http://linked.data.gov.au/def/plot/x/isLocationOf) (op)<br />
### Organism Occurrence 
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/OrganismOccurence`
Description | <ol> <li>sub-class of Sample because observations of an organism occurrence are primarily interesting if they represents a commuity or assemblage</li> <li>sub-class of SpatialObject because it is bound to a specified location</li> <li>sub-class of TemporalEntity because it is bound to a specified time</li> </ol>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />[geosparql:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />[time:TemporalEntity](http://www.w3.org/2006/time#TemporalEntity) (c)<br />
Restrictions |[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** [http://linked.data.gov.au/def/plot/x/EcologicalCommunity](http://linked.data.gov.au/def/plot/x/EcologicalCommunity) (c)<br />[geosparql:defaultGeometry](http://www.opengis.net/ont/geosparql#defaultGeometry) **only** [geo:Point](http://www.w3.org/2003/01/geo/wgs84_pos#Point) (c)<br />[geosparql:defaultGeometry](http://www.opengis.net/ont/geosparql#defaultGeometry) **exactly** 1<br />
### Site or location
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/Site`
Description | <p>Location where observations may be made May be a plot, quadrat, transect, trap etc</p>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />[geosparql:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Restrictions |[sosa:isResultOf](http://www.w3.org/ns/sosa/isResultOf) **only** [http://linked.data.gov.au/def/plot/SiteVisit](http://linked.data.gov.au/def/plot/SiteVisit) (c)<br />[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) **only** [prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />[locn:location](http://www.w3.org/ns/locn#location) **only** [http://linked.data.gov.au/def/plot/Location](http://linked.data.gov.au/def/plot/Location) (c)<br />[dct:created](http://purl.org/dc/terms/created) **exactly** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** ([http://linked.data.gov.au/def/plot/x/EnvironmentalSystem](http://linked.data.gov.au/def/plot/x/EnvironmentalSystem) (c) or [http://linked.data.gov.au/def/plot/x/EnvironmentalZone](http://linked.data.gov.au/def/plot/x/EnvironmentalZone) (c))<br />[http://linked.data.gov.au/def/plot/siteDescription](http://linked.data.gov.au/def/plot/siteDescription) (op) **min** 1<br />[dct:relation](http://purl.org/dc/terms/relation) **some** [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[dct:isPartOf](http://purl.org/dc/terms/isPartOf) **only** [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[dct:hasPart](http://purl.org/dc/terms/hasPart) **only** [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
In domain of |[http://linked.data.gov.au/def/plot/x/sampleLevel](http://linked.data.gov.au/def/plot/x/sampleLevel) (op)<br />[http://linked.data.gov.au/def/plot/siteDescription](http://linked.data.gov.au/def/plot/siteDescription) (op)<br />[http://linked.data.gov.au/def/plot/x/sampleType](http://linked.data.gov.au/def/plot/x/sampleType) (op)<br />[http://linked.data.gov.au/def/plot/x/floristics](http://linked.data.gov.au/def/plot/x/floristics) (op)<br />
### Vegetation stratum
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/SiteStratum`
Description | <p>Structural element covering a recognisable height range in vegetation ecosystem occurring at an observation site</p>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />
Restrictions |[http://linked.data.gov.au/def/plot/stratum](http://linked.data.gov.au/def/plot/stratum) (op) **exactly** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **only** [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
### Single taxon community
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/SiteStratumTaxon`
Description | <p>Community of a single taxon in an identified stratum in a vegetation ecosystem occurring at an observation site</p>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />
Restrictions |[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** [http://linked.data.gov.au/def/plot/SiteStratum](http://linked.data.gov.au/def/plot/SiteStratum) (c)<br />[http://linked.data.gov.au/def/plot/taxon](http://linked.data.gov.au/def/plot/taxon) (op) **exactly** 1<br />[http://linked.data.gov.au/def/plot/stratum](http://linked.data.gov.au/def/plot/stratum) (op) **exactly** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **some** [http://linked.data.gov.au/def/plot/SiteTaxon](http://linked.data.gov.au/def/plot/SiteTaxon) (c)<br />[sosa:isFeatureOfInterestOf](http://www.w3.org/ns/sosa/isFeatureOfInterestOf) **min** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **min** 1 [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
### Single taxon community
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/SiteTaxon`
Description | <p>Community of a single taxon in vegetation ecosystem occurring at an observation site</p>
Super-classes |[sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />
Restrictions |[http://linked.data.gov.au/def/plot/taxon](http://linked.data.gov.au/def/plot/taxon) (op) **exactly** 1<br />[sosa:isSampleOf](http://www.w3.org/ns/sosa/isSampleOf) **only** [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
### Visit to a site
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/SiteVisit`
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Restrictions |[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **only** [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[http://linked.data.gov.au/def/plot/hadSubActivity](http://linked.data.gov.au/def/plot/hadSubActivity) (op) **some** ([sosa:Sampling](http://www.w3.org/ns/sosa/Sampling) (c) or [sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c) or [http://www.w3.org/ns/ssn/ext/ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c))<br />[http://linked.data.gov.au/def/plot/wasSubActivityOf](http://linked.data.gov.au/def/plot/wasSubActivityOf) (op) **some** [http://linked.data.gov.au/def/plot/x/Survey](http://linked.data.gov.au/def/plot/x/Survey) (c)<br />
### Vegetation strata classification 
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/Stratum`
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
### Organism assemblage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/Assemblage`
Super-classes |[http://linked.data.gov.au/def/plot/x/EcologicalCommunity](http://linked.data.gov.au/def/plot/x/EcologicalCommunity) (c)<br />
### Ecological Community
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/EcologicalCommunity`
Super-classes |[http://linked.data.gov.au/def/plot/x/EnvironmentalSystem](http://linked.data.gov.au/def/plot/x/EnvironmentalSystem) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/plot/x/Assemblage](http://linked.data.gov.au/def/plot/x/Assemblage) (c)<br />
### Environmental continuant
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant`
Description | <p>Union of environmental system, environmental zone, and ecological community?</p>
Super-classes |[sosa:FeatureOfInterest](http://www.w3.org/ns/sosa/FeatureOfInterest) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/plot/x/EnvironmentalSystem](http://linked.data.gov.au/def/plot/x/EnvironmentalSystem) (c)<br />[http://linked.data.gov.au/def/plot/x/EnvironmentalZone](http://linked.data.gov.au/def/plot/x/EnvironmentalZone) (c)<br />
### Environmental region defined primarily by its function and membership
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/EnvironmentalSystem`
Super-classes |[http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c)<br />[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/plot/x/EcologicalCommunity](http://linked.data.gov.au/def/plot/x/EcologicalCommunity) (c)<br />
### Environmental region defined primarily by its location and extent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/EnvironmentalZone`
Super-classes |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />[http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c)<br />
### Flux tower
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/FluxTower`
Super-classes |[sosa:Platform](http://www.w3.org/ns/sosa/Platform) (c)<br />
Restrictions |[locn:location](http://www.w3.org/ns/locn#location) **min** 1<br />[sosa:hosts](http://www.w3.org/ns/sosa/hosts) **min** 1 [sosa:Sensor](http://www.w3.org/ns/sosa/Sensor) (c)<br />
### Ecology Observation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/Observation`
Super-classes |[sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c)<br />
Restrictions |[http://www.w3.org/ns/ssn/ext/hasUltimateFeatureOfInterest](http://www.w3.org/ns/ssn/ext/hasUltimateFeatureOfInterest) **only** ([http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c) or [http://linked.data.gov.au/def/plot/OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c) or [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c) or [http://linked.data.gov.au/def/plot/OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c))<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **only** ([http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant](http://linked.data.gov.au/def/plot/x/EnvironmentalContinuant) (c) or [http://linked.data.gov.au/def/plot/OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c) or [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c) or [http://linked.data.gov.au/def/plot/OrganismOccurence](http://linked.data.gov.au/def/plot/OrganismOccurence) (c))<br />
### Location of study
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/StudyLocation`
Super-classes |[prov:Entity](http://www.w3.org/ns/prov#Entity) (c)<br />
### Visit to a study location
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/StudyLocationVisit`
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Restrictions |[prov:used](http://www.w3.org/ns/prov#used) **some** [http://linked.data.gov.au/def/plot/x/StudyLocation](http://linked.data.gov.au/def/plot/x/StudyLocation) (c)<br />
### Survey
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/Survey`
Description | <p>Survey is composed of a set of Observations and ObservationCollections, which may have a site as its feature-of-interest In this context the value of feature-of-interest is expected to be the value of the chain   (ssn-ext:hasMember)+/sosa:hasFeatureOfInterest</p>
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Restrictions |[dct:title](http://purl.org/dc/terms/title) **exactly** 1<br />[dc:creator](http://purl.org/dc/elements/1.1/creator) **min** 1<br />[locn:location](http://www.w3.org/ns/locn#location) **only** [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith) **some** [prov:Organization](http://www.w3.org/ns/prov#Organization) (c)<br />[dct:accessRights](http://purl.org/dc/terms/accessRights) **exactly** 1 [odrl:Permission](http://www.w3.org/ns/odrl/2/Permission) (c)<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **min** 1 [http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />[dct:license](http://purl.org/dc/terms/license) **exactly** 1 [odrl:Policy](http://www.w3.org/ns/odrl/2/Policy) (c)<br />
### Taxon assignment observation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/TaxonAssignment`
Super-classes |[sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c)<br />
Restrictions |[sosa:observedProperty](http://www.w3.org/ns/sosa/observedProperty) **value** [http://www.tern.org.au/cv/op/Taxon-identity](http://www.tern.org.au/cv/op/Taxon-identity) (c)<br />

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
URI | `http://linked.data.gov.au/def/plot/hadSubActivity`
Description | To allow links between observations or site-visits and projects, programs and initiatives, between observations and site-visits, etc
Domain(s) |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Range(s) |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
[](Mapscale)
### Map scale
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/mapScale`
[](siteDescription)
### siteDescription
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/siteDescription`
Super-properties |[sosa:isFeatureOfInterestOf](http://www.w3.org/ns/sosa/isFeatureOfInterestOf)<br />
Domain(s) |[http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[http://www.w3.org/ns/ssn/ext/ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c)<br />
[](stratumclassification)
### stratum classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/stratum`
Super-properties |[dct:type](http://purl.org/dc/terms/type)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](taxonclassification)
### taxon classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/taxon`
Super-properties |[dct:type](http://purl.org/dc/terms/type)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](pointertoparentactivity)
### pointer to parent activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/wasSubActivityOf`
Super-properties |[prov:wasInformedBy](http://www.w3.org/ns/prov#wasInformedBy)<br />
[](Sitefloristicsclassification)
### Site floristics classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/floristics`
Super-properties |[dct:type](http://purl.org/dc/terms/type)<br />
Domain(s) |[http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](Qualityofindividualorrelatedobservationresults)
### Quality of individual or related observation results
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/hasResultQuality`
Description | this property allows an indication of the quality of the data to be provided at the level of either an individual observation or a thematic group. This is commonly done by some kind of description of the method, protocol, sensor, observer, etc. 
Domain(s) |([sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c) or [http://www.w3.org/ns/ssn/ext/ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c))<br />
[](describesthelocationof)
### describes the location of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/isLocationOf`
Description | Links an individual location description to the resource (e.g. a plot:Site) that it relates to
Domain(s) |[http://linked.data.gov.au/def/plot/Location](http://linked.data.gov.au/def/plot/Location) (c)<br />
[](Observer)
### Observer
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/observer`
Super-properties |[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />[sosa:madeBySensor](http://www.w3.org/ns/sosa/madeBySensor)<br />
[](samplelevelclassification)
### sample level classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/sampleLevel`
Super-properties |[dct:type](http://purl.org/dc/terms/type)<br />
Domain(s) |[http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](sampletypeclassification)
### sample type classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/sampleType`
Description | The site's plot shape description, e.g. square, circle, etc.
Super-properties |[dct:type](http://purl.org/dc/terms/type)<br />
Domain(s) |[http://linked.data.gov.au/def/plot/Site](http://linked.data.gov.au/def/plot/Site) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](Sampler)
### Sampler
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/sampler`
Super-properties |[sosa:madeBySampler](http://www.w3.org/ns/sosa/madeBySampler)<br />[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />
[](Sitevisitor)
### Site visitor
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/x/visitor`
Super-properties |[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />
[](ismemberof)
### is member of
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/ext/isMemberOf`
Description | indicates a collection of which the context resource is a member
Super-properties |[http://linked.data.gov.au/def/plot/wasSubActivityOf](http://linked.data.gov.au/def/plot/wasSubActivityOf) (op)<br />
Domain(s) |([sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c) or [http://www.w3.org/ns/ssn/ext/ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c))<br />
Range(s) |[http://www.w3.org/ns/ssn/ext/ObservationCollection](http://www.w3.org/ns/ssn/ext/ObservationCollection) (c)<br />

## Datatype Properties
[Mapsheet](#Mapsheet),
[Mapsheet](#mapsheetNumber),
[](Mapsheet)
### Mapsheet
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/mapsheetName`
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](mapsheetNumber)
### Mapsheet
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/plot/mapsheetNumber`
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

## Named Individuals
## Namespaces
* **cdao**
  * `http://purl.obolibrary.org/obo/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **dwc**
  * `http://rs.tdwg.org/dwc/terms/`
* **geo**
  * `http://www.w3.org/2003/01/geo/wgs84_pos#`
* **geosparql**
  * `http://www.opengis.net/ont/geosparql#`
* **locn**
  * `http://www.w3.org/ns/locn#`
* **odrl**
  * `http://www.w3.org/ns/odrl/2/`
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
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **sosa**
  * `http://www.w3.org/ns/sosa/`
* **time**
  * `http://www.w3.org/2006/time#`
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