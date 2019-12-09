# HY Features Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `https://www.opengis.net/def/appschema/hy_features/hyf`
* **Imports**
  * <a href="http://shapechange.net/resources/ont/base">http://shapechange.net/resources/ont/base</a>
  * <a href="http://eelst.cs.unibo.it/apps/LODE/source?url=http://def.seegrid.csiro.au/isotc211/iso19115/2003/metadata.ttl">http://eelst.cs.unibo.it/apps/LODE/source?url=http://def.seegrid.csiro.au/isotc211/iso19115/2003/metadata.ttl</a>
  * <a href="http://www.opengis.net/ont/geosparql">http://www.opengis.net/ont/geosparql</a>
* **Ontology Source**
  * <a href="hy_features.ttl">RDF (turtle)</a>
### Description
<p>The HydroFeature module (Figure 21) provides the core concepts of a named hydrologic feature in the Named Feature, of a hydrologic complex in which the union of catchment and its common outlet is realized in several ways by a collection of hydrologic features, and of a river referencing system which allows placement of an arbitrary feature ‘along a river’ using linear referencing along a one-dimensional topological, flowpath realization. The HY_HydroFeature feature type is defined as hydrology-specific instance of the General Feature metaclass (as defined in the OGC General Feature Model, GFM), whose identity needs to be maintained and tracked through a processing chain from measurement to distribution of hydrologic information.As an instance of the General Feature metaclass a feature type is identified by a unique identifier and typical properties. Typically, a hydrologic feature is additionally identified through names in common usage and through hydrologically significant characteristics. The HY_HydroFeature feature type is specialized into more specific feature types (Figure 23), which specify additional properties and represent particular hydrologic phenomena.Providing a standard terminology for the typical relationships between hydrologic features allows the hydrosphere to be expressed in a consistent way across multiple data products, regardless of various spatial or temporal representations.The definitions of HydroFeature feature types are rooted in the definitions documented in the WMO/UNESCO Glossary of Hydrology. They are applied regardless of their application context in respect to the Earth's surface. For the purpose of testing the applicability of the HY_Features conceptual model in the context of surface water hydrology, the definitions in this standard refer to surface water hydrology. A conceptual model capturing the specifics of features associated with the groundwater domain is developed with reference to the OGC WaterML 2: Part 4 – GroundwaterML2 standard.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Namespaces](#namespaces)  


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
### HY_CartographicRealization <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CartographicRealization`
Description | The HY_CartographicRealization feature type realizes a catchment as set of separate cartographic layers or maps, displaying a network of hydrologic features which may be connected at the representation level, or not. Specializing HY_CatchmentRealization, it inherits from generalization the shape attribute and the realizedCatchment association.
Super-classes |<a href="#HY_CatchmentRealization">hyf:HY_CatchmentRealization</a><sup class="sup-c" title="class">c</sup><br />
### HY_Catchment <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_Catchment`
Description | The Catchment model conceptualizes the hydrologic determination of a catchment through inflow and outflow hydro nexus features with the role of getting flow from a contributing catchment, or providing inflow to a receiving catchment (Figure 25 and Figure 26). Conceptually, each catchment has an outflow hydro nexus, and any hydro nexus has a corresponding catchment, even if catchment and/or hydro nexus may not be present in a particular application. A catchment interacts with upper and lower catchments via associated hydro nexuses, and ultimately contributes flow to the hydro nexus of a containing catchment. The catchment should be understood as the logical link between two hydro nexuses.The HY_Catchment feature type captures the union of catchment and hydro nexus, and the multiple realizations of the holistic catchment concept. These realizations include both topological realizations, as well as their geometric representation. HY_Catchment may be further specialized with respect to catchment interaction. The HY_Catchment feature type (Figure 26) specializes the general HY_HydroFeature type. Through generalization, HY_Catchment inherits the name property. It carries a code attribute and the associations: outflow, inflow, containingCatchment, containedCatchment, conjointCatchment, upperCatchment, lowerCatchment, catchmentRealization.
Super-classes |<a href="#HY_HydroFeature">hyf:HY_HydroFeature</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#conjointCatchment">hyf:conjointCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#catchmentRealization">hyf:catchmentRealization</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_CatchmentRealization">hyf:HY_CatchmentRealization</a><sup class="sup-c" title="class">c</sup><br /><a href="#outflow">hyf:outflow</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_HydroNexus">hyf:HY_HydroNexus</a><sup class="sup-c" title="class">c</sup><br /><a href="#containedCatchment">hyf:containedCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#upperCatchment">hyf:upperCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#containingCatchment">hyf:containingCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#code">hyf:code</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br /><a href="#lowerCatchment">hyf:lowerCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#inflow">hyf:inflow</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_HydroNexus">hyf:HY_HydroNexus</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#HY_DendriticCatchment">hyf:HY_DendriticCatchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#HY_CatchmentAggregate">hyf:HY_CatchmentAggregate</a><sup class="sup-c" title="class">c</sup><br /><a href="#HY_InteriorCatchment">hyf:HY_InteriorCatchment</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#receivingCatchment">hyf:receivingCatchment</a><sup class="sup-op" title="object property">op</sup><br /><a href="#containingCatchment">hyf:containingCatchment</a><sup class="sup-op" title="object property">op</sup><br /><a href="#conjointCatchment">hyf:conjointCatchment</a><sup class="sup-op" title="object property">op</sup><br /><a href="#contributingCatchment">hyf:contributingCatchment</a><sup class="sup-op" title="object property">op</sup><br /><a href="#realizedCatchment">hyf:realizedCatchment</a><sup class="sup-op" title="object property">op</sup><br /><a href="#containedCatchment">hyf:containedCatchment</a><sup class="sup-op" title="object property">op</sup><br /><a href="#lowerCatchment">hyf:lowerCatchment</a><sup class="sup-op" title="object property">op</sup><br /><a href="#upperCatchment">hyf:upperCatchment</a><sup class="sup-op" title="object property">op</sup><br />
### HY_CatchmentAggregate <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentAggregate`
Description | The HY_CatchmentAggregate feature type (Figure 30) specializes the HY_Catchment type as a set of non-overlapping dendritic and interior catchments arranged in an encompassing catchment. This can be used to describe multiple inflows into a catchment aggregate through several hydrologically discrete sub-catchments each with a single inflow, and contributing to a joined outflow of the catchment aggregate, including the 'nillable' outflow of interior catchments. Nillable is meant here to signify that the hydro nexus logically exists in the form of flow to the subsurface or atmosphere but is unknown in a given implementation. Being a special type of the HY_Catchment, the catchment aggregate may be part of a containing catchment at the next higher level of hierarchy, which consists of similar-scale neighboring catchments. The catchment aggregate does not necessarily imply a series of nested containing catchments. It primarily allows navigation to the 'highest' level system (total drainage basin) as typically used for reporting purposes.HY_CatchmentAggregate inherits through generalization the outflow, inflow, containingCatchment, containedCatchment, conjointCatchment, upperCatchment, lowerCatchment, and catchmentRealization properties, and has exorheicDrainage and endorheicDrainage associations.
Super-classes |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#endorheicDrainage">hyf:endorheicDrainage</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_InteriorCatchment">hyf:HY_InteriorCatchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#exorheicDrainage">hyf:exorheicDrainage</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_DendriticCatchment">hyf:HY_DendriticCatchment</a><sup class="sup-c" title="class">c</sup><br />
### HY_CatchmentArea <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentArea`
Description | The HY_CatchmentArea feature type realizes a catchment specifically as a catchment area connecting the inflow and outflow of the catchment it realizes. HY_CatchmentArea specializes HY_CatchmentRealization with respect to an implied areal geometric representation. Topologically, the catchment area connecting the inflow and outflow of the catchment is a face bounded inwards by an inflow edge and outwards by an outflow edge. Hydrologically, catchment area refers to the area having a common outlet for its runoff. Through generalization, HY_CatchmentArea inherits the shape and the realizedCatchment properties. The optional shape of the catchment may be implemented as a surface.
Super-classes |<a href="#HY_CatchmentRealization">hyf:HY_CatchmentRealization</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#catchmentArea">hyf:catchmentArea</a><sup class="sup-op" title="object property">op</sup><br />
### HY_CatchmentDivide <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentDivide`
Description | The HY_CatchmentDivide feature type realizes a catchment specifically as catchment boundary connecting the inflow and outflow of the catchment it realizes, whereby inflow and outflow may overlay.Implying a linear geometric representation, a catchment boundary is topologically understood as an edge bounded by inflow node and outflow nodes, and corresponding to left-bank and right-bank catchment faces inside of the boundary. Hydrologically, the boundary refers to the summit line separating adjacent catchments. Through generalization, HY_CatchmentDivide inherits the shape and the realizedCatchment properties. The shape of the catchment divide may be implemented as a composition of succeeding curves or a polygon ring.
Super-classes |<a href="#HY_CatchmentRealization">hyf:HY_CatchmentRealization</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#catchmentDivide">hyf:catchmentDivide</a><sup class="sup-op" title="object property">op</sup><br />
### HY_CatchmentRealization <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_CatchmentRealization`
Description | The HY_CatchmentRealization feature type (Figure 34) is based on the idea that there are multiple hydrology-specific perspectives of the holistic catchment concept that are used to describe a catchment as a unit of study shared across sub-domains and studies. A given catchment realization exists within a hydrologic complex in that, if a catchment realization exists, it exists in the same hydrologic complex as the catchment it realizes. In this way, any realization of a catchment has the same hydrologic determination of the catchment it realizes. If a catchment is connected with other catchments via inflow and/or outflow hydro nexuses, its realizations are also connected. A realization of the logical catchment is always of higher topological dimension than the realization of the corresponding hydro nexus topological boundary. For example, a linear flowpath realizing a catchment may be understood as an edge between inflow and outflow nodes; the areal realization of a catchment as a face bounded by linear inflow and outflow.The catchment realization features defined in this standard refer to objects on the land surface for the purpose of surface water hydrology. In other contexts, other types of catchment realization may exist. Catchment realizations that do not conform to those defined in this standard, for instance realizations in 3- or 4-dimensional perspectives, may be implemented using the general HY_CatchmentRealization type. HY_CatchmentRealization carries a shape attribute and as a realizedCatchment association.
Restrictions |<a href="http://www.opengis.net/ont/geosparql#hasGeometry">gsp:hasGeometry</a> <span class="cardinality">only</span> <a href="http://www.opengis.net/ont/geosparql#Geometry">gsp:Geometry</a><sup class="sup-c" title="class">c</sup><br /><a href="#realizedCatchment">hyf:realizedCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#HY_FlowPath">hyf:HY_FlowPath</a><sup class="sup-c" title="class">c</sup><br /><a href="#HY_CartographicRealization">hyf:HY_CartographicRealization</a><sup class="sup-c" title="class">c</sup><br /><a href="#HY_CatchmentArea">hyf:HY_CatchmentArea</a><sup class="sup-c" title="class">c</sup><br /><a href="#HY_HydroNetwork">hyf:HY_HydroNetwork</a><sup class="sup-c" title="class">c</sup><br /><a href="#HY_CatchmentDivide">hyf:HY_CatchmentDivide</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#catchmentRealization">hyf:catchmentRealization</a><sup class="sup-op" title="object property">op</sup><br />
### HY_DendriticCatchment <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_DendriticCatchment`
Description | The HY_DendriticCatchment feature type (Figure 31) specializes the general HY_Catchment class as a catchment which is determined by a single common downstream catchment. It represents the catchment as the topological link between an inflow and an outflow. This allows catchments to be connected in a dendritic network by upstream-downstream relationships without knowing the complex hydrology between inflow and outflow. This concept requires a stable identifier purposefully assigned to the catchment and that catchments are delineated as a simple tree hierarchy. HY_DendriticCatchment inherits from generalization the code, outflow, inflow, containingCatchment, containedCatchment, conjointCatchment, upperCatchment, lowerCatchment, and catchmentRealization properties, and has an encompassingCatchment association. The dendritic nature of this feature is enforced through single-outflow, single-receiving-catchment and single-lower-catchment constraints.
Super-classes |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#exorheicDrainage">hyf:exorheicDrainage</a><sup class="sup-op" title="object property">op</sup><br />
### HY_DistanceDescription <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_DistanceDescription`
Description | list of general terms commonly used in hydrology to describe a spatial relationship between two locations.If required, an implementation should use terms from this code list, defined specifically to conform to a terminology common in the hydrology domain. Note that alternative code lists may be used but should be related to the terms in but should be related to the terms in this code list using an appropriate formalism.
Super-classes |<a href="http://www.w3.org/2004/02/skos/core#Concept">skos:Concept</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#distanceDescription">hyf:distanceDescription</a><sup class="sup-op" title="object property">op</sup><br />
### HY_DistanceFromReferent <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_DistanceFromReferent`
Description | The HY_DistanceFromReferent data type provides the distance from a located referent as an absolute or interpolative value, including simple statements on accuracy and precision of the measured position.
Restrictions |<a href="#accuracyStatement">hyf:accuracyStatement</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">only</span> <a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br /><a href="#precisionStatement">hyf:precisionStatement</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">only</span> <a href="http://shapechange.net/resources/ont/base#Measure">sc:Measure</a><sup class="sup-c" title="class">c</sup><br /><a href="#interpolative">hyf:interpolative</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">only</span> <a href="http://www.w3.org/2001/XMLSchema#double">xsd:double</a><sup class="sup-c" title="class">c</sup><br /><a href="#absolute">hyf:absolute</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">only</span> <a href="http://shapechange.net/resources/ont/base#Measure">sc:Measure</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#distanceExpression">hyf:distanceExpression</a><sup class="sup-op" title="object property">op</sup><br />
### HY_FlowPath <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_FlowPath`
Description | The HY_Flowpath feature type realizes a catchment specifically as a path connecting the inflow and outflow of the catchment it realizes.HY_Flowpath specializes HY_CatchmentRealization with respect to an implied linear geometric representation including a straight or curved line. Topologically, the flowpath connects the inflow and outflow of the catchment, and is understood as an edge bounded by an inflow node and an outflow node, and corresponding to left-bank and right-bank catchment faces. Hydrologically, the flowpath is a line describing a moving particle of water. Through generalization, HY_Flowpath inherits the shape and the realizedCatchment properties. The optional shape of the flowpath is usually a single curve.
Super-classes |<a href="#HY_CatchmentRealization">hyf:HY_CatchmentRealization</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#linearElement">hyf:linearElement</a><sup class="sup-op" title="object property">op</sup><br /><a href="#flowpath">hyf:flowpath</a><sup class="sup-op" title="object property">op</sup><br />
### HY_HydroFeature <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeature`
Description | basic feature to reflect the properties that all hydrologic features have.
Restrictions |<a href="#HY_HydroFeature.name">hyf:HY_HydroFeature.name</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_HydroFeatureName">hyf:HY_HydroFeatureName</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
In domain of |<a href="#HY_HydroFeature.name">hyf:HY_HydroFeature.name</a><sup class="sup-op" title="object property">op</sup><br />
### HY_HydroFeatureName <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeatureName`
Description | pattern to handle cultural, political and historical variability of names. This supports the assignment of a referenceable name for all or parts of a hydrologic feature without necessarily having a formal model for the naming.
Restrictions |<a href="#preferredBy">hyf:preferredBy</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty">http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty</a><sup class="sup-c" title="class">c</sup><br /><a href="#variantSpelling">hyf:variantSpelling</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">only</span> <a href="http://www.w3.org/2001/XMLSchema#boolean">xsd:boolean</a><sup class="sup-c" title="class">c</sup><br /><a href="#HY_HydroFeatureName.name">hyf:HY_HydroFeatureName.name</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">only</span> <a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br /><a href="#usage">hyf:usage</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_NameUsage">hyf:HY_NameUsage</a><sup class="sup-c" title="class">c</sup><br /><a href="#namesPart">hyf:namesPart</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">only</span> <a href="http://www.w3.org/2001/XMLSchema#boolean">xsd:boolean</a><sup class="sup-c" title="class">c</sup><br />
In domain of |<a href="#HY_HydroFeatureName.name">hyf:HY_HydroFeatureName.name</a><sup class="sup-dp" title="datatype property">dp</sup><br />
In range of |<a href="#HY_HydroFeature.name">hyf:HY_HydroFeature.name</a><sup class="sup-op" title="object property">op</sup><br />
### ReferenceLocation <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroLocation`
Description | The HY_HydroLocation feature type (Figure 35) conceptualizes the idea that a hydro nexus can be realized by practically any feature of interest. The hydro nexus concept is used to define the hydrologic determination of a catchment but, like the catchment concept, does not have inherent realization(s). Any hydrologically significant feature that can be identified as (said to be) the outlet of a catchment may realize the hydro nexus. Typically, this will be a permanent, stable location that is fixed and/or referenced by coordinates. Landmarks such as confluences, points corresponding to vertical sections, or the position of a monitoring station on a river are typical realizations of the hydro nexus. Other kinds of hydro nexus realizations that don't carry normal surface water characteristics as defined in this standard, e.g. a spring where groundwater enters the surface, an arbitrary point projected onto the surface, or a nexus that collects many disjoint locations may use or specialize the general HY_HydroLocation type. Topologically, the HY_HydroLocation should be understood to be the boundary of the corresponding catchment, and always of lower topological dimension than the catchment. Even though the topological realization of a hydro nexus is typically as a node between catchment edges, a nexus realization may also have any geometric representation, including a single point.In many cases, HY_HydroLocations are known but corresponding catchments and hydro nexuses are not defined. For example, stream gages that are part of a catchment dataset whose hydro nexus features are realized by confluences. Both the stream gages and confluences are HY_HydroLocations, but the stream gages’ hydro nexus features are not defined. Using this concept, HY_HydroLocation is expected to be used to link between datasets that have catchments delineated for different HY_HydroLocations.HY_HydroLocation carries two attributes: shape and hydroLocationType. It has referencedPosition and realizedNexus associations implying the hydro-complex feature collection.
Restrictions |<a href="#realizedNexus">hyf:realizedNexus</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_HydroNexus">hyf:HY_HydroNexus</a><sup class="sup-c" title="class">c</sup><br /><a href="http://www.opengis.net/ont/geosparql#hasGeometry">gsp:hasGeometry</a> <span class="cardinality">only</span> <a href="http://www.opengis.net/ont/geosparql#Geometry">gsp:Geometry</a><sup class="sup-c" title="class">c</sup><br /><a href="#referencedPosition">hyf:referencedPosition</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_IndirectPosition">hyf:HY_IndirectPosition</a><sup class="sup-c" title="class">c</sup><br /><a href="#hydroLocationType">hyf:hydroLocationType</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_HydroLocationType">hyf:HY_HydroLocationType</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#locatedReferent">hyf:locatedReferent</a><sup class="sup-op" title="object property">op</sup><br /><a href="#nexusRealization">hyf:nexusRealization</a><sup class="sup-op" title="object property">op</sup><br /><a href="#referenceLocation">hyf:referenceLocation</a><sup class="sup-op" title="object property">op</sup><br />
### HY_HydroLocationType <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroLocationType`
Description | terms identifying a Hydro Location determined to realize the conceptual nexus.If required, an implementation should use terms from this code list, defined specifically to conform to a terminology common in the hydrology domain. Note that alternative code lists may be used but should be related to the terms in but should be related to the terms in this code list using an appropriate formalism.
Super-classes |<a href="http://www.w3.org/2004/02/skos/core#Concept">skos:Concept</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#hydroLocationType">hyf:hydroLocationType</a><sup class="sup-op" title="object property">op</sup><br />
### HY_HydroNetwork <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroNetwork`
Description | The HY_HydroNetwork feature type realizes a catchment as a network of connected hydrologic features. Such a network realizes the hierarchical network of logically connected catchments contained in a larger catchment. It may be a sequence of flowpaths, an aggregate of catchment areas or a mesh of catchment divides. HY_HydroNetwork feature type specializes HY_CatchmentRealization. Through generalization it inherits the shape and the realizedCatchment properties, and carries the associations flowpath, catchmentDivide and catchmentArea. The optional shape of the is usually given through the individual geometry of the network parts.
Super-classes |<a href="#HY_CatchmentRealization">hyf:HY_CatchmentRealization</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#flowpath">hyf:flowpath</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_FlowPath">hyf:HY_FlowPath</a><sup class="sup-c" title="class">c</sup><br /><a href="#catchmentDivide">hyf:catchmentDivide</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_CatchmentDivide">hyf:HY_CatchmentDivide</a><sup class="sup-c" title="class">c</sup><br /><a href="#catchmentArea">hyf:catchmentArea</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_CatchmentArea">hyf:HY_CatchmentArea</a><sup class="sup-c" title="class">c</sup><br />
### HY_HydroNexus <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroNexus`
Description | The HY_HydroNexus feature type (Figure 33) conceptualizes a hydrologically determined nexus of a corresponding catchment (Figure 26). The hydro nexus represents the place where a catchment interacts with another catchment, i.e. where the outflow of a contributing catchment becomes inflow into a receiving catchment. A catchment may receive flow from several upstream catchments or contribute flow to several downstream catchments through a single hydro nexus. Through shared identity, each hydro nexus feature may be associated with different realizations within a hydrologic complex given that each realization has the same hydrologic function or characteristics. This includes the topological realization as a node on the one-dimensional flowpath (edge) in terms of a topological 'boundary'. Placed topologically relative to a catchment which links inflow and outflow, a hydro nexus has a position relative to another hydro nexus that is 'fixed' in the network by the catchments it is associated with. Additionally, the union of catchment and hydro nexus(es) can be used to define a linear river reference system, where an inflow or outflow node is the origin and the flowpath realizing the catchment is the linear element along which a position can be determined.
Restrictions |<a href="#nexusRealization">hyf:nexusRealization</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#ReferenceLocation">hyf:HY_HydroLocation</a><sup class="sup-c" title="class">c</sup><br /><a href="#receivingCatchment">hyf:receivingCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br /><a href="#contributingCatchment">hyf:contributingCatchment</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#inflow">hyf:inflow</a><sup class="sup-op" title="object property">op</sup><br /><a href="#realizedNexus">hyf:realizedNexus</a><sup class="sup-op" title="object property">op</sup><br /><a href="#outflow">hyf:outflow</a><sup class="sup-op" title="object property">op</sup><br />
### HY_IndirectPosition <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_IndirectPosition`
Description | The HY_IndirectPosition feature type defines the location referenced along an axis, without the necessity of a geometric realization. Indirect position uses a catchment-specific reference system which defines the flowpath as the required linear element along which the position is determined. The indirect position is then expressed as the distance from the upstream and/or downstream end of the flowpath, or from a referent that is already located on that flowpath. The (indirect) position of an outflow node referenced along an upstream oriented flowpath can be expressed as the distance from an upstream inflow node located on that flowpath, while the (indirect) position of an inflow node referenced along a downstream oriented flowpath can be expressed as distance from a downstream outflow node located on the flowpath. An ‘intermediate’ position referencing known inflow and outflow nodes bounding a flowpath at both ends can be expressed as part of the distance along the entire flowpath, measured from the upstream end of an upstream flowpath, and/or from the downstream end of a downstream flowpath. A position referencing an already referenced location on the flowpath can be expressed as part of the distance along the entire flowpath, measured from the ‘located referent’.  HY_IndirectPosition carries the distanceExpression, and distanceDescription attributes, and has linearElement, locatedReferent and a referenceLocation associations. A point-referent constraint emphasizes the topological relationship between the linear element and point representation of the reference location; a measure-along-flowpath constraint defines the flowpath as the linear element to be used whenever a position is expressed as a distance from a referent.
Restrictions |<a href="#locatedReferent">hyf:locatedReferent</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#ReferenceLocation">hyf:HY_HydroLocation</a><sup class="sup-c" title="class">c</sup><br /><a href="#distanceExpression">hyf:distanceExpression</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_DistanceFromReferent">hyf:HY_DistanceFromReferent</a><sup class="sup-c" title="class">c</sup><br /><a href="#linearElement">hyf:linearElement</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_FlowPath">hyf:HY_FlowPath</a><sup class="sup-c" title="class">c</sup><br /><a href="#referenceLocation">hyf:referenceLocation</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#ReferenceLocation">hyf:HY_HydroLocation</a><sup class="sup-c" title="class">c</sup><br /><a href="#distanceDescription">hyf:distanceDescription</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#HY_DistanceDescription">hyf:HY_DistanceDescription</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#referencedPosition">hyf:referencedPosition</a><sup class="sup-op" title="object property">op</sup><br />
### HY_InteriorCatchment <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_InteriorCatchment`
Description | The HY_InteriorCatchment feature type (Figure 32) specializes the general HY_Catchment class as a catchment which is generally not connected to other catchments. This class describes the interior catchment as a catchment enveloped by other catchments to which it may temporarily contribute. While the interior catchment concept precludes flow to neighboring surface catchments, holistically it is a candidate for establishing connections to groundwater or atmospheric systems.
Super-classes |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#endorheicDrainage">hyf:endorheicDrainage</a><sup class="sup-op" title="object property">op</sup><br />
### HY_NameUsage <sup>c</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_NameUsage`
Description | terms used to indicate the type of name usage.If required, an implementation should use terms from this code list, defined specifically to conform to a terminology common in the hydrology domain. Note that alternative code lists may be used but should be related to the terms in but should be related to the terms in this code list using an appropriate formalism.
Super-classes |<a href="http://www.w3.org/2004/02/skos/core#Concept">skos:Concept</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#usage">hyf:usage</a><sup class="sup-op" title="object property">op</sup><br />

