# The Australian Government Records Interoperability Framework (AGRIF) ontology
<sub>metadata by [pyLODE](http://github.com/rdflib/pyLODE)</sub>
## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/agrif`
* **Publisher(s)**
  * <a href="http://linked.data.gov.au/org/finance">Department of Finance</a>
* **Creators(s)**
  * John Machin of <a href="http://linked.data.gov.au/org/finance">Department of Finance</a>
  * <a href="https://orcid.org/0000-0003-3425-0780">Armin Haller</a> (<a href="mailto:armin.haller@anu.edu.au">armin.haller@anu.edu.au</a>) of <a href="http://linked.data.gov.au/org/anu">Australian National University</a>
  * Katherine Stuart of <a href="http://linked.data.gov.au/org/finance">Department of Finance</a>
* **Contributor(s)**
  * <a href="http://orcid.org/0000-0002-8742-7730">Nicholas Car</a>
* **Created**
  * 2016-12-06
* **Modified**
  * 2019-11-04
* **Version Information**
  * 0.7
* **Rights**
  * (c) Commonwealth of Australia (Department of Finance) 2017
* **Ontology Source**
  * <a href="agrif.ttl">RDF (turtle)</a>
* **Code Repository**
  * <https://github.com/AGLDWG/agrif-ont>
### Description
<p>The Australian Government Records Interoperability Framework (AGRIF, ‘the Framework’) is a system of related semantic ontologies that describe the structure, functions, and activities of the Australian Government, providing sufficient context for the effective use – including but not limited to management – of Australian Government information assets. It complies with the World Wide Web Consortium’s Web Ontology Language (OWL2) Recommendation and makes reference to other Recommendations and existing domain ontologies for archival and preservation processes.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Namespaces](#namespaces)  


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
[Association](#Association),
[Audit Event](#AuditEvent),
[Business Owner](#BusinessOwner),
[Classifier](#Classifier),
[Control](#Control),
[Control Event](#ControlEvent),
[Controlled Vocabulary](#ControlledVocabulary),
[Coverage](#Coverage),
[Creation Event](#CreationEvent),
[Creator](#Creator),
[Decision Event](#DecisionEvent),
[Decision Status](#DecisionStatus),
[Destroy Event](#DestroyEvent),
[Digital Artefact](#DigitalArtefact),
[Digital Holding Space](#DigitalHoldingSpace),
[Digital Preservation Policy](#DigitalPreservationPolicy),
[Disposal Class](#DisposalClass),
[Disposal Event](#DisposalEvent),
[Event](#Event),
[Form Factor](#FormFactor),
[Freeze Event](#FreezeEvent),
[Function](#Function),
[Holding Space](#HoldingSpace),
[Information Management Policy](#InformationManagementPolicy),
[Information System](#InformationSystem),
[Intellectual Control System](#IntellectualControlSystem),
[Jurisdictional Coverage](#JurisdictionalCoverage),
[Maintain Activity](#MaintainActivity),
[Manifest](#Manifest),
[Minimum Metadata Set Policy](#MinimumMetadataSetPolicy),
[Organisation](#Organisation),
[Organisational Unit](#OrganisationalUnit),
[Permission](#Permission),
[Person](#Person),
[Physical Artefact](#PhysicalArtefact),
[Physical Holding Space](#PhysicalHoldingSpace),
[Policy](#Policy),
[Preservation Quality](#PreservationQuality),
[Quality](#Quality),
[Record](#Record),
[Record Storage Standard](#RecordStorageStandard),
[Records Authority Disposal Class Policy](#RecordsAuthorityDisposalClassPolicy),
[Records Authority Function](#RecordsAuthorityFunction),
[Replace Event](#ReplaceEvent),
[Role](#Role),
[Security Classification](#SecurityClassification),
[Security Control](#SecurityControl),
[Sentencing Event](#SentencingEvent),
[Series](#Series),
[Share Activity](#ShareActivity),
[Spatial Coverage](#SpatialCoverage),
[Spatial Location](#SpatialLocation),
[Status](#Status),
[Temporal Coverage](#TemporalCoverage),
[Transfer Event](#TransferEvent),
[Trigger](#Trigger),
[User](#User),
[Version History](#VersionHistory),
[VocabularyEncodingScheme](#VocabularyEncodingScheme),
### AGIFT Function <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AGIFTFunction`
Description | An AGIFT Function is a Function that classifies a Record according to the Australian Governments' Interactive Functions Thesaurus.
Super-classes |<a href="#Function">Function</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Access Activity <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AccessActivity`
Description | An Access Activity is an Activity where a Record is accessed by an Agent over a period of time.
Super-classes |<a href="#Activity">Activity</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#accessedBy">accessedBy</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Agent">Agent</a><sup class="sup-c" title="class">c</sup><br /><a href="#triggers">triggers</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#AccessTrigger">AccessTrigger</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Access Control <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AccessControl`
Description | Access Control is the selective restriction of access to a Record or Artefact.
Super-classes |<a href="#Control">Control</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |<a href="#SecurityClassification">SecurityClassification</a><sup class="sup-c" title="class">c</sup><br />
### Access Trigger <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AccessTrigger`
Description | An Access Trigger is a Trigger that can be initiated when a Record is accessed.
Super-classes |<a href="#Trigger">Trigger</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Activity <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Activity`
Description | An Activity is something that occurs over a period of time on a Record.
### Administrator <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Administrator`
Description | An Administrator is a Role that has overall responsibility for the administration and functions of an Information System, but not necessarily for the information stored within.
Super-classes |<a href="#Role">Role</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Agent <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Agent`
Description | An Agent is a corporate entity, organisational element or system, or individual responsible for the performance of some Activity or Event, including those on Records.
### Artefact <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Artefact`
Description | An Artefact is an object that is made by a Person and that is to be preserved.
### Association <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Association`
Description | An Association is a qualified assignment of responsibility to an Agent in an Activity or Event, indicating that the Agent had a Role in the Activity.
### Audit Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#AuditEvent`
Description | An Audit Event is the systematic examination of a Record to ascertain how and where the Record is stored, who created it, or manages it, who uses it and how much longer the Record is required to be maintained.
Super-classes |<a href="#ControlEvent">ControlEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Business Owner <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#BusinessOwner`
Description | A Business Owner is the Role that has the managerial control of a Function.
Super-classes |<a href="#Role">Role</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Classifier <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Classifier`
Description | A Classifier is a machine-generated and applied category that a set of Records belong to.
### Control <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Control`
Description | A Control is a security or access measure that safeguards or restricts access to an asset.
### Control Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ControlEvent`
Description | A Control Event is an Event that requires a particular level of access to the Record.
Super-classes |<a href="#Event">Event</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#requiresControl">hasControl</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Control">Control</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#SentencingEvent">SentencingEvent</a><sup class="sup-c" title="class">c</sup><br /><a href="#ReplaceEvent">ReplaceEvent</a><sup class="sup-c" title="class">c</sup><br /><a href="#AuditEvent">AuditEvent</a><sup class="sup-c" title="class">c</sup><br /><a href="#DisposalEvent">DisposalEvent</a><sup class="sup-c" title="class">c</sup><br /><a href="#DecisionEvent">DecisionEvent</a><sup class="sup-c" title="class">c</sup><br />
### Controlled Vocabulary <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ControlledVocabulary`
Description | A Controlled Vocabulary is an Intellectual Control System that provides a way to organize Records that facilitates a later discovery of a Record.
Super-classes |<a href="#IntellectualControlSystem">IntellectualControlSystem</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#associatedFunction">associatedFunction</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 1 <a href="#Function">Function</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Coverage <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Coverage`
Description | A Coverage denotes the jurisdictional applicability, or the temporal and/or spatial extent to which a Record is observed.
### Creation Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#CreationEvent`
Description | A Creation Event is a Change Event that results in the creation of a Record.
Super-classes |<a href="#Event">Event</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Creator <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Creator`
Description | A Creator is the Agent that has created a Record or Artefact.
Super-classes |<a href="#Role">Role</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Decision Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DecisionEvent`
Description | A Decision Event changes the Decision Status on the Control of a Record.
Super-classes |<a href="#ControlEvent">ControlEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#hasPrerequisiteDecisionEvent">hasPrerequisiteDecisionEvent</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#DecisionEvent">DecisionEvent</a><sup class="sup-c" title="class">c</sup><br /><a href="#hasDecisionStatus">hasDecisionStatus</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#DecisionStatus">DecisionStatus</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Decision Status <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DecisionStatus`
Description | A Decision Status is a Status that indicates the approval or disapproval of a Decision Event.
Super-classes |<a href="#Status">Status</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Destroy Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DestroyEvent`
Description | A Destroy Event is a Disposal Event that results in the regular authorised permanent desctruction of a Record that is no longer required for business purposes.
Super-classes |<a href="#DisposalEvent">DisposalEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Digital Artefact <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DigitalArtefact`
Description | A Digital Artefact is an Artefact that is of a digital nature and stored in an Information System.
Super-classes |<a href="#Artefact">Artefact</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#filesize">filesize</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">some</span> <a href="http://www.w3.org/2001/XMLSchema#long">xsd:long</a><sup class="sup-c" title="class">c</sup><br /><a href="#filename">filename</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">some</span> <a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br /><a href="#storedIn">storedIn</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#InformationSystem">InformationSystem</a><sup class="sup-c" title="class">c</sup><br /><a href="#format">format</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">some</span> <a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Digital Holding Space <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DigitalHoldingSpace`
Description | A Digital Holding Space is a space that is used or reserved for the storage of a Digital Artefact on a storage medium or virtual storage space.
Super-classes |<a href="#HoldingSpace">HoldingSpace</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Digital Preservation Policy <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DigitalPreservationPolicy`
Description | The Digital Preservation Policy defines the process of active management by which the National Archives ensures that a digital object will be accessible in the future.
Super-classes |<a href="#Policy">Policy</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Disposal Class <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DisposalClass`
Description | A Disposal Class is a Policy that defines the sentencing requirements of an item.
Super-classes |<a href="#RecordsAuthorityDisposalClassPolicy">RecordsAuthorityPolicy</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#disposalClassNumber">disposalClassNumber</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">exactly</span> 1<br />
Sub-classes |
### Disposal Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#DisposalEvent`
Description | A Disposal Event is an Event that results in the regular authorised destruction or change of custody of a Record that is no longer required for business purposes.
Super-classes |<a href="#ControlEvent">ControlEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |<a href="#TransferEvent">TransferEvent</a><sup class="sup-c" title="class">c</sup><br /><a href="#FreezeEvent">FreezeEvent</a><sup class="sup-c" title="class">c</sup><br /><a href="#DestroyEvent">DestroyEvent</a><sup class="sup-c" title="class">c</sup><br />
### Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Event`
Description | An Event denotes an instantaneous transition in the world.
### Form Factor <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#FormFactor`
Description | A Form Factor defines and prescribes the size, shape, and other physical specifications of a Physical Artefact that is stored.
### Freeze Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#FreezeEvent`
Description | A Freeze Event is a Disposal Event that leads to a records disposal freeze or retention notice in support of compliance requirements or an identified need to suspend the Archives' records destruction permissions.
Super-classes |<a href="#DisposalEvent">DisposalEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Function <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Function`
Description | A Function reflects the responsibilities of an Organisation that can be delegated through official channels. [Commonwealth Records Series Manual]
### Holding Space <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#HoldingSpace`
Description | A Holding Space is a space that is used or reserved for the storage of an Artefact.
Super-classes |<a href="#SpatialLocation">SpatialLocation</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |<a href="#PhysicalHoldingSpace">PhysicalHoldingSpace</a><sup class="sup-c" title="class">c</sup><br /><a href="#DigitalHoldingSpace">DigitalHoldingSpace</a><sup class="sup-c" title="class">c</sup><br />
### Information Management Policy <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#InformationManagementPolicy`
Description | An Information Management Policy is a Policy that helps to align information management practices to fulfill the requirements of an information governance framework. An Information Management Policy provides direction and guidance to staff for creating, capturing and managing information to satisfy business, legal and stakeholder requirements, and assigns responsibilities across the agency.
Super-classes |<a href="#Policy">Policy</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#hasDisposalClass">hasDisposalClass</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#DisposalClass">DisposalClass</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Information System <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#InformationSystem`
Description | An Information System is an organized system for the collection, organization, storage and communication of information, typically Digital Artefacts or Records.
### Intellectual Control System <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#IntellectualControlSystem`
Description | An Intellectual Control System is a System that enables Agents to locate and manage information.
Super-classes |<a href="#InformationSystem">InformationSystem</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#guidingPolicy">guidingPolicy</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#Policy">Policy</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#Series">Series</a><sup class="sup-c" title="class">c</sup><br /><a href="#ControlledVocabulary">ControlledVocabulary</a><sup class="sup-c" title="class">c</sup><br />
### Jurisdictional Coverage <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#JurisdictionalCoverage`
Description | A Jurisdictional Coverage denotes the jurisdictional applicability of the Record.
Super-classes |<a href="#Coverage">Coverage</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Maintain Activity <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#MaintainActivity`
Description | A Maintain Activity is an Activity to maintain a Record over a period of time due to a BusinessFunction or Policy.
Super-classes |<a href="#Activity">Activity</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#hasQuality">hasQuality</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#PreservationQuality">PreservationQuality</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Manifest <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Manifest`
Description | A Manifest describes the files involved in the transfer of a Record from an Agency to the National Archives, including details such as the filesize, the destination hierarchy and the file's metadata.
### Minimum Metadata Set Policy <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#MinimumMetadataSetPolicy`
Description | The Minimum Metadata Set Policy is a Policy that has been developed by the National Archives of Australia to identify metadata properties essential for agency management of information as well as those needed for records which will be transferred to the Archives. It supports the Digital Continuity 2020 principles of interoperable systems and processes and is a practical application of the Australian Government Recordkeeping Metadata Standard 2.2 (AGRkMS) to support metadata implementation and information use in agencies.
Super-classes |<a href="#Policy">Policy</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Organisation <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Organisation`
Description | An Organisation is a type of Agent that denotes a social or legal institution such as a government agency, a corporation, society, etc.
Super-classes |<a href="#Agent">Agent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#associatedFunction">associatedFunction</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Function">Function</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#OrganisationalUnit">OrganisationalUnit</a><sup class="sup-c" title="class">c</sup><br />
### Organisational Unit <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#OrganisationalUnit`
Description | An Organisational Unit is a division of labour typically organised around a business function that form part of the Organisation.
Super-classes |<a href="#Organisation">Organisation</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#partOf">partOf</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Organisation">Organisation</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Permission <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Permission`
Description | A Permission denotes the Security Clearance of an Agent that determines its access and use rights to Records.
### Person <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Person`
Description | A Person is an Agent that denotes a human.
Super-classes |<a href="#Agent">Agent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Physical Artefact <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#PhysicalArtefact`
Description | A Physical Artefact is an Artefact that is of physical nature.
Super-classes |<a href="#Artefact">Artefact</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#hasFormFactor">hasFormFactor</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#FormFactor">FormFactor</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Physical Holding Space <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#PhysicalHoldingSpace`
Description | A Physical Holding Space is a Spatial Location that is used or reserved for the storage of a Physical Artefact.
Super-classes |<a href="#HoldingSpace">HoldingSpace</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Policy <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Policy`
Description | A Policy is a deliberate system of principles to guide decisions and achieve rational outcomes.
### Preservation Quality <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#PreservationQuality`
Description | A Preservation Quality describes a Quality of an Artefact that supports or threatens the long term preservation of the information that is to be preserved.
Super-classes |<a href="#Quality">Quality</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Quality <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Quality`
Description | A Quality is an attribute that is intrinsically associated with an entity.
### Record <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Record`
Description | A Record is information in any format created, received and maintained as evidence by an Organisation or Person, in pursuance of legal obligations or in the transaction of business. A Record may comprise a Digital or Physical Artefact.
### Record Storage Standard <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordStorageStandard`
Description | The Standard for the storage of non-digital archival Records is designed to set out the requirements for the safe storage and preservation of non-digital records in the Archives’ custody; to ensure all non-digital records are protected, secure and accessible for as long as they are required to meet business and accountability needs and community expectations; and to ensure all non-digital records are stored in the most cost-effective manner possible.
Super-classes |<a href="#Policy">Policy</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Records Authority Function <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityFunction`
Description | A Records Authority Function is a Function that is assigned by the National Archives to classify Agency business.
Super-classes |<a href="#Function">Function</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Records Authority Disposal Class Policy <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#RecordsAuthorityPolicy`
Description | A Records Authority Disposal Class Policy is a Policy that identifies the specific disposal class that authorises the retention or destruction of a Record.
Super-classes |<a href="#Policy">Policy</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#hasDisposalClass">hasDisposalClass</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#DisposalClass">DisposalClass</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#DisposalClass">DisposalClass</a><sup class="sup-c" title="class">c</sup><br />
### Replace Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ReplaceEvent`
Description | A Replace Event is an Event that results in the replacement of a Record with a new version. Edits to a Record constitute a Replace Event.
Super-classes |<a href="#ControlEvent">ControlEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#hasVersionHistory">hasVersionHistory</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#VersionHistory">VersionHistory</a><sup class="sup-c" title="class">c</sup><br /><a href="#replacedBy">replacedBy</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">exactly</span> 1 <a href="#Record">Record</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Role <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Role`
Description | A Role is the function of an entity or agent with respect to an Activity or Event, in the context of a usage, generation, invalidation, association, start, and end.
### Security Classification <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SecurityClassification`
Description | A Security Classification denotes the security status of a Record that an Agent needs to possess to access the Record.
Super-classes |<a href="#AccessControl">AccessControl</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Security Control <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SecurityControl`
Description | A Security Control is a safeguard or countermeasures to avoid, detect, counteract, or minimize security risks to a Record or Artefact.
Super-classes |<a href="#Control">Control</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Sentencing Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SentencingEvent`
Description | A Sentencing Event is an Event that classifies an Agencies Record to a specific class of a Records Authority Policy. This helps determine the Records value and how it should be managed throughout its lifecycle.
Super-classes |<a href="#ControlEvent">ControlEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Series <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Series`
Description | A Series is an identifier for an item, and when combined with a control symbol gives an item its intellectual context.
Super-classes |<a href="#IntellectualControlSystem">IntellectualControlSystem</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#associatedFunction">associatedFunction</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#Function">Function</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Share Activity <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#ShareActivity`
Description | A Share Activity is an Activity where the custodianship of a Record is transferred to or shared with Agents over a period of time.
Super-classes |<a href="#Activity">Activity</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#sharedWith">sharedWith</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Agent">Agent</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Spatial Coverage <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SpatialCoverage`
Description | A Spatial Coverage denotes the spatial extent to which a Record is observed.
Super-classes |<a href="#Coverage">Coverage</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Spatial Location <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#SpatialLocation`
Description | A Spatial Location describes where a something (e.g. a Record, Collection or Artefact) is physically located, using geospatial coordinates such as latitude and longitude.
### Status <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Status`
Description | A Status indicates an Activities current state.
### Temporal Coverage <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#TemporalCoverage`
Description | A Temporal Coverage denotes the temporal extent to which a Record is observed.
Super-classes |<a href="#Coverage">Coverage</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Transfer Event <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#TransferEvent`
Description | A Transfer Event is a Disposal Event that results in a change of custody.
Super-classes |<a href="#DisposalEvent">DisposalEvent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#transferredTo">transferredTo</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#BusinessOwner">BusinessOwner</a><sup class="sup-c" title="class">c</sup><br /><a href="#transferredFrom">transferredFrom</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Role">Role</a><sup class="sup-c" title="class">c</sup><br /><a href="#transferredTo">transferredTo</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Role">Role</a><sup class="sup-c" title="class">c</sup><br /><a href="#transferredFrom">transferredFrom</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#BusinessOwner">BusinessOwner</a><sup class="sup-c" title="class">c</sup><br /><a href="#hasManifest">hasManifest</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">some</span> <a href="#Manifest">Manifest</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |
### Trigger <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#Trigger`
Description | A Trigger is an entity that initiated an Activity or Event.
### User <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#User`
Description | A User is an Agent that uses a Record.
Super-classes |<a href="#Role">Role</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Version History <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#VersionHistory`
Description | A Version History is the cumulative change to a previous version of a file.
### VocabularyEncodingScheme <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/dcam/VocabularyEncodingScheme`

## Object Properties
[accessed By](accessedBy),
[acts As](actsAs),
[associated Function](associatedFunction),
[associated Role](associatedRole),
[guiding Policy](guidingPolicy),
[has Activity](hasActivity),
[has Agent](hasAgent),
[has Classifier](hasClassifier),
[requires Control](requiresControl),
[has Coverage](hasCoverage),
[has Decision Status](hasDecisionStatus),
[has Disposal Class](hasDisposalClass),
[has Form Factor](hasFormFactor),
[has Location](hasLocation),
[has Manifest](hasManifest),
[has Part](hasPart),
[has Permission](hasPermission),
[has Prerequisite Decision Event](hasPrerequisiteDecisionEvent),
[has Quality](hasQuality),
[has Series](hasSeries),
[has Status](hasStatus),
[has Version History](hasVersionHistory),
[is Changed By](isChangedBy),
[notifies](notifies),
[part Of](partOf),
[position In](positionIn),
[qualified Association](qualifiedAssociation),
[record Of](recordOf),
[related To](relatedTo),
[replaced By](replacedBy),
[replaces](replaces),
[requires Security Classification](requiresSecurityClassification),
[shared With](sharedWith),
[stored In](storedIn),
[transferred From](transferredFrom),
[transferred To](transferredTo),
[triggered By](triggeredBy),
[triggers](triggers),
[used Record](usedRecord),
[was Associated With](wasAssociatedWith),
[](accessedBy)
### accessed By <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#accessedBy`
Description | A relation that indicates that an Agent has accessed a Record as defined in an Access Activity.
Super-properties |<a href="#wasAssociatedWith">wasAssociatedWith</a><sup class="sup-op" title="object property">op</sup><br />
[](actsAs)
### acts As <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#actsAs`
Description | A relation between an Agent and the Role that Agent acts in.
[](associatedFunction)
### associated Function <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#associatedFunction`
Description | A relation that associates a Function to an Entity, Event or Activity.
[](associatedRole)
### associated Role <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#associatedRole`
Description | An associated Role is a qualified association between a Role and an Activity or Event defined by an Association.
[](guidingPolicy)
### guiding Policy <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#guidingPolicy`
Description | A relation that defines a Policy that is guiding an Activity or Change Event.
[](hasActivity)
### has Activity <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasActivity`
Description | A relation between a Record and an Activity that acts upon the Record.
[](hasAgent)
### has Agent <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasAgent`
Description | A qualified relation between an Agent and a Change Event defined through an Association.
[](hasClassifier)
### has Classifier <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasClassifier`
Super-properties |<a href="http://www.w3.org/2002/07/owl#topObjectProperty">owl:topObjectProperty</a><br />
[](requiresControl)
### requires Control <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasControl`
Description | A relation between a Record, Artefact or Event and a Control that denotes the required level of Access or Security Control.
[](hasCoverage)
### has Coverage <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasCoverage`
Description | A relation between a Record and its Jurisdictional Coverage, or its Temporal or Spatial Coverage.
[](hasDecisionStatus)
### has Decision Status <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasDecisionStatus`
Description | A relation that indicates what the Decision on a Decision Event was.
[](hasDisposalClass)
### has Disposal Class <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasDisposalClass`
Description | A relation that associates a Disposal Class with a Record.
[](hasFormFactor)
### has Form Factor <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasFormFactor`
Description | A relation that defines the size, shape, and other physical specifications of a Physical Artefact.
[](hasLocation)
### has Location <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasLocation`
Description | A relation that defines the Spatial Location of an Activity or Artefact.
[](hasManifest)
### has Manifest <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasManifest`
Description | A relation between a Manifest and a Transfer Event that describes the files involved in the transfer of a Record.
[](hasPart)
### has Part <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasPart`
Description | A relation that defines part-whole relations amongst Organisational Units.
[](hasPermission)
### has Permission <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasPermission`
Description | A relation between an Agent and the Permission the Agent possesses.
[](hasPrerequisiteDecisionEvent)
### has Prerequisite Decision Event <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasPrerequisiteDecisionEvent`
Description | A relation between a Decision Event and a prerequisite Decision Event, indicating a Decision chain in a Chain of Command.
[](hasQuality)
### has Quality <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasQuality`
Description | A relation that indicates a specific Quality of an Artefact.
[](hasSeries)
### has Series <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasSeries`
Description | A relation between a Record and its Series Number.
Super-properties |<a href="http://www.w3.org/2002/07/owl#topObjectProperty">owl:topObjectProperty</a><br />
[](hasStatus)
### has Status <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasStatus`
Description | A relation between an Activity and a Status that indicates its current state.
[](hasVersionHistory)
### has Version History <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#hasVersionHistory`
Description | A relation between a Record and its previous Version qualified through a Replace Event.
[](isChangedBy)
### is Changed By <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#isChangedBy`
Description | A relation between an Artefact or a Record and a Change Event.
Super-properties |<a href="http://www.w3.org/2002/07/owl#topObjectProperty">owl:topObjectProperty</a><br />
[](notifies)
### notifies <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#notifies`
Description | A relation between a Trigger and an Agent that is to be notified.
[](partOf)
### part Of <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#partOf`
Description | A relation that defines part-whole relations amongst Organisational Units.
[](positionIn)
### position In <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#positionIn`
Description | A relation that defines the position an Agent occupies in an Organisation or Organisational Unit.
[](qualifiedAssociation)
### qualified Association <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#qualifiedAssociation`
Description | A relation that associates an assignment of responsibility to an Agent for an Activity or Event, indicating that the Agent had a Role in the Activity or Event.
[](recordOf)
### record Of <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#recordOf`
Description | A relation that defines what Artefact the Record is about.
[](relatedTo)
### related To <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#relatedTo`
Description | A relation that indicates that there is some form of relation between a Record and another Record or between an Artefact and another Artefact.
[](replacedBy)
### replaced By <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#replacedBy`
Description | A relation that defines that a Record has been replaced by another Record, qualified through a Replace Event.
[](replaces)
### replaces <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#replaces`
Description | A relation that defines that a Record replaces another Record, qualified through a Replace Event.
[](requiresSecurityClassification)
### requires Security Classification <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#requiresSecurityClassification`
Description | A relation between a Record and a Security Classification that denotes the required level of Security Clearance an Agent needs to possess to access the Record.
Super-properties |<a href="#requiresControl">hasControl</a><sup class="sup-op" title="object property">op</sup><br />
[](sharedWith)
### shared With <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#sharedWith`
Description | A relation that indicates that a Record was shared with an Agent as defined in a Share Activity.
Super-properties |<a href="#wasAssociatedWith">wasAssociatedWith</a><sup class="sup-op" title="object property">op</sup><br />
[](storedIn)
### stored In <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#storedIn`
Description | A relation that indicates the Storage Location of an Artefact.
Super-properties |<a href="http://www.w3.org/2002/07/owl#topObjectProperty">owl:topObjectProperty</a><br />
[](transferredFrom)
### transferred From <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#transferredFrom`
Description | A relation that defines that the Control of a Record has been transferred from that Role.
[](transferredTo)
### transferred To <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#transferredTo`
Description | A relation that defines that the Control of a Record has been transferred to that new Role.
[](triggeredBy)
### triggered By <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#triggeredBy`
Description | A relation that indicates that a Change Event has been initiated by a Trigger.
[](triggers)
### triggers <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#triggers`
Description | A relation that indicates that a Trigger has initiated a Change Event.
[](usedRecord)
### used Record <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#usedRecord`
Description | A relation between an Activity and a Record the Activity uses.
[](wasAssociatedWith)
### was Associated With <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#wasAssociatedWith`
Description | A relation that assigns responsibility of an Agent for an Activity or Change Event.

## Datatype Properties
[checksum](checksum),
[disposalClassNumber](disposalClassNumber),
[endedAtTime](endedAtTime),
[filename](filename),
[filesize](filesize),
[format](format),
[seriesNumber](seriesNumber),
[](checksum)
### checksum <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#checksum`
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#float">xsd:float</a><sup class="sup-c" title="class">c</sup><br />
[](disposalClassNumber)
### disposalClassNumber <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#disposalClassNumber`
Description | The number defining the sentencing requirements of a Record.
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a><sup class="sup-c" title="class">c</sup><br />
[](endedAtTime)
### endedAtTime <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#endedAtTime`
Description | The time at which an Activity ended.
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#dateTime">xsd:dateTime</a><sup class="sup-c" title="class">c</sup><br />
[](filename)
### filename <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#filename`
Description | A filename is a name used to uniquely identify a computer file stored in a file system.
[](filesize)
### filesize <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#filesize`
Description | File size is a measure of how much data a computer file contains or how much storage it consumes.
[](format)
### format <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#format`
Description | The file format, physical medium, or dimensions of the resource.
[](seriesNumber)
### seriesNumber <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/agrif#seriesNumber`
Description | A seriesNumber is a numerical identifier for a Series.
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#integer">xsd:integer</a><sup class="sup-c" title="class">c</sup><br />

## Annotation Properties
[source](source),
[example](example),
[](source)
### source <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/source`
[](example)
### example <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#example`

## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/agrif#`
* **:**
  * `http://linked.data.gov.au/def/agrif#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
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