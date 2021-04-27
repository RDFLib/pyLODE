Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.7

# Geofabric Ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/geofabric`
* **Publisher(s)**
  * [CSIRO](http://catalogue.linked.data.gov.au/org/csiro)
* **Creators(s)**
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
* **Contributor(s)**
  * None
* **Created**
  * 2019-06-07
* **Modified**
  * 2019-07-29
* **Version Information**
  * Version 1.0 only characterises 3 types of Feature - Contracted Catchment, River Region & Drianage Division - and requires that each CC be within a RR and that an RR be within a DD.
* **Version URI**
  * [http://linked.data.gov.au/def/geofabric/1.0](http://linked.data.gov.au/def/geofabric/1.0)
* **Imports**
  * [geosparql:](http://www.opengis.net/ont/geosparql#)
* **Source**
  * [http://www.bom.gov.au/water/geofabric/documents/v3_0/ahgf_productguide_V3_0_release.pdf](http://www.bom.gov.au/water/geofabric/documents/v3_0/ahgf_productguide_V3_0_release.pdf)
* **Ontology RDF**
  * RDF ([geofabric.ttl](turtle))
### Description
<p>A bare-bones ontology for the Australian Hydrological Geospatial Fabric.</p>
<p>This small ontology characterises major parts of the <a href="http://www.bom.gov.au/water/geofabric/">Australian Hydrological Geospatial Fabric</a> for their delivery as <a href="https://www.w3.org/wiki/LinkedData">Linked Data</a> via the <a href="http://linked.data.gov.au/dataset/geofabric">Geofabric LDAPI</a>.</p>
<p>This ontology accords with the <a href="http://locationindex.org">Loc-I Project</a>'s requirements for the delivery of spatial <a href="https://www.w3.org/standards/semanticweb/">Semantic Web</a> objects.</p>

## Table of Contents
1. [Classes](#classes)
1. [Annotation Properties](#annotationproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Catchment](#Catchment),
[Catchment Aggregate](#CatchmentAggregate),
[Contracted Catchment](#ContractedCatchment),
[Drainage Division](#DrainageDivision),
[Feature](#Feature),
[Geofabric Hydrology reporting region](#GeofabricHydrologyreportingregion),
[River Region](#RiverRegion),
### Contracted Catchment
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geofabric#ContractedCatchment`
Source | Section 5.4.3 Page 40 in the Australian Hydrological Geospatial Fabric (Geofabric) v3.0 Product Guide
Description | <p>The Geofabric's Hydrology Reporting Catchments product's AHGF Contracted Catchment object.</p> <p>Contracted Catchments are always within River Revions.</p>
Super-classes |[https://www.opengis.net/def/appschema/hy_features/hyf/HY_Catchment](https://www.opengis.net/def/appschema/hy_features/hyf/HY_Catchment) (c)<br />[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Restrictions |[geosparql:sfWithin](http://www.opengis.net/ont/geosparql#sfWithin) **exactly** 1 [http://linked.data.gov.au/def/geofabric#RiverRegion](http://linked.data.gov.au/def/geofabric#RiverRegion) (c)<br />
### Drainage Division
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geofabric#DrainageDivision`
Source | Page 44 in the Australian Hydrological Geospatial Fabric (Geofabric) v3.0 Product Guide
Description | <p>The Geofabric's Hydrology Reporting Region product's AWRA Drainage Division object.</p> <p>Drainage Division is defined for the purpose of providing a stable set of reporting regions specifically for the purpose of the Bureau’s Australian Water Resources Assessment (AWRA) and are referred to as the 2010 and 2012 Assessment Reporting Regions</p>
Super-classes |[https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate](https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate) (c)<br />[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />[http://linked.data.gov.au/def/geofabric#ReportingRegion](http://linked.data.gov.au/def/geofabric#ReportingRegion) (c)<br />
### Geofabric Hydrology reporting region
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geofabric#ReportingRegion`
Source | Section 5.5 Page 44 in the Australian Hydrological Geospatial Fabric (Geofabric) v3.0 Product Guide
Description | <p>Geofabric Hydrology Reporting Regions are derived from aggregations of contracted catchments from Geofabric Hydrology Reporting Catchments. This product contains two candidate reporting regions, namely AWRA Drainage Division for national scale reporting purposes and River Region for regional scale reporting purposes. More reporting regions may be added in future releases based on user requirements.</p> <p>The AWRA Drainage Division is defined for the purpose of providing a stable set of reporting regions specifically for the purpose of the Bureau’s Australian Water Resources Assessment and are referred to as the 2010 and 2012 Assessment Reporting Regions.</p> <p>The River Regions were based on a specification developed by Bureau hydrologists involved in water resources assessment in consultation with the Geofabric team and scientists from CSIRO and ANU. These boundaries were developed for use in regional scale reporting and hydrological modelling. The River Region boundaries were not used in the Australian Water Resources Assessment 2010 and 2012 but may be considered in the future as the resolution of reporting increases.</p> <p>Though the Geofabric Hydrology Reporting Regions have been developed for the purposes of the Australian Water Resources Assessment, it is envisaged that these units can be used more generally as a standard for hydrological reporting at the national and regional scale, and thus replace the Australia River Basins 1997 (http://www.ga.gov.au/metadatagateway/metadata/record/gcat_42343). Table 31 shows the Geofabric Hydrology Reporting Regions feature class terminology and feature subtypes. </p>
Super-classes |[https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate](https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate) (c)<br />[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/geofabric#DrainageDivision](http://linked.data.gov.au/def/geofabric#DrainageDivision) (c)<br />[http://linked.data.gov.au/def/geofabric#RiverRegion](http://linked.data.gov.au/def/geofabric#RiverRegion) (c)<br />
### River Region
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geofabric#RiverRegion`
Description | <p>The Geofabric's Hydrology Reporting Region product's River Region object.</p> <p>Reporting Regions are derived from aggregations of Contracted Catchments for regional scale reporting purposes.</p> <p>A River Regions is always within one and only one Drainage Division.</p>
Super-classes |[https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate](https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate) (c)<br />[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />[http://linked.data.gov.au/def/geofabric#ReportingRegion](http://linked.data.gov.au/def/geofabric#ReportingRegion) (c)<br />
Restrictions |[geosparql:sfWithin](http://www.opengis.net/ont/geosparql#sfWithin) **exactly** 1 [http://linked.data.gov.au/def/geofabric#DrainageDivision](http://linked.data.gov.au/def/geofabric#DrainageDivision) (c)<br />
### Feature
Property | Value
--- | ---
URI | `http://www.opengis.net/ont/geosparql#Feature`
Sub-classes |[http://linked.data.gov.au/def/geofabric#RiverRegion](http://linked.data.gov.au/def/geofabric#RiverRegion) (c)<br />[http://linked.data.gov.au/def/geofabric#ContractedCatchment](http://linked.data.gov.au/def/geofabric#ContractedCatchment) (c)<br />[http://linked.data.gov.au/def/geofabric#DrainageDivision](http://linked.data.gov.au/def/geofabric#DrainageDivision) (c)<br />[http://linked.data.gov.au/def/geofabric#ReportingRegion](http://linked.data.gov.au/def/geofabric#ReportingRegion) (c)<br />
### Catchment
Property | Value
--- | ---
URI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_Catchment`
Description | <p>The HY Features Ontology's generic class for a catchment</p>
Sub-classes |[http://linked.data.gov.au/def/geofabric#ContractedCatchment](http://linked.data.gov.au/def/geofabric#ContractedCatchment) (c)<br />
### Catchment Aggregate
Property | Value
--- | ---
URI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate`
Description | <p>The HY Features Ontology's generic class for an aggregation of catchments</p>
Sub-classes |[http://linked.data.gov.au/def/geofabric#DrainageDivision](http://linked.data.gov.au/def/geofabric#DrainageDivision) (c)<br />[http://linked.data.gov.au/def/geofabric#ReportingRegion](http://linked.data.gov.au/def/geofabric#ReportingRegion) (c)<br />[http://linked.data.gov.au/def/geofabric#RiverRegion](http://linked.data.gov.au/def/geofabric#RiverRegion) (c)<br />

## Annotation Properties
[source](#source),
[identifier](#identifier),
[name](#name),
[](source)
### source
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/source`
[](identifier)
### identifier
Property | Value
--- | ---
URI | `https://schema.org/identifier`
[](name)
### name
Property | Value
--- | ---
URI | `https://schema.org/name`

## Named Individuals
## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
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