## Object Properties
[HY_HydroFeature.name](HY_HydroFeature.name),
[catchmentArea](catchmentArea),
[catchmentDivide](catchmentDivide),
[catchmentRealization](catchmentRealization),
[code](code),
[conjointCatchment](conjointCatchment),
[containedCatchment](containedCatchment),
[containingCatchment](containingCatchment),
[contributingCatchment](contributingCatchment),
[distanceDescription](distanceDescription),
[distanceExpression](distanceExpression),
[endorheicDrainage](endorheicDrainage),
[exorheicDrainage](exorheicDrainage),
[flowpath](flowpath),
[hydroLocationType](hydroLocationType),
[inflow](inflow),
[linearElement](linearElement),
[locatedReferent](locatedReferent),
[lowerCatchment](lowerCatchment),
[nexusRealization](nexusRealization),
[outflow](outflow),
[preferredBy](preferredBy),
[realizedCatchment](realizedCatchment),
[realizedNexus](realizedNexus),
[receivingCatchment](receivingCatchment),
[referenceLocation](referenceLocation),
[referencedPosition](referencedPosition),
[upperCatchment](upperCatchment),
[usage](usage),
[](HY_HydroFeature.name)
### HY_HydroFeature.name <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeature.name`
Description | name given to the hydrologic feature in cultural, political or historical context.
Domain(s) |<a href="#HY_HydroFeature">hyf:HY_HydroFeature</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#HY_HydroFeatureName">hyf:HY_HydroFeatureName</a><sup class="sup-c" title="class">c</sup><br />
[](catchmentArea)
### catchmentArea <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/catchmentArea`
Description | catchment area that participates in the network.
Range(s) |<a href="#HY_CatchmentArea">hyf:HY_CatchmentArea</a><sup class="sup-c" title="class">c</sup><br />
[](catchmentDivide)
### catchmentDivide <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/catchmentDivide`
Description | catchment boundary that participates in the network.
Range(s) |<a href="#HY_CatchmentDivide">hyf:HY_CatchmentDivide</a><sup class="sup-c" title="class">c</sup><br />
[](catchmentRealization)
### catchmentRealization <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/catchmentRealization`
Description | topological or geographic feature which realizes the logical catchment.
Range(s) |<a href="#HY_CatchmentRealization">hyf:HY_CatchmentRealization</a><sup class="sup-c" title="class">c</sup><br />
[](code)
### code <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/code`
Description | unique identifier to the catchment in given context. The code attribute should be implemented using a controlled classification or coding system. Example: WMO Basin Codes.
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](conjointCatchment)
### conjointCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/conjointCatchment`
Description | catchment that interacts with the catchment across an internal boundary line.
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](containedCatchment)
### containedCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/containedCatchment`
Description | catchment nested in a containing catchment.
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](containingCatchment)
### containingCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/containingCatchment`
Description | catchment nesting contained catchments.
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](contributingCatchment)
### contributingCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/contributingCatchment`
Description | identifies the catchment that contributes flow to this hydro nexus. This allows connection of a catchment's outflow to an identified inflow and to determine its position through referencing the inflow.
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](distanceDescription)
### distanceDescription <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/distanceDescription`
Description | term describing the distance from the feature being used as a reference. An implementation may use the HY_DistanceDescription code list. Alternatively, the types described in ISO 19103: Conceptual Schema may be used.
Range(s) |<a href="#HY_DistanceDescription">hyf:HY_DistanceDescription</a><sup class="sup-c" title="class">c</sup><br />
[](distanceExpression)
### distanceExpression <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/distanceExpression`
Description | absolute or interpolative value of the distance from the feature being used as a reference, including an indication of accuracy and precision of the absolute value. An implementation may use the HY_DistanceFromReferent (data type) referencing basic types. Alternatively, the types described in ISO 19103: Conceptual Schema may be used.
Range(s) |<a href="#HY_DistanceFromReferent">hyf:HY_DistanceFromReferent</a><sup class="sup-c" title="class">c</sup><br />
[](endorheicDrainage)
### endorheicDrainage <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/endorheicDrainage`
Description | should be used to identify an endorheic-drained catchment, which is not, but may be temporarily connected to the enveloping catchment.
Range(s) |<a href="#HY_InteriorCatchment">hyf:HY_InteriorCatchment</a><sup class="sup-c" title="class">c</sup><br />
[](exorheicDrainage)
### exorheicDrainage <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/exorheicDrainage`
Description | should be used to identify an exorheic-drained catchment which is permanently connected to the encompassing catchment.
Range(s) |<a href="#HY_DendriticCatchment">hyf:HY_DendriticCatchment</a><sup class="sup-c" title="class">c</sup><br />
[](flowpath)
### flowpath <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/flowpath`
Description | flowpath that participates in the network.
Range(s) |<a href="#HY_FlowPath">hyf:HY_FlowPath</a><sup class="sup-c" title="class">c</sup><br />
[](hydroLocationType)
### hydroLocationType <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/hydroLocationType`
Description | expresses the type of the realized nexus, using a term from the HY_HydroLocationType code list, or a controlled vocabulary. Alternative code lists may be used but should be related to the terms in this code list using an appropriate formalism.
Range(s) |<a href="#HY_HydroLocationType">hyf:HY_HydroLocationType</a><sup class="sup-c" title="class">c</sup><br />
[](inflow)
### inflow <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/inflow`
Description | hydro nexus in terms of an inflow to the receiving catchment. For a dendritic network of catchments, the outflow of a contributing catchment coincides with the inflow to a receiving catchment. This supports description of upstream-downstream relationships between catchments.
Range(s) |<a href="#HY_HydroNexus">hyf:HY_HydroNexus</a><sup class="sup-c" title="class">c</sup><br />
[](linearElement)
### linearElement <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/linearElement`
Description | identifies a flowpath used as the linear element along which a position is assigned to a hydro-location, or any feature of interest.
Range(s) |<a href="#HY_FlowPath">hyf:HY_FlowPath</a><sup class="sup-c" title="class">c</sup><br />
[](locatedReferent)
### locatedReferent <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/locatedReferent`
Description | identifies an already referenced location such as a catchment outlet relative to which a position may be assigned to a feature of interest.
Range(s) |<a href="#ReferenceLocation">hyf:HY_HydroLocation</a><sup class="sup-c" title="class">c</sup><br />
[](lowerCatchment)
### lowerCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/lowerCatchment`
Description | catchment located immediately below of the catchment,
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](nexusRealization)
### nexusRealization <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/nexusRealization`
Description | identifies a hydrologic feature which realizes the hydro nexus. A topological nexus realization is of lower dimension than the realization of the corresponding catchment. Example: an outflow node realizing the nexus would be of lower dimension than the flowpath edge realizing the contributing catchment.
Range(s) |<a href="#ReferenceLocation">hyf:HY_HydroLocation</a><sup class="sup-c" title="class">c</sup><br />
[](outflow)
### outflow <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/outflow`
Description | hydro nexus in terms of an outflow of the contributing catchment. For a dendritic network of catchments, the outflow of a contributing catchment coincides with the inflow to a receiving catchment. This supports description of upstream-downstream relationships between catchments.
Range(s) |<a href="#HY_HydroNexus">hyf:HY_HydroNexus</a><sup class="sup-c" title="class">c</sup><br />
[](preferredBy)
### preferredBy <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/preferredBy`
Description | specifies that the name is the preferred name according to the named entity. The CI_Responsibility type may be used to further structure the information about the responsible party and their role.
Range(s) |<a href="http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty">http://def.seegrid.csiro.au/isotc211/iso19115/2003/citationResponsibleParty</a><sup class="sup-c" title="class">c</sup><br />
[](realizedCatchment)
### realizedCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/realizedCatchment`
Description | identifies the one and only one catchment that is realized by a particular feature. Referencing the hydrologic complex containing the catchment and all of its realizations, supports a catchment's existence to be recognized and linked to multiple realizations without the complexity and full detail of a scientific model. By referencing the catchment topology, topological relationships can be established and common identifiers assigned.
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](realizedNexus)
### realizedNexus <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/realizedNexus`
Description | identifies the one and only one nexus that is realized by a particular feature. Referencing the hydrologic complex containing the hydro nexus and all of its realizations, supports an arbitrary feature of interest to be recognized as outlet of a catchment, and to be placed using the river referencing defined in this standard.
Range(s) |<a href="#HY_HydroNexus">hyf:HY_HydroNexus</a><sup class="sup-c" title="class">c</sup><br />
[](receivingCatchment)
### receivingCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/receivingCatchment`
Description | identifies the catchment that receives flow from this hydro nexus. This allows connection of a catchment's inflow to an identified outflow and to determine its position through referencing the outflow.
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](referenceLocation)
### referenceLocation <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/referenceLocation`
Description | identifies the permanent reference location, usually an existing inflow or outflow hydro nexus relative to which a position is assigned to a hydro location feature of interest.
Range(s) |<a href="#ReferenceLocation">hyf:HY_HydroLocation</a><sup class="sup-c" title="class">c</sup><br />
[](referencedPosition)
### referencedPosition <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/referencedPosition`
Description | position expressed as measured or otherwise described distance from a known, already located referent. Commonly, this is used to locate a feature of interest such as a hydrometric station in relation to a catchment's outlet fixed by co-ordinates.
Range(s) |<a href="#HY_IndirectPosition">hyf:HY_IndirectPosition</a><sup class="sup-c" title="class">c</sup><br />
[](upperCatchment)
### upperCatchment <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/upperCatchment`
Description | catchment located immediately above of the catchment,
Range(s) |<a href="#HY_Catchment">hyf:HY_Catchment</a><sup class="sup-c" title="class">c</sup><br />
[](usage)
### usage <sup>op</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/usage`
Description | expresses the kind of name usage in a specific community, using a term from the HY_NameUsage code list, or a controlled vocabulary. Alternative code lists may be used but should be related to the terms in the HY_NameUsage codelist using an appropriate formalism.
Range(s) |<a href="#HY_NameUsage">hyf:HY_NameUsage</a><sup class="sup-c" title="class">c</sup><br />

