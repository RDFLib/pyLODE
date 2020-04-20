# GeoSPARQL Extensions Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/geox`
* **Publisher(s)**
  * <a href='http://catalogue.linked.data.gov.au/org/csiro'>CSIRO</a>
* **Creators(s)**
  * <a href='https://orcid.org/0000-0002-8742-7730'>Nicholas J Car, Surround Australia</a>
  * <a href='https://orcid.org/0000-0002-3884-3420'>Simon J D Cox, CSIRO</a>
* **Created**
  * 2019-01-08
* **Modified**
  * 2020-02-04
* **Version Information**
  * Alpha version
* **Version IRI**
  * [http://linked.data.gov.au/def/geox/1.1](http://linked.data.gov.au/def/geox/1.1)
* **Imports**
  * [http://linked.data.gov.au/def/datatype](http://linked.data.gov.au/def/datatype)
  * [http://www.opengis.net/ont/geosparql](http://www.opengis.net/ont/geosparql)
* **Ontology RDF**
  * RDF ([geox.ttl](turtle))
* **Code Repository**
  * <[https://github.com/CSIRO-enviro-informatics/geosparql-ext-ont](https://github.com/CSIRO-enviro-informatics/geosparql-ext-ont)>
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
IRI | `http://linked.data.gov.au/def/geox#SpatialMeasure`
Description | <p>Spatial quantity computed or defined within a specified coordinate reference system</p>
Super-classes |[data:QuantitativeMeasure](http://linked.data.gov.au/def/datatype/QuantitativeMeasure) (c)<br />
Restrictions |[geox:inCRS](InCoordinateReferenceSystem) (op) **exactly** 1<br />
In domain of |[geox:inCRS](InCoordinateReferenceSystem) (op)<br />
In range of |[geox:hasLength](haslength) (op)<br />[geox:hasVolume](hasvolume) (op)<br />[geox:hasArea](hasarea) (op)<br />

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
IRI | `http://linked.data.gov.au/def/geox#hasArea`
Example | <pre>my:plot456<br />  :hasArea [<br />    data:uncertainty 0.5 ;<br />    data:unit &lt;http://qudt.org/vocab/unit/M2> ;<br />    data:value 63.9 ;<br />  ] ;<br />.</pre>
Domain(s) |[geo:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Range(s) |[geox:SpatialMeasure](Spatialmeasure) (c)<br />
[](hasareainm2)
### has area in m2
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#hasAreaM2`
Example | <pre>my:plot456<br />  :hasAreaM2 [<br />    data:value 63.9 ;<br />  ] ;<br />.</pre>
Super-properties |[geox:hasArea](hasarea) (op)<br />
[](haslength)
### has length
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#hasLength`
Example | <pre>my:road456<br />  :hasLength [<br />    data:uncertainty 5.0 ;<br />    data:unit &lt;http://qudt.org/vocab/unit/M> ;<br />    data:value 234.0 ;<br />  ] ;<br />.</pre>
Domain(s) |[geo:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Range(s) |[geox:SpatialMeasure](Spatialmeasure) (c)<br />
[](haslengthinm)
### has length in m
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#hasLengthM`
Example | <pre>my:road456<br />  :hasLengthM [<br />    data:value 234.0 ;<br />  ] ;<br />.</pre>
Super-properties |[geox:hasLength](haslength) (op)<br />
[](hasspatialresolution)
### has spatial resolution
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#hasResolution`
Example | <pre>my:image456<br />  :hasResolution [<br />    data:unit &lt;http://qudt.org/vocab/unit/M> ;<br />    data:value 30.0 ;<br />  ] ;<br />.</pre>
Domain(s) |[geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
Range(s) |[data:QuantitativeMeasure](http://linked.data.gov.au/def/datatype/QuantitativeMeasure) (c)<br />
[](hasspatialresolutioninmetres)
### has spatial resolution in metres
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#hasResolutionM`
Example | <pre>my:image456<br />  :hasResolutionM [<br />    data:value 30.0 ;<br />  ] ;<br />.</pre>
Super-properties |[geox:hasResolution](hasspatialresolution) (op)<br />
Domain(s) |[geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
[](hasvolume)
### has volume
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#hasVolume`
Example | <pre>my:swimmingPool99<br />  :hasVolume [<br />    data:unit &lt;http://qudt.org/vocab/unit/M3> ;<br />    data:value 3050.0 ;<br />  ] ;<br />.</pre>
Domain(s) |[geo:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject) (c)<br />
Range(s) |[geox:SpatialMeasure](Spatialmeasure) (c)<br />
[](hasvolumeinm3)
### has volume in m3
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#hasVolumeM3`
Example | <pre>my:swimmingPool99<br />  :hasVolumeM3 [<br />    data:value 3050.0 ;<br />  ] ;<br />.</pre>
Super-properties |[geox:hasVolume](hasvolume) (op)<br />
[](InCoordinateReferenceSystem)
### In Coordinate Reference System
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#inCRS`
Domain(s) |[geox:SpatialMeasure](Spatialmeasure) (c)<br />
[](isgeometryof)
### is geometry of
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/geox#isGeometryOf`
Domain(s) |[geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
Range(s) |[geo:Feature](http://www.opengis.net/ont/geosparql#Feature) (c)<br />

## Named Individuals
## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/geox#`
* **data**
  * `http://linked.data.gov.au/def/datatype/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dcterms**
  * `http://purl.org/dc/terms/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
* **geo**
  * `http://www.opengis.net/ont/geosparql#`
* **geox**
  * `http://linked.data.gov.au/def/geox#`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
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