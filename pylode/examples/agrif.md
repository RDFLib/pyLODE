Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# The Australian Government Records Interoperability Framework (AGRIF) ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/agrif`
* **Publisher(s)**
  * [Department of Finance](http://linked.data.gov.au/org/finance)
* **Creators(s)**
  * John Machin of [Department of Finance](https://www.finance.gov.au)
  * Katherine Stuart of [Department of Finance](https://www.finance.gov.au)
  * [Armin Haller](http://orcid.org/0000-0003-3425-0780)
    [[0000-0003-3425-0780](http://orcid.org/0000-0003-3425-0780)]
    [armin.haller@anu.edu.au](armin.haller@anu.edu.au) of [Australian National University](https://www.anu.edu.au)
* **Contributor(s)**
  * Kerry Taylor
  * Pouya Ghiasnezhad Omran
  * Sergio José Rodríguez Méndez
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[0000-0002-8742-7730](http://orcid.org/0000-0002-8742-7730)]
    [nicholas.car@surroundaustralia.com](nicholas.car@surroundaustralia.com)
* **Created**
  * 2016-12-06
* **Modified**
  * 2019-10-21
* **Version Information**
  * 0.9
* **License &amp; Rights**
  * [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
  * &copy; Commonwealth of Australia (Department of Finance) 2019
* **Ontology RDF**
  * RDF ([agrif.ttl](turtle))
### Description
The Australian Government Records Interoperability Framework (AGRIF, ‘the Framework’) is a system of related semantic ontologies that describe the structure, functions, and activities of the Australian Government, providing sufficient context for the effective use – including but not limited to management – of Australian Government information assets. It complies with the World Wide Web Consortium’s Web Ontology Language (OWL2) Recommendation and makes reference to other Recommendations and existing domain ontologies for archival and preservation processes.

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Named Individuals](#namedindividuals)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[AGIFT Function](#AGIFTFunction),
[Access Activity](#AccessActivity),
[Access Control](#AccessControl),
[Access Trigger](#AccessTrigger),
[Activity](#Activity),
[Administrator](#Administrator),
[Agent](#Agent),
[Artefact](#Artefact),
[Artefact Change Event](#ArtefactChangeEvent),
[Artefact Control Event](#ArtefactControlEvent),
[Artefact Publish Event](#ArtefactPublishEvent),
[Artefact Send Event](#ArtefactSendEvent),
[Artefact Share Event](#ArtefactShareEvent),
[Association](#Association),
[Business Owner](#BusinessOwner),
[Classifier](#Classifier),
[Collection](#Collection),
[Control](#Control),
[Controlled Vocabulary](#ControlledVocabulary),
[Coverage](#Coverage),
[Creator](#Creator),
[Decision Status](#DecisionStatus),
[Digital Artefact](#DigitalArtefact),
[Digital Holding Space](#DigitalHoldingSpace),
[Digital Preservation Policy](#DigitalPreservationPolicy),
[Disposal Class](#DisposalClass),
[Event](#Event),
[Form Factor](#FormFactor),
[Function](#Function),
[Holding Space](#HoldingSpace),
[Information Management Policy](#InformationManagementPolicy),
[Information System](#InformationSystem),
[Intellectual Control System](#IntellectualControlSystem),
[Jurisdictional Coverage](#JurisdictionalCoverage),
[Logical Collection](#LogicalCollection),
[Maintain Activity](#MaintainActivity),
[Manifest](#Manifest),
[Minimum Metadata Set Policy](#MinimumMetadataSetPolicy),
[Organisation](#Organisation),
[Organisational Unit](#OrganisationalUnit),
[Person](#Person),
[Physical Artefact](#PhysicalArtefact),
[Physical Collection](#PhysicalCollection),
[Physical Holding Space](#PhysicalHoldingSpace),
[Policy](#Policy),
[Preservation Quality](#PreservationQuality),
[Quality](#Quality),
[Record](#Record),
[Record Audit Event](#RecordAuditEvent),
[Record Control Event](#RecordControlEvent),
[Record Creation Event](#RecordCreationEvent),
[Record Decision Event](#RecordDecisionEvent),
[Record Destruction Event](#RecordDestructionEvent),
[Record Disposal Event](#RecordDisposalEvent),
[Record Freeze Event](#RecordFreezeEvent),
[Record Replacement Event](#RecordReplacementEvent),
[Record Sentencing Event](#RecordSentencingEvent),
[Record Storage Standard](#RecordStorageStandard),
[Record Transfer Event](#RecordTransferEvent),
[Records Authority Disposal Class Policy](#RecordsAuthorityDisposalClassPolicy),
[Records Authority Function](#RecordsAuthorityFunction),
[Role](#Role),
[Security Classification](#SecurityClassification),
[Security Clearance](#SecurityClearance),
[Security Control](#SecurityControl),
[Series](#Series),
[Share Activity](#ShareActivity),
[Spatial Coverage](#SpatialCoverage),
[Spatial Location](#SpatialLocation),
[Status](#Status),
[Temporal Coverage](#TemporalCoverage),
[Trigger](#Trigger),
[User](#User),
[Version History](#VersionHistory),
### AGIFT Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AGIFTFunction`
Is Defined By | https://data.naa.gov.au/def/agift/
Description | An AGIFT Function is a Function that classifies a Record according to the Australian Governments' Interactive Functions Thesaurus.
Super-classes |[agrif:Function](Function) (c)<br />
### Access Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AccessActivity`
Description | An Access Activity is an Activity where a Record is accessed by an Agent over a period of time.
Super-classes |[agrif:Activity](Activity) (c)<br />
Restrictions |[agrif:triggers](triggers) (op) **only** [agrif:AccessTrigger](AccessTrigger) (c)<br />[agrif:accessedBy](accessedBy) (op) **some** [agrif:Agent](Agent) (c)<br />
### Access Control
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AccessControl`
Description | Access Control is the selective restriction of access to a Record or Artefact.
Super-classes |[agrif:Control](Control) (c)<br />
Sub-classes |[agrif:SecurityClassification](SecurityClassification) (c)<br />
### Access Trigger
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AccessTrigger`
Description | An Access Trigger is a Trigger that can be initiated when a Record is accessed.
Super-classes |[agrif:Trigger](Trigger) (c)<br />
### Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Activity`
Source | [https://www.w3.org/TR/prov-o/#Activity](https://www.w3.org/TR/prov-o/#Activity)
Description | An Activity is something that occurs over a period of time on a Record.
Restrictions |[agrif:associatedFunction](associatedFunction) (op) **only** [agrif:Function](Function) (c)<br />[agrif:hasStatus](hasStatus) (op) **only** [agrif:Status](Status) (c)<br />[agrif:startedAtTime](startedAtTime) (dp) **max** 1<br />[agrif:wasAssociatedWith](wasAssociatedWith) (op) **some** [agrif:Agent](Agent) (c)<br />[agrif:endedAtTime](endedAtTime) (dp) **max** 1<br />[agrif:hasLocation](hasLocation) (op) **only** [agrif:SpatialLocation](SpatialLocation) (c)<br />[agrif:guidingPolicy](guidingPolicy) (op) **only** [agrif:Policy](Policy) (c)<br />[agrif:usedRecord](usedRecord) (op) **only** [agrif:Record](Record) (c)<br />[agrif:requiresSecurityClassification](requiresSecurityClassification) (op) **only** [agrif:SecurityClassification](SecurityClassification) (c)<br />[agrif:qualifiedAssociation](qualifiedAssociation) (op) **some** [agrif:Association](Association) (c)<br />
Sub-classes |[agrif:MaintainActivity](MaintainActivity) (c)<br />[agrif:ShareActivity](ShareActivity) (c)<br />[agrif:AccessActivity](AccessActivity) (c)<br />
### Administrator
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Administrator`
Description | An Administrator is a Role that has overall responsibility for the administration and functions of an Information System, but not necessarily for the information stored within.
Super-classes |[agrif:Role](Role) (c)<br />
### Agent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Agent`
Source | [https://www.w3.org/TR/prov-o/#Agent](https://www.w3.org/TR/prov-o/#Agent)
Description | An Agent is a corporate entity, organisational element or system, or individual responsible for the performance of some Activity or Event, including those on Records.
Restrictions |[agrif:positionIn](positionIn) (op) **some** [agrif:Organisation](Organisation) (c)<br />[agrif:actsAs](actsAs) (op) **some** [agrif:Role](Role) (c)<br />[agrif:hasPermission](hasPermission) (op) **some** [agrif:Permission](SecurityClearance) (c)<br />
Sub-classes |[agrif:Organisation](Organisation) (c)<br />[agrif:Person](Person) (c)<br />
### Artefact
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Artefact`
Description | An Artefact is an object that is made by a Person and that is to be preserved.
Restrictions |[agrif:relatedTo](relatedTo) (op) **only** [agrif:Artefact](Artefact) (c)<br />[agrif:requiresSecurityClassification](requiresSecurityClassification) (op) **only** [agrif:SecurityClassification](SecurityClassification) (c)<br />[agrif:isChangedBy](isChangedBy) (op) **some** [agrif:InformationSystem](InformationSystem) (c)<br />[agrif:hasLocation](hasLocation) (op) **only** [agrif:SpatialLocation](SpatialLocation) (c)<br />[agrif:softwareAssignedID](softwareAssignedID) (dp) **some** [xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />[agrif:isAffectedBy](isAffectedBy) (op) **some** [agrif:Event](Event) (c)<br />[agrif:hasQuality](hasQuality) (op) **some** [agrif:PreservationQuality](PreservationQuality) (c)<br />[agrif:storedIn](storedIn) (op) **some** [agrif:IntellectualControlSystem](IntellectualControlSystem) (c)<br />
Sub-classes |[agrif:PhysicalArtefact](PhysicalArtefact) (c)<br />[agrif:DigitalArtefact](DigitalArtefact) (c)<br />
### Artefact Change Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactChangeEvent`
Description | An Artefact Change Event is an Event that results in a new version of an Artefact.
Super-classes |[agrif:Event](Event) (c)<br />
Restrictions |[agrif:affects](affects) (op) **min** 2 [agrif:Artefact](Artefact) (c)<br />
Sub-classes |[agrif:ArtefactSendEvent](ArtefactSendEvent) (c)<br />
### Artefact Control Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactControlEvent`
Description | An Artefact Control Event is an Event that requires a particular level of access to an Artefact.
Super-classes |[agrif:Event](Event) (c)<br />
Restrictions |[agrif:hasControl](requiresControl) (op) **only** [agrif:Control](Control) (c)<br />
Sub-classes |[agrif:ArtefactPublishEvent](ArtefactPublishEvent) (c)<br />[agrif:ArtefactShareEvent](ArtefactShareEvent) (c)<br />
### Artefact Publish Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactPublishEvent`
Description | An Artefact Publish Event is an Event that gives indiscriminate access to an Artefact to a set of Agents.
Super-classes |[agrif:ArtefactControlEvent](ArtefactControlEvent) (c)<br />
### Artefact Send Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactSendEvent`
Description | An Artefact Send Event is an Event that results in a new version or a set of new versions of an Artefact at a target Agent or a set of target Agents.
Super-classes |[agrif:ArtefactChangeEvent](ArtefactChangeEvent) (c)<br />
Restrictions |[agrif:hasTargetAgent](hasTargetAgent) (op) **min** 1 [agrif:Agent](Agent) (c)<br />[agrif:hasSourceAgent](hasSourceAgent) (op) **exactly** 1 [agrif:Agent](Agent) (c)<br />
### Artefact Share Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ArtefactShareEvent`
Description | An Artefact Share Event is an Event that gives access to an Artefact to an Agent or a defined set of Agents.
Super-classes |[agrif:ArtefactControlEvent](ArtefactControlEvent) (c)<br />
Restrictions |[agrif:hasSourceAgent](hasSourceAgent) (op) **exactly** 1 [agrif:Agent](Agent) (c)<br />[agrif:hasTargetAgent](hasTargetAgent) (op) **min** 1 [agrif:Agent](Agent) (c)<br />
### Association
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Association`
Source | [https://www.w3.org/TR/prov-o/#Association](https://www.w3.org/TR/prov-o/#Association)
Description | An Association is a qualified assignment of responsibility to an Agent in an Activity or Event, indicating that the Agent had a Role in the Activity.
Restrictions |[agrif:associatedRole](associatedRole) (op) **only** [agrif:Role](Role) (c)<br />[agrif:hasAgent](hasAgent) (op) **only** [agrif:Agent](Agent) (c)<br />
### Business Owner
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#BusinessOwner`
Description | A Business Owner is the Role that has the managerial control of a Function.
Super-classes |[agrif:Role](Role) (c)<br />
### Classifier
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Classifier`
Description | A Classifier is a machine-generated and applied category that a set of Records belong to.
Restrictions |[agrif:associatedFunction](associatedFunction) (op) **only** [agrif:Function](Function) (c)<br />
### Collection
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Collection`
Description | A Collection is an aggregation of Artefact items.
Restrictions |[agrif:hasPart](hasPart) (op) **some** [agrif:Artefact](Artefact) (c)<br />
Sub-classes |[agrif:PhysicalCollection](PhysicalCollection) (c)<br />[agrif:LogicalCollection](LogicalCollection) (c)<br />
### Control
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Control`
Description | A Control is a security or access measure that safeguards or restricts access to an asset.
Sub-classes |[agrif:SecurityControl](SecurityControl) (c)<br />[agrif:AccessControl](AccessControl) (c)<br />
### Controlled Vocabulary
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ControlledVocabulary`
Description | A Controlled Vocabulary is an Intellectual Control System that provides a way to organize Records that facilitates a later discovery of a Record.
Super-classes |[agrif:IntellectualControlSystem](IntellectualControlSystem) (c)<br />
Restrictions |[agrif:associatedFunction](associatedFunction) (op) **only** [agrif:Function](Function) (c)<br />
### Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Coverage`
Description | A Coverage denotes the jurisdictional applicability, or the temporal and/or spatial extent to which a Record is observed.
Sub-classes |[agrif:SpatialCoverage](SpatialCoverage) (c)<br />[agrif:JurisdictionalCoverage](JurisdictionalCoverage) (c)<br />[agrif:TemporalCoverage](TemporalCoverage) (c)<br />
### Record Creation Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#CreationEvent`
Description | A Record Creation Event is an Event that results in the creation of a Record.
Super-classes |[agrif:Event](Event) (c)<br />
### Creator
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Creator`
Description | A Creator is the Agent that has created a Record or Artefact.
Super-classes |[agrif:Role](Role) (c)<br />
### Decision Status
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DecisionStatus`
Description | A Decision Status is a Status that indicates the approval or disapproval of a Decision Event.
Super-classes |[agrif:Status](Status) (c)<br />
Has members |[agrif:Approved](http://linked.data.gov.au/def/agrif#Approved)<br />[agrif:Disapproved](http://linked.data.gov.au/def/agrif#Disapproved)<br />
### Digital Artefact
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DigitalArtefact`
Description | A Digital Artefact is an Artefact that is of a digital nature and stored in an Information System.
Super-classes |[agrif:Artefact](Artefact) (c)<br />
Restrictions |[agrif:filename](filename) (dp) **some** [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />[agrif:storedIn](storedIn) (op) **some** [agrif:InformationSystem](InformationSystem) (c)<br />[agrif:format](format) (dp) **some** [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />[agrif:filesize](filesize) (dp) **some** [xsd:long](http://www.w3.org/2001/XMLSchema#long) (c)<br />
### Digital Holding Space
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DigitalHoldingSpace`
Description | A Digital Holding Space is a space that is used or reserved for the storage of a Digital Artefact on a storage medium or virtual storage space.
Super-classes |[agrif:HoldingSpace](HoldingSpace) (c)<br />
### Digital Preservation Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DigitalPreservationPolicy`
Description | The Digital Preservation Policy defines the process of active management by which the National Archives ensures that a digital object will be accessible in the future.
Super-classes |[agrif:Policy](Policy) (c)<br />
### Disposal Class
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#DisposalClass`
Description | A Disposal Class is a Policy that defines the sentencing requirements of an item.
Super-classes |[agrif:RecordsAuthorityPolicy](RecordsAuthorityDisposalClassPolicy) (c)<br />
Restrictions |[agrif:disposalClassNumber](disposalClassNumber) (dp) **exactly** 1<br />
Has members |[agrif:RetainAsNationalArchives](http://linked.data.gov.au/def/agrif#RetainAsNationalArchives)<br />
### Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Event`
Source | [https://www.w3.org/TR/prov-o/#InstantaneousEvent](https://www.w3.org/TR/prov-o/#InstantaneousEvent)
Description | An Event denotes an instantaneous transition in the world.
Restrictions |[agrif:associatedFunction](associatedFunction) (op) **only** [agrif:Function](Function) (c)<br />[agrif:guidingPolicy](guidingPolicy) (op) **only** [agrif:Policy](Policy) (c)<br />[agrif:priorEvent](priorEvent) (op) **only** [agrif:Event](Event) (c)<br />[agrif:qualifiedAssociation](qualifiedAssociation) (op) **some** [agrif:Association](Association) (c)<br />[agrif:hasStatus](hasStatus) (op) **only** [agrif:Status](Status) (c)<br />[agrif:affects](affects) (op) **some** ([agrif:Artefact](Artefact) (c) or [agrif:Record](Record) (c))<br />[agrif:wasAssociatedWith](wasAssociatedWith) (op) **some** [agrif:Agent](Agent) (c)<br />[agrif:triggeredBy](triggeredBy) (op) **only** [agrif:Trigger](Trigger) (c)<br />
Sub-classes |[agrif:ArtefactChangeEvent](ArtefactChangeEvent) (c)<br />[agrif:RecordControlEvent](RecordControlEvent) (c)<br />[agrif:ArtefactControlEvent](ArtefactControlEvent) (c)<br />[agrif:CreationEvent](RecordCreationEvent) (c)<br />
### Form Factor
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#FormFactor`
Description | A Form Factor defines and prescribes the size, shape, and other physical specifications of a Physical Artefact that is stored.
### Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Function`
Description | A Function is a process that is performed routinely to carry out a part of the mandate of an Australian Government Agency.
Restrictions |[agrif:guidingPolicy](guidingPolicy) (op) **only** [agrif:Policy](Policy) (c)<br />
Sub-classes |[agrif:AGIFTFunction](AGIFTFunction) (c)<br />[agrif:RecordsAuthorityFunction](RecordsAuthorityFunction) (c)<br />
### Holding Space
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#HoldingSpace`
Description | A Holding Space is a space that is used or reserved for the storage of an Artefact.
Super-classes |[agrif:SpatialLocation](SpatialLocation) (c)<br />
Sub-classes |[agrif:PhysicalHoldingSpace](PhysicalHoldingSpace) (c)<br />[agrif:DigitalHoldingSpace](DigitalHoldingSpace) (c)<br />
### Information Management Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#InformationManagementPolicy`
Description | An Information Management Policy is a Policy that helps to align information management practices to fulfill the requirements of an information governance framework. An Information Management Policy provides direction and guidance to staff for creating, capturing and managing information to satisfy business, legal and stakeholder requirements, and assigns responsibilities across the agency.
Super-classes |[agrif:Policy](Policy) (c)<br />
Restrictions |[agrif:hasDisposalClass](hasDisposalClass) (op) **only** [agrif:DisposalClass](DisposalClass) (c)<br />
### Information System
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#InformationSystem`
Description | An Information System is an organized system for the collection, organization, storage and communication of information, typically Digital Artefacts or Records.
Sub-classes |[agrif:IntellectualControlSystem](IntellectualControlSystem) (c)<br />
### Intellectual Control System
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#IntellectualControlSystem`
Description | An Intellectual Control System is a System that enables Agents to locate and manage information.
Super-classes |[agrif:InformationSystem](InformationSystem) (c)<br />
Restrictions |[agrif:guidingPolicy](guidingPolicy) (op) **only** [agrif:Policy](Policy) (c)<br />
Sub-classes |[agrif:ControlledVocabulary](ControlledVocabulary) (c)<br />[agrif:Series](Series) (c)<br />
### Jurisdictional Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#JurisdictionalCoverage`
Description | A Jurisdictional Coverage denotes the jurisdictional applicability of the Record.
Super-classes |[agrif:Coverage](Coverage) (c)<br />
### Logical Collection
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#LogicalCollection`
Description | A Logical Collection is an aggregation of Artefact items that are stored within one physical file.
Super-classes |[agrif:Collection](Collection) (c)<br />
### Maintain Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#MaintainActivity`
Description | A Maintain Activity is an Activity to maintain a Record over a period of time due to a BusinessFunction or Policy.
Super-classes |[agrif:Activity](Activity) (c)<br />
Restrictions |[agrif:hasQuality](hasQuality) (op) **some** [agrif:PreservationQuality](PreservationQuality) (c)<br />
### Manifest
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Manifest`
Description | A Manifest describes the files involved in the transfer of a Record from an Agency to the National Archives, including details such as the filesize, the destination hierarchy and the file's metadata.
Restrictions |[agrif:checksum](checksum) (dp) **exactly** 1<br />
### Minimum Metadata Set Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#MinimumMetadataSetPolicy`
Description | The Minimum Metadata Set Policy is a Policy that has been developed by the National Archives of Australia to identify metadata properties essential for agency management of information as well as those needed for records which will be transferred to the Archives. It supports the Digital Continuity 2020 principles of interoperable systems and processes and is a practical application of the Australian Government Recordkeeping Metadata Standard 2.2 (AGRkMS) to support metadata implementation and information use in agencies.
Super-classes |[agrif:Policy](Policy) (c)<br />
### Organisation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Organisation`
Source | [https://www.w3.org/TR/prov-o/#Organization](https://www.w3.org/TR/prov-o/#Organization)
Description | An Organisation is a type of Agent that denotes a social or legal institution such as a government agency, a corporation, society, etc.
Super-classes |[agrif:Agent](Agent) (c)<br />
Restrictions |[agrif:associatedFunction](associatedFunction) (op) **some** [agrif:Function](Function) (c)<br />
Sub-classes |[agrif:OrganisationalUnit](OrganisationalUnit) (c)<br />
### Organisational Unit
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#OrganisationalUnit`
Description | An Organisational Unit is a division of labour typically organised around a business function that form part of the Organisation.
Super-classes |[agrif:Organisation](Organisation) (c)<br />
Restrictions |[agrif:partOf](partOf) (op) **only** [agrif:Organisation](Organisation) (c)<br />
### Security Clearance
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Permission`
Source | Australian Government Recordkeeping Metadata Standard
Description | A Permission denotes the Security Clearance of an Agent that determines its access and use rights.
### Person
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Person`
Source | [https://www.w3.org/TR/prov-o/#Person](https://www.w3.org/TR/prov-o/#Person)
Description | A Person is an Agent that denotes a human.
Super-classes |[agrif:Agent](Agent) (c)<br />
### Physical Artefact
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PhysicalArtefact`
Description | A Physical Artefact is an Artefact that is of physical nature.
Example | `An example of a Phyiscal Artefact in the context of record keeping is information printed or written on paper.`<br />
Super-classes |[agrif:Artefact](Artefact) (c)<br />
Restrictions |[agrif:hasFormFactor](hasFormFactor) (op) **only** [agrif:FormFactor](FormFactor) (c)<br />
### Physical Collection
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PhysicalCollection`
Description | A Physical Collection is an aggregation of Artefact items that are stored in separate physical files.
Super-classes |[agrif:Collection](Collection) (c)<br />
### Physical Holding Space
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace`
Description | A Physical Holding Space is a Spatial Location that is used or reserved for the storage of a Physical Artefact.
Super-classes |[agrif:HoldingSpace](HoldingSpace) (c)<br />
### Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Policy`
Source | [dct:Policy](http://purl.org/dc/terms/Policy)
Description | A Policy is a deliberate system of principles to guide decisions and achieve rational outcomes.
Sub-classes |[agrif:MinimumMetadataSetPolicy](MinimumMetadataSetPolicy) (c)<br />[agrif:RecordsAuthorityPolicy](RecordsAuthorityDisposalClassPolicy) (c)<br />[agrif:InformationManagementPolicy](InformationManagementPolicy) (c)<br />[agrif:DigitalPreservationPolicy](DigitalPreservationPolicy) (c)<br />[agrif:RecordStorageStandard](RecordStorageStandard) (c)<br />
### Preservation Quality
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#PreservationQuality`
Description | A Preservation Quality describes a Quality of an Artefact that supports or threatens the long term preservation of the information that is to be preserved.
Super-classes |[agrif:Quality](Quality) (c)<br />
### Quality
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Quality`
Description | A Quality is an attribute that is intrinsically associated with an entity.
Sub-classes |[agrif:PreservationQuality](PreservationQuality) (c)<br />
### Record
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Record`
Description | A Record is information in any format created, received and maintained as evidence by an Organisation or Person, in pursuance of legal obligations or in the transaction of business. A Record may comprise a Digital or Physical Artefact.
Restrictions |[agrif:recordOf](recordOf) (op) **min** 1 [agrif:Artefact](Artefact) (c)<br />[agrif:hasControl](requiresControl) (op) **only** [agrif:Control](Control) (c)<br />[agrif:isAffectedBy](isAffectedBy) (op) **exactly** 1 [agrif:CreationEvent](RecordCreationEvent) (c)<br />[agrif:associatedFunction](associatedFunction) (op) **min** 1 [agrif:Function](Function) (c)<br />[agrif:qualifiedAssociation](qualifiedAssociation) (op) **some** [agrif:Association](Association) (c)<br />[agrif:hasDisposalClass](hasDisposalClass) (op) **exactly** 1 [agrif:DisposalClass](DisposalClass) (c)<br />[agrif:hasSeries](hasSeries) (op) **only** [agrif:Series](Series) (c)<br />[agrif:replaces](replaces) (op) **only** [agrif:Record](Record) (c)<br />[agrif:requiresSecurityClassification](requiresSecurityClassification) (op) **only** [agrif:SecurityClassification](SecurityClassification) (c)<br />[agrif:hasCoverage](hasCoverage) (op) **only** [agrif:Coverage](Coverage) (c)<br />[agrif:hasClassifier](hasClassifier) (op) **some** [agrif:Classifier](Classifier) (c)<br />[agrif:hasActivity](hasActivity) (op) **only** [agrif:Activity](Activity) (c)<br />[agrif:isAffectedBy](isAffectedBy) (op) **only** [agrif:Event](Event) (c)<br />[agrif:checksum](checksum) (dp) **max** 1<br />[agrif:relatedTo](relatedTo) (op) **only** [agrif:Record](Record) (c)<br />[agrif:hasStatus](hasStatus) (op) **only** [agrif:Status](Status) (c)<br />
### Record Audit Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordAuditEvent`
Description | An Record Audit Event is the systematic examination of a Record to ascertain how and where the Record is stored, who created it, or manages it, who uses it and how much longer the Record is required to be maintained.
Super-classes |[agrif:RecordControlEvent](RecordControlEvent) (c)<br />
### Record Control Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordControlEvent`
Description | A Record Control Event is an Event that requires a particular level of access to the Record.
Super-classes |[agrif:Event](Event) (c)<br />
Restrictions |[agrif:hasControl](requiresControl) (op) **only** [agrif:Control](Control) (c)<br />
Sub-classes |[agrif:RecordDecisionEvent](RecordDecisionEvent) (c)<br />[agrif:RecordAuditEvent](RecordAuditEvent) (c)<br />[agrif:RecordDisposalEvent](RecordDisposalEvent) (c)<br />[agrif:RecordSentencingEvent](RecordSentencingEvent) (c)<br />[agrif:RecordReplacementEvent](RecordReplacementEvent) (c)<br />
### Record Decision Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordDecisionEvent`
Description | A Record Decision Event changes the Decision Status on the Control of a Record.
Super-classes |[agrif:RecordControlEvent](RecordControlEvent) (c)<br />
Restrictions |[agrif:hasPrerequisiteDecisionEvent](prerequisiteDecisionEvent) (op) **only** [agrif:RecordDecisionEvent](RecordDecisionEvent) (c)<br />[agrif:hasDecisionStatus](hasDecisionStatus) (op) **only** [agrif:DecisionStatus](DecisionStatus) (c)<br />
### Record Destruction Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordDestructionEvent`
Description | A Record Destruction Event is a Disposal Event that results in the regular authorised permanent desctruction of a Record that is no longer required for business purposes.
Super-classes |[agrif:RecordDisposalEvent](RecordDisposalEvent) (c)<br />
### Record Disposal Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordDisposalEvent`
Description | A Record Disposal Event is an Event that results in the regular authorised destruction or change of custody of a Record that is no longer required for business purposes.
Super-classes |[agrif:RecordControlEvent](RecordControlEvent) (c)<br />
Sub-classes |[agrif:RecordDestructionEvent](RecordDestructionEvent) (c)<br />[agrif:RecordFreezeEvent](RecordFreezeEvent) (c)<br />[agrif:RecordTransferEvent](RecordTransferEvent) (c)<br />
### Record Freeze Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordFreezeEvent`
Description | A Record Freeze Event is a Disposal Event that leads to a records disposal freeze or retention notice in support of compliance requirements or an identified need to suspend the Archives' records destruction permissions.
Super-classes |[agrif:RecordDisposalEvent](RecordDisposalEvent) (c)<br />
### Record Replacement Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordReplacementEvent`
Description | A Record Replacement Event is an Event that results in the replacement of a Record with a new version. Edits to a Record constitute a Replace Event.
Super-classes |[agrif:RecordControlEvent](RecordControlEvent) (c)<br />
Restrictions |[agrif:replacedBy](replacedBy) (op) **exactly** 1 [agrif:Record](Record) (c)<br />[agrif:hasVersionHistory](hasVersionHistory) (op) **only** [agrif:VersionHistory](VersionHistory) (c)<br />
### Record Sentencing Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordSentencingEvent`
Description | A Record Sentencing Event is an Event that classifies an Agencies Record to a specific class of a Records Authority Disposal Class Policy. This helps determine the Records value and how it should be managed throughout its lifecycle.
Super-classes |[agrif:RecordControlEvent](RecordControlEvent) (c)<br />
### Record Storage Standard
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordStorageStandard`
Description | The Standard for the storage of non-digital archival Records is designed to set out the requirements for the safe storage and preservation of non-digital records in the Archives’ custody; to ensure all non-digital records are protected, secure and accessible for as long as they are required to meet business and accountability needs and community expectations; and to ensure all non-digital records are stored in the most cost-effective manner possible.
Super-classes |[agrif:Policy](Policy) (c)<br />
### Record Transfer Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordTransferEvent`
Description | A Transfer Event is a Disposal Event that results in a change of custody.
Example | `An example of a Record Transfer Event is the transfer of a Record from an Agency to the National Archives. Section 27 of the Archives Act 1983 requires Australian government agencies to transfer Records to the Archives within 15 years of their creation.`<br />
Super-classes |[agrif:RecordDisposalEvent](RecordDisposalEvent) (c)<br />
Restrictions |[agrif:transferredTo](transferredTo) (op) **some** [agrif:Role](Role) (c)<br />[agrif:transferredFrom](transferredFrom) (op) **some** [agrif:Role](Role) (c)<br />[agrif:hasManifest](hasManifest) (op) **only** [agrif:Manifest](Manifest) (c)<br />
### Records Authority Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityFunction`
Description | A Records Authority Function is a Function that is assigned by the National Archives to classify Agency business.
Super-classes |[agrif:Function](Function) (c)<br />
### Records Authority Disposal Class Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy`
Source | Australian Government Recordkeeping Metadata Standard
Description | A Records Authority Disposal Class Policy is a Policy that identifies the specific disposal class that authorises the retention or destruction of a Record.
Super-classes |[agrif:Policy](Policy) (c)<br />
Restrictions |[agrif:hasDisposalClass](hasDisposalClass) (op) **exactly** 1 [agrif:DisposalClass](DisposalClass) (c)<br />
Sub-classes |[agrif:DisposalClass](DisposalClass) (c)<br />
### Role
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Role`
Source | [https://www.w3.org/TR/prov-o/#Role](https://www.w3.org/TR/prov-o/#Role)
Description | A Role is the function of an entity or agent with respect to an Activity or Event, in the context of a usage, generation, invalidation, association, start, and end.
Restrictions |[agrif:hasPermission](hasPermission) (op) **some** [agrif:Permission](SecurityClearance) (c)<br />
Sub-classes |[agrif:BusinessOwner](BusinessOwner) (c)<br />[agrif:Creator](Creator) (c)<br />[agrif:User](User) (c)<br />[agrif:Administrator](Administrator) (c)<br />
### Security Classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SecurityClassification`
Source | Australian Government Recordkeeping Metadata Standard
Description | A Security Classification denotes the security status of a Record that an Agent needs to possess to access the Record.
Super-classes |[agrif:AccessControl](AccessControl) (c)<br />
Has members |[agrif:Secret](http://linked.data.gov.au/def/agrif#Secret)<br />[agrif:TopSecretPV](http://linked.data.gov.au/def/agrif#TopSecretPV)<br />[agrif:TopSecretNV](http://linked.data.gov.au/def/agrif#TopSecretNV)<br />[agrif:Protected](http://linked.data.gov.au/def/agrif#Protected)<br />[agrif:HighlyProtected](http://linked.data.gov.au/def/agrif#HighlyProtected)<br />[agrif:Confidential](http://linked.data.gov.au/def/agrif#Confidential)<br />[agrif:Unclassified](http://linked.data.gov.au/def/agrif#Unclassified)<br />
### Security Control
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SecurityControl`
Description | A Security Control is a safeguard or countermeasures to avoid, detect, counteract, or minimize security risks to a Record or Artefact.
Super-classes |[agrif:Control](Control) (c)<br />
### Series
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Series`
Description | A Series is an identifier for an item, and when combined with a control symbol gives an item its intellectual context.
Super-classes |[agrif:IntellectualControlSystem](IntellectualControlSystem) (c)<br />
Restrictions |[agrif:associatedFunction](associatedFunction) (op) **only** [agrif:Function](Function) (c)<br />
### Share Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#ShareActivity`
Description | A Share Activity is an Activity where the custodianship of a Record is transferred to or shared with Agents over a period of time.
Super-classes |[agrif:Activity](Activity) (c)<br />
Restrictions |[agrif:sharedWith](sharedWith) (op) **some** [agrif:Agent](Agent) (c)<br />
### Spatial Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SpatialCoverage`
Description | A Spatial Coverage denotes the spatial extent to which a Record is observed.
Super-classes |[agrif:Coverage](Coverage) (c)<br />
### Spatial Location
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#SpatialLocation`
Description | A Spatial Location describes where a something (e.g. a Record, Collection or Artefact) is physically located, using geospatial coordinates such as latitude and longitude.
Sub-classes |[agrif:HoldingSpace](HoldingSpace) (c)<br />
### Status
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Status`
Description | A Status indicates an Activities current state.
Sub-classes |[agrif:DecisionStatus](DecisionStatus) (c)<br />
Has members |[agrif:Disposed](http://linked.data.gov.au/def/agrif#Disposed)<br />[agrif:AwaitingDisposal](http://linked.data.gov.au/def/agrif#AwaitingDisposal)<br />[agrif:Redundant](http://linked.data.gov.au/def/agrif#Redundant)<br />[agrif:Active](http://linked.data.gov.au/def/agrif#Active)<br />[agrif:Completed](http://linked.data.gov.au/def/agrif#Completed)<br />
### Temporal Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#TemporalCoverage`
Description | A Temporal Coverage denotes the temporal extent to which a Record is observed.
Super-classes |[agrif:Coverage](Coverage) (c)<br />
### Trigger
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Trigger`
Description | A Trigger is an entity that initiated an Activity or Event.
Restrictions |[agrif:notifies](notifies) (op) **some** [agrif:Agent](Agent) (c)<br />
Sub-classes |[agrif:AccessTrigger](AccessTrigger) (c)<br />
### User
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#User`
Description | A User is an Agent that uses a Record.
Super-classes |[agrif:Role](Role) (c)<br />
### Version History
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#VersionHistory`
Description | A Version History is the cumulative change to a previous version of a file.

## Object Properties
[accessed By](#accessedBy),
[acts As](#actsAs),
[affects](#affects),
[associated Function](#associatedFunction),
[associated Role](#associatedRole),
[guiding Policy](#guidingPolicy),
[has Activity](#hasActivity),
[has Agent](#hasAgent),
[has Classifier](#hasClassifier),
[requires Control](#requiresControl),
[has Coverage](#hasCoverage),
[has Decision Status](#hasDecisionStatus),
[has Disposal Class](#hasDisposalClass),
[has Form Factor](#hasFormFactor),
[has Location](#hasLocation),
[has Manifest](#hasManifest),
[has Next Version](#hasNextVersion),
[has Part](#hasPart),
[has Permission](#hasPermission),
[prerequisite Decision Event](#prerequisiteDecisionEvent),
[has Previous Version](#hasPreviousVersion),
[has Quality](#hasQuality),
[has Series](#hasSeries),
[has Source Agent](#hasSourceAgent),
[has Status](#hasStatus),
[has Target Agent](#hasTargetAgent),
[has Version History](#hasVersionHistory),
[is Affected By](#isAffectedBy),
[is Attached To](#isAttachedTo),
[is Based On](#isBasedOn),
[is Changed By](#isChangedBy),
[is Duplicate Of](#isDuplicateOf),
[is Mentioned In](#isMentionedIn),
[is Part Of](#isPartOf),
[notifies](#notifies),
[part Of](#partOf),
[position In](#positionIn),
[prior Event](#priorEvent),
[qualified Association](#qualifiedAssociation),
[record Of](#recordOf),
[related To](#relatedTo),
[replaced By](#replacedBy),
[replaces](#replaces),
[requires Security Classification](#requiresSecurityClassification),
[shared With](#sharedWith),
[stored In](#storedIn),
[transferred From](#transferredFrom),
[transferred To](#transferredTo),
[triggered By](#triggeredBy),
[triggers](#triggers),
[used Record](#usedRecord),
[was Associated With](#wasAssociatedWith),
[](accessedBy)
### accessed By
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#accessedBy`
Description | A relation that indicates that an Agent has accessed a Record as defined in an Access Activity.
Super-properties |[agrif:wasAssociatedWith](wasAssociatedWith) (op)<br />
[](actsAs)
### acts As
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#actsAs`
Description | A relation between an Agent and the Role that Agent acts in.
[](affects)
### affects
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#affects`
Description | A relation between an Event and an Artefact or a Record.
[](associatedFunction)
### associated Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#associatedFunction`
Description | A relation that associates a Function to an Entity, Event or Activity.
[](associatedRole)
### associated Role
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#associatedRole`
Source | [https://www.w3.org/TR/prov-o/#hadRole](https://www.w3.org/TR/prov-o/#hadRole)
Description | An associated Role is a qualified association between a Role and an Activity or Event defined by an Association.
[](guidingPolicy)
### guiding Policy
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#guidingPolicy`
Description | A relation that defines a Policy that is guiding an Activity or Change Event.
[](hasActivity)
### has Activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasActivity`
Source | [https://www.w3.org/TR/prov-o/#p_activity](https://www.w3.org/TR/prov-o/#p_activity)
Description | A relation between a Record and an Activity that acts upon the Record.
[](hasAgent)
### has Agent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasAgent`
Source | [https://www.w3.org/TR/prov-o/#p_agent](https://www.w3.org/TR/prov-o/#p_agent)
Description | A qualified relation between an Agent and a Change Event defined through an Association.
[](hasClassifier)
### has Classifier
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasClassifier`
Super-properties |[owl:topObjectProperty](http://www.w3.org/2002/07/owl#topObjectProperty)<br />
[](requiresControl)
### requires Control
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasControl`
Description | A relation between a Record, Artefact or Event and a Control that denotes the required level of Access or Security Control.
[](hasCoverage)
### has Coverage
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasCoverage`
Description | A relation between a Record and its Jurisdictional Coverage, or its Temporal or Spatial Coverage.
[](hasDecisionStatus)
### has Decision Status
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasDecisionStatus`
Description | A relation that indicates what the Decision on a Decision Event was.
[](hasDisposalClass)
### has Disposal Class
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasDisposalClass`
Description | A relation that associates a Disposal Class with a Record.
[](hasFormFactor)
### has Form Factor
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasFormFactor`
Description | A relation that defines the size, shape, and other physical specifications of a Physical Artefact.
[](hasLocation)
### has Location
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasLocation`
Description | A relation that defines the Spatial Location of an Activity or Artefact.
[](hasManifest)
### has Manifest
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasManifest`
Description | A relation between a Manifest and a Transfer Event that describes the files involved in the transfer of a Record.
[](hasNextVersion)
### has Next Version
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasNextVersion`
Description | A relation that indicates that an Artefact has a newer version.
Super-properties |[agrif:relatedTo](relatedTo) (op)<br />
[](hasPart)
### has Part
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasPart`
Description | A relation that defines part-whole relations.
[](hasPermission)
### has Permission
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasPermission`
Description | A relation between an Agent and the Permission the Agent possesses.
[](prerequisiteDecisionEvent)
### prerequisite Decision Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasPrerequisiteDecisionEvent`
Description | A relation between a Decision Event and a prerequisite Decision Event, indicating a Decision chain in a Chain of Command.
Super-properties |[agrif:priorEvent](priorEvent) (op)<br />
[](hasPreviousVersion)
### has Previous Version
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasPreviousVersion`
Description | A relation that indicates that an Artefact has an older version.
Super-properties |[agrif:relatedTo](relatedTo) (op)<br />
[](hasQuality)
### has Quality
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasQuality`
Description | A relation that indicates a specific Quality of an Artefact.
[](hasSeries)
### has Series
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasSeries`
Description | A relation between a Record and its Series Number.
Super-properties |[owl:topObjectProperty](http://www.w3.org/2002/07/owl#topObjectProperty)<br />
[](hasSourceAgent)
### has Source Agent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasSourceAgent`
Description | A relation that denotes the source Agent of a Record or an Artefact in an Event or Activity.
Super-properties |[agrif:wasAssociatedWith](wasAssociatedWith) (op)<br />
[](hasStatus)
### has Status
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasStatus`
Description | A relation between an Activity and a Status that indicates its current state.
[](hasTargetAgent)
### has Target Agent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasTargetAgent`
Description | A relation that denotes the target Agent of a Record or an Artefact in an Event or Activity.
Super-properties |[agrif:wasAssociatedWith](wasAssociatedWith) (op)<br />
[](hasVersionHistory)
### has Version History
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#hasVersionHistory`
Description | A relation between a Record and its previous Version qualified through a Replace Event.
[](isAffectedBy)
### is Affected By
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#isAffectedBy`
Description | A relation between an Artefact or a Record and an Event.
Super-properties |[owl:topObjectProperty](http://www.w3.org/2002/07/owl#topObjectProperty)<br />
[](isAttachedTo)
### is Attached To
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#isAttachedTo`
Description | A relation that indicates that an Artefact is logically or physically attached to another Artefact.
Super-properties |[agrif:relatedTo](relatedTo) (op)<br />
[](isBasedOn)
### is Based On
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#isBasedOn`
Description | A relation that indicates that an Artefact is in part or as a whole based on another Artefact.
Super-properties |[agrif:relatedTo](relatedTo) (op)<br />
[](isChangedBy)
### is Changed By
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#isChangedBy`
Description | A relation that denotes the Information System that has been used to change an Artefact.
[](isDuplicateOf)
### is Duplicate Of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#isDuplicateOf`
Description | A relation that indicates that an Artefact is an exact copy of another Artefact, i.e. the content is exactly the same, but its Record may be different.
Super-properties |[agrif:relatedTo](relatedTo) (op)<br />
[](isMentionedIn)
### is Mentioned In
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#isMentionedIn`
Description | A relation that indicates that an Artefact is mentioned in another Artefact. An example of such a relation is a citation of a document in another document.
Super-properties |[agrif:relatedTo](relatedTo) (op)<br />
[](isPartOf)
### is Part Of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#isPartOf`
Description | A Collection in which the described Artefact is physically or logically included.
[](notifies)
### notifies
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#notifies`
Description | A relation between a Trigger and an Agent that is to be notified.
[](partOf)
### part Of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#partOf`
Description | A relation that defines part-whole relations.
[](positionIn)
### position In
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#positionIn`
Description | A relation that defines the position an Agent occupies in an Organisation or Organisational Unit.
[](priorEvent)
### prior Event
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#priorEvent`
Description | A relation indicating some causal link between an Event and a previously happening Event.
[](qualifiedAssociation)
### qualified Association
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#qualifiedAssociation`
Description | A relation that associates an assignment of responsibility to an Agent for an Activity or Event, indicating that the Agent had a Role in the Activity or Event.
[](recordOf)
### record Of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#recordOf`
Description | A relation that defines what Artefact the Record is about.
[](relatedTo)
### related To
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#relatedTo`
Description | A relation that indicates that there is some form of relation between a Record and another Record or between an Artefact and another Artefact.
[](replacedBy)
### replaced By
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#replacedBy`
Description | A relation that defines that a Record has been replaced by another Record, qualified through a Replace Event.
[](replaces)
### replaces
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#replaces`
Description | A relation that defines that a Record replaces another Record, qualified through a Replace Event.
[](requiresSecurityClassification)
### requires Security Classification
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#requiresSecurityClassification`
Description | A relation between a Record and a Security Classification that denotes the required level of Security Clearance an Agent needs to possess to access the Record.
Super-properties |[agrif:hasControl](requiresControl) (op)<br />
[](sharedWith)
### shared With
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#sharedWith`
Description | A relation that indicates that a Record was shared with an Agent as defined in a Share Activity.
Super-properties |[agrif:wasAssociatedWith](wasAssociatedWith) (op)<br />
[](storedIn)
### stored In
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#storedIn`
Description | A relation that indicates the Storage Location of an Artefact.
Super-properties |[owl:topObjectProperty](http://www.w3.org/2002/07/owl#topObjectProperty)<br />
[](transferredFrom)
### transferred From
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#transferredFrom`
Description | A relation that defines that the Control of a Record has been transferred from that Role.
[](transferredTo)
### transferred To
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#transferredTo`
Description | A relation that defines that the Control of a Record has been transferred to that new Role.
[](triggeredBy)
### triggered By
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#triggeredBy`
Description | A relation that indicates that an Event has been initiated by a Trigger.
[](triggers)
### triggers
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#triggers`
Description | A relation that indicates that a Trigger has initiated a Change Event.
[](usedRecord)
### used Record
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#usedRecord`
Description | A relation between an Activity and a Record the Activity uses.
[](wasAssociatedWith)
### was Associated With
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#wasAssociatedWith`
Source | [https://www.w3.org/TR/prov-o/#wasAssociatedWith](https://www.w3.org/TR/prov-o/#wasAssociatedWith)
Description | A relation that assigns responsibility of an Agent with an Activity or Event.

## Datatype Properties
[checksum](#checksum),
[disposalClassNumber](#disposalClassNumber),
[endedAtTime](#endedAtTime),
[filename](#filename),
[filesize](#filesize),
[format](#format),
[seriesNumber](#seriesNumber),
[softwareAssignedID](#softwareAssignedID),
[startedAtTime](#startedAtTime),
[](checksum)
### checksum
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#checksum`
Description | A checksum is a small-sized datum derived from a block of digital data representing a Record for the purpose of detecting errors during the transfer or storage of a Record.
Range(s) |[[xsd:float](http://www.w3.org/2001/XMLSchema#float)]([xsd:float](http://www.w3.org/2001/XMLSchema#float)) (c)<br />
[](disposalClassNumber)
### disposalClassNumber
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#disposalClassNumber`
Description | The number defining the sentencing requirements of a Record.
Range(s) |[[xsd:integer](http://www.w3.org/2001/XMLSchema#integer)]([xsd:integer](http://www.w3.org/2001/XMLSchema#integer)) (c)<br />
[](endedAtTime)
### endedAtTime
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#endedAtTime`
Source | [https://www.w3.org/TR/prov-o/#endedAtTime](https://www.w3.org/TR/prov-o/#endedAtTime)
Description | The time at which an Activity ended.
Range(s) |[[xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime)]([xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime)) (c)<br />
[](filename)
### filename
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#filename`
Description | A filename is a name used to uniquely identify a computer file stored in a file system.
[](filesize)
### filesize
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#filesize`
Description | File size is a measure of how much data a computer file contains or how much storage it consumes.
[](format)
### format
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#format`
Source | [dc:format](http://purl.org/dc/elements/1.1/format)
Description | The file format, physical medium, or dimensions of the resource.
[](seriesNumber)
### seriesNumber
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#seriesNumber`
Description | A seriesNumber is a numerical identifier for a Series.
Range(s) |[[xsd:integer](http://www.w3.org/2001/XMLSchema#integer)]([xsd:integer](http://www.w3.org/2001/XMLSchema#integer)) (c)<br />
[](softwareAssignedID)
### softwareAssignedID
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#softwareAssignedID`
Description | A softwareAssignedID is an identifier given to an Artefact by an Information System.
Range(s) |[[xsd:string](http://www.w3.org/2001/XMLSchema#string)]([xsd:string](http://www.w3.org/2001/XMLSchema#string)) (c)<br />
[](startedAtTime)
### startedAtTime
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#startedAtTime`
Source | [https://www.w3.org/TR/prov-o/#startedAtTime](https://www.w3.org/TR/prov-o/#startedAtTime)
Description | The time at which and Activity started
Range(s) |[[xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime)]([xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime)) (c)<br />

## Annotation Properties
[contributor](#contributor),
[source](#source),
[example](#example),
[identifier](#identifier),
[name](#name),
[](contributor)
### contributor
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/contributor`
[](source)
### source
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/source`
[](example)
### example
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#example`
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
[Active](#Active),
[Approved](#Approved),
[AwaitingDisposal](#AwaitingDisposal),
[Completed](#Completed),
[Confidential](#Confidential),
[Disapproved](#Disapproved),
[Disposed](#Disposed),
[Highly Protected](#HighlyProtected),
[Protected](#Protected),
[Redundant](#Redundant),
[RetainAsNationalArchives](#RetainAsNationalArchives),
[Secret](#Secret),
[Top Secret (NV)](#TopSecret(NV)),
[Top Secret (PV)](#TopSecret(PV)),
[Unclassified](#Unclassified),
### Active <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Active`
* **Contributor(s)**
  * [agrif:Status](http://linked.data.gov.au/def/agrif#Status)
### Approved <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Approved`
* **Contributor(s)**
  * [agrif:DecisionStatus](http://linked.data.gov.au/def/agrif#DecisionStatus)
### AwaitingDisposal <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#AwaitingDisposal`
* **Contributor(s)**
  * [agrif:Status](http://linked.data.gov.au/def/agrif#Status)
### Completed <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Completed`
* **Contributor(s)**
  * [agrif:Status](http://linked.data.gov.au/def/agrif#Status)
### Confidential <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Confidential`
* **Contributor(s)**
  * [agrif:SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification)
### Disapproved <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Disapproved`
* **Contributor(s)**
  * [agrif:DecisionStatus](http://linked.data.gov.au/def/agrif#DecisionStatus)
### Disposed <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Disposed`
* **Contributor(s)**
  * [agrif:Status](http://linked.data.gov.au/def/agrif#Status)
### Highly Protected <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#HighlyProtected`
* **Contributor(s)**
  * [agrif:SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification)
### Protected <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Protected`
* **Contributor(s)**
  * [agrif:SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification)
### Redundant <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Redundant`
* **Contributor(s)**
  * [agrif:Status](http://linked.data.gov.au/def/agrif#Status)
### RetainAsNationalArchives <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#RetainAsNationalArchives`
* **Contributor(s)**
  * [agrif:DisposalClass](http://linked.data.gov.au/def/agrif#DisposalClass)
### Secret <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Secret`
* **Contributor(s)**
  * [agrif:SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification)
### Top Secret (NV) <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#TopSecretNV`
* **Contributor(s)**
  * [agrif:SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification)
### Top Secret (PV) <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#TopSecretPV`
* **Contributor(s)**
  * [agrif:SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification)
### Unclassified <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/agrif#Unclassified`
* **Contributor(s)**
  * [agrif:SecurityClassification](http://linked.data.gov.au/def/agrif#SecurityClassification)
## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/agrif#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
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
* **vann**
  * `http://purl.org/vocab/vann/`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`
* **agrif**
  * `http://linked.data.gov.au/def/agrif#`

## Legend
* Classes: c
* Object Properties: op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: dp
* Properties: p
* Named Individuals: ni