## Datatype Properties
[HY_HydroFeatureName.name](HY_HydroFeatureName.name),
[absolute](absolute),
[accuracyStatement](accuracyStatement),
[interpolative](interpolative),
[namesPart](namesPart),
[precisionStatement](precisionStatement),
[variantSpelling](variantSpelling),
[](HY_HydroFeatureName.name)
### HY_HydroFeatureName.name <sup>dp</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeatureName.name`
Description | indicates whether the name applies to a part of feature only or not, using the Boolean value type
Domain(s) |<a href="#HY_HydroFeatureName">hyf:HY_HydroFeatureName</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](absolute)
### absolute <sup>dp</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/absolute`
Description | geometric expression of the distance from a located referent. An implementation may use the types described in ISO 19103: Conceptual Schema.
Range(s) |<a href="http://shapechange.net/resources/ont/base#Measure">sc:Measure</a><sup class="sup-c" title="class">c</sup><br />
[](accuracyStatement)
### accuracyStatement <sup>dp</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/accuracyStatement`
Description | simple statement whether the distance value agrees with the value accepted as being true.  This statement assumes that all known corrections have been applied. An implementation may use the types described in ISO 19103: Conceptual Schema.
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](interpolative)
### interpolative <sup>dp</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/interpolative`
Description | interpolative expression (percentage) of the distance from a located referent. An implementation may use the types described in ISO 19103: Conceptual Schema.
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#double">xsd:double</a><sup class="sup-c" title="class">c</sup><br />
[](namesPart)
### namesPart <sup>dp</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/namesPart`
Description | indicates whether the name applies to a part of feature only or not, using the Boolean value type
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#boolean">xsd:boolean</a><sup class="sup-c" title="class">c</sup><br />
[](precisionStatement)
### precisionStatement <sup>dp</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/precisionStatement`
Description | simple statement on the smallest unit of division on the scale of measurement. An implementation may use the types described in ISO 19103: Conceptual Schema.
Range(s) |<a href="http://shapechange.net/resources/ont/base#Measure">sc:Measure</a><sup class="sup-c" title="class">c</sup><br />
[](variantSpelling)
### variantSpelling <sup>dp</sup>
Property | Value
--- | ---
IRI | `https://www.opengis.net/def/appschema/hy_features/hyf/variantSpelling`
Description | indicates whether the name is a variant spelling or not using the Boolean value type.
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#boolean">xsd:boolean</a><sup class="sup-c" title="class">c</sup><br />

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
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sc**
  * `http://shapechange.net/resources/ont/base#`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Classes: c
* Object Properties :op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: dp
* Properties: p
* Named Individuals: ni