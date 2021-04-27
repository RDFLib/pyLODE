Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Registry ontology

## Metadata
* **URI**
  * `http://purl.org/linked-data/registry`
* **Creators(s)**
  * Dave Reynolds
* **Modified**
  * 2015-04-29
* **Version Information**
  * 0.4
* **Ontology RDF**
  * RDF ([reg.ttl](turtle))
### Description
<p>Core ontology for linked data registry services. Based on ISO19135 but heavily modified to suit Linked Data representations and applications.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Delegated](#Delegated),
[Delegated Register](#DelegatedRegister),
[Entity Reference](#EntityReference),
[Federated Register](#FederatedRegister),
[Namespace Forward](#NamespaceForward),
[Register](#Register),
[RegisterItem](#RegisterItem),
[SPARQL ASK query](#SPARQLASKquery),
[SPARQL CONSTRUCT query](#SPARQLCONSTRUCTquery),
[SPARQL SELECT query](#SPARQLSELECTquery),
[SPARQL query](#SPARQLquery),
[Status](#Status),
### Delegated
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#Delegated`
Description | <p>A registerable entity which represents some form of delegation</p>
Restrictions |[http://purl.org/linked-data/registry#delegationTarget](http://purl.org/linked-data/registry#delegationTarget) (op) **exactly** 1<br />
Sub-classes |[http://purl.org/linked-data/registry#FederatedRegister](http://purl.org/linked-data/registry#FederatedRegister) (c)<br />[http://purl.org/linked-data/registry#DelegatedRegister](http://purl.org/linked-data/registry#DelegatedRegister) (c)<br />[http://purl.org/linked-data/registry#NamespaceForward](http://purl.org/linked-data/registry#NamespaceForward) (c)<br />
In domain of |[http://purl.org/linked-data/registry#delegationTarget](http://purl.org/linked-data/registry#delegationTarget) (op)<br />
### Delegated Register
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#DelegatedRegister`
Description | <p>A register whose member contents are determined through delegation to a SPARQL endpoint</p>
Super-classes |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />[http://purl.org/linked-data/registry#Delegated](http://purl.org/linked-data/registry#Delegated) (c)<br />
Restrictions |[http://purl.org/linked-data/registry#enumerationPredicate](http://purl.org/linked-data/registry#enumerationPredicate) (op) **max** 1<br />[http://purl.org/linked-data/registry#enumerationObject](http://purl.org/linked-data/registry#enumerationObject) (op) **max** 1<br />[http://purl.org/linked-data/registry#enumerationSubject](http://purl.org/linked-data/registry#enumerationSubject) (op) **max** 1<br />
In domain of |[http://purl.org/linked-data/registry#enumerationSubject](http://purl.org/linked-data/registry#enumerationSubject) (op)<br />[http://purl.org/linked-data/registry#enumerationPredicate](http://purl.org/linked-data/registry#enumerationPredicate) (op)<br />[http://purl.org/linked-data/registry#enumerationObject](http://purl.org/linked-data/registry#enumerationObject) (op)<br />
### Entity Reference
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#EntityReference`
Description | <p>A reference to some internal or external Linked Data resource. The reg:reference gives the URI of the resource being referenced. If a reg:sourceGraph value is present then it is the URI for a named graph within the Registry containing the properties of the referenced entity. If reg:entityVersion is present it gives URI for the particular version:Version of the entity being referenced. Normally only one of reg:sourceGraph and reg:entityVersion is needed since versioned entities are normally stored in the default graph.</p>
Restrictions |[http://purl.org/linked-data/registry#entityVersion](http://purl.org/linked-data/registry#entityVersion) (op) **max** 1<br />[http://purl.org/linked-data/registry#sourceGraph](http://purl.org/linked-data/registry#sourceGraph) (op) **max** 1<br />[http://purl.org/linked-data/registry#entity](http://purl.org/linked-data/registry#entity) (op) **exactly** 1<br />
In domain of |[http://purl.org/linked-data/registry#entityVersion](http://purl.org/linked-data/registry#entityVersion) (op)<br />[http://purl.org/linked-data/registry#entity](http://purl.org/linked-data/registry#entity) (op)<br />[http://purl.org/linked-data/registry#sourceGraph](http://purl.org/linked-data/registry#sourceGraph) (op)<br />
In range of |[http://purl.org/linked-data/registry#alias](http://purl.org/linked-data/registry#alias) (op)<br />[http://purl.org/linked-data/registry#definition](http://purl.org/linked-data/registry#definition) (op)<br />
### Federated Register
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#FederatedRegister`
Description | <p>A registerable entity which forwards all requests to a remote register. Queries which traverse the register hierarchy such as entity search will also be forwarded</p>
Super-classes |[http://purl.org/linked-data/registry#Delegated](http://purl.org/linked-data/registry#Delegated) (c)<br />[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
### Namespace Forward
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#NamespaceForward`
Description | <p>A registerable entity which simply forwards all requests to the delegation target.</p>
Super-classes |[http://purl.org/linked-data/registry#Delegated](http://purl.org/linked-data/registry#Delegated) (c)<br />
Restrictions |[http://purl.org/linked-data/registry#forwardingCode](http://purl.org/linked-data/registry#forwardingCode) (dp) **max** 1<br />
In domain of |[http://purl.org/linked-data/registry#forwardingCode](http://purl.org/linked-data/registry#forwardingCode) (dp)<br />
### Register
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#Register`
Description | <p>Represents a collection of registered items, together with some associated governance regime. If one or more licenses is stated then each license applies to all the entries in the register. </p>
Super-classes |[void:Dataset](http://rdfs.org/ns/void#Dataset) (c)<br />[ldp:Container](http://www.w3.org/ns/ldp#Container) (c)<br />[http://purl.org/linked-data/version#VersionedThing](http://purl.org/linked-data/version#VersionedThing) (c)<br />
Restrictions |[dct:modified](http://purl.org/dc/terms/modified) **max** 1<br />[void:uriLookupEndpoint](http://rdfs.org/ns/void#uriLookupEndpoint) **min** 0<br />[http://purl.org/linked-data/registry#manager](http://purl.org/linked-data/registry#manager) (op) **exactly** 1<br />[http://purl.org/linked-data/registry#owner](http://purl.org/linked-data/registry#owner) (op) **exactly** 1<br />[http://purl.org/linked-data/registry#containedItemClass](http://purl.org/linked-data/registry#containedItemClass) (op) **min** 0<br />[void:exampleResource](http://rdfs.org/ns/void#exampleResource) **min** 0<br />[dct:description](http://purl.org/dc/terms/description) **min** 1<br />[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) **min** 1<br />[http://purl.org/linked-data/registry#operatingLanguage](http://purl.org/linked-data/registry#operatingLanguage) (op) **min** 0<br />[void:openSearchDescription](http://rdfs.org/ns/void#openSearchDescription) **min** 0<br />[void:uriSpace](http://rdfs.org/ns/void#uriSpace) **max** 1<br />[http://purl.org/linked-data/registry#governancePolicy](http://purl.org/linked-data/registry#governancePolicy) (op) **min** 0<br />[http://purl.org/linked-data/registry#validationQuery](http://purl.org/linked-data/registry#validationQuery) (op) **min** 0<br />[dct:license](http://purl.org/dc/terms/license) **min** 0<br />
Sub-classes |[http://purl.org/linked-data/registry#DelegatedRegister](http://purl.org/linked-data/registry#DelegatedRegister) (c)<br />[http://purl.org/linked-data/registry#FederatedRegister](http://purl.org/linked-data/registry#FederatedRegister) (c)<br />
In domain of |[http://purl.org/linked-data/registry#owner](http://purl.org/linked-data/registry#owner) (op)<br />[http://purl.org/linked-data/registry#subregister](http://purl.org/linked-data/registry#subregister) (op)<br />[http://purl.org/linked-data/registry#containedItemClass](http://purl.org/linked-data/registry#containedItemClass) (op)<br />[http://purl.org/linked-data/registry#governancePolicy](http://purl.org/linked-data/registry#governancePolicy) (op)<br />[http://purl.org/linked-data/registry#release](http://purl.org/linked-data/registry#release) (op)<br />[http://purl.org/linked-data/registry#manager](http://purl.org/linked-data/registry#manager) (op)<br />[http://purl.org/linked-data/registry#operatingLanguage](http://purl.org/linked-data/registry#operatingLanguage) (op)<br />[http://purl.org/linked-data/registry#validationQuery](http://purl.org/linked-data/registry#validationQuery) (op)<br />
In range of |[http://purl.org/linked-data/registry#subregister](http://purl.org/linked-data/registry#subregister) (op)<br />[http://purl.org/linked-data/registry#register](http://purl.org/linked-data/registry#register) (op)<br />
### RegisterItem
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#RegisterItem`
Description | <p>A metadata record for an entry in a register. Note that cardinality constraints can be met by sub-properties, for example an item with a skos:prefLabel implies an rdfs:label and so meets the cardinality constraint on rdfs:label.</p>
Super-classes |[http://purl.org/linked-data/version#VersionedThing](http://purl.org/linked-data/version#VersionedThing) (c)<br />
Restrictions |[dct:modified](http://purl.org/dc/terms/modified) **max** 1<br />[http://purl.org/linked-data/registry#category](http://purl.org/linked-data/registry#category) (op) **min** 0<br />[dct:license](http://purl.org/dc/terms/license) **min** 0<br />[http://purl.org/linked-data/registry#predecessor](http://purl.org/linked-data/registry#predecessor) (op) **min** 0<br />[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) **min** 1<br />[dct:dateSubmitted](http://purl.org/dc/terms/dateSubmitted) **exactly** 1<br />[http://purl.org/linked-data/registry#representationOf](http://purl.org/linked-data/registry#representationOf) (op) **min** 0<br />[http://purl.org/linked-data/registry#hasView](http://purl.org/linked-data/registry#hasView) **min** 0<br />[http://purl.org/linked-data/registry#itemClass](http://purl.org/linked-data/registry#itemClass) (op) **min** 1<br />[http://purl.org/linked-data/registry#submitter](http://purl.org/linked-data/registry#submitter) (op) **exactly** 1<br />[http://purl.org/linked-data/registry#definition](http://purl.org/linked-data/registry#definition) (op) **exactly** 1<br />[http://purl.org/linked-data/registry#notation](http://purl.org/linked-data/registry#notation) (dp) **max** 1<br />[http://purl.org/linked-data/registry#alias](http://purl.org/linked-data/registry#alias) (op) **min** 0<br />[http://purl.org/linked-data/registry#status](http://purl.org/linked-data/registry#status) (op) **min** 1<br />[dct:description](http://purl.org/dc/terms/description) **min** 0<br />[dct:dateAccepted](http://purl.org/dc/terms/dateAccepted) **max** 1<br />
In domain of |[http://purl.org/linked-data/registry#itemClass](http://purl.org/linked-data/registry#itemClass) (op)<br />[http://purl.org/linked-data/registry#status](http://purl.org/linked-data/registry#status) (op)<br />[http://purl.org/linked-data/registry#successor](http://purl.org/linked-data/registry#successor) (op)<br />[http://purl.org/linked-data/registry#submitter](http://purl.org/linked-data/registry#submitter) (op)<br />[http://purl.org/linked-data/registry#notation](http://purl.org/linked-data/registry#notation) (dp)<br />[http://purl.org/linked-data/registry#definition](http://purl.org/linked-data/registry#definition) (op)<br />[http://purl.org/linked-data/registry#annotation](http://purl.org/linked-data/registry#annotation) (op)<br />[http://purl.org/linked-data/registry#representationOf](http://purl.org/linked-data/registry#representationOf) (op)<br />[http://purl.org/linked-data/registry#predecessor](http://purl.org/linked-data/registry#predecessor) (op)<br />[http://purl.org/linked-data/registry#category](http://purl.org/linked-data/registry#category) (op)<br />[http://purl.org/linked-data/registry#alias](http://purl.org/linked-data/registry#alias) (op)<br />[http://purl.org/linked-data/registry#register](http://purl.org/linked-data/registry#register) (op)<br />
In range of |[http://purl.org/linked-data/registry#successor](http://purl.org/linked-data/registry#successor) (op)<br />[http://purl.org/linked-data/registry#predecessor](http://purl.org/linked-data/registry#predecessor) (op)<br />
### SPARQL ASK query
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#SPARQLAskQuery`
Description | <p>Represents a SPARQL ASK query as might be used for validation.</p>
In range of |[http://purl.org/linked-data/registry#validationQuery](http://purl.org/linked-data/registry#validationQuery) (op)<br />
### SPARQL CONSTRUCT query
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#SPARQLConstructQuery`
Description | <p>Represents a SPARQL CONSTRUCT query.</p>
### SPARQL query
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#SPARQLQuery`
Description | <p>Represents a SPARQL query as a reusable resource.</p>
Restrictions |[http://purl.org/linked-data/registry#query](http://purl.org/linked-data/registry#query) (dp) **exactly** 1<br />
### SPARQL SELECT query
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#SPARQLSelectQuery`
Description | <p>Represents a SPARQL SELECT query.</p>
### Status
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#Status`
Description | <p>Open set of status code for entries in a register</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In domain of |[http://purl.org/linked-data/registry#presentation](http://purl.org/linked-data/registry#presentation) (dp)<br />[http://purl.org/linked-data/registry#nextState](http://purl.org/linked-data/registry#nextState) (dp)<br />[http://purl.org/linked-data/registry#priorState](http://purl.org/linked-data/registry#priorState) (dp)<br />
In range of |[http://purl.org/linked-data/registry#status](http://purl.org/linked-data/registry#status) (op)<br />
Has members |[http://purl.org/linked-data/registry#statusRetired](http://purl.org/linked-data/registry#statusRetired)<br />[http://purl.org/linked-data/registry#statusAccepted](http://purl.org/linked-data/registry#statusAccepted)<br />[http://purl.org/linked-data/registry#statusExperimental](http://purl.org/linked-data/registry#statusExperimental)<br />[http://purl.org/linked-data/registry#statusStable](http://purl.org/linked-data/registry#statusStable)<br />[http://purl.org/linked-data/registry#statusNotAccepted](http://purl.org/linked-data/registry#statusNotAccepted)<br />[http://purl.org/linked-data/registry#statusSubmitted](http://purl.org/linked-data/registry#statusSubmitted)<br />[http://purl.org/linked-data/registry#statusInvalid](http://purl.org/linked-data/registry#statusInvalid)<br />[http://purl.org/linked-data/registry#statusReserved](http://purl.org/linked-data/registry#statusReserved)<br />[http://purl.org/linked-data/registry#statusDeprecated](http://purl.org/linked-data/registry#statusDeprecated)<br />[http://purl.org/linked-data/registry#statusValid](http://purl.org/linked-data/registry#statusValid)<br />[http://purl.org/linked-data/registry#statusSuperseded](http://purl.org/linked-data/registry#statusSuperseded)<br />

## Object Properties
[alias](#alias),
[annotation](#annotation),
[category](#category),
[contained item class](#containeditemclass),
[definition](#definition),
[delegation target](#delegationtarget),
[entity](#entity),
[entity version](#entityversion),
[enumeration object](#enumerationobject),
[enumeration predicate](#enumerationpredicate),
[enumeration subject](#enumerationsubject),
[governance policy](#governancepolicy),
[inverse membership predicate](#inversemembershippredicate),
[item class](#itemclass),
[manager](#manager),
[operating language](#operatinglanguage),
[owner](#owner),
[predecessor](#predecessor),
[register](#register),
[release](#release),
[representation of](#representationof),
[source dataset](#sourcedataset),
[source graph](#sourcegraph),
[status](#status),
[submitter](#submitter),
[subregister](#subregister),
[successor](#successor),
[validation query](#validationquery),
[](alias)
### alias
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#alias`
Description | An alternative URI for the entity, the alias resource is regarded by this register as owl:sameAs the definition entity
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#EntityReference](http://purl.org/linked-data/registry#EntityReference) (c)<br />
[](annotation)
### annotation
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#annotation`
Description | The URI of a graph of annotation statements associate with this item
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
[](category)
### category
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#category`
Description | Optional classification for a registered item within one or more SKOS classification schemes to support navigation and discovery. Orthogonal to the structure provided by the register hierarchy which is about governance.
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](containeditemclass)
### contained item class
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#containedItemClass`
Description | A class of entities that can occur in this register
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[owl:Class](http://www.w3.org/2002/07/owl#Class) (c)<br />
[](definition)
### definition
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#definition`
Description | The entity which has been registered.
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#EntityReference](http://purl.org/linked-data/registry#EntityReference) (c)<br />
[](delegationtarget)
### delegation target
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#delegationTarget`
Description | A resource to which the delegated register delegates, may be a register in another registry service, a SPARQL endpoint or some other web resource
Domain(s) |[http://purl.org/linked-data/registry#Delegated](http://purl.org/linked-data/registry#Delegated) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](entity)
### entity
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#entity`
Description | The RDF resource identified by an entity reference
Domain(s) |[http://purl.org/linked-data/registry#EntityReference](http://purl.org/linked-data/registry#EntityReference) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](entityversion)
### entity version
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#entityVersion`
Description | Indicates the particular version:Version of the entity being referenced.
Domain(s) |[http://purl.org/linked-data/registry#EntityReference](http://purl.org/linked-data/registry#EntityReference) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](enumerationobject)
### enumeration object
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#enumerationObject`
Description | Specifies the object part of a triple pattern used to enumerate the members of a delegated register
Domain(s) |[http://purl.org/linked-data/registry#DelegatedRegister](http://purl.org/linked-data/registry#DelegatedRegister) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](enumerationpredicate)
### enumeration predicate
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#enumerationPredicate`
Description | Specifies the predicate part of a triple pattern used to enumerate the members of a delegated register
Domain(s) |[http://purl.org/linked-data/registry#DelegatedRegister](http://purl.org/linked-data/registry#DelegatedRegister) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](enumerationsubject)
### enumeration subject
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#enumerationSubject`
Description | Specifies the subject part of a triple pattern used to enumerate the members of a delegated register
Domain(s) |[http://purl.org/linked-data/registry#DelegatedRegister](http://purl.org/linked-data/registry#DelegatedRegister) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](governancepolicy)
### governance policy
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#governancePolicy`
Description | A resource, such as a web accessible-document, which describes the governance policy applicable to this register.
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](inversemembershippredicate)
### inverse membership predicate
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#inverseMembershipPredicate`
Description | Indicates a property which links a member of a collection back to the collection itself, this is the reverse direction to the normal ldp:membershipPredicate
Domain(s) |[ldp:Container](http://www.w3.org/ns/ldp#Container) (c)<br />
Range(s) |[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) (c)<br />
[](itemclass)
### item class
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#itemClass`
Description | The type of the entity that this record is about. Note that it may be possible to register a non-RDF resource in which case this property provides a way to state the intended class of the entity even though no direct RDF assertion of type is available.
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) (c)<br />
[](manager)
### manager
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#manager`
Description | The manager of the register, may be a person (foaf:Person) or an organization (org:Organization). Operates the register on behalf of the owner, makes day to day decisions on acceptance of entries based on agreed principles but it may be possible to appeal to the owner to override a decision by the manager.
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
[](operatinglanguage)
### operating language
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#operatingLanguage`
Description | Indicates a language supported by the register and the items within it. The language should be indicated by a resource within a well-maintained URI set such as the Library of Congress language URIs e.g. http://id.loc.gov/vocabulary/iso639-1/en
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](owner)
### owner
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#owner`
Description | The owner of the register, may be a person (foaf:Person) or an organization (org:Organization). The owner has final authority over the contents of the regster.
Super-properties |[dct:publisher](http://purl.org/dc/terms/publisher)<br />
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
[](predecessor)
### predecessor
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#predecessor`
Description | An item which has been replaced this one within the register. Should be asserted between hub resources (VersionedThing).
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
[](register)
### register
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#register`
Description | The register in which this item has been registered.
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
[](release)
### release
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#release`
Description | A tagged snapshot of a register
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[prov:Collection](http://www.w3.org/ns/prov#Collection) (c)<br />
[](representationof)
### representation of
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#representationOf`
Description | A resource, typically a real-world object, which the registered entity is a representation for.
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
[](sourcedataset)
### source dataset
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#sourceDataset`
Description | Gives the source dataset in a Linkset, the other link target is assumed to be the destination
Domain(s) |[void:Linkset](http://rdfs.org/ns/void#Linkset) (c)<br />
Range(s) |[void:Dataset](http://rdfs.org/ns/void#Dataset) (c)<br />
[](sourcegraph)
### source graph
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#sourceGraph`
Description | A resource representing an RDF graph (within the Registry's SPARQL dataset) containing the properties of the reference entity. If not present then assume default graph.
Domain(s) |[http://purl.org/linked-data/registry#EntityReference](http://purl.org/linked-data/registry#EntityReference) (c)<br />
Range(s) |[sd:Graph](http://www.w3.org/ns/sparql-service-description#Graph) (c)<br />
[](status)
### status
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#status`
Description | The status of this register entry
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#Status](http://purl.org/linked-data/registry#Status) (c)<br />
[](submitter)
### submitter
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#submitter`
Description | The person or organization who originally submitted this register entry. Subsequent chages to the entry may have been made by other agents.
Super-properties |[dct:publisher](http://purl.org/dc/terms/publisher)<br />
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
[](subregister)
### subregister
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#subregister`
Description | Indicates a register that is itself an entry in this principle register.
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
[](successor)
### successor
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#successor`
Description | Indicates the replacement for a superseded item.
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
[](validationquery)
### validation query
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#validationQuery`
Description | A SPARQL ASK query which can be used to validate a proposed entry in this register. Returns true of an error is found.
Domain(s) |[http://purl.org/linked-data/registry#Register](http://purl.org/linked-data/registry#Register) (c)<br />
Range(s) |[http://purl.org/linked-data/registry#SPARQLAskQuery](http://purl.org/linked-data/registry#SPARQLAskQuery) (c)<br />

## Datatype Properties
[forwarding code](#forwardingcode),
[next state](#nextstate),
[notation](#notation),
[presentation](#presentation),
[next state](#priorState),
[query](#query),
[tag](#tag),
[](forwardingcode)
### forwarding code
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#forwardingCode`
Description | The HTTP status code to return the requester in order to forward the request.
Domain(s) |[http://purl.org/linked-data/registry#NamespaceForward](http://purl.org/linked-data/registry#NamespaceForward) (c)<br />
Range(s) |[xsd:int](http://www.w3.org/2001/XMLSchema#int) (c)<br />
[](nextstate)
### next state
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#nextState`
Description | Gives the label of a state which can follow from this state
Domain(s) |[http://purl.org/linked-data/registry#Status](http://purl.org/linked-data/registry#Status) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](notation)
### notation
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#notation`
Description | A short text string which can be used to denote the register item. Must be unique within the register. If available it should be used as the path segment, relative to the parent register, for the RegisterItem (and for the item itself, if managed). Restricted to be a syntactically legal URI segment (i.e. *pchar).
Domain(s) |[http://purl.org/linked-data/registry#RegisterItem](http://purl.org/linked-data/registry#RegisterItem) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](presentation)
### presentation
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#presentation`
Description | Presentational hint for showing items with this status
Domain(s) |[http://purl.org/linked-data/registry#Status](http://purl.org/linked-data/registry#Status) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](priorState)
### next state
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#priorState`
Description | Gives the label of a state which can precede this state
Domain(s) |[http://purl.org/linked-data/registry#Status](http://purl.org/linked-data/registry#Status) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](query)
### query
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#query`
Description | The source of a SPARQL query
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](tag)
### tag
Property | Value
--- | ---
URI | `http://purl.org/linked-data/registry#tag`
Description | The tag used to label a collection which snapshots the state of a register
Domain(s) |[prov:Collection](http://www.w3.org/ns/prov#Collection) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />

## Named Individuals
## Namespaces
* **dct**
  * `http://purl.org/dc/terms/`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
* **ldp**
  * `http://www.w3.org/ns/ldp#`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sd**
  * `http://www.w3.org/ns/sparql-service-description#`
* **sdo**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **void**
  * `http://rdfs.org/ns/void#`
* **vs**
  * `http://www.w3.org/2003/06/sw-vocab-status/ns#`
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