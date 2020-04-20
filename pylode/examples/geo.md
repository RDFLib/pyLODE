# GeoSPARQL Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://www.opengis.net/ont/geosparql`
* **Creators(s)**
  * Open Geospatial Consortium
* **Version Information**
  * OGC GeoSPARQL 1.0
* **Ontology RDF**
  * RDF ([geo.ttl](turtle))
### Description
<p>An RDF/OWL vocabulary for representing spatial information</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Feature](#Feature),
[Geometry](#Geometry),
[SpatialObject](#SpatialObject),
### Feature
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#Feature`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | <pre><code>  This class represents the top-level feature type. This class is
  equivalent to GFI_Feature defined in ISO 19156:2011, and it is
  superclass of all feature types.
</code></pre>
Super-classes |[SpatialObject](SpatialObject) (c)<br />
In domain of |[defaultGeometry](defaultGeometry) (op)<br />[hasGeometry](hasGeometry) (op)<br />
### Geometry
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#Geometry`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | <pre><code>  The class represents the top-level geometry type. This class is
  equivalent to the UML class GM_Object defined in ISO 19107, and
  it is superclass of all geometry types.
</code></pre>
Super-classes |[SpatialObject](SpatialObject) (c)<br />
In domain of |[asGML](asGML) (dp)<br />[asWKT](asWKT) (dp)<br />[coordinateDimension](coordinateDimension) (dp)<br />[hasSerialization](hasserialization) (dp)<br />[isSimple](isSimple) (dp)<br />[spatialDimension](spatialDimension) (dp)<br />[dimension](dimension) (dp)<br />[isEmpty](isEmpty) (dp)<br />
In range of |[defaultGeometry](defaultGeometry) (op)<br />[hasGeometry](hasGeometry) (op)<br />
### SpatialObject
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#SpatialObject`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | <pre><code>  The class spatial-object represents everything that can have
  a spatial representation. It is superclass of feature and geometry.
</code></pre>
Sub-classes |[Feature](Feature) (c)<br />[Geometry](Geometry) (c)<br />
In domain of |[ehOverlap](overlap) (op)<br />[ehInside](inside) (op)<br />[rcc8dc](disconnected) (op)<br />[sfEquals](sfEquals) (op)<br />[rcc8tpp](tangentialproperpart) (op)<br />[sfWithin](within) (op)<br />[ehDisjoint](disjoint) (op)<br />[sfCrosses](crosses) (op)<br />[rcc8po](partiallyoverlapping) (op)<br />[ehCovers](covers) (op)<br />[ehMeet](meet) (op)<br />[rcc8tppi](tangentialproperpartinverse) (op)<br />[rcc8ntppi](non-tangentialproperpartinverse) (op)<br />[sfDisjoint](sfDisjoint) (op)<br />[rcc8eq](rcc8eq) (op)<br />[sfTouches](touches) (op)<br />[rcc8ec](externallyconnected) (op)<br />[ehContains](contains) (op)<br />[sfOverlaps](overlaps) (op)<br />[rcc8ntpp](non-tangentialproperpart) (op)<br />[ehEquals](equals) (op)<br />[sfContains](sfContains) (op)<br />[sfIntersects](intersects) (op)<br />[ehCoveredBy](coveredBy) (op)<br />
In range of |[sfOverlaps](overlaps) (op)<br />[ehContains](contains) (op)<br />[rcc8tpp](tangentialproperpart) (op)<br />[rcc8ec](externallyconnected) (op)<br />[sfTouches](touches) (op)<br />[ehInside](inside) (op)<br />[ehOverlap](overlap) (op)<br />[ehCoveredBy](coveredBy) (op)<br />[sfIntersects](intersects) (op)<br />[ehEquals](equals) (op)<br />[rcc8po](partiallyoverlapping) (op)<br />[sfCrosses](crosses) (op)<br />[rcc8eq](rcc8eq) (op)<br />[ehDisjoint](disjoint) (op)<br />[sfWithin](within) (op)<br />[sfEquals](sfEquals) (op)<br />[rcc8dc](disconnected) (op)<br />[sfDisjoint](sfDisjoint) (op)<br />[rcc8ntppi](non-tangentialproperpartinverse) (op)<br />[rcc8tppi](tangentialproperpartinverse) (op)<br />[ehMeet](meet) (op)<br />[ehCovers](covers) (op)<br />[sfContains](sfContains) (op)<br />[rcc8ntpp](non-tangentialproperpart) (op)<br />

## Object Properties
[defaultGeometry](#defaultGeometry),
[contains](#contains),
[coveredBy](#coveredBy),
[covers](#covers),
[disjoint](#disjoint),
[equals](#equals),
[inside](#inside),
[meet](#meet),
[overlap](#overlap),
[hasGeometry](#hasGeometry),
[disconnected](#disconnected),
[externally connected](#externallyconnected),
[equals](#rcc8eq),
[non-tangential proper part](#non-tangentialproperpart),
[non-tangential proper part inverse](#non-tangentialproperpartinverse),
[partially overlapping](#partiallyoverlapping),
[tangential proper part](#tangentialproperpart),
[tangential proper part inverse](#tangentialproperpartinverse),
[contains](#sfContains),
[crosses](#crosses),
[disjoint](#sfDisjoint),
[equals](#sfEquals),
[intersects](#intersects),
[overlaps](#overlaps),
[touches](#touches),
[within](#within),
[](defaultGeometry)
### defaultGeometry
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#defaultGeometry`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      The default geometry to be used in spatial calculations.
      It is Usually the most detailed geometry.
    
Super-properties |[hasGeometry](hasGeometry) (op)<br />
Domain(s) |[Feature](Feature) (c)<br />
Range(s) |[Geometry](Geometry) (c)<br />
[](contains)
### contains
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehContains`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially contains the
      object SpatialObject. DE-9IM: T*TFF*FF*
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](coveredBy)
### coveredBy
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehCoveredBy`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject is spatially covered
      by the object SpatialObject. DE-9IM: TFF*TFT**
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](covers)
### covers
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehCovers`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject spatially covers the
      object SpatialObject. DE-9IM: T*TFT*FF*
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](disjoint)
### disjoint
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehDisjoint`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject is spatially disjoint
      from the object SpatialObject. DE-9IM: FF*FF****
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](equals)
### equals
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehEquals`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially equals the
      object SpatialObject. DE-9IM: TFFFTFFFT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](inside)
### inside
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehInside`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject is spatially inside
      the object SpatialObject. DE-9IM: TFF*FFT**
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](meet)
### meet
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehMeet`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject spatially meets the
      object SpatialObject.
      DE-9IM: FT******* ^ F**T***** ^ F***T****
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](overlap)
### overlap
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#ehOverlap`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject spatially overlaps the
      object SpatialObject. DE-9IM: T*T***T**
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](hasGeometry)
### hasGeometry
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#hasGeometry`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      A spatial representation for a given feature.
    
Domain(s) |[Feature](Feature) (c)<br />
Range(s) |[Geometry](Geometry) (c)<br />
[](disconnected)
### disconnected
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8dc`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject is spatially disjoint
      from the object SpatialObject. DE-9IM: FFTFFTTTT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](externallyconnected)
### externally connected
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8ec`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially meets the
      object SpatialObject. DE-9IM: FFTFTTTTT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](rcc8eq)
### equals
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8eq`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially equals the
      object SpatialObject. DE-9IM: TFFFTFFFT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](non-tangentialproperpart)
### non-tangential proper part
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8ntpp`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject is spatially inside
      the object SpatialObject. DE-9IM: TFFTFFTTT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](non-tangentialproperpartinverse)
### non-tangential proper part inverse
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8ntppi`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially contains the
      object SpatialObject. DE-9IM: TTTFFTFFT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](partiallyoverlapping)
### partially overlapping
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8po`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject spatially overlaps the
      object SpatialObject. DE-9IM: TTTTTTTTT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](tangentialproperpart)
### tangential proper part
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8tpp`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject is spatially covered
      by the object SpatialObject. DE-9IM: TFFTTFTTT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](tangentialproperpartinverse)
### tangential proper part inverse
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#rcc8tppi`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially covers the
      object SpatialObject. DE-9IM: TTTFTTFFT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](sfContains)
### contains
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfContains`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject spatially contains the
      object SpatialObject. DE-9IM: T*****FF*
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](crosses)
### crosses
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfCrosses`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially crosses the
      object SpatialObject. DE-9IM: T*T******
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](sfDisjoint)
### disjoint
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfDisjoint`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject is spatially disjoint
      from the object SpatialObject. DE-9IM: FF*FF****
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](sfEquals)
### equals
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfEquals`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject spatially equals the
      object SpatialObject. DE-9IM: TFFFTFFFT
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](intersects)
### intersects
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfIntersects`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject is not spatially disjoint
      from the object SpatialObject.
      DE-9IM: T******** ^ *T******* ^ ***T***** ^ ****T****
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](overlaps)
### overlaps
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfOverlaps`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially overlaps the
      object SpatialObject. DE-9IM: T*T***T**
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](touches)
### touches
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfTouches`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      Exists if the subject SpatialObject spatially touches the
      object SpatialObject.
      DE-9IM: FT******* ^ F**T***** ^ F***T****
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />
[](within)
### within
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#sfWithin`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Exists if the subject SpatialObject is spatially within the
      object SpatialObject. DE-9IM: T*F**F***
    
Domain(s) |[SpatialObject](SpatialObject) (c)<br />
Range(s) |[SpatialObject](SpatialObject) (c)<br />

## Datatype Properties
[asGML](#asGML),
[asWKT](#asWKT),
[coordinateDimension](#coordinateDimension),
[dimension](#dimension),
[has serialization](#hasserialization),
[isEmpty](#isEmpty),
[isSimple](#isSimple),
[spatialDimension](#spatialDimension),
[](asGML)
### asGML
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#asGML`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      The GML serialization of a geometry
    
Super-properties |[hasSerialization](hasserialization) (dp)<br />
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[gmlLiteral](http://www.opengis.net/ont/geosparql#gmlLiteral) (c)<br />
[](asWKT)
### asWKT
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#asWKT`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      The WKT serialization of a geometry
    
Super-properties |[hasSerialization](hasserialization) (dp)<br />
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[wktLiteral](http://www.opengis.net/ont/geosparql#wktLiteral) (c)<br />
[](coordinateDimension)
### coordinateDimension
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#coordinateDimension`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      The number of measurements or axes needed to describe the position of this
      geometry in a coordinate system.
    
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](dimension)
### dimension
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#dimension`
Is Defined By | http://www.opengis.net/ont/geosparql
Description | 
      The topological dimension of this geometric object, which
      must be less than or equal to the coordinate dimension.
      In non-homogeneous collections, this will return the largest
      topological dimension of the contained objects.
    
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />
[](hasserialization)
### has serialization
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#hasSerialization`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      Connects a geometry object with its text-based serialization.
    
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](isEmpty)
### isEmpty
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#isEmpty`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      (true) if this geometric object is the empty Geometry. If
      true, then this geometric object represents the empty point
      set for the coordinate space.
    
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />
[](isSimple)
### isSimple
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#isSimple`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      (true) if this geometric object has no anomalous geometric
      points, such as self intersection or self tangency.
    
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />
[](spatialDimension)
### spatialDimension
Property | Value
--- | ---
IRI | `http://www.opengis.net/ont/geosparql#spatialDimension`
Is Defined By | http://www.opengis.net/spec/geosparql/1.0
Description | 
      The number of measurements or axes needed to describe the spatial position of
      this geometry in a coordinate system.
    
Domain(s) |[Geometry](Geometry) (c)<br />
Range(s) |[xsd:integer](http://www.w3.org/2001/XMLSchema#integer) (c)<br />

## Annotation Properties
[Contributor](#Contributor),
[Creator](#Creator),
[Date](#Date),
[Description](#Description),
[description](#description),
[hasVersion](#hasVersion),
[issued](#issued),
[modified](#modified),
[publisher](#publisher),
[title](#title),
[definition](#definition),
[note](#note),
[prefLabel](#prefLabel),
[](Contributor)
### Contributor
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/contributor`
Is Defined By | http://purl.org/dc/elements/1.1/
Description | An entity responsible for making contributions to the resource.
[](Creator)
### Creator
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/creator`
Is Defined By | http://purl.org/dc/elements/1.1/
Description | An entity primarily responsible for making the resource.
[](Date)
### Date
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/date`
Is Defined By | http://purl.org/dc/elements/1.1/
Description | A point or period of time associated with an event in the lifecycle of the resource.
[](Description)
### Description
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/description`
Is Defined By | http://purl.org/dc/elements/1.1/
Description | An account of the resource.
[](description)
### description
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/description`
[](hasVersion)
### hasVersion
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/hasVersion`
[](issued)
### issued
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/issued`
[](modified)
### modified
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/modified`
[](publisher)
### publisher
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/publisher`
[](title)
### title
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/title`
[](definition)
### definition
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#definition`
[](note)
### note
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#note`
[](prefLabel)
### prefLabel
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#prefLabel`

## Named Individuals
## Namespaces
* **default (:)**
  * `http://www.opengis.net/ont/geosparql#`
* **:**
  * `http://www.opengis.net/ont/geosparql#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
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