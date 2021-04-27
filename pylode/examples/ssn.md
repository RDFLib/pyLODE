Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Semantic Sensor Network Ontology

## Metadata
* **URI**
  * `http://www.w3.org/ns/ssn/`
* **Creators(s)**
  * W3C/OGC Spatial Data on the Web Working Group
* **Created**
  * 2017-04-17
* **Version Information**
  * New modular version of the SSN ontology.

This ontology was originally developed in 2009-2011 by the W3C Semantic Sensor Networks Incubator Group (SSN-XG). For more information on the group's activities see: http://www.w3.org/2005/Incubator/ssn/. The ontology was revised and modularized in 2015-2017 by the W3C/OGC Spatial Data on the Web Working Group, see: https://www.w3.org/2015/spatial/wiki/Semantic_Sensor_Network_Ontology.

In particular, (a) the scope is extended to include actuation and sampling; (b) the core concepts and properties are factored out into the SOSA ontology. The SSN ontology imports SOSA and adds formal axiomatization consistent with the text definitions in SOSA, and adds classes and properties to accommodate the scope of the original SSN ontology. 
* **Imports**
  * [sosa:](http://www.w3.org/ns/sosa/)
* **License &amp; Rights**
  * [http://www.opengeospatial.org/ogc/Software](http://www.opengeospatial.org/ogc/Software)
  * &copy; 2017 W3C/OGC.
* **Ontology RDF**
  * RDF ([ssn.ttl](turtle))
### Description
<p>Please report any errors to the W3C Spatial Data on the Web Working Group via the SDW WG Public List public-sdw-wg@w3.org</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Functional Properties](#functionalproperties)
1. [Annotation Properties](#annotationproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Actuation](#Actuation),
[Agent](#Agent),
[Deployment](#Deployment),
[Input](#Input),
[Observation](#Observation),
[Output](#Output),
[Property](#Property),
[Sampling](#Sampling),
[Stimulus](#Stimulus),
[System](#System),
[Vocabulary](#Vocabulary),
### Vocabulary
Property | Value
--- | ---
URI | `http://purl.org/vocommons/voaf#Vocabulary`
Has members |[ssn:](http://www.w3.org/ns/ssn/)<br />
### Actuation
Property | Value
--- | ---
URI | `http://www.w3.org/ns/sosa/Actuation`
Is Defined By | http://www.w3.org/ns/sosa/
Restrictions |[sosa:resultTime](http://www.w3.org/ns/sosa/resultTime) **exactly** 1<br />[sosa:actsOnProperty](http://www.w3.org/ns/sosa/actsOnProperty) **only** [sosa:ActuatableProperty](http://www.w3.org/ns/sosa/ActuatableProperty) (c)<br />[sosa:hasResult](http://www.w3.org/ns/sosa/hasResult) **min** 1<br />[sosa:madeByActuator](http://www.w3.org/ns/sosa/madeByActuator) **only** [sosa:Actuator](http://www.w3.org/ns/sosa/Actuator) (c)<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **only** [sosa:FeatureOfInterest](http://www.w3.org/ns/sosa/FeatureOfInterest) (c)<br />[sosa:usedProcedure](http://www.w3.org/ns/sosa/usedProcedure) **only** [sosa:Procedure](http://www.w3.org/ns/sosa/Procedure) (c)<br />[sosa:hasResult](http://www.w3.org/ns/sosa/hasResult) **only** [sosa:Result](http://www.w3.org/ns/sosa/Result) (c)<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **exactly** 1<br />[sosa:actsOnProperty](http://www.w3.org/ns/sosa/actsOnProperty) **min** 1<br />[sosa:madeByActuator](http://www.w3.org/ns/sosa/madeByActuator) **exactly** 1<br />
### Observation
Property | Value
--- | ---
URI | `http://www.w3.org/ns/sosa/Observation`
Is Defined By | http://www.w3.org/ns/sosa/
Restrictions |[ssn:wasOriginatedBy](http://www.w3.org/ns/ssn/wasOriginatedBy) (op) **only** [ssn:Stimulus](http://www.w3.org/ns/ssn/Stimulus) (c)<br />[sosa:madeBySensor](http://www.w3.org/ns/sosa/madeBySensor) **only** [sosa:Sensor](http://www.w3.org/ns/sosa/Sensor) (c)<br />[sosa:usedProcedure](http://www.w3.org/ns/sosa/usedProcedure) **only** [sosa:Procedure](http://www.w3.org/ns/sosa/Procedure) (c)<br />[sosa:hasResult](http://www.w3.org/ns/sosa/hasResult) **only** [sosa:Result](http://www.w3.org/ns/sosa/Result) (c)<br />[ssn:wasOriginatedBy](http://www.w3.org/ns/ssn/wasOriginatedBy) (op) **exactly** 1<br />[sosa:observedProperty](http://www.w3.org/ns/sosa/observedProperty) **exactly** 1<br />[sosa:phenomenonTime](http://www.w3.org/ns/sosa/phenomenonTime) **exactly** 1<br />[sosa:resultTime](http://www.w3.org/ns/sosa/resultTime) **exactly** 1<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **only** [sosa:FeatureOfInterest](http://www.w3.org/ns/sosa/FeatureOfInterest) (c)<br />[sosa:hasResult](http://www.w3.org/ns/sosa/hasResult) **min** 1<br />[sosa:observedProperty](http://www.w3.org/ns/sosa/observedProperty) **only** [sosa:ObservableProperty](http://www.w3.org/ns/sosa/ObservableProperty) (c)<br />[sosa:madeBySensor](http://www.w3.org/ns/sosa/madeBySensor) **exactly** 1<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **exactly** 1<br />
### Sampling
Property | Value
--- | ---
URI | `http://www.w3.org/ns/sosa/Sampling`
Is Defined By | http://www.w3.org/ns/sosa/
Restrictions |[sosa:usedProcedure](http://www.w3.org/ns/sosa/usedProcedure) **only** [sosa:Procedure](http://www.w3.org/ns/sosa/Procedure) (c)<br />[sosa:resultTime](http://www.w3.org/ns/sosa/resultTime) **exactly** 1<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **only** [sosa:FeatureOfInterest](http://www.w3.org/ns/sosa/FeatureOfInterest) (c)<br />[sosa:hasFeatureOfInterest](http://www.w3.org/ns/sosa/hasFeatureOfInterest) **exactly** 1<br />[sosa:hasResult](http://www.w3.org/ns/sosa/hasResult) **only** [sosa:Sample](http://www.w3.org/ns/sosa/Sample) (c)<br />[sosa:madeBySampler](http://www.w3.org/ns/sosa/madeBySampler) **only** [sosa:Sampler](http://www.w3.org/ns/sosa/Sampler) (c)<br />[sosa:madeBySampler](http://www.w3.org/ns/sosa/madeBySampler) **exactly** 1<br />[sosa:hasResult](http://www.w3.org/ns/sosa/hasResult) **min** 1<br />
### Deployment
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/Deployment`
Is Defined By | http://www.w3.org/ns/ssn/
Description | <p>Describes the Deployment of one or more Systems for a particular purpose. Deployment may be done on a Platform.</p>
Example | `For example, a temperature Sensor deployed on a wall, or a whole network of Sensors deployed for an Observation campaign.`<br />
Restrictions |[ssn:deployedOnPlatform](http://www.w3.org/ns/ssn/deployedOnPlatform) (op) **only** [sosa:Platform](http://www.w3.org/ns/sosa/Platform) (c)<br />[ssn:forProperty](http://www.w3.org/ns/ssn/forProperty) (op) **only** [ssn:Property](http://www.w3.org/ns/ssn/Property) (c)<br />[ssn:deployedSystem](http://www.w3.org/ns/ssn/deployedSystem) (op) **only** [ssn:System](http://www.w3.org/ns/ssn/System) (c)<br />
### Input
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/Input`
Is Defined By | http://www.w3.org/ns/ssn/
Description | <p>Any information that is provided to a Procedure for its use.</p>
Restrictions |[ub60bL143C60](ub60bL143C60) **min** 1<br />[ub60bL144C60](ub60bL144C60) **only** [sosa:Procedure](http://www.w3.org/ns/sosa/Procedure) (c)<br />
### Output
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/Output`
Is Defined By | http://www.w3.org/ns/ssn/
Description | <p>Any information that is reported from a Procedure.</p>
Restrictions |[ub60bL158C60](ub60bL158C60) **only** [sosa:Procedure](http://www.w3.org/ns/sosa/Procedure) (c)<br />[ub60bL157C60](ub60bL157C60) **min** 1<br />
### Property
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/Property`
Is Defined By | http://www.w3.org/ns/ssn/
Description | <p>A quality of an entity. An aspect of an entity that is intrinsic to and cannot exist without the entity.</p>
Restrictions |[ssn:isPropertyOf](http://www.w3.org/ns/ssn/isPropertyOf) (op) **only** [sosa:FeatureOfInterest](http://www.w3.org/ns/sosa/FeatureOfInterest) (c)<br />
Sub-classes |[sosa:ObservableProperty](http://www.w3.org/ns/sosa/ObservableProperty) (c)<br />[sosa:ActuatableProperty](http://www.w3.org/ns/sosa/ActuatableProperty) (c)<br />
### Stimulus
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/Stimulus`
Is Defined By | http://www.w3.org/ns/ssn/
Description | <p>An event in the real world that 'triggers' the Sensor. The properties associated to the Stimulus may be different to the eventual observed ObservableProperty. It is the event, not the object, that triggers the Sensor.</p>
Restrictions |[ub60bL298C56](ub60bL298C56) **only** [sosa:Observation](http://www.w3.org/ns/sosa/Observation) (c)<br />[ub60bL299C56](ub60bL299C56) **only** [sosa:Sensor](http://www.w3.org/ns/sosa/Sensor) (c)<br />[ssn:isProxyFor](http://www.w3.org/ns/ssn/isProxyFor) (op) **only** [sosa:ObservableProperty](http://www.w3.org/ns/sosa/ObservableProperty) (c)<br />
### System
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/System`
Is Defined By | http://www.w3.org/ns/ssn/
Description | <p>System is a unit of abstraction for pieces of infrastructure that implement Procedures. A System may have components, its subsystems, which are other systems.</p>
Restrictions |[ssn:hasDeployment](http://www.w3.org/ns/ssn/hasDeployment) (op) **only** [ssn:Deployment](http://www.w3.org/ns/ssn/Deployment) (c)<br />[ub60bL354C56](ub60bL354C56) **only** [ssn:System](http://www.w3.org/ns/ssn/System) (c)<br />[sosa:isHostedBy](http://www.w3.org/ns/sosa/isHostedBy) **only** [sosa:Platform](http://www.w3.org/ns/sosa/Platform) (c)<br />[ssn:implements](http://www.w3.org/ns/ssn/implements) (op) **only** [sosa:Procedure](http://www.w3.org/ns/sosa/Procedure) (c)<br />[ssn:hasSubSystem](http://www.w3.org/ns/ssn/hasSubSystem) (op) **only** [ssn:System](http://www.w3.org/ns/ssn/System) (c)<br />
Sub-classes |[sosa:Sensor](http://www.w3.org/ns/sosa/Sensor) (c)<br />[sosa:Actuator](http://www.w3.org/ns/sosa/Actuator) (c)<br />[sosa:Sampler](http://www.w3.org/ns/sosa/Sampler) (c)<br />
### Agent
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Agent`
Has members |[ub60bL33C19](ub60bL33C19)<br />

## Object Properties
[deployed on platform](#deployedonplatform),
[deployed system](#deployedsystem),
[detects](#detects),
[for property](#forproperty),
[has deployment](#hasdeployment),
[has input](#hasinput),
[has output](#hasoutput),
[has property](#hasproperty),
[has subsystem](#hassubsystem),
[implemented by](#implementedby),
[implements](#implements),
[in deployment](#indeployment),
[is property of](#ispropertyof),
[is proxy for](#isproxyfor),
[was originated by](#wasoriginatedby),
[](deployedonplatform)
### deployed on platform
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/deployedOnPlatform`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a Deployment and the Platform on which the Systems are deployed.
[](deployedsystem)
### deployed system
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/deployedSystem`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a Deployment and a deployed System.
[](detects)
### detects
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/detects`
Is Defined By | http://www.w3.org/ns/ssn/
Description | A relation from a Sensor to the Stimulus that the Sensor detects. The Stimulus itself will be serving as a proxy for some ObservableProperty.
[](forproperty)
### for property
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/forProperty`
Is Defined By | http://www.w3.org/ns/ssn/
Description | A relation between some aspect of an entity and a Property.
Example | ````For example, from a Sensor to the properties it can observe; from an Actuator to the properties it can act on; from a Deployment to the properties it was installed to observe or act on; from a SystemCapability to the Property the capability is described for.`<br />```
[](hasdeployment)
### has deployment
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/hasDeployment`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a System and a Deployment, recording that the System is deployed in that Deployment.
[](hasinput)
### has input
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/hasInput`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a Procedure and an Input to it.
[](hasoutput)
### has output
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/hasOutput`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a Procedure and an Output of it.
[](hasproperty)
### has property
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/hasProperty`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between an entity and a Property of that entity.
[](hassubsystem)
### has subsystem
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/hasSubSystem`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a System and its component parts.
[](implementedby)
### implemented by
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/implementedBy`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a Procedure (an algorithm, procedure or method) and an entity that implements that Procedure in some executable way.
Example | ````For example, the relationship between a scientific measuring Procedure and a sensor that senses via that Procedure.`<br />```
[](implements)
### implements
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/implements`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between an entity that implements a Procedure in some executable way and the Procedure (an algorithm, procedure or method).
Example | ````For example, the relationship between a sensor and the scientific measuring Procedure via which it senses.`<br />```
[](indeployment)
### in deployment
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/inDeployment`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a Platform and a Deployment, meaning that the deployedSystems of the Deployment are hosted on the Platform.
Example | ````For example, a relation between a buoy and a deployment of several Sensors.`<br />```
[](ispropertyof)
### is property of
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/isPropertyOf`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between a Property and the entity it belongs to.
[](isproxyfor)
### is proxy for
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/isProxyFor`
Is Defined By | http://www.w3.org/ns/ssn/
Description | A relation from a Stimulus to the Property that the Stimulus is serving as a proxy for.
Example | ````For example, the expansion of quicksilver is a stimulus that serves as a proxy for some temperature property. An increase or decrease in the velocity of spinning cups on a wind sensor is serving as a proxy for the wind speed.`<br />```
[](wasoriginatedby)
### was originated by
Property | Value
--- | ---
URI | `http://www.w3.org/ns/ssn/wasOriginatedBy`
Is Defined By | http://www.w3.org/ns/ssn/
Description | Relation between an Observation and the Stimulus that originated it.

## Functional Properties
[isSampleOf](#isSampleOf),
[](isSampleOf)
### isSampleOf
Property | Value
--- | ---
URI | `http://www.w3.org/ns/sosa/isSampleOf`
Is Defined By | http://www.w3.org/ns/sosa/

## Annotation Properties
[created](#created),
[creator](#creator),
[description](#description),
[license](#license),
[rights](#rights),
[title](#title),
[preferredNamespacePrefix](#preferredNamespacePrefix),
[preferredNamespaceUri](#preferredNamespaceUri),
[definition](#definition),
[example](#example),
[name](#name),
[](created)
### created
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/created`
[](creator)
### creator
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/creator`
[](description)
### description
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/description`
[](license)
### license
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/license`
[](rights)
### rights
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/rights`
[](title)
### title
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/title`
[](preferredNamespacePrefix)
### preferredNamespacePrefix
Property | Value
--- | ---
URI | `http://purl.org/vocab/vann/preferredNamespacePrefix`
[](preferredNamespaceUri)
### preferredNamespaceUri
Property | Value
--- | ---
URI | `http://purl.org/vocab/vann/preferredNamespaceUri`
[](definition)
### definition
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#definition`
[](example)
### example
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#example`
[](name)
### name
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/name`

## Named Individuals
## Namespaces
* **dct**
  * `http://purl.org/dc/terms/`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
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
* **sosa**
  * `http://www.w3.org/ns/sosa/`
* **ssn**
  * `http://www.w3.org/ns/ssn/`
* **vann**
  * `http://purl.org/vocab/vann/`
* **voaf**
  * `http://purl.org/vocommons/voaf#`
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