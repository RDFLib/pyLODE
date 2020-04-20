# Sensor, Observation, Sample, and Actuator (SOSA) Ontology
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://www.w3.org/ns/sosa/`
* **Creators(s)**
  * W3C/OGC Spatial Data on the Web Working Group
* **Created**
  * 2017-04-17
* **License &amp; Rights**
  * [http://www.opengeospatial.org/ogc/Software](http://www.opengeospatial.org/ogc/Software)
  * &copy; 2017 W3C/OGC.
* **Ontology RDF**
  * RDF ([sosa.ttl](turtle))
### Description
<p>This ontology is based on the SSN Ontology by the W3C Semantic Sensor Networks Incubator Group (SSN-XG), together with considerations from the W3C/OGC Spatial Data on the Web Working Group.</p>

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
[Actuatable Property](#ActuatableProperty),
[Actuation](#Actuation),
[Actuator](#Actuator),
[Agent](#Agent),
[Feature Of Interest](#FeatureOfInterest),
[Observable Property](#ObservableProperty),
[Observation](#Observation),
[Platform](#Platform),
[Procedure](#Procedure),
[Result](#Result),
[Sample](#Sample),
[Sampler](#Sampler),
[Sampling](#Sampling),
[Sensor](#Sensor),
[TemporalEntity](#TemporalEntity),
[Vocabulary](#Vocabulary),
### Vocabulary
Property | Value
--- | ---
IRI | `http://purl.org/vocommons/voaf#Vocabulary`
### TemporalEntity
Property | Value
--- | ---
IRI | `http://www.w3.org/2006/time#TemporalEntity`
### Actuatable Property
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/ActuatableProperty`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>An actuatable quality (property, characteristic) of a FeatureOfInterest.</p>
Example | A window actuator acts by changing the state between a frame and a window. The ability of the window to be opened and closed is its ActuatableProperty.
### Actuation
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Actuation`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>An Actuation carries out an (Actuation) Procedure to change the state of the world using an Actuator.</p>
Example | The activity of automatically closing a window if the temperature in a room drops below 20 degree Celsius. The activity is the Actuation and the device that closes the window is the Actuator. The Procedure is the rule, plan, or specification that defines the conditions that triggers the Actuation, here a drop in temperature. 
### Actuator
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Actuator`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>A device that is used by, or implements, an (Actuation) Procedure that changes the state of the world.</p>
Example | A window actuator for automatic window control, i.e., opening or closing the window.
### Feature Of Interest
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/FeatureOfInterest`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>The thing whose property is being estimated or calculated in the course of an Observation to arrive at a Result or whose property is being manipulated by an Actuator, or which is being sampled or transformed in an act of Sampling.</p>
Example | When measuring the height of a tree, the height is the observed ObservableProperty, 20m may be the Result of the Observation, and the tree is the FeatureOfInterest. A window is a FeatureOfInterest for an automatic window control Actuator.
### Observable Property
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/ObservableProperty`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>An observable quality (property, characteristic) of a FeatureOfInterest.</p>
Example | The height of a tree, the depth of a water body, or the temperature of a surface are examples of observable properties, while the value of a classic car is not (directly) observable but asserted.
### Observation
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Observation`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>Act of carrying out an (Observation) Procedure to estimate or calculate a value of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how; links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest to detail what that property was associated with.</p>
Example | The activity of estimating the intensity of an Earthquake using the Mercalli intensity scale is an Observation as is measuring the moment magnitude, i.e., the energy released by said earthquake.
### Platform
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Platform`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>A Platform is an entity that hosts other entities, particularly Sensors, Actuators, Samplers, and other Platforms.</p>
Example | A post, buoy, vehicle, ship, aircraft, satellite, cell-phone, human or animal may act as platforms for (technical or biological) sensors or actuators.
### Procedure
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Procedure`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>A workflow, protocol, plan, algorithm, or computational method specifying how to make an Observation, create a Sample, or make a change to the state of the world (via an Actuator). A Procedure is re-usable, and might be involved in many Observations, Samplings, or Actuations. It explains the steps to be carried out to arrive at reproducible results.</p>
Example | The measured wind speed differs depending on the height of the sensor above the surface, e.g., due to friction. Consequently, procedures for measuring wind speed define a standard height for anemometers above ground, typically 10m for meteorological measures and 2m in Agrometeorology. This definition of height, sensor placement, and so forth are defined by the Procedure.
### Result
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Result`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>The Result of an Observation, Actuation, or act of Sampling. To store an observation's simple result value one can use the hasSimpleResult property.</p>
Example | The value 20 as the height of a certain tree together with the unit, e.g., Meter.
### Sample
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Sample`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>Samples are artifacts of an observational strategy, and have no significant function outside of their role in the observation process. The characteristics of the samples themselves are of little interest, except perhaps to the manager of a sampling campaign.</p>
<p>A Sample is intended to sample some FatureOfInterest, so there is an expectation of at least one isSampleOf property. However, in some cases the identity, and even the exact type, of the sampled feature may not be known when observations are made using the sampling features.</p>
Example | A statistical sample is often designed to be characteristic of an entire population, so that observations can be made regarding the sample that provide a good estimate of the properties of the population.
### Sampler
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Sampler`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>A device that is used by, or implements, a Sampling Procedure to create or transform one or more samples.</p>
Example | A ball mill, diamond drill, hammer, hypodermic syringe and needle, image Sensor or a soil auger can all act as sampling devices (i.e., be Samplers). However, sometimes the distinction between the Sampler and the Sensor is not evident, as they are packaged as a unit. A Sampler need not be a physical device.
### Sampling
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Sampling`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>An act of Sampling carries out a sampling Procedure to create or transform one or more samples.</p>
Example | Crushing a rock sample in a ball mill.
### Sensor
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/Sensor`
Is Defined By | http://www.w3.org/ns/sosa/
Description | <p>Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure. Sensors respond to a stimulus, e.g., a change in the environment, or input data composed from the results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.</p>
Example | Accelerometers, gyroscopes, barometers, magnetometers, and so forth are Sensors that are typically mounted on a modern smart phone (which acts as Platform). Other examples of sensors include the human eyes.
### Agent
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Agent`

## Object Properties
[acts on property](#actsonproperty),
[has feature of interest](#hasfeatureofinterest),
[has result](#hasresult),
[has sample](#hassample),
[hosts](#hosts),
[is acted on by](#isactedonby),
[is feature of interest of](#isfeatureofinterestof),
[is hosted by](#ishostedby),
[is observed by](#isobservedby),
[is result of](#isresultof),
[is sample of](#issampleof),
[made actuation](#madeactuation),
[made by actuator](#madebyactuator),
[made by sampler](#madebysampler),
[made by sensor](#madebysensor),
[made observation](#madeobservation),
[made sampling](#madesampling),
[observed property](#observedproperty),
[observes](#observes),
[phenomenon time](#phenomenontime),
[used procedure](#usedprocedure),
[](actsonproperty)
### acts on property
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/actsOnProperty`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between an Actuation and the property of a FeatureOfInterest it is acting upon.
Example | <pre>In the activity (Actuation) of automatically closing a window if the temperature in a room drops below 20 degrees Celsius, the property on which the Actuator acts upon is the state of the window as it changes from being open to being closed. </pre>
[](hasfeatureofinterest)
### has feature of interest
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/hasFeatureOfInterest`
Is Defined By | http://www.w3.org/ns/sosa/
Description | A relation between an Observation and the entity whose quality was observed, or between an Actuation and the entity whose property was modified, or between an act of Sampling and the entity that was sampled.
Example | <pre>For example, in an Observation of the weight of a person, the FeatureOfInterest is the person and the property is its weight.</pre>
[](hasresult)
### has result
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/hasResult`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation linking an Observation or Actuation or act of Sampling and a Result or Sample.
[](hassample)
### has sample
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/hasSample`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between a FeatureOfInterest and the Sample used to represent it.
[](hosts)
### hosts
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/hosts`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between a Platform and a Sensor, Actuator, Sampler, or Platform, hosted or mounted on it.
[](isactedonby)
### is acted on by
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/isActedOnBy`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between an ActuatableProperty of a FeatureOfInterest and an Actuation changing its state.
Example | <pre>In the activity (Actuation) of automatically closing a window if the temperature in a room drops below 20 degrees Celsius, the property on which the Actuator acts upon is the state of the window as it changes from being open to being closed. </pre>
[](isfeatureofinterestof)
### is feature of interest of
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/isFeatureOfInterestOf`
Is Defined By | http://www.w3.org/ns/sosa/
Description | A relation between a FeatureOfInterest and an Observation about it, an Actuation acting on it, or an act of Sampling that sampled it.
[](ishostedby)
### is hosted by
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/isHostedBy`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between a Sensor, Actuator, Sampler, or Platform, and the Platform that it is mounted on or hosted by.
[](isobservedby)
### is observed by
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/isObservedBy`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between an ObservableProperty and the Sensor able to observe it.
[](isresultof)
### is result of
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/isResultOf`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation linking a Result to the Observation or Actuation or act of Sampling that created or caused it.
[](issampleof)
### is sample of
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/isSampleOf`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation from a Sample to the FeatureOfInterest that it is intended to be representative of.
[](madeactuation)
### made actuation
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/madeActuation`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between an Actuator and the Actuation it has made.
[](madebyactuator)
### made by actuator
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/madeByActuator`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation linking an Actuation to the Actuator that made that Actuation.
[](madebysampler)
### made by sampler
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/madeBySampler`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation linking an act of Sampling to the Sampler (sampling device or entity) that made it.
[](madebysensor)
### made by sensor
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/madeBySensor`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between an Observation and the Sensor which made the Observation.
[](madeobservation)
### made observation
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/madeObservation`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between a Sensor and an Observation made by the Sensor.
[](madesampling)
### made sampling
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/madeSampling`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between a Sampler (sampling device or entity) and the Sampling act it performed.
[](observedproperty)
### observed property
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/observedProperty`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation linking an Observation to the property that was observed. The ObservableProperty should be a property of the FeatureOfInterest (linked by hasFeatureOfInterest) of this Observation.
[](observes)
### observes
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/observes`
Is Defined By | http://www.w3.org/ns/sosa/
Description | Relation between a Sensor and an ObservableProperty that it is capable of sensing.
[](phenomenontime)
### phenomenon time
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/phenomenonTime`
Is Defined By | http://www.w3.org/ns/sosa/
Description | The time that the Result of an Observation, Actuation or Sampling applies to the FeatureOfInterest. Not necessarily the same as the resultTime. May be an Interval or an Instant, or some other compound TemporalEntity.
[](usedprocedure)
### used procedure
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/usedProcedure`
Is Defined By | http://www.w3.org/ns/sosa/
Description | A relation to link to a re-usable Procedure used in making an Observation, an Actuation, or a Sample, typically through a Sensor, Actuator or Sampler.

## Datatype Properties
[has simple result](#hassimpleresult),
[result time](#resulttime),
[](hassimpleresult)
### has simple result
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/hasSimpleResult`
Is Defined By | http://www.w3.org/ns/sosa/
Description | The simple value of an Observation or Actuation or act of Sampling.
Example | <pre>For instance, the values 23 or true.</pre>
[](resulttime)
### result time
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/sosa/resultTime`
Is Defined By | http://www.w3.org/ns/sosa/
Description | The result time is the instant of time when the Observation, Actuation or Sampling activity was completed.
Range(s) |[xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) (c)<br />

## Annotation Properties
[created](#created),
[creator](#creator),
[description](#description),
[license](#license),
[rights](#rights),
[title](#title),
[preferredNamespacePrefix](#preferredNamespacePrefix),
[preferredNamespaceUri](#preferredNamespaceUri),
[domainIncludes](#domainIncludes),
[rangeIncludes](#rangeIncludes),
[definition](#definition),
[example](#example),
[note](#note),
[name](#name),
[](created)
### created
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/created`
[](creator)
### creator
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/creator`
[](description)
### description
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/description`
[](license)
### license
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/license`
[](rights)
### rights
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/rights`
[](title)
### title
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/title`
[](preferredNamespacePrefix)
### preferredNamespacePrefix
Property | Value
--- | ---
IRI | `http://purl.org/vocab/vann/preferredNamespacePrefix`
[](preferredNamespaceUri)
### preferredNamespaceUri
Property | Value
--- | ---
IRI | `http://purl.org/vocab/vann/preferredNamespaceUri`
[](domainIncludes)
### domainIncludes
Property | Value
--- | ---
IRI | `http://schema.org/domainIncludes`
[](rangeIncludes)
### rangeIncludes
Property | Value
--- | ---
IRI | `http://schema.org/rangeIncludes`
[](definition)
### definition
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#definition`
[](example)
### example
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#example`
[](note)
### note
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#note`
[](name)
### name
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/name`

## Named Individuals
## Namespaces
* **dcterms**
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
* **vann**
  * `http://purl.org/vocab/vann/`
* **voaf**
  * `http://purl.org/vocommons/voaf#`
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