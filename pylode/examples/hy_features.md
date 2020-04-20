# HY Features Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `https://www.opengis.net/def/appschema/hy_features/hyf`
* **Imports**
  * [http://www.opengis.net/ont/geosparql](http://www.opengis.net/ont/geosparql)
  * [http://shapechange.net/resources/ont/base](http://shapechange.net/resources/ont/base)
  * [http://eelst.cs.unibo.it/apps/LODE/source?url=http://def.seegrid.csiro.au/isotc211/iso19115/2003/metadata.ttl](http://eelst.cs.unibo.it/apps/LODE/source?url=http://def.seegrid.csiro.au/isotc211/iso19115/2003/metadata.ttl)
* **Ontology RDF**
  * RDF ([hy_features.ttl](turtle))
### Description
<p>The HydroFeature module (Figure 21) provides the core concepts of a named hydrologic feature in the Named Feature, of a hydrologic complex in which the union of catchment and its common outlet is realized in several ways by a collection of hydrologic features, and of a river referencing system which allows placement of an arbitrary feature ‘along a river’ using linear referencing along a one-dimensional topological, flowpath realization. The HY_HydroFeature feature type is defined as hydrology-specific instance of the General Feature metaclass (as defined in the OGC General Feature Model, GFM), whose identity needs to be maintained and tracked through a processing chain from measurement to distribution of hydrologic information.As an instance of the General Feature metaclass a feature type is identified by a unique identifier and typical properties. Typically, a hydrologic feature is additionally identified through names in common usage and through hydrologically significant characteristics. The HY_HydroFeature feature type is specialized into more specific feature types (Figure 23), which specify additional properties and represent particular hydrologic phenomena.Providing a standard terminology for the typical relationships between hydrologic features allows the hydrosphere to be expressed in a consistent way across multiple data products, regardless of various spatial or temporal representations.The definitions of HydroFeature feature types are rooted in the definitions documented in the WMO/UNESCO Glossary of Hydrology. They are applied regardless of their application context in respect to the Earth's surface. For the purpose of testing the applicability of the HY_Features conceptual model in the context of surface water hydrology, the definitions in this standard refer to surface water hydrology. A conceptual model capturing the specifics of features associated with the groundwater domain is developed with reference to the OGC WaterML 2: Part 4 – GroundwaterML2 standard.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[HY_CartographicRealization](#HY_CartographicRealization),
[HY_Catchment](#HY_Catchment),
[HY_CatchmentAggregate](#HY_CatchmentAggregate),
[HY_CatchmentArea](#HY_CatchmentArea),
[HY_CatchmentDivide](#HY_CatchmentDivide),
[HY_CatchmentRealization](#HY_CatchmentRealization),
[HY_DendriticCatchment](#HY_DendriticCatchment),
[HY_DistanceDescription](#HY_DistanceDescription),
[HY_DistanceFromReferent](#HY_DistanceFromReferent),
[HY_FlowPath](#HY_FlowPath),
[HY_HydroFeature](#HY_HydroFeature),
[HY_HydroFeatureName](#HY_HydroFeatureName),
[HY_HydroLocationType](#HY_HydroLocationType),
[HY_HydroNetwork](#HY_HydroNetwork),
[HY_HydroNexus](#HY_HydroNexus),
[HY_IndirectPosition](#HY_IndirectPosition),
[HY_InteriorCatchment](#HY_InteriorCatchment),
[HY_NameUsage](#HY_NameUsage),
[ReferenceLocation](#ReferenceLocation),
### HY_CartographicRealization
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CartographicRealization`
Description | <p>The HY_CartographicRealization feature type realizes a catchment as set of separate cartographic layers or maps, displaying a network of hydrologic features which may be connected at the representation level, or not. Specializing HY_CatchmentRealization, it inherits from generalization the shape attribute and the realizedCatchment association.</p>
Super-classes |[hyf:HY_CatchmentRealization](HY_CatchmentRealization) (c)<br />
### HY_Catchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_Catchment`
Description | <p>The Catchment model conceptualizes the hydrologic determination of a catchment through inflow and outflow hydro nexus features with the role of getting flow from a contributing catchment, or providing inflow to a receiving catchment (Figure 25 and Figure 26). Conceptually, each catchment has an outflow hydro nexus, and any hydro nexus has a corresponding catchment, even if catchment and/or hydro nexus may not be present in a particular application. A catchment interacts with upper and lower catchments via associated hydro nexuses, and ultimately contributes flow to the hydro nexus of a containing catchment. The catchment should be understood as the logical link between two hydro nexuses.The HY_Catchment feature type captures the union of catchment and hydro nexus, and the multiple realizations of the holistic catchment concept. These realizations include both topological realizations, as well as their geometric representation. HY_Catchment may be further specialized with respect to catchment interaction. The HY_Catchment feature type (Figure 26) specializes the general HY_HydroFeature type. Through generalization, HY_Catchment inherits the name property. It carries a code attribute and the associations: outflow, inflow, containingCatchment, containedCatchment, conjointCatchment, upperCatchment, lowerCatchment, catchmentRealization.</p>
Super-classes |[hyf:HY_HydroFeature](HY_HydroFeature) (c)<br />
Restrictions |[hyf:upperCatchment](upperCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />[hyf:catchmentRealization](catchmentRealization) (op) **only** [hyf:HY_CatchmentRealization](HY_CatchmentRealization) (c)<br />[hyf:containedCatchment](containedCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />[hyf:containingCatchment](containingCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />[hyf:outflow](outflow) (op) **only** [hyf:HY_HydroNexus](HY_HydroNexus) (c)<br />[hyf:lowerCatchment](lowerCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />[hyf:code](code) (op) **only** [rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />[hyf:inflow](inflow) (op) **only** [hyf:HY_HydroNexus](HY_HydroNexus) (c)<br />[hyf:conjointCatchment](conjointCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />
Sub-classes |[hyf:HY_DendriticCatchment](HY_DendriticCatchment) (c)<br />[hyf:HY_CatchmentAggregate](HY_CatchmentAggregate) (c)<br />[hyf:HY_InteriorCatchment](HY_InteriorCatchment) (c)<br />
In range of |[hyf:lowerCatchment](lowerCatchment) (op)<br />[hyf:contributingCatchment](contributingCatchment) (op)<br />[hyf:conjointCatchment](conjointCatchment) (op)<br />[hyf:containingCatchment](containingCatchment) (op)<br />[hyf:upperCatchment](upperCatchment) (op)<br />[hyf:receivingCatchment](receivingCatchment) (op)<br />[hyf:realizedCatchment](realizedCatchment) (op)<br />[hyf:containedCatchment](containedCatchment) (op)<br />
### HY_CatchmentAggregate
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate`
Description | <p>The HY_CatchmentAggregate feature type (Figure 30) specializes the HY_Catchment type as a set of non-overlapping dendritic and interior catchments arranged in an encompassing catchment. This can be used to describe multiple inflows into a catchment aggregate through several hydrologically discrete sub-catchments each with a single inflow, and contributing to a joined outflow of the catchment aggregate, including the 'nillable' outflow of interior catchments. Nillable is meant here to signify that the hydro nexus logically exists in the form of flow to the subsurface or atmosphere but is unknown in a given implementation. Being a special type of the HY_Catchment, the catchment aggregate may be part of a containing catchment at the next higher level of hierarchy, which consists of similar-scale neighboring catchments. The catchment aggregate does not necessarily imply a series of nested containing catchments. It primarily allows navigation to the 'highest' level system (total drainage basin) as typically used for reporting purposes.HY_CatchmentAggregate inherits through generalization the outflow, inflow, containingCatchment, containedCatchment, conjointCatchment, upperCatchment, lowerCatchment, and catchmentRealization properties, and has exorheicDrainage and endorheicDrainage associations.</p>
Super-classes |[hyf:HY_Catchment](HY_Catchment) (c)<br />
Restrictions |[hyf:endorheicDrainage](endorheicDrainage) (op) **only** [hyf:HY_InteriorCatchment](HY_InteriorCatchment) (c)<br />[hyf:exorheicDrainage](exorheicDrainage) (op) **only** [hyf:HY_DendriticCatchment](HY_DendriticCatchment) (c)<br />
### HY_CatchmentArea
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentArea`
Description | <p>The HY_CatchmentArea feature type realizes a catchment specifically as a catchment area connecting the inflow and outflow of the catchment it realizes. HY_CatchmentArea specializes HY_CatchmentRealization with respect to an implied areal geometric representation. Topologically, the catchment area connecting the inflow and outflow of the catchment is a face bounded inwards by an inflow edge and outwards by an outflow edge. Hydrologically, catchment area refers to the area having a common outlet for its runoff. Through generalization, HY_CatchmentArea inherits the shape and the realizedCatchment properties. The optional shape of the catchment may be implemented as a surface.</p>
Super-classes |[hyf:HY_CatchmentRealization](HY_CatchmentRealization) (c)<br />
In range of |[hyf:catchmentArea](catchmentArea) (op)<br />
### HY_CatchmentDivide
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentDivide`
Description | <p>The HY_CatchmentDivide feature type realizes a catchment specifically as catchment boundary connecting the inflow and outflow of the catchment it realizes, whereby inflow and outflow may overlay.Implying a linear geometric representation, a catchment boundary is topologically understood as an edge bounded by inflow node and outflow nodes, and corresponding to left-bank and right-bank catchment faces inside of the boundary. Hydrologically, the boundary refers to the summit line separating adjacent catchments. Through generalization, HY_CatchmentDivide inherits the shape and the realizedCatchment properties. The shape of the catchment divide may be implemented as a composition of succeeding curves or a polygon ring.</p>
Super-classes |[hyf:HY_CatchmentRealization](HY_CatchmentRealization) (c)<br />
In range of |[hyf:catchmentDivide](catchmentDivide) (op)<br />
### HY_CatchmentRealization
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentRealization`
Description | <p>The HY_CatchmentRealization feature type (Figure 34) is based on the idea that there are multiple hydrology-specific perspectives of the holistic catchment concept that are used to describe a catchment as a unit of study shared across sub-domains and studies. A given catchment realization exists within a hydrologic complex in that, if a catchment realization exists, it exists in the same hydrologic complex as the catchment it realizes. In this way, any realization of a catchment has the same hydrologic determination of the catchment it realizes. If a catchment is connected with other catchments via inflow and/or outflow hydro nexuses, its realizations are also connected. A realization of the logical catchment is always of higher topological dimension than the realization of the corresponding hydro nexus topological boundary. For example, a linear flowpath realizing a catchment may be understood as an edge between inflow and outflow nodes; the areal realization of a catchment as a face bounded by linear inflow and outflow.The catchment realization features defined in this standard refer to objects on the land surface for the purpose of surface water hydrology. In other contexts, other types of catchment realization may exist. Catchment realizations that do not conform to those defined in this standard, for instance realizations in 3- or 4-dimensional perspectives, may be implemented using the general HY_CatchmentRealization type. HY_CatchmentRealization carries a shape attribute and as a realizedCatchment association.</p>
Restrictions |[hyf:realizedCatchment](realizedCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />[gsp:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) **only** [gsp:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />
Sub-classes |[hyf:HY_CatchmentArea](HY_CatchmentArea) (c)<br />[hyf:HY_CatchmentDivide](HY_CatchmentDivide) (c)<br />[hyf:HY_HydroNetwork](HY_HydroNetwork) (c)<br />[hyf:HY_FlowPath](HY_FlowPath) (c)<br />[hyf:HY_CartographicRealization](HY_CartographicRealization) (c)<br />
In range of |[hyf:catchmentRealization](catchmentRealization) (op)<br />
### HY_DendriticCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_DendriticCatchment`
Description | <p>The HY_DendriticCatchment feature type (Figure 31) specializes the general HY_Catchment class as a catchment which is determined by a single common downstream catchment. It represents the catchment as the topological link between an inflow and an outflow. This allows catchments to be connected in a dendritic network by upstream-downstream relationships without knowing the complex hydrology between inflow and outflow. This concept requires a stable identifier purposefully assigned to the catchment and that catchments are delineated as a simple tree hierarchy. HY_DendriticCatchment inherits from generalization the code, outflow, inflow, containingCatchment, containedCatchment, conjointCatchment, upperCatchment, lowerCatchment, and catchmentRealization properties, and has an encompassingCatchment association. The dendritic nature of this feature is enforced through single-outflow, single-receiving-catchment and single-lower-catchment constraints.</p>
Super-classes |[hyf:HY_Catchment](HY_Catchment) (c)<br />
In range of |[hyf:exorheicDrainage](exorheicDrainage) (op)<br />
### HY_DistanceDescription
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_DistanceDescription`
Description | <p>list of general terms commonly used in hydrology to describe a spatial relationship between two locations.If required, an implementation should use terms from this code list, defined specifically to conform to a terminology common in the hydrology domain. Note that alternative code lists may be used but should be related to the terms in but should be related to the terms in this code list using an appropriate formalism.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[hyf:distanceDescription](distanceDescription) (op)<br />
### HY_DistanceFromReferent
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_DistanceFromReferent`
Description | <p>The HY_DistanceFromReferent data type provides the distance from a located referent as an absolute or interpolative value, including simple statements on accuracy and precision of the measured position.</p>
Restrictions |[hyf:interpolative](interpolative) (dp) **only** [xsd:double](http://www.w3.org/2001/XMLSchema#double) (c)<br />[hyf:precisionStatement](precisionStatement) (dp) **only** [sc:Measure](http://shapechange.net/resources/ont/base#Measure) (c)<br />[hyf:absolute](absolute) (dp) **only** [sc:Measure](http://shapechange.net/resources/ont/base#Measure) (c)<br />[hyf:accuracyStatement](accuracyStatement) (dp) **only** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
In range of |[hyf:distanceExpression](distanceExpression) (op)<br />
### HY_FlowPath
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_FlowPath`
Description | <p>The HY_Flowpath feature type realizes a catchment specifically as a path connecting the inflow and outflow of the catchment it realizes.HY_Flowpath specializes HY_CatchmentRealization with respect to an implied linear geometric representation including a straight or curved line. Topologically, the flowpath connects the inflow and outflow of the catchment, and is understood as an edge bounded by an inflow node and an outflow node, and corresponding to left-bank and right-bank catchment faces. Hydrologically, the flowpath is a line describing a moving particle of water. Through generalization, HY_Flowpath inherits the shape and the realizedCatchment properties. The optional shape of the flowpath is usually a single curve.</p>
Super-classes |[hyf:HY_CatchmentRealization](HY_CatchmentRealization) (c)<br />
In range of |[hyf:flowpath](flowpath) (op)<br />[hyf:linearElement](linearElement) (op)<br />
### HY_HydroFeature
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeature`
Description | <p>basic feature to reflect the properties that all hydrologic features have.</p>
Restrictions |[hyf:HY_HydroFeature.name](HY_HydroFeature.name) (op) **only** [hyf:HY_HydroFeatureName](HY_HydroFeatureName) (c)<br />
Sub-classes |[hyf:HY_Catchment](HY_Catchment) (c)<br />
In domain of |[hyf:HY_HydroFeature.name](HY_HydroFeature.name) (op)<br />
### HY_HydroFeatureName
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeatureName`
Description | <p>pattern to handle cultural, political and historical variability of names. This supports the assignment of a referenceable name for all or parts of a hydrologic feature without necessarily having a formal model for the naming.</p>
Restrictions |[hyf:namesPart](namesPart) (dp) **only** [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />[hyf:preferredBy](preferredBy) (op) **only** [http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty](http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty) (c)<br />[hyf:HY_HydroFeatureName.name](HY_HydroFeatureName.name) (dp) **only** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />[hyf:variantSpelling](variantSpelling) (dp) **only** [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />[hyf:usage](usage) (op) **only** [hyf:HY_NameUsage](HY_NameUsage) (c)<br />
In domain of |[hyf:HY_HydroFeatureName.name](HY_HydroFeatureName.name) (dp)<br />
In range of |[hyf:HY_HydroFeature.name](HY_HydroFeature.name) (op)<br />
### ReferenceLocation
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroLocation`
Description | <p>The HY_HydroLocation feature type (Figure 35) conceptualizes the idea that a hydro nexus can be realized by practically any feature of interest. The hydro nexus concept is used to define the hydrologic determination of a catchment but, like the catchment concept, does not have inherent realization(s). Any hydrologically significant feature that can be identified as (said to be) the outlet of a catchment may realize the hydro nexus. Typically, this will be a permanent, stable location that is fixed and/or referenced by coordinates. Landmarks such as confluences, points corresponding to vertical sections, or the position of a monitoring station on a river are typical realizations of the hydro nexus. Other kinds of hydro nexus realizations that don't carry normal surface water characteristics as defined in this standard, e.g. a spring where groundwater enters the surface, an arbitrary point projected onto the surface, or a nexus that collects many disjoint locations may use or specialize the general HY_HydroLocation type. Topologically, the HY_HydroLocation should be understood to be the boundary of the corresponding catchment, and always of lower topological dimension than the catchment. Even though the topological realization of a hydro nexus is typically as a node between catchment edges, a nexus realization may also have any geometric representation, including a single point.In many cases, HY_HydroLocations are known but corresponding catchments and hydro nexuses are not defined. For example, stream gages that are part of a catchment dataset whose hydro nexus features are realized by confluences. Both the stream gages and confluences are HY_HydroLocations, but the stream gages’ hydro nexus features are not defined. Using this concept, HY_HydroLocation is expected to be used to link between datasets that have catchments delineated for different HY_HydroLocations.HY_HydroLocation carries two attributes: shape and hydroLocationType. It has referencedPosition and realizedNexus associations implying the hydro-complex feature collection.</p>
Restrictions |[hyf:realizedNexus](realizedNexus) (op) **only** [hyf:HY_HydroNexus](HY_HydroNexus) (c)<br />[hyf:referencedPosition](referencedPosition) (op) **only** [hyf:HY_IndirectPosition](HY_IndirectPosition) (c)<br />[gsp:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) **only** [gsp:Geometry](http://www.opengis.net/ont/geosparql#Geometry) (c)<br />[hyf:hydroLocationType](hydroLocationType) (op) **only** [hyf:HY_HydroLocationType](HY_HydroLocationType) (c)<br />
In range of |[hyf:locatedReferent](locatedReferent) (op)<br />[hyf:referenceLocation](referenceLocation) (op)<br />[hyf:nexusRealization](nexusRealization) (op)<br />
### HY_HydroLocationType
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroLocationType`
Description | <p>terms identifying a Hydro Location determined to realize the conceptual nexus.If required, an implementation should use terms from this code list, defined specifically to conform to a terminology common in the hydrology domain. Note that alternative code lists may be used but should be related to the terms in but should be related to the terms in this code list using an appropriate formalism.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[hyf:hydroLocationType](hydroLocationType) (op)<br />
### HY_HydroNetwork
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroNetwork`
Description | <p>The HY_HydroNetwork feature type realizes a catchment as a network of connected hydrologic features. Such a network realizes the hierarchical network of logically connected catchments contained in a larger catchment. It may be a sequence of flowpaths, an aggregate of catchment areas or a mesh of catchment divides. HY_HydroNetwork feature type specializes HY_CatchmentRealization. Through generalization it inherits the shape and the realizedCatchment properties, and carries the associations flowpath, catchmentDivide and catchmentArea. The optional shape of the is usually given through the individual geometry of the network parts.</p>
Super-classes |[hyf:HY_CatchmentRealization](HY_CatchmentRealization) (c)<br />
Restrictions |[hyf:catchmentArea](catchmentArea) (op) **only** [hyf:HY_CatchmentArea](HY_CatchmentArea) (c)<br />[hyf:flowpath](flowpath) (op) **only** [hyf:HY_FlowPath](HY_FlowPath) (c)<br />[hyf:catchmentDivide](catchmentDivide) (op) **only** [hyf:HY_CatchmentDivide](HY_CatchmentDivide) (c)<br />
### HY_HydroNexus
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroNexus`
Description | <p>The HY_HydroNexus feature type (Figure 33) conceptualizes a hydrologically determined nexus of a corresponding catchment (Figure 26). The hydro nexus represents the place where a catchment interacts with another catchment, i.e. where the outflow of a contributing catchment becomes inflow into a receiving catchment. A catchment may receive flow from several upstream catchments or contribute flow to several downstream catchments through a single hydro nexus. Through shared identity, each hydro nexus feature may be associated with different realizations within a hydrologic complex given that each realization has the same hydrologic function or characteristics. This includes the topological realization as a node on the one-dimensional flowpath (edge) in terms of a topological 'boundary'. Placed topologically relative to a catchment which links inflow and outflow, a hydro nexus has a position relative to another hydro nexus that is 'fixed' in the network by the catchments it is associated with. Additionally, the union of catchment and hydro nexus(es) can be used to define a linear river reference system, where an inflow or outflow node is the origin and the flowpath realizing the catchment is the linear element along which a position can be determined.</p>
Restrictions |[hyf:contributingCatchment](contributingCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />[hyf:nexusRealization](nexusRealization) (op) **only** [hyf:HY_HydroLocation](ReferenceLocation) (c)<br />[hyf:receivingCatchment](receivingCatchment) (op) **only** [hyf:HY_Catchment](HY_Catchment) (c)<br />
In range of |[hyf:outflow](outflow) (op)<br />[hyf:realizedNexus](realizedNexus) (op)<br />[hyf:inflow](inflow) (op)<br />
### HY_IndirectPosition
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_IndirectPosition`
Description | <p>The HY_IndirectPosition feature type defines the location referenced along an axis, without the necessity of a geometric realization. Indirect position uses a catchment-specific reference system which defines the flowpath as the required linear element along which the position is determined. The indirect position is then expressed as the distance from the upstream and/or downstream end of the flowpath, or from a referent that is already located on that flowpath. The (indirect) position of an outflow node referenced along an upstream oriented flowpath can be expressed as the distance from an upstream inflow node located on that flowpath, while the (indirect) position of an inflow node referenced along a downstream oriented flowpath can be expressed as distance from a downstream outflow node located on the flowpath. An ‘intermediate’ position referencing known inflow and outflow nodes bounding a flowpath at both ends can be expressed as part of the distance along the entire flowpath, measured from the upstream end of an upstream flowpath, and/or from the downstream end of a downstream flowpath. A position referencing an already referenced location on the flowpath can be expressed as part of the distance along the entire flowpath, measured from the ‘located referent’.  HY_IndirectPosition carries the distanceExpression, and distanceDescription attributes, and has linearElement, locatedReferent and a referenceLocation associations. A point-referent constraint emphasizes the topological relationship between the linear element and point representation of the reference location; a measure-along-flowpath constraint defines the flowpath as the linear element to be used whenever a position is expressed as a distance from a referent.</p>
Restrictions |[hyf:linearElement](linearElement) (op) **only** [hyf:HY_FlowPath](HY_FlowPath) (c)<br />[hyf:distanceExpression](distanceExpression) (op) **only** [hyf:HY_DistanceFromReferent](HY_DistanceFromReferent) (c)<br />[hyf:distanceDescription](distanceDescription) (op) **only** [hyf:HY_DistanceDescription](HY_DistanceDescription) (c)<br />[hyf:locatedReferent](locatedReferent) (op) **only** [hyf:HY_HydroLocation](ReferenceLocation) (c)<br />[hyf:referenceLocation](referenceLocation) (op) **only** [hyf:HY_HydroLocation](ReferenceLocation) (c)<br />
In range of |[hyf:referencedPosition](referencedPosition) (op)<br />
### HY_InteriorCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_InteriorCatchment`
Description | <p>The HY_InteriorCatchment feature type (Figure 32) specializes the general HY_Catchment class as a catchment which is generally not connected to other catchments. This class describes the interior catchment as a catchment enveloped by other catchments to which it may temporarily contribute. While the interior catchment concept precludes flow to neighboring surface catchments, holistically it is a candidate for establishing connections to groundwater or atmospheric systems.</p>
Super-classes |[hyf:HY_Catchment](HY_Catchment) (c)<br />
In range of |[hyf:endorheicDrainage](endorheicDrainage) (op)<br />
### HY_NameUsage
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_NameUsage`
Description | <p>terms used to indicate the type of name usage.If required, an implementation should use terms from this code list, defined specifically to conform to a terminology common in the hydrology domain. Note that alternative code lists may be used but should be related to the terms in but should be related to the terms in this code list using an appropriate formalism.</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[hyf:usage](usage) (op)<br />

## Object Properties
[HY_HydroFeature.name](#HY_HydroFeature.name),
[catchmentArea](#catchmentArea),
[catchmentDivide](#catchmentDivide),
[catchmentRealization](#catchmentRealization),
[code](#code),
[conjointCatchment](#conjointCatchment),
[containedCatchment](#containedCatchment),
[containingCatchment](#containingCatchment),
[contributingCatchment](#contributingCatchment),
[distanceDescription](#distanceDescription),
[distanceExpression](#distanceExpression),
[endorheicDrainage](#endorheicDrainage),
[exorheicDrainage](#exorheicDrainage),
[flowpath](#flowpath),
[hydroLocationType](#hydroLocationType),
[inflow](#inflow),
[linearElement](#linearElement),
[locatedReferent](#locatedReferent),
[lowerCatchment](#lowerCatchment),
[nexusRealization](#nexusRealization),
[outflow](#outflow),
[preferredBy](#preferredBy),
[realizedCatchment](#realizedCatchment),
[realizedNexus](#realizedNexus),
[receivingCatchment](#receivingCatchment),
[referenceLocation](#referenceLocation),
[referencedPosition](#referencedPosition),
[upperCatchment](#upperCatchment),
[usage](#usage),
[](HY_HydroFeature.name)
### HY_HydroFeature.name
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeature.name`
Domain(s) |[hyf:HY_HydroFeature](HY_HydroFeature) (c)<br />
Range(s) |[hyf:HY_HydroFeatureName](HY_HydroFeatureName) (c)<br />
[](catchmentArea)
### catchmentArea
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/catchmentArea`
Range(s) |[hyf:HY_CatchmentArea](HY_CatchmentArea) (c)<br />
[](catchmentDivide)
### catchmentDivide
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/catchmentDivide`
Range(s) |[hyf:HY_CatchmentDivide](HY_CatchmentDivide) (c)<br />
[](catchmentRealization)
### catchmentRealization
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/catchmentRealization`
Range(s) |[hyf:HY_CatchmentRealization](HY_CatchmentRealization) (c)<br />
[](code)
### code
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/code`
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](conjointCatchment)
### conjointCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/conjointCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](containedCatchment)
### containedCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/containedCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](containingCatchment)
### containingCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/containingCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](contributingCatchment)
### contributingCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/contributingCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](distanceDescription)
### distanceDescription
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/distanceDescription`
Range(s) |[hyf:HY_DistanceDescription](HY_DistanceDescription) (c)<br />
[](distanceExpression)
### distanceExpression
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/distanceExpression`
Range(s) |[hyf:HY_DistanceFromReferent](HY_DistanceFromReferent) (c)<br />
[](endorheicDrainage)
### endorheicDrainage
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/endorheicDrainage`
Range(s) |[hyf:HY_InteriorCatchment](HY_InteriorCatchment) (c)<br />
[](exorheicDrainage)
### exorheicDrainage
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/exorheicDrainage`
Range(s) |[hyf:HY_DendriticCatchment](HY_DendriticCatchment) (c)<br />
[](flowpath)
### flowpath
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/flowpath`
Range(s) |[hyf:HY_FlowPath](HY_FlowPath) (c)<br />
[](hydroLocationType)
### hydroLocationType
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/hydroLocationType`
Range(s) |[hyf:HY_HydroLocationType](HY_HydroLocationType) (c)<br />
[](inflow)
### inflow
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/inflow`
Range(s) |[hyf:HY_HydroNexus](HY_HydroNexus) (c)<br />
[](linearElement)
### linearElement
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/linearElement`
Range(s) |[hyf:HY_FlowPath](HY_FlowPath) (c)<br />
[](locatedReferent)
### locatedReferent
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/locatedReferent`
Range(s) |[hyf:HY_HydroLocation](ReferenceLocation) (c)<br />
[](lowerCatchment)
### lowerCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/lowerCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](nexusRealization)
### nexusRealization
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/nexusRealization`
Range(s) |[hyf:HY_HydroLocation](ReferenceLocation) (c)<br />
[](outflow)
### outflow
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/outflow`
Range(s) |[hyf:HY_HydroNexus](HY_HydroNexus) (c)<br />
[](preferredBy)
### preferredBy
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/preferredBy`
Range(s) |[http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty](http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty) (c)<br />
[](realizedCatchment)
### realizedCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/realizedCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](realizedNexus)
### realizedNexus
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/realizedNexus`
Range(s) |[hyf:HY_HydroNexus](HY_HydroNexus) (c)<br />
[](receivingCatchment)
### receivingCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/receivingCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](referenceLocation)
### referenceLocation
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/referenceLocation`
Range(s) |[hyf:HY_HydroLocation](ReferenceLocation) (c)<br />
[](referencedPosition)
### referencedPosition
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/referencedPosition`
Range(s) |[hyf:HY_IndirectPosition](HY_IndirectPosition) (c)<br />
[](upperCatchment)
### upperCatchment
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/upperCatchment`
Range(s) |[hyf:HY_Catchment](HY_Catchment) (c)<br />
[](usage)
### usage
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/usage`
Range(s) |[hyf:HY_NameUsage](HY_NameUsage) (c)<br />

## Datatype Properties
[HY_HydroFeatureName.name](#HY_HydroFeatureName.name),
[absolute](#absolute),
[accuracyStatement](#accuracyStatement),
[interpolative](#interpolative),
[namesPart](#namesPart),
[precisionStatement](#precisionStatement),
[variantSpelling](#variantSpelling),
[](HY_HydroFeatureName.name)
### HY_HydroFeatureName.name
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeatureName.name`
Domain(s) |[hyf:HY_HydroFeatureName](HY_HydroFeatureName) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](absolute)
### absolute
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/absolute`
Range(s) |[sc:Measure](http://shapechange.net/resources/ont/base#Measure) (c)<br />
[](accuracyStatement)
### accuracyStatement
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/accuracyStatement`
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](interpolative)
### interpolative
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/interpolative`
Range(s) |[xsd:double](http://www.w3.org/2001/XMLSchema#double) (c)<br />
[](namesPart)
### namesPart
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/namesPart`
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />
[](precisionStatement)
### precisionStatement
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/precisionStatement`
Range(s) |[sc:Measure](http://shapechange.net/resources/ont/base#Measure) (c)<br />
[](variantSpelling)
### variantSpelling
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/variantSpelling`
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

## Named Individuals
## Namespaces
* **default (:)**
  * `https://www.opengis.net/def/appschema/hy_features/hyf/`
* **gsp**
  * `http://www.opengis.net/ont/geosparql#`
* **hyf**
  * `https://www.opengis.net/def/appschema/hy_features/hyf/`
* **meta**
  * `http://def.seegrid.csiro.au/isotc211/iso19115/2003/citation`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sc**
  * `http://shapechange.net/resources/ont/base#`
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