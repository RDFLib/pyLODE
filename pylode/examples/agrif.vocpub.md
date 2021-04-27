Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 

# The Australian Government Records Interoperability Framework (AGRIF) ontology
### A taxonomy

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/agrif`
* **Publisher(s)**
  * [Department of Finance](http://linked.data.gov.au/org/finance)
* **Creators(s)**
  * John Machin of [Department of Finance](https://www.finance.gov.au)
  * Katherine Stuart of [Department of Finance](https://www.finance.gov.au)
  * [Armin Haller](http://orcid.org/0000-0003-3425-0780)
    [[ORCID]](http://orcid.org/0000-0003-3425-0780)
    (<armin.haller@anu.edu.au></a>) of [Australian National University](https://www.anu.edu.au)
* **Contributor(s)**
  * Kerry Taylor
  * Pouya Ghiasnezhad Omran
  * Sergio José Rodríguez Méndez
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@surroundaustralia.com></a>)
* **Created**
  * 2016-12-06
* **Modified**
  * 2019-10-21
* **Version Information**
  * 0.9
* **Version URI**
  * [http://linked.data.gov.au/def/agrif/0.9](http://linked.data.gov.au/def/agrif/0.9)

* **License &amp; Rights**
  * [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
  * &copy; Commonwealth of Australia (Department of Finance) 2019

* **Taxonomy RDF**
  * RDF ([agrif.ttl](turtle))
### Description
<p>The Australian Government Records Interoperability Framework (AGRIF, ‘the Framework’) is a system of related semantic ontologies that describe the structure, functions, and activities of the Australian Government, providing sufficient context for the effective use – including but not limited to management – of Australian Government information assets. It complies with the World Wide Web Consortium’s Web Ontology Language (OWL2) Recommendation and makes reference to other Recommendations and existing domain ontologies for archival and preservation processes.</p>


## Table of Contents
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Concepts
* [Activity](http://linked.data.gov.au/def/agrif#Activity)
	* [Access Activity](http://linked.data.gov.au/def/agrif#AccessActivity)
	* [Maintain Activity](http://linked.data.gov.au/def/agrif#MaintainActivity)
	* [Share Activity](http://linked.data.gov.au/def/agrif#ShareActivity)
* [Agent](http://linked.data.gov.au/def/agrif#Agent)
	* [Organisation](http://linked.data.gov.au/def/agrif#Organisation)
		* [Organisational Unit](http://linked.data.gov.au/def/agrif#OrganisationalUnit)
	* [Person](http://linked.data.gov.au/def/agrif#Person)
* [Artefact](http://linked.data.gov.au/def/agrif#Artefact)
	* [Digital Artefact](http://linked.data.gov.au/def/agrif#DigitalArtefact)
	* [Physical Artefact](http://linked.data.gov.au/def/agrif#PhysicalArtefact)
* [Association](http://linked.data.gov.au/def/agrif#Association)
* [Classifier](http://linked.data.gov.au/def/agrif#Classifier)
* [Collection](http://linked.data.gov.au/def/agrif#Collection)
	* [Logical Collection](http://linked.data.gov.au/def/agrif#LogicalCollection)
	* [Physical Collection](http://linked.data.gov.au/def/agrif#PhysicalCollection)
* [Control](http://linked.data.gov.au/def/agrif#Control)
	* [Access Control](http://linked.data.gov.au/def/agrif#AccessControl)
		* [Security Classification](http://linked.data.gov.au/def/agrif#SecurityClassification)
	* [Security Control](http://linked.data.gov.au/def/agrif#SecurityControl)
* [Coverage](http://linked.data.gov.au/def/agrif#Coverage)
	* [Jurisdictional Coverage](http://linked.data.gov.au/def/agrif#JurisdictionalCoverage)
	* [Spatial Coverage](http://linked.data.gov.au/def/agrif#SpatialCoverage)
	* [Temporal Coverage](http://linked.data.gov.au/def/agrif#TemporalCoverage)
* [Event](http://linked.data.gov.au/def/agrif#Event)
	* [Artefact Change Event](http://linked.data.gov.au/def/agrif#ArtefactChangeEvent)
		* [Artefact Send Event](http://linked.data.gov.au/def/agrif#ArtefactSendEvent)
	* [Artefact Control Event](http://linked.data.gov.au/def/agrif#ArtefactControlEvent)
		* [Artefact Publish Event](http://linked.data.gov.au/def/agrif#ArtefactPublishEvent)
		* [Artefact Share Event](http://linked.data.gov.au/def/agrif#ArtefactShareEvent)
	* [Record Creation Event](http://linked.data.gov.au/def/agrif#CreationEvent)
	* [Record Control Event](http://linked.data.gov.au/def/agrif#RecordControlEvent)
		* [Record Audit Event](http://linked.data.gov.au/def/agrif#RecordAuditEvent)
		* [Record Decision Event](http://linked.data.gov.au/def/agrif#RecordDecisionEvent)
		* [Record Disposal Event](http://linked.data.gov.au/def/agrif#RecordDisposalEvent)
			* [Record Destruction Event](http://linked.data.gov.au/def/agrif#RecordDestructionEvent)
			* [Record Freeze Event](http://linked.data.gov.au/def/agrif#RecordFreezeEvent)
			* [Record Transfer Event](http://linked.data.gov.au/def/agrif#RecordTransferEvent)
		* [Record Replacement Event](http://linked.data.gov.au/def/agrif#RecordReplacementEvent)
		* [Record Sentencing Event](http://linked.data.gov.au/def/agrif#RecordSentencingEvent)
* [Form Factor](http://linked.data.gov.au/def/agrif#FormFactor)
* [Function](http://linked.data.gov.au/def/agrif#Function)
	* [AGIFT Function](http://linked.data.gov.au/def/agrif#AGIFTFunction)
	* [Records Authority Function](http://linked.data.gov.au/def/agrif#RecordsAuthorityFunction)
* [Information System](http://linked.data.gov.au/def/agrif#InformationSystem)
	* [Intellectual Control System](http://linked.data.gov.au/def/agrif#IntellectualControlSystem)
		* [Controlled Vocabulary](http://linked.data.gov.au/def/agrif#ControlledVocabulary)
		* [Series](http://linked.data.gov.au/def/agrif#Series)
* [Manifest](http://linked.data.gov.au/def/agrif#Manifest)
* [Permission](http://linked.data.gov.au/def/agrif#Permission)
* [Policy](http://linked.data.gov.au/def/agrif#Policy)
	* [Digital Preservation Policy](http://linked.data.gov.au/def/agrif#DigitalPreservationPolicy)
	* [Information Management Policy](http://linked.data.gov.au/def/agrif#InformationManagementPolicy)
	* [Minimum Metadata Set Policy](http://linked.data.gov.au/def/agrif#MinimumMetadataSetPolicy)
	* [Record Storage Standard](http://linked.data.gov.au/def/agrif#RecordStorageStandard)
	* [Records Authority Disposal Class Policy](http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy)
		* [Disposal Class](http://linked.data.gov.au/def/agrif#DisposalClass)
* [Quality](http://linked.data.gov.au/def/agrif#Quality)
	* [Preservation Quality](http://linked.data.gov.au/def/agrif#PreservationQuality)
* [Record](http://linked.data.gov.au/def/agrif#Record)
* [Role](http://linked.data.gov.au/def/agrif#Role)
	* [Administrator](http://linked.data.gov.au/def/agrif#Administrator)
	* [Business Owner](http://linked.data.gov.au/def/agrif#BusinessOwner)
	* [Creator](http://linked.data.gov.au/def/agrif#Creator)
	* [User](http://linked.data.gov.au/def/agrif#User)
* [Spatial Location](http://linked.data.gov.au/def/agrif#SpatialLocation)
	* [Holding Space](http://linked.data.gov.au/def/agrif#HoldingSpace)
		* [Digital Holding Space](http://linked.data.gov.au/def/agrif#DigitalHoldingSpace)
		* [Physical Holding Space](http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace)
* [Status](http://linked.data.gov.au/def/agrif#Status)
	* [Decision Status](http://linked.data.gov.au/def/agrif#DecisionStatus)
* [Trigger](http://linked.data.gov.au/def/agrif#Trigger)
	* [Access Trigger](http://linked.data.gov.au/def/agrif#AccessTrigger)
* [Version History](http://linked.data.gov.au/def/agrif#VersionHistory)
* [None](ub64bL849C45)

### AGIFT Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AGIFTFunction`
Preferred Labels |AGIFT Function (en)<br />
Definitions |["An AGIFT Function is a Function that classifies a Record according to the Australian Governments' Interactive Functions Thesaurus."]<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Function](http://linked.data.gov.au/def/agrif#Function) (cp)<br />
### Access Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AccessActivity`
Preferred Labels |Access Activity (en)<br />
Definitions |['An Access Activity is an Activity where a Record is accessed by an Agent over a period of time.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Activity](http://linked.data.gov.au/def/agrif#Activity) (cp)<br />
### Access Control
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AccessControl`
Preferred Labels |Access Control (en)<br />
Definitions |['Access Control is the selective restriction of access to a Record or Artefact.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Control](http://linked.data.gov.au/def/agrif#Control) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification) (cp)<br />
### Access Trigger
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AccessTrigger`
Preferred Labels |Access Trigger (en)<br />
Definitions |['An Access Trigger is a Trigger that can be initiated when a Record is accessed.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Trigger](http://linked.data.gov.au/def/agrif#Trigger) (cp)<br />
### Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Activity`
Preferred Labels |Activity (en)<br />
Definitions |['An Activity is something that occurs over a period of time on a Record.']<br />
Source | https://www.w3.org/TR/prov-o/#Activity
Narrower Concepts |[http://linked.data.gov.au/def/agrif#ShareActivity](http://linked.data.gov.au/def/agrif#ShareActivity) (cp)<br />[http://linked.data.gov.au/def/agrif#AccessActivity](http://linked.data.gov.au/def/agrif#AccessActivity) (cp)<br />[http://linked.data.gov.au/def/agrif#MaintainActivity](http://linked.data.gov.au/def/agrif#MaintainActivity) (cp)<br />
### Administrator
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Administrator`
Preferred Labels |Administrator (en)<br />
Definitions |['An Administrator is a Role that has overall responsibility for the administration and functions of an Information System, but not necessarily for the information stored within.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Role](http://linked.data.gov.au/def/agrif#Role) (cp)<br />
### Agent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Agent`
Preferred Labels |Agent (en)<br />
Definitions |['An Agent is a corporate entity, organisational element or system, or individual responsible for the performance of some Activity or Event, including those on Records.']<br />
Source | https://www.w3.org/TR/prov-o/#Agent
Narrower Concepts |[http://linked.data.gov.au/def/agrif#Organisation](http://linked.data.gov.au/def/agrif#Organisation) (cp)<br />[http://linked.data.gov.au/def/agrif#Person](http://linked.data.gov.au/def/agrif#Person) (cp)<br />
### Artefact
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Artefact`
Preferred Labels |Artefact (en)<br />
Definitions |['An Artefact is an object that is made by a Person and that is to be preserved.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#DigitalArtefact](http://linked.data.gov.au/def/agrif#DigitalArtefact) (cp)<br />[http://linked.data.gov.au/def/agrif#PhysicalArtefact](http://linked.data.gov.au/def/agrif#PhysicalArtefact) (cp)<br />
### Artefact Change Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactChangeEvent`
Preferred Labels |Artefact Change Event (en)<br />
Definitions |['An Artefact Change Event is an Event that results in a new version of an Artefact.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Event](http://linked.data.gov.au/def/agrif#Event) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#ArtefactSendEvent](http://linked.data.gov.au/def/agrif#ArtefactSendEvent) (cp)<br />
### Artefact Control Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactControlEvent`
Preferred Labels |Artefact Control Event (en)<br />
Definitions |['An Artefact Control Event is an Event that requires a particular level of access to an Artefact.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Event](http://linked.data.gov.au/def/agrif#Event) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#ArtefactPublishEvent](http://linked.data.gov.au/def/agrif#ArtefactPublishEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#ArtefactShareEvent](http://linked.data.gov.au/def/agrif#ArtefactShareEvent) (cp)<br />
### Artefact Publish Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactPublishEvent`
Preferred Labels |Artefact Publish Event (en)<br />
Definitions |['An Artefact Publish Event is an Event that gives indiscriminate access to an Artefact to a set of Agents.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#ArtefactControlEvent](http://linked.data.gov.au/def/agrif#ArtefactControlEvent) (cp)<br />
### Artefact Send Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactSendEvent`
Preferred Labels |Artefact Send Event (en)<br />
Definitions |['An Artefact Send Event is an Event that results in a new version or a set of new versions of an Artefact at a target Agent or a set of target Agents.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#ArtefactChangeEvent](http://linked.data.gov.au/def/agrif#ArtefactChangeEvent) (cp)<br />
### Artefact Share Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactShareEvent`
Preferred Labels |Artefact Share Event (en)<br />
Definitions |['An Artefact Share Event is an Event that gives access to an Artefact to an Agent or a defined set of Agents.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#ArtefactControlEvent](http://linked.data.gov.au/def/agrif#ArtefactControlEvent) (cp)<br />
### Association
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Association`
Preferred Labels |Association (en)<br />
Definitions |['An Association is a qualified assignment of responsibility to an Agent in an Activity or Event, indicating that the Agent had a Role in the Activity.']<br />
Source | https://www.w3.org/TR/prov-o/#Association
### Business Owner
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#BusinessOwner`
Preferred Labels |Business Owner (en)<br />
Definitions |['A Business Owner is the Role that has the managerial control of a Function.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Role](http://linked.data.gov.au/def/agrif#Role) (cp)<br />
### Classifier
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Classifier`
Preferred Labels |Classifier (en)<br />
Definitions |['A Classifier is a machine-generated and applied category that a set of Records belong to.']<br />
### Collection
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Collection`
Preferred Labels |Collection (en)<br />
Definitions |['A Collection is an aggregation of Artefact items.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#LogicalCollection](http://linked.data.gov.au/def/agrif#LogicalCollection) (cp)<br />[http://linked.data.gov.au/def/agrif#PhysicalCollection](http://linked.data.gov.au/def/agrif#PhysicalCollection) (cp)<br />
### Control
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Control`
Preferred Labels |Control (en)<br />
Definitions |['A Control is a security or access measure that safeguards or restricts access to an asset.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#AccessControl](http://linked.data.gov.au/def/agrif#AccessControl) (cp)<br />[http://linked.data.gov.au/def/agrif#SecurityControl](http://linked.data.gov.au/def/agrif#SecurityControl) (cp)<br />
### Controlled Vocabulary
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ControlledVocabulary`
Preferred Labels |Controlled Vocabulary (en)<br />
Definitions |['A Controlled Vocabulary is an Intellectual Control System that provides a way to organize Records that facilitates a later discovery of a Record.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#IntellectualControlSystem](http://linked.data.gov.au/def/agrif#IntellectualControlSystem) (cp)<br />
### Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Coverage`
Preferred Labels |Coverage (en)<br />
Definitions |['A Coverage denotes the jurisdictional applicability, or the temporal and/or spatial extent to which a Record is observed.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#JurisdictionalCoverage](http://linked.data.gov.au/def/agrif#JurisdictionalCoverage) (cp)<br />[http://linked.data.gov.au/def/agrif#TemporalCoverage](http://linked.data.gov.au/def/agrif#TemporalCoverage) (cp)<br />[http://linked.data.gov.au/def/agrif#SpatialCoverage](http://linked.data.gov.au/def/agrif#SpatialCoverage) (cp)<br />
### Record Creation Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#CreationEvent`
Preferred Labels |Record Creation Event (en)<br />
Definitions |['A Record Creation Event is an Event that results in the creation of a Record.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Event](http://linked.data.gov.au/def/agrif#Event) (cp)<br />
### Creator
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Creator`
Preferred Labels |Creator (en)<br />
Definitions |['A Creator is the Agent that has created a Record or Artefact.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Role](http://linked.data.gov.au/def/agrif#Role) (cp)<br />
### Decision Status
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DecisionStatus`
Preferred Labels |Decision Status (en)<br />
Definitions |['A Decision Status is a Status that indicates the approval or disapproval of a Decision Event.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Status](http://linked.data.gov.au/def/agrif#Status) (cp)<br />
### Digital Artefact
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DigitalArtefact`
Preferred Labels |Digital Artefact (en)<br />
Definitions |['A Digital Artefact is an Artefact that is of a digital nature and stored in an Information System.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Artefact](http://linked.data.gov.au/def/agrif#Artefact) (cp)<br />
### Digital Holding Space
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DigitalHoldingSpace`
Preferred Labels |Digital Holding Space (en)<br />
Definitions |['A Digital Holding Space is a space that is used or reserved for the storage of a Digital Artefact on a storage medium or virtual storage space.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#HoldingSpace](http://linked.data.gov.au/def/agrif#HoldingSpace) (cp)<br />
### Digital Preservation Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DigitalPreservationPolicy`
Preferred Labels |Digital Preservation Policy (en)<br />
Definitions |['The Digital Preservation Policy defines the process of active management by which the National Archives ensures that a digital object will be accessible in the future.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Policy](http://linked.data.gov.au/def/agrif#Policy) (cp)<br />
### Disposal Class
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DisposalClass`
Preferred Labels |Disposal Class (en)<br />
Definitions |['A Disposal Class is a Policy that defines the sentencing requirements of an item.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy](http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy) (cp)<br />
### Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Event`
Preferred Labels |Event (en)<br />
Definitions |['An Event denotes an instantaneous transition in the world.']<br />
Source | https://www.w3.org/TR/prov-o/#InstantaneousEvent
Narrower Concepts |[http://linked.data.gov.au/def/agrif#RecordControlEvent](http://linked.data.gov.au/def/agrif#RecordControlEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#CreationEvent](http://linked.data.gov.au/def/agrif#CreationEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#ArtefactControlEvent](http://linked.data.gov.au/def/agrif#ArtefactControlEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#ArtefactChangeEvent](http://linked.data.gov.au/def/agrif#ArtefactChangeEvent) (cp)<br />
### Form Factor
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#FormFactor`
Preferred Labels |Form Factor (en)<br />
Definitions |['A Form Factor defines and prescribes the size, shape, and other physical specifications of a Physical Artefact that is stored.']<br />
### Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Function`
Preferred Labels |Function (en)<br />
Definitions |['A Function is a process that is performed routinely to carry out a part of the mandate of an Australian Government Agency.', 'A Function reflects the responsibilities of an Organisation that can be delegated through official channels. [Commonwealth Records Series Manual]']<br />['A Function is a process that is performed routinely to carry out a part of the mandate of an Australian Government Agency.', 'A Function reflects the responsibilities of an Organisation that can be delegated through official channels. [Commonwealth Records Series Manual]']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#RecordsAuthorityFunction](http://linked.data.gov.au/def/agrif#RecordsAuthorityFunction) (cp)<br />[http://linked.data.gov.au/def/agrif#AGIFTFunction](http://linked.data.gov.au/def/agrif#AGIFTFunction) (cp)<br />
### Holding Space
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#HoldingSpace`
Preferred Labels |Holding Space (en)<br />
Definitions |['A Holding Space is a space that is used or reserved for the storage of an Artefact.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#SpatialLocation](http://linked.data.gov.au/def/agrif#SpatialLocation) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace](http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace) (cp)<br />[http://linked.data.gov.au/def/agrif#DigitalHoldingSpace](http://linked.data.gov.au/def/agrif#DigitalHoldingSpace) (cp)<br />
### Information Management Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#InformationManagementPolicy`
Preferred Labels |Information Management Policy (en)<br />
Definitions |['An Information Management Policy is a Policy that helps to align information management practices to fulfill the requirements of an information governance framework. An Information Management Policy provides direction and guidance to staff for creating, capturing and managing information to satisfy business, legal and stakeholder requirements, and assigns responsibilities across the agency.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Policy](http://linked.data.gov.au/def/agrif#Policy) (cp)<br />
### Information System
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#InformationSystem`
Preferred Labels |Information System (en)<br />
Definitions |['An Information System is an organized system for the collection, organization, storage and communication of information, typically Digital Artefacts or Records.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#IntellectualControlSystem](http://linked.data.gov.au/def/agrif#IntellectualControlSystem) (cp)<br />
### Intellectual Control System
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#IntellectualControlSystem`
Preferred Labels |Intellectual Control System (en)<br />
Definitions |['An Intellectual Control System is a System that enables Agents to locate and manage information.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#InformationSystem](http://linked.data.gov.au/def/agrif#InformationSystem) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#Series](http://linked.data.gov.au/def/agrif#Series) (cp)<br />[http://linked.data.gov.au/def/agrif#ControlledVocabulary](http://linked.data.gov.au/def/agrif#ControlledVocabulary) (cp)<br />
### Jurisdictional Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#JurisdictionalCoverage`
Preferred Labels |Jurisdictional Coverage (en)<br />
Definitions |['A Jurisdictional Coverage denotes the jurisdictional applicability of the Record.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Coverage](http://linked.data.gov.au/def/agrif#Coverage) (cp)<br />
### Logical Collection
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#LogicalCollection`
Preferred Labels |Logical Collection (en)<br />
Definitions |['A Logical Collection is an aggregation of Artefact items that are stored within one physical file.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Collection](http://linked.data.gov.au/def/agrif#Collection) (cp)<br />
### Maintain Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#MaintainActivity`
Preferred Labels |Maintain Activity (en)<br />
Definitions |['A Maintain Activity is an Activity to maintain a Record over a period of time due to a BusinessFunction or Policy.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Activity](http://linked.data.gov.au/def/agrif#Activity) (cp)<br />
### Manifest
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Manifest`
Preferred Labels |Manifest (en)<br />
Definitions |["A Manifest describes the files involved in the transfer of a Record from an Agency to the National Archives, including details such as the filesize, the destination hierarchy and the file's metadata."]<br />
### Minimum Metadata Set Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#MinimumMetadataSetPolicy`
Preferred Labels |Minimum Metadata Set Policy (en)<br />
Definitions |['The Minimum Metadata Set Policy is a Policy that has been developed by the National Archives of Australia to identify metadata properties essential for agency management of information as well as those needed for records which will be transferred to the Archives. It supports the Digital Continuity 2020 principles of interoperable systems and processes and is a practical application of the Australian Government Recordkeeping Metadata Standard 2.2 (AGRkMS) to support metadata implementation and information use in agencies.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Policy](http://linked.data.gov.au/def/agrif#Policy) (cp)<br />
### Organisation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Organisation`
Preferred Labels |Organisation (en)<br />
Definitions |['An Organisation is a type of Agent that denotes a social or legal institution such as a government agency, a corporation, society, etc.']<br />
Source | https://www.w3.org/TR/prov-o/#Organization
Broader Concepts |[http://linked.data.gov.au/def/agrif#Agent](http://linked.data.gov.au/def/agrif#Agent) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#OrganisationalUnit](http://linked.data.gov.au/def/agrif#OrganisationalUnit) (cp)<br />
### Organisational Unit
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#OrganisationalUnit`
Preferred Labels |Organisational Unit (en)<br />
Definitions |['An Organisational Unit is a division of labour typically organised around a business function that form part of the Organisation.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Organisation](http://linked.data.gov.au/def/agrif#Organisation) (cp)<br />
### Permission
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Permission`
Preferred Labels |Permission (en)<br />Security Clearance (en)<br />
Definitions |['A Permission denotes the Security Clearance of an Agent that determines its access and use rights.']<br />
Source | Australian Government Recordkeeping Metadata Standard
### Person
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Person`
Preferred Labels |Person (en)<br />
Definitions |['A Person is an Agent that denotes a human.']<br />
Source | https://www.w3.org/TR/prov-o/#Person
Broader Concepts |[http://linked.data.gov.au/def/agrif#Agent](http://linked.data.gov.au/def/agrif#Agent) (cp)<br />
### Physical Artefact
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PhysicalArtefact`
Preferred Labels |Physical Artefact (en)<br />
Definitions |['A Physical Artefact is an Artefact that is of physical nature.']<br />
Examples |`An example of a Phyiscal Artefact in the context of record keeping is information printed or written on paper.`<br /><br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Artefact](http://linked.data.gov.au/def/agrif#Artefact) (cp)<br />
### Physical Collection
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PhysicalCollection`
Preferred Labels |Physical Collection (en)<br />
Definitions |['A Physical Collection is an aggregation of Artefact items that are stored in separate physical files.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Collection](http://linked.data.gov.au/def/agrif#Collection) (cp)<br />
### Physical Holding Space
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace`
Preferred Labels |Physical Holding Space (en)<br />
Definitions |['A Physical Holding Space is a Spatial Location that is used or reserved for the storage of a Physical Artefact.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#HoldingSpace](http://linked.data.gov.au/def/agrif#HoldingSpace) (cp)<br />
### Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Policy`
Preferred Labels |Policy (en)<br />
Definitions |['A Policy is a deliberate system of principles to guide decisions and achieve rational outcomes.']<br />
Source | http://purl.org/dc/terms/Policy
Narrower Concepts |[http://linked.data.gov.au/def/agrif#InformationManagementPolicy](http://linked.data.gov.au/def/agrif#InformationManagementPolicy) (cp)<br />[http://linked.data.gov.au/def/agrif#MinimumMetadataSetPolicy](http://linked.data.gov.au/def/agrif#MinimumMetadataSetPolicy) (cp)<br />[http://linked.data.gov.au/def/agrif#DigitalPreservationPolicy](http://linked.data.gov.au/def/agrif#DigitalPreservationPolicy) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordStorageStandard](http://linked.data.gov.au/def/agrif#RecordStorageStandard) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy](http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy) (cp)<br />
### Preservation Quality
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PreservationQuality`
Preferred Labels |Preservation Quality (en)<br />
Definitions |['A Preservation Quality describes a Quality of an Artefact that supports or threatens the long term preservation of the information that is to be preserved.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Quality](http://linked.data.gov.au/def/agrif#Quality) (cp)<br />
### Quality
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Quality`
Preferred Labels |Quality (en)<br />
Definitions |['A Quality is an attribute that is intrinsically associated with an entity.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#PreservationQuality](http://linked.data.gov.au/def/agrif#PreservationQuality) (cp)<br />
### Record
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Record`
Preferred Labels |Record (en)<br />
Definitions |['A Record is information in any format created, received and maintained as evidence by an Organisation or Person, in pursuance of legal obligations or in the transaction of business. A Record may comprise a Digital or Physical Artefact.']<br />
### Record Audit Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordAuditEvent`
Preferred Labels |Record Audit Event (en)<br />
Definitions |['An Record Audit Event is the systematic examination of a Record to ascertain how and where the Record is stored, who created it, or manages it, who uses it and how much longer the Record is required to be maintained.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordControlEvent](http://linked.data.gov.au/def/agrif#RecordControlEvent) (cp)<br />
### Record Control Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordControlEvent`
Preferred Labels |Record Control Event (en)<br />
Definitions |['A Record Control Event is an Event that requires a particular level of access to the Record.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Event](http://linked.data.gov.au/def/agrif#Event) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#RecordSentencingEvent](http://linked.data.gov.au/def/agrif#RecordSentencingEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordDecisionEvent](http://linked.data.gov.au/def/agrif#RecordDecisionEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordReplacementEvent](http://linked.data.gov.au/def/agrif#RecordReplacementEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordAuditEvent](http://linked.data.gov.au/def/agrif#RecordAuditEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordDisposalEvent](http://linked.data.gov.au/def/agrif#RecordDisposalEvent) (cp)<br />
### Record Decision Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordDecisionEvent`
Preferred Labels |Record Decision Event (en)<br />
Definitions |['A Record Decision Event changes the Decision Status on the Control of a Record.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordControlEvent](http://linked.data.gov.au/def/agrif#RecordControlEvent) (cp)<br />
### Record Destruction Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordDestructionEvent`
Preferred Labels |Record Destruction Event (en)<br />
Definitions |['A Record Destruction Event is a Disposal Event that results in the regular authorised permanent desctruction of a Record that is no longer required for business purposes.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordDisposalEvent](http://linked.data.gov.au/def/agrif#RecordDisposalEvent) (cp)<br />
### Record Disposal Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordDisposalEvent`
Preferred Labels |Record Disposal Event (en)<br />
Definitions |['A Record Disposal Event is an Event that results in the regular authorised destruction or change of custody of a Record that is no longer required for business purposes.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordControlEvent](http://linked.data.gov.au/def/agrif#RecordControlEvent) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#RecordDestructionEvent](http://linked.data.gov.au/def/agrif#RecordDestructionEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordFreezeEvent](http://linked.data.gov.au/def/agrif#RecordFreezeEvent) (cp)<br />[http://linked.data.gov.au/def/agrif#RecordTransferEvent](http://linked.data.gov.au/def/agrif#RecordTransferEvent) (cp)<br />
### Record Freeze Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordFreezeEvent`
Preferred Labels |Record Freeze Event (en)<br />
Definitions |["A Record Freeze Event is a Disposal Event that leads to a records disposal freeze or retention notice in support of compliance requirements or an identified need to suspend the Archives' records destruction permissions."]<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordDisposalEvent](http://linked.data.gov.au/def/agrif#RecordDisposalEvent) (cp)<br />
### Record Replacement Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordReplacementEvent`
Preferred Labels |Record Replacement Event (en)<br />
Definitions |['A Record Replacement Event is an Event that results in the replacement of a Record with a new version. Edits to a Record constitute a Replace Event.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordControlEvent](http://linked.data.gov.au/def/agrif#RecordControlEvent) (cp)<br />
### Record Sentencing Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordSentencingEvent`
Preferred Labels |Record Sentencing Event (en)<br />
Definitions |['A Record Sentencing Event is an Event that classifies an Agencies Record to a specific class of a Records Authority Disposal Class Policy. This helps determine the Records value and how it should be managed throughout its lifecycle.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordControlEvent](http://linked.data.gov.au/def/agrif#RecordControlEvent) (cp)<br />
### Record Storage Standard
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordStorageStandard`
Preferred Labels |Record Storage Standard (en)<br />
Definitions |['The Standard for the storage of non-digital archival Records is designed to set out the requirements for the safe storage and preservation of non-digital records in the Archives’ custody; to ensure all non-digital records are protected, secure and accessible for as long as they are required to meet business and accountability needs and community expectations; and to ensure all non-digital records are stored in the most cost-effective manner possible.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Policy](http://linked.data.gov.au/def/agrif#Policy) (cp)<br />
### Record Transfer Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordTransferEvent`
Preferred Labels |Record Transfer Event (en)<br />
Definitions |['A Transfer Event is a Disposal Event that results in a change of custody.']<br />
Examples |`An example of a Record Transfer Event is the transfer of a Record from an Agency to the National Archives. Section 27 of the Archives Act 1983 requires Australian government agencies to transfer Records to the Archives within 15 years of their creation.`<br /><br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#RecordDisposalEvent](http://linked.data.gov.au/def/agrif#RecordDisposalEvent) (cp)<br />
### Records Authority Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityFunction`
Preferred Labels |Records Authority Function (en)<br />
Definitions |['A Records Authority Function is a Function that is assigned by the National Archives to classify Agency business.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Function](http://linked.data.gov.au/def/agrif#Function) (cp)<br />
### Records Authority Disposal Class Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy`
Preferred Labels |Records Authority Disposal Class Policy (en)<br />
Definitions |['A Records Authority Disposal Class Policy is a Policy that identifies the specific disposal class that authorises the retention or destruction of a Record.']<br />
Source | Australian Government Recordkeeping Metadata Standard
Broader Concepts |[http://linked.data.gov.au/def/agrif#Policy](http://linked.data.gov.au/def/agrif#Policy) (cp)<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#DisposalClass](http://linked.data.gov.au/def/agrif#DisposalClass) (cp)<br />
### Role
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Role`
Preferred Labels |Role (en)<br />
Definitions |['A Role is the function of an entity or agent with respect to an Activity or Event, in the context of a usage, generation, invalidation, association, start, and end.']<br />
Source | https://www.w3.org/TR/prov-o/#Role
Narrower Concepts |[http://linked.data.gov.au/def/agrif#Creator](http://linked.data.gov.au/def/agrif#Creator) (cp)<br />[http://linked.data.gov.au/def/agrif#Administrator](http://linked.data.gov.au/def/agrif#Administrator) (cp)<br />[http://linked.data.gov.au/def/agrif#User](http://linked.data.gov.au/def/agrif#User) (cp)<br />[http://linked.data.gov.au/def/agrif#BusinessOwner](http://linked.data.gov.au/def/agrif#BusinessOwner) (cp)<br />
### Security Classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SecurityClassification`
Preferred Labels |Security Classification (en)<br />
Definitions |['A Security Classification denotes the security status of a Record that an Agent needs to possess to access the Record.']<br />
Source | Australian Government Recordkeeping Metadata Standard
Broader Concepts |[http://linked.data.gov.au/def/agrif#AccessControl](http://linked.data.gov.au/def/agrif#AccessControl) (cp)<br />
### Security Control
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SecurityControl`
Preferred Labels |Security Control (en)<br />
Definitions |['A Security Control is a safeguard or countermeasures to avoid, detect, counteract, or minimize security risks to a Record or Artefact.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Control](http://linked.data.gov.au/def/agrif#Control) (cp)<br />
### Series
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Series`
Preferred Labels |Series (en)<br />
Definitions |['A Series is an identifier for an item, and when combined with a control symbol gives an item its intellectual context.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#IntellectualControlSystem](http://linked.data.gov.au/def/agrif#IntellectualControlSystem) (cp)<br />
### Share Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ShareActivity`
Preferred Labels |Share Activity (en)<br />
Definitions |['A Share Activity is an Activity where the custodianship of a Record is transferred to or shared with Agents over a period of time.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Activity](http://linked.data.gov.au/def/agrif#Activity) (cp)<br />
### Spatial Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SpatialCoverage`
Preferred Labels |Spatial Coverage (en)<br />
Definitions |['A Spatial Coverage denotes the spatial extent to which a Record is observed.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Coverage](http://linked.data.gov.au/def/agrif#Coverage) (cp)<br />
### Spatial Location
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SpatialLocation`
Preferred Labels |Spatial Location (en)<br />
Definitions |['A Spatial Location describes where a something (e.g. a Record, Collection or Artefact) is physically located, using geospatial coordinates such as latitude and longitude.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#HoldingSpace](http://linked.data.gov.au/def/agrif#HoldingSpace) (cp)<br />
### Status
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Status`
Preferred Labels |Status (en)<br />
Definitions |['A Status indicates an Activities current state.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#DecisionStatus](http://linked.data.gov.au/def/agrif#DecisionStatus) (cp)<br />
### Temporal Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#TemporalCoverage`
Preferred Labels |Temporal Coverage (en)<br />
Definitions |['A Temporal Coverage denotes the temporal extent to which a Record is observed.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Coverage](http://linked.data.gov.au/def/agrif#Coverage) (cp)<br />
### Trigger
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Trigger`
Preferred Labels |Trigger (en)<br />
Definitions |['A Trigger is an entity that initiated an Activity or Event.']<br />
Narrower Concepts |[http://linked.data.gov.au/def/agrif#AccessTrigger](http://linked.data.gov.au/def/agrif#AccessTrigger) (cp)<br />
### User
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#User`
Preferred Labels |User (en)<br />
Definitions |['A User is an Agent that uses a Record.']<br />
Broader Concepts |[http://linked.data.gov.au/def/agrif#Role](http://linked.data.gov.au/def/agrif#Role) (cp)<br />
### Version History
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#VersionHistory`
Preferred Labels |Version History (en)<br />
Definitions |['A Version History is the cumulative change to a previous version of a file.']<br />
### None
Property | Value
--- | ---
URI | `ub64bL849C45`
Preferred Labels |None (en)<br />

## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **vann**
  * `http://purl.org/vocab/vann/`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Collections: cl
* Concepts: cp