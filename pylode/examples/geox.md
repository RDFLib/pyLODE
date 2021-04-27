Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# GeoSPARQL Extensions Ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/geox`
* **Publisher(s)**
  * <a href='http://catalogue.linked.data.gov.au/org/csiro'>CSIRO</a>
* **Creators(s)**
  * <a href='https://orcid.org/0000-0002-3884-3420'>Simon J D Cox, CSIRO</a>
  * <a href='https://orcid.org/0000-0002-8742-7730'>Nicholas J Car, Surround Australia</a>
* **Created**
  * 2019-01-08
* **Modified**
  * 2020-02-04
* **Version Information**
  * Alpha version
* **Version URI**
  * [http://linked.data.gov.au/def/geox/1.1](http://linked.data.gov.au/def/geox/1.1)
* **Imports**
  * [http://linked.data.gov.au/def/datatype](http://linked.data.gov.au/def/datatype)
  * [http://www.opengis.net/ont/geosparql](http://www.opengis.net/ont/geosparql)
* **Ontology RDF**
  * RDF ([geox.ttl](turtle))
* **Code Repository**
  * [https://github.com/CSIRO-enviro-informatics/geosparql-ext-ont](https://github.com/CSIRO-enviro-informatics/geosparql-ext-ont)
### Description
<p>An extension to <a href="http://www.opengeospatial.org/standards/geosparql">GeoSPARQL</a> with new features for the representation of additional elements of feature geometry, such as spatial-resolution, length, area and volume. </p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Spatial measure](#Spatialmeasure),
### Spatial measure
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#SpatialMeasure`
Description | <p>Spatial quantity computed or defined within a specified coordinate reference system</p>
Super-classes |[http://linked.data.gov.au/def/datatype/QuantitativeMeasure](http://linked.data.gov.au/def/datatype/QuantitativeMeasure) (c)<br />
Restrictions |[http://linked.data.gov.au/def/geox#inCRS](http://linked.data.gov.au/def/geox#inCRS) (op) **exactly** 1<br />
In domain of |[http://linked.data.gov.au/def/geox#inCRS](http://linked.data.gov.au/def/geox#inCRS) (op)<br />
In range of |[http://linked.data.gov.au/def/geox#hasVolume](http://linked.data.gov.au/def/geox#hasVolume) (op)<br />[http://linked.data.gov.au/def/geox#hasLength](http://linked.data.gov.au/def/geox#hasLength) (op)<br />[http://linked.data.gov.au/def/geox#hasArea](http://linked.data.gov.au/def/geox#hasArea) (op)<br />

## Object Properties
[has area](#hasarea),
[has area in m2](#hasareainm2),
[has length](#haslength),
[has length in m](#haslengthinm),
[has spatial resolution](#hasspatialresolution),
[has spatial resolution in metres](#hasspatialresolutioninmetres),
[has volume](#hasvolume),
[has volume in m3](#hasvolumeinm3),
[In Coordinate Reference System](#InCoordinateReferenceSystem),
[is geometry of](#isgeometryof),
[](hasarea)
### has area
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasArea`
Description | The area of a spatial object, expressed as a scaled number
Example | ````my:plot456`<br />`  :hasArea [`<br />`    data:uncertainty 0.5 ;`<br />`    data:unit <http://qudt.org/vocab/unit/M2> ;`<br />`    data:value 63.9 ;`<br />`  ] ;`<br />`.`<br />```
Domain(s) |[geosparql:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Range(s) |[http://linked.data.gov.au/def/geox#SpatialMeasure](http://linked.data.gov.au/def/geox#SpatialMeasure) (c)<br />
[](hasareainm2)
### has area in m2
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasAreaM2`
Description | The area of the spatial object in m^2
Example | ````my:plot456`<br />`  :hasAreaM2 [`<br />`    data:value 63.9 ;`<br />`  ] ;`<br />`.`<br />```
Super-properties |[http://linked.data.gov.au/def/geox#hasArea](http://linked.data.gov.au/def/geox#hasArea) (op)<br />
[](haslength)
### has length
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasLength`
Description | The length of a spatial object, expressed as a scaled number
Example | ````my:road456`<br />`  :hasLength [`<br />`    data:uncertainty 5.0 ;`<br />`    data:unit <http://qudt.org/vocab/unit/M> ;`<br />`    data:value 234.0 ;`<br />`  ] ;`<br />`.`<br />```
Domain(s) |[geosparql:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Range(s) |[http://linked.data.gov.au/def/geox#SpatialMeasure](http://linked.data.gov.au/def/geox#SpatialMeasure) (c)<br />
[](haslengthinm)
### has length in m
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasLengthM`
Description | The length of a spatial object in metres
Example | ````my:road456`<br />`  :hasLengthM [`<br />`    data:value 234.0 ;`<br />`  ] ;`<br />`.`<br />```
Super-properties |[http://linked.data.gov.au/def/geox#hasLength](http://linked.data.gov.au/def/geox#hasLength) (op)<br />
[](hasspatialresolution)
### has spatial resolution
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasResolution`
Description | The spatial resolution of the Geometry object, expressed as a linear measurement.
Example | ````my:image456`<br />`  :hasResolution [`<br />`    data:unit <http://qudt.org/vocab/unit/M> ;`<br />`    data:value 30.0 ;`<br />`  ] ;`<br />`.`<br />```
Domain(s) |[geosparql:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
Range(s) |[http://linked.data.gov.au/def/datatype/QuantitativeMeasure](http://linked.data.gov.au/def/datatype/QuantitativeMeasure) (c)<br />
[](hasspatialresolutioninmetres)
### has spatial resolution in metres
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasResolutionM`
Description | The spatial resolution of the Geometry object, expressed as a linear distance in metres
Example | ````my:image456`<br />`  :hasResolutionM [`<br />`    data:value 30.0 ;`<br />`  ] ;`<br />`.`<br />```
Super-properties |[http://linked.data.gov.au/def/geox#hasResolution](http://linked.data.gov.au/def/geox#hasResolution) (op)<br />
Domain(s) |[geosparql:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
[](hasvolume)
### has volume
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasVolume`
Description | The volume of a spatial object, expressed as a scaled number
Example | ````my:swimmingPool99`<br />`  :hasVolume [`<br />`    data:unit <http://qudt.org/vocab/unit/M3> ;`<br />`    data:value 3050.0 ;`<br />`  ] ;`<br />`.`<br />```
Domain(s) |[geosparql:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Range(s) |[http://linked.data.gov.au/def/geox#SpatialMeasure](http://linked.data.gov.au/def/geox#SpatialMeasure) (c)<br />
[](hasvolumeinm3)
### has volume in m3
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#hasVolumeM3`
Description | The volume of a spatial object in cubic-metres
Example | ````my:swimmingPool99`<br />`  :hasVolumeM3 [`<br />`    data:value 3050.0 ;`<br />`  ] ;`<br />`.`<br />```
Super-properties |[http://linked.data.gov.au/def/geox#hasVolume](http://linked.data.gov.au/def/geox#hasVolume) (op)<br />
[](InCoordinateReferenceSystem)
### In Coordinate Reference System
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#inCRS`
Description | The measure is defined or computed using this CRS.  The CRS should be denoted by a URI Reference to a CRS definition, e.g. https://www.opengis.net/def/crs/EPSG/0/4326
Domain(s) |[http://linked.data.gov.au/def/geox#SpatialMeasure](http://linked.data.gov.au/def/geox#SpatialMeasure) (c)<br />
[](isgeometryof)
### is geometry of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/geox#isGeometryOf`
Description | link from a geometry object to the feature(s) for which it is a geometry
Domain(s) |[geosparql:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
Range(s) |[geosparql:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />

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