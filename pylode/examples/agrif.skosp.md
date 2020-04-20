# The Australian Government Records Interoperability Framework (AGRIF) ontology
### A taxonomy

Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)

## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/agrif`
* **Publisher(s)**
  * [Department of Finance](http://linked.data.gov.au/org/finance)
* **Creators(s)**
  * [Armin Haller](http://orcid.org/0000-0003-3425-0780)
    [[ORCID]](http://orcid.org/0000-0003-3425-0780)
    (<armin.haller@anu.edu.au></a>) of [Australian National University](https://www.anu.edu.au)
  * Katherine Stuart of [Department of Finance](https://www.finance.gov.au)
  * John Machin of [Department of Finance](https://www.finance.gov.au)
* **Contributor(s)**
  * Pouya Ghiasnezhad Omran
  * Kerry Taylor
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
* **License &amp; Rights**
  * [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
  * (c) Commonwealth of Australia (Department of Finance) 2019
* **Ontology RDF**
  * RDF ([agrif.ttl](turtle))
### Description
<p>The Australian Government Records Interoperability Framework (AGRIF, ‘the Framework’) is a system of related semantic ontologies that describe the structure, functions, and activities of the Australian Government, providing sufficient context for the effective use – including but not limited to management – of Australian Government information assets. It complies with the World Wide Web Consortium’s Web Ontology Language (OWL2) Recommendation and makes reference to other Recommendations and existing domain ontologies for archival and preservation processes.</p>


## Table of Contents
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
* [Control](http://linked.data.gov.au/def/agrif#Control)
	* [Access Control](http://linked.data.gov.au/def/agrif#AccessControl)
		* [Security Classification](http://linked.data.gov.au/def/agrif#SecurityClassification)
	* [Security Control](http://linked.data.gov.au/def/agrif#SecurityControl)
* [Coverage](http://linked.data.gov.au/def/agrif#Coverage)
	* [Jurisdictional Coverage](http://linked.data.gov.au/def/agrif#JurisdictionalCoverage)
	* [Spatial Coverage](http://linked.data.gov.au/def/agrif#SpatialCoverage)
	* [Temporal Coverage](http://linked.data.gov.au/def/agrif#TemporalCoverage)
* [Form Factor](http://linked.data.gov.au/def/agrif#FormFactor)
* [Information System](http://linked.data.gov.au/def/agrif#InformationSystem)
	* [Intellectual Control System](http://linked.data.gov.au/def/agrif#IntellectualControlSystem)
		* [Controlled Vocabulary](http://linked.data.gov.au/def/agrif#ControlledVocabulary)
		* [Series](http://linked.data.gov.au/def/agrif#Series)
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
* [Spatial Location](http://linked.data.gov.au/def/agrif#SpatialLocation)
	* [Holding Space](http://linked.data.gov.au/def/agrif#HoldingSpace)
		* [Digital Holding Space](http://linked.data.gov.au/def/agrif#DigitalHoldingSpace)
		* [Physical Holding Space](http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace)
* [Status](http://linked.data.gov.au/def/agrif#Status)
	* [Decision Status](http://linked.data.gov.au/def/agrif#DecisionStatus)
* [Version History](http://linked.data.gov.au/def/agrif#VersionHistory)
* [None](ub68bL849C45)

### AGIFT Function
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AGIFTFunction`
Preferred Labels |AGIFT Function (en)<br />
Broader Concepts |[Function](Function) (cp)<br />
### Access Activity
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AccessActivity`
Preferred Labels |Access Activity (en)<br />
Broader Concepts |[Activity](Activity) (cp)<br />
### Access Control
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AccessControl`
Preferred Labels |Access Control (en)<br />
Broader Concepts |[Control](Control) (cp)<br />
Narrower Concepts |[Security Classification](SecurityClassification) (cp)<br />
### Access Trigger
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AccessTrigger`
Preferred Labels |Access Trigger (en)<br />
Broader Concepts |[Trigger](Trigger) (cp)<br />
### Activity
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Activity`
Preferred Labels |Activity (en)<br />
Source | https://www.w3.org/TR/prov-o/#Activity
Narrower Concepts |[Share Activity](ShareActivity) (cp)<br />[Access Activity](AccessActivity) (cp)<br />[Maintain Activity](MaintainActivity) (cp)<br />
### Administrator
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Administrator`
Preferred Labels |Administrator (en)<br />
Broader Concepts |[Role](Role) (cp)<br />
### Agent
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Agent`
Preferred Labels |Agent (en)<br />
Source | https://www.w3.org/TR/prov-o/#Agent
Narrower Concepts |[Person](Person) (cp)<br />[Organisation](Organisation) (cp)<br />
### Artefact
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Artefact`
Preferred Labels |Artefact (en)<br />
Narrower Concepts |[Digital Artefact](DigitalArtefact) (cp)<br />[Physical Artefact](PhysicalArtefact) (cp)<br />
### Artefact Change Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ArtefactChangeEvent`
Preferred Labels |Artefact Change Event (en)<br />
Broader Concepts |[Event](Event) (cp)<br />
Narrower Concepts |[Artefact Send Event](ArtefactSendEvent) (cp)<br />
### Artefact Control Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ArtefactControlEvent`
Preferred Labels |Artefact Control Event (en)<br />
Broader Concepts |[Event](Event) (cp)<br />
Narrower Concepts |[Artefact Publish Event](ArtefactPublishEvent) (cp)<br />[Artefact Share Event](ArtefactShareEvent) (cp)<br />
### Artefact Publish Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ArtefactPublishEvent`
Preferred Labels |Artefact Publish Event (en)<br />
Broader Concepts |[Artefact Control Event](ArtefactControlEvent) (cp)<br />
### Artefact Send Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ArtefactSendEvent`
Preferred Labels |Artefact Send Event (en)<br />
Broader Concepts |[Artefact Change Event](ArtefactChangeEvent) (cp)<br />
### Artefact Share Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ArtefactShareEvent`
Preferred Labels |Artefact Share Event (en)<br />
Broader Concepts |[Artefact Control Event](ArtefactControlEvent) (cp)<br />
### Association
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Association`
Preferred Labels |Association (en)<br />
Source | https://www.w3.org/TR/prov-o/#Association
### Business Owner
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#BusinessOwner`
Preferred Labels |Business Owner (en)<br />
Broader Concepts |[Role](Role) (cp)<br />
### Classifier
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Classifier`
Preferred Labels |Classifier (en)<br />
### Collection
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Collection`
Preferred Labels |Collection (en)<br />
Narrower Concepts |[Logical Collection](LogicalCollection) (cp)<br />[Physical Collection](PhysicalCollection) (cp)<br />
### Control
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Control`
Preferred Labels |Control (en)<br />
Narrower Concepts |[Access Control](AccessControl) (cp)<br />[Security Control](SecurityControl) (cp)<br />
### Controlled Vocabulary
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ControlledVocabulary`
Preferred Labels |Controlled Vocabulary (en)<br />
Broader Concepts |[Intellectual Control System](IntellectualControlSystem) (cp)<br />
### Coverage
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Coverage`
Preferred Labels |Coverage (en)<br />
Narrower Concepts |[Spatial Coverage](SpatialCoverage) (cp)<br />[Temporal Coverage](TemporalCoverage) (cp)<br />[Jurisdictional Coverage](JurisdictionalCoverage) (cp)<br />
### Record Creation Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#CreationEvent`
Preferred Labels |Record Creation Event (en)<br />
Broader Concepts |[Event](Event) (cp)<br />
### Creator
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Creator`
Preferred Labels |Creator (en)<br />
Broader Concepts |[Role](Role) (cp)<br />
### Decision Status
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DecisionStatus`
Preferred Labels |Decision Status (en)<br />
Broader Concepts |[Status](Status) (cp)<br />
### Digital Artefact
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DigitalArtefact`
Preferred Labels |Digital Artefact (en)<br />
Broader Concepts |[Artefact](Artefact) (cp)<br />
### Digital Holding Space
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DigitalHoldingSpace`
Preferred Labels |Digital Holding Space (en)<br />
Broader Concepts |[Holding Space](HoldingSpace) (cp)<br />
### Digital Preservation Policy
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DigitalPreservationPolicy`
Preferred Labels |Digital Preservation Policy (en)<br />
Broader Concepts |[Policy](Policy) (cp)<br />
### Disposal Class
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DisposalClass`
Preferred Labels |Disposal Class (en)<br />
Broader Concepts |[Records Authority Disposal Class Policy](RecordsAuthorityDisposalClassPolicy) (cp)<br />
### Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Event`
Preferred Labels |Event (en)<br />
Source | https://www.w3.org/TR/prov-o/#InstantaneousEvent
Narrower Concepts |[Artefact Change Event](ArtefactChangeEvent) (cp)<br />[Record Control Event](RecordControlEvent) (cp)<br />[Artefact Control Event](ArtefactControlEvent) (cp)<br />[Record Creation Event](RecordCreationEvent) (cp)<br />
### Form Factor
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#FormFactor`
Preferred Labels |Form Factor (en)<br />
### Function
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Function`
Preferred Labels |Function (en)<br />
Narrower Concepts |[AGIFT Function](AGIFTFunction) (cp)<br />[Records Authority Function](RecordsAuthorityFunction) (cp)<br />
### Holding Space
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#HoldingSpace`
Preferred Labels |Holding Space (en)<br />
Broader Concepts |[Spatial Location](SpatialLocation) (cp)<br />
Narrower Concepts |[Physical Holding Space](PhysicalHoldingSpace) (cp)<br />[Digital Holding Space](DigitalHoldingSpace) (cp)<br />
### Information Management Policy
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#InformationManagementPolicy`
Preferred Labels |Information Management Policy (en)<br />
Broader Concepts |[Policy](Policy) (cp)<br />
### Information System
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#InformationSystem`
Preferred Labels |Information System (en)<br />
Narrower Concepts |[Intellectual Control System](IntellectualControlSystem) (cp)<br />
### Intellectual Control System
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#IntellectualControlSystem`
Preferred Labels |Intellectual Control System (en)<br />
Broader Concepts |[Information System](InformationSystem) (cp)<br />
Narrower Concepts |[Controlled Vocabulary](ControlledVocabulary) (cp)<br />[Series](Series) (cp)<br />
### Jurisdictional Coverage
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#JurisdictionalCoverage`
Preferred Labels |Jurisdictional Coverage (en)<br />
Broader Concepts |[Coverage](Coverage) (cp)<br />
### Logical Collection
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#LogicalCollection`
Preferred Labels |Logical Collection (en)<br />
Broader Concepts |[Collection](Collection) (cp)<br />
### Maintain Activity
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#MaintainActivity`
Preferred Labels |Maintain Activity (en)<br />
Broader Concepts |[Activity](Activity) (cp)<br />
### Manifest
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Manifest`
Preferred Labels |Manifest (en)<br />
### Minimum Metadata Set Policy
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#MinimumMetadataSetPolicy`
Preferred Labels |Minimum Metadata Set Policy (en)<br />
Broader Concepts |[Policy](Policy) (cp)<br />
### Organisation
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Organisation`
Preferred Labels |Organisation (en)<br />
Source | https://www.w3.org/TR/prov-o/#Organization
Broader Concepts |[Agent](Agent) (cp)<br />
Narrower Concepts |[Organisational Unit](OrganisationalUnit) (cp)<br />
### Organisational Unit
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#OrganisationalUnit`
Preferred Labels |Organisational Unit (en)<br />
Broader Concepts |[Organisation](Organisation) (cp)<br />
### Permission
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Permission`
Preferred Labels |Security Clearance (en)<br />Permission (en)<br />
Source | Australian Government Recordkeeping Metadata Standard
### Person
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Person`
Preferred Labels |Person (en)<br />
Source | https://www.w3.org/TR/prov-o/#Person
Broader Concepts |[Agent](Agent) (cp)<br />
### Physical Artefact
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#PhysicalArtefact`
Preferred Labels |Physical Artefact (en)<br />
Examples |An example of a Phyiscal Artefact in the context of record keeping is information printed or written on paper.<br />
Broader Concepts |[Artefact](Artefact) (cp)<br />
### Physical Collection
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#PhysicalCollection`
Preferred Labels |Physical Collection (en)<br />
Broader Concepts |[Collection](Collection) (cp)<br />
### Physical Holding Space
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace`
Preferred Labels |Physical Holding Space (en)<br />
Broader Concepts |[Holding Space](HoldingSpace) (cp)<br />
### Policy
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Policy`
Preferred Labels |Policy (en)<br />
Source | http://purl.org/dc/terms/Policy
Narrower Concepts |[Records Authority Disposal Class Policy](RecordsAuthorityDisposalClassPolicy) (cp)<br />[Digital Preservation Policy](DigitalPreservationPolicy) (cp)<br />[Minimum Metadata Set Policy](MinimumMetadataSetPolicy) (cp)<br />[Record Storage Standard](RecordStorageStandard) (cp)<br />[Information Management Policy](InformationManagementPolicy) (cp)<br />
### Preservation Quality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#PreservationQuality`
Preferred Labels |Preservation Quality (en)<br />
Broader Concepts |[Quality](Quality) (cp)<br />
### Quality
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Quality`
Preferred Labels |Quality (en)<br />
Narrower Concepts |[Preservation Quality](PreservationQuality) (cp)<br />
### Record
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Record`
Preferred Labels |Record (en)<br />
### Record Audit Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordAuditEvent`
Preferred Labels |Record Audit Event (en)<br />
Broader Concepts |[Record Control Event](RecordControlEvent) (cp)<br />
### Record Control Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordControlEvent`
Preferred Labels |Record Control Event (en)<br />
Broader Concepts |[Event](Event) (cp)<br />
Narrower Concepts |[Record Audit Event](RecordAuditEvent) (cp)<br />[Record Disposal Event](RecordDisposalEvent) (cp)<br />[Record Decision Event](RecordDecisionEvent) (cp)<br />[Record Replacement Event](RecordReplacementEvent) (cp)<br />[Record Sentencing Event](RecordSentencingEvent) (cp)<br />
### Record Decision Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordDecisionEvent`
Preferred Labels |Record Decision Event (en)<br />
Broader Concepts |[Record Control Event](RecordControlEvent) (cp)<br />
### Record Destruction Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordDestructionEvent`
Preferred Labels |Record Destruction Event (en)<br />
Broader Concepts |[Record Disposal Event](RecordDisposalEvent) (cp)<br />
### Record Disposal Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordDisposalEvent`
Preferred Labels |Record Disposal Event (en)<br />
Broader Concepts |[Record Control Event](RecordControlEvent) (cp)<br />
Narrower Concepts |[Record Transfer Event](RecordTransferEvent) (cp)<br />[Record Destruction Event](RecordDestructionEvent) (cp)<br />[Record Freeze Event](RecordFreezeEvent) (cp)<br />
### Record Freeze Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordFreezeEvent`
Preferred Labels |Record Freeze Event (en)<br />
Broader Concepts |[Record Disposal Event](RecordDisposalEvent) (cp)<br />
### Record Replacement Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordReplacementEvent`
Preferred Labels |Record Replacement Event (en)<br />
Broader Concepts |[Record Control Event](RecordControlEvent) (cp)<br />
### Record Sentencing Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordSentencingEvent`
Preferred Labels |Record Sentencing Event (en)<br />
Broader Concepts |[Record Control Event](RecordControlEvent) (cp)<br />
### Record Storage Standard
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordStorageStandard`
Preferred Labels |Record Storage Standard (en)<br />
Broader Concepts |[Policy](Policy) (cp)<br />
### Record Transfer Event
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordTransferEvent`
Preferred Labels |Record Transfer Event (en)<br />
Examples |An example of a Record Transfer Event is the transfer of a Record from an Agency to the National Archives. Section 27 of the Archives Act 1983 requires Australian government agencies to transfer Records to the Archives within 15 years of their creation.<br />
Broader Concepts |[Record Disposal Event](RecordDisposalEvent) (cp)<br />
### Records Authority Function
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityFunction`
Preferred Labels |Records Authority Function (en)<br />
Broader Concepts |[Function](Function) (cp)<br />
### Records Authority Disposal Class Policy
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy`
Preferred Labels |Records Authority Disposal Class Policy (en)<br />
Source | Australian Government Recordkeeping Metadata Standard
Broader Concepts |[Policy](Policy) (cp)<br />
Narrower Concepts |[Disposal Class](DisposalClass) (cp)<br />
### Role
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Role`
Preferred Labels |Role (en)<br />
Source | https://www.w3.org/TR/prov-o/#Role
Narrower Concepts |[Creator](Creator) (cp)<br />[Administrator](Administrator) (cp)<br />[User](User) (cp)<br />[Business Owner](BusinessOwner) (cp)<br />
### Security Classification
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SecurityClassification`
Preferred Labels |Security Classification (en)<br />
Source | Australian Government Recordkeeping Metadata Standard
Broader Concepts |[Access Control](AccessControl) (cp)<br />
### Security Control
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SecurityControl`
Preferred Labels |Security Control (en)<br />
Broader Concepts |[Control](Control) (cp)<br />
### Series
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Series`
Preferred Labels |Series (en)<br />
Broader Concepts |[Intellectual Control System](IntellectualControlSystem) (cp)<br />
### Share Activity
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ShareActivity`
Preferred Labels |Share Activity (en)<br />
Broader Concepts |[Activity](Activity) (cp)<br />
### Spatial Coverage
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SpatialCoverage`
Preferred Labels |Spatial Coverage (en)<br />
Broader Concepts |[Coverage](Coverage) (cp)<br />
### Spatial Location
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SpatialLocation`
Preferred Labels |Spatial Location (en)<br />
Narrower Concepts |[Holding Space](HoldingSpace) (cp)<br />
### Status
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Status`
Preferred Labels |Status (en)<br />
Narrower Concepts |[Decision Status](DecisionStatus) (cp)<br />
### Temporal Coverage
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#TemporalCoverage`
Preferred Labels |Temporal Coverage (en)<br />
Broader Concepts |[Coverage](Coverage) (cp)<br />
### Trigger
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Trigger`
Preferred Labels |Trigger (en)<br />
Narrower Concepts |[Access Trigger](AccessTrigger) (cp)<br />
### User
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#User`
Preferred Labels |User (en)<br />
Broader Concepts |[Role](Role) (cp)<br />
### Version History
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#VersionHistory`
Preferred Labels |Version History (en)<br />
### None
Property | Value
--- | ---
IRI | `ub68bL849C45`

## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/agrif#`
* **:**
  * `http://linked.data.gov.au/def/agrif#`
* **dcterms**
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
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Collections: cl
* Concepts: cp