# Registry ontology
<sub>metadata by [pyLODE](http://github.com/rdflib/pyLODE)</sub>
## Metadata
* **IRI**
  * `http://purl.org/linked-data/registry`
* **Creators(s)**
  * Dave Reynolds
* **Modified**
  * 2015-04-29
* **Version Information**
  * 0.4
* **Ontology Source**
  * <a href="reg.ttl">RDF (turtle)</a>
### Description
<div id="description">
<p>Core ontology for linked data registry services. Based on ISO19135 but heavily modified to suit Linked Data representations and applications.</p>

## Table of Contents
* [Classes](#classes)
* [Object Properties](#objectproperties)
* [Datatype Properties](#datatypeproperties)
* [Namespaces](#namespaces)  


## Overview
<img style="width:500px; height:500px; background-color: black;" /><br />
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
### Delegated <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#Delegated`
Description | A registerable entity which represents some form of delegation
In domain of |<a href="#delegationtarget">reg:delegationTarget</a><sup class="sup-op" title="object property">op</sup><br />
### Delegated Register <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#DelegatedRegister`
Description | A register whose member contents are determined through delegation to a SPARQL endpoint
Super-classes |<a href="#Delegated">reg:Delegated</a><sup class="sup-c" title="class">c</sup><br /><a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#enumerationobject">reg:enumerationObject</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">max</span> 1<br /><a href="#enumerationsubject">reg:enumerationSubject</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">max</span> 1<br /><a href="#enumerationpredicate">reg:enumerationPredicate</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">max</span> 1<br />
Sub-classes |
In domain of |<a href="#enumerationsubject">reg:enumerationSubject</a><sup class="sup-op" title="object property">op</sup><br /><a href="#enumerationobject">reg:enumerationObject</a><sup class="sup-op" title="object property">op</sup><br /><a href="#enumerationpredicate">reg:enumerationPredicate</a><sup class="sup-op" title="object property">op</sup><br />
### Entity Reference <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#EntityReference`
Description | A reference to some internal or external Linked Data resource. The reg:reference gives the URI of the resource being referenced. If a reg:sourceGraph value is present then it is the URI for a named graph within the Registry containing the properties of the referenced entity. If reg:entityVersion is present it gives URI for the particular version:Version of the entity being referenced. Normally only one of reg:sourceGraph and reg:entityVersion is needed since versioned entities are normally stored in the default graph.
In domain of |<a href="#sourcegraph">reg:sourceGraph</a><sup class="sup-op" title="object property">op</sup><br /><a href="#entityversion">reg:entityVersion</a><sup class="sup-op" title="object property">op</sup><br /><a href="#entity">reg:entity</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="#definition">reg:definition</a><sup class="sup-op" title="object property">op</sup><br /><a href="#alias">reg:alias</a><sup class="sup-op" title="object property">op</sup><br />
### Federated Register <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#FederatedRegister`
Description | A registerable entity which forwards all requests to a remote register. Queries which traverse the register hierarchy such as entity search will also be forwarded
Super-classes |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br /><a href="#Delegated">reg:Delegated</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Namespace Forward <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#NamespaceForward`
Description | A registerable entity which simply forwards all requests to the delegation target.
Super-classes |<a href="#Delegated">reg:Delegated</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#forwardingcode">reg:forwardingCode</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">max</span> 1<br />
Sub-classes |
In domain of |<a href="#forwardingcode">reg:forwardingCode</a><sup class="sup-dp" title="datatype property">dp</sup><br />
### Register <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#Register`
Description | Represents a collection of registered items, together with some associated governance regime. If one or more licenses is stated then each license applies to all the entries in the register. 
Super-classes |<a href="http://www.w3.org/ns/ldp#Container">ldp:Container</a><sup class="sup-c" title="class">c</sup><br /><a href="http://purl.org/linked-data/version#VersionedThing">version:VersionedThing</a><sup class="sup-c" title="class">c</sup><br /><a href="http://rdfs.org/ns/void#Dataset">void:Dataset</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#containeditemclass">reg:containedItemClass</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="http://rdfs.org/ns/void#uriSpace">void:uriSpace</a> <span class="cardinality">max</span> 1<br /><a href="#validationquery">reg:validationQuery</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="#governancepolicy">reg:governancePolicy</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="http://rdfs.org/ns/void#exampleResource">void:exampleResource</a> <span class="cardinality">min</span> 0<br /><a href="http://purl.org/dc/terms/description">dct:description</a> <span class="cardinality">min</span> 1<br /><a href="#manager">reg:manager</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">exactly</span> 1<br /><a href="#owner">reg:owner</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">exactly</span> 1<br /><a href="http://rdfs.org/ns/void#uriLookupEndpoint">void:uriLookupEndpoint</a> <span class="cardinality">min</span> 0<br /><a href="#operatinglanguage">reg:operatingLanguage</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="http://www.w3.org/2000/01/rdf-schema#label">rdfs:label</a> <span class="cardinality">min</span> 1<br /><a href="http://purl.org/dc/terms/modified">dct:modified</a> <span class="cardinality">max</span> 1<br /><a href="http://rdfs.org/ns/void#openSearchDescription">void:openSearchDescription</a> <span class="cardinality">min</span> 0<br /><a href="http://purl.org/dc/terms/license">dct:license</a> <span class="cardinality">min</span> 0<br />
Sub-classes |<a href="#DelegatedRegister">reg:DelegatedRegister</a><sup class="sup-c" title="class">c</sup><br /><a href="#FederatedRegister">reg:FederatedRegister</a><sup class="sup-c" title="class">c</sup><br />
In domain of |<a href="#containeditemclass">reg:containedItemClass</a><sup class="sup-op" title="object property">op</sup><br /><a href="#subregister">reg:subregister</a><sup class="sup-op" title="object property">op</sup><br /><a href="#owner">reg:owner</a><sup class="sup-op" title="object property">op</sup><br /><a href="#operatinglanguage">reg:operatingLanguage</a><sup class="sup-op" title="object property">op</sup><br /><a href="#manager">reg:manager</a><sup class="sup-op" title="object property">op</sup><br /><a href="#release">reg:release</a><sup class="sup-op" title="object property">op</sup><br /><a href="#validationquery">reg:validationQuery</a><sup class="sup-op" title="object property">op</sup><br /><a href="#governancepolicy">reg:governancePolicy</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="#subregister">reg:subregister</a><sup class="sup-op" title="object property">op</sup><br /><a href="#register">reg:register</a><sup class="sup-op" title="object property">op</sup><br />
### RegisterItem <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#RegisterItem`
Description | A metadata record for an entry in a register. Note that cardinality constraints can be met by sub-properties, for example an item with a skos:prefLabel implies an rdfs:label and so meets the cardinality constraint on rdfs:label.
Super-classes |<a href="http://purl.org/linked-data/version#VersionedThing">version:VersionedThing</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="http://purl.org/linked-data/registry#hasView">reg:hasView</a> <span class="cardinality">min</span> 0<br /><a href="#submitter">reg:submitter</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">exactly</span> 1<br /><a href="#representationof">reg:representationOf</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="http://purl.org/dc/terms/license">dct:license</a> <span class="cardinality">min</span> 0<br /><a href="#itemclass">reg:itemClass</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 1<br /><a href="http://purl.org/dc/terms/modified">dct:modified</a> <span class="cardinality">max</span> 1<br /><a href="#category">reg:category</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="#definition">reg:definition</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">exactly</span> 1<br /><a href="http://purl.org/dc/terms/dateSubmitted">dct:dateSubmitted</a> <span class="cardinality">exactly</span> 1<br /><a href="#alias">reg:alias</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="#notation">reg:notation</a><sup class="sup-dp" title="datatype property">dp</sup> <span class="cardinality">max</span> 1<br /><a href="http://purl.org/dc/terms/dateAccepted">dct:dateAccepted</a> <span class="cardinality">max</span> 1<br /><a href="#predecessor">reg:predecessor</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0<br /><a href="http://www.w3.org/2000/01/rdf-schema#label">rdfs:label</a> <span class="cardinality">min</span> 1<br /><a href="#status">reg:status</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 1<br /><a href="http://purl.org/dc/terms/description">dct:description</a> <span class="cardinality">min</span> 0<br />
Sub-classes |
In domain of |<a href="#predecessor">reg:predecessor</a><sup class="sup-op" title="object property">op</sup><br /><a href="#register">reg:register</a><sup class="sup-op" title="object property">op</sup><br /><a href="#annotation">reg:annotation</a><sup class="sup-op" title="object property">op</sup><br /><a href="#notation">reg:notation</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="#definition">reg:definition</a><sup class="sup-op" title="object property">op</sup><br /><a href="#category">reg:category</a><sup class="sup-op" title="object property">op</sup><br /><a href="#status">reg:status</a><sup class="sup-op" title="object property">op</sup><br /><a href="#itemclass">reg:itemClass</a><sup class="sup-op" title="object property">op</sup><br /><a href="#alias">reg:alias</a><sup class="sup-op" title="object property">op</sup><br /><a href="#representationof">reg:representationOf</a><sup class="sup-op" title="object property">op</sup><br /><a href="#submitter">reg:submitter</a><sup class="sup-op" title="object property">op</sup><br /><a href="#successor">reg:successor</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="#successor">reg:successor</a><sup class="sup-op" title="object property">op</sup><br /><a href="#predecessor">reg:predecessor</a><sup class="sup-op" title="object property">op</sup><br />
### SPARQL ASK query <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#SPARQLAskQuery`
Description | Represents a SPARQL ASK query as might be used for validation.
In range of |<a href="#validationquery">reg:validationQuery</a><sup class="sup-op" title="object property">op</sup><br />
### SPARQL CONSTRUCT query <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#SPARQLConstructQuery`
Description | Represents a SPARQL CONSTRUCT query.
### SPARQL query <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#SPARQLQuery`
Description | Represents a SPARQL query as a reusable resource.
### SPARQL SELECT query <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#SPARQLSelectQuery`
Description | Represents a SPARQL SELECT query.
### Status <sup>c</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#Status`
Description | Open set of status code for entries in a register
Super-classes |<a href="http://www.w3.org/2004/02/skos/core#Concept">skos:Concept</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
In domain of |<a href="#nextstate">reg:nextState</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="#priorState">reg:priorState</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="#presentation">reg:presentation</a><sup class="sup-dp" title="datatype property">dp</sup><br />
In range of |<a href="#status">reg:status</a><sup class="sup-op" title="object property">op</sup><br />

## Object Properties
[alias](alias),
[annotation](annotation),
[category](category),
[contained item class](containeditemclass),
[definition](definition),
[delegation target](delegationtarget),
[entity](entity),
[entity version](entityversion),
[enumeration object](enumerationobject),
[enumeration predicate](enumerationpredicate),
[enumeration subject](enumerationsubject),
[governance policy](governancepolicy),
[inverse membership predicate](inversemembershippredicate),
[item class](itemclass),
[manager](manager),
[operating language](operatinglanguage),
[owner](owner),
[predecessor](predecessor),
[register](register),
[release](release),
[representation of](representationof),
[source dataset](sourcedataset),
[source graph](sourcegraph),
[status](status),
[submitter](submitter),
[subregister](subregister),
[successor](successor),
[validation query](validationquery),
[](alias)
### alias <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#alias`
Description | An alternative URI for the entity, the alias resource is regarded by this register as owl:sameAs the definition entity
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#EntityReference">reg:EntityReference</a><sup class="sup-c" title="class">c</sup><br />
[](annotation)
### annotation <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#annotation`
Description | The URI of a graph of annotation statements associate with this item
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
[](category)
### category <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#category`
Description | Optional classification for a registered item within one or more SKOS classification schemes to support navigation and discovery. Orthogonal to the structure provided by the register hierarchy which is about governance.
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2004/02/skos/core#Concept">skos:Concept</a><sup class="sup-c" title="class">c</sup><br />
[](containeditemclass)
### contained item class <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#containedItemClass`
Description | A class of entities that can occur in this register
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Class">owl:Class</a><sup class="sup-c" title="class">c</sup><br />
[](definition)
### definition <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#definition`
Description | The entity which has been registered.
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#EntityReference">reg:EntityReference</a><sup class="sup-c" title="class">c</sup><br />
[](delegationtarget)
### delegation target <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#delegationTarget`
Description | A resource to which the delegated register delegates, may be a register in another registry service, a SPARQL endpoint or some other web resource
Domain(s) |<a href="#Delegated">reg:Delegated</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](entity)
### entity <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#entity`
Description | The RDF resource identified by an entity reference
Domain(s) |<a href="#EntityReference">reg:EntityReference</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](entityversion)
### entity version <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#entityVersion`
Description | Indicates the particular version:Version of the entity being referenced.
Domain(s) |<a href="#EntityReference">reg:EntityReference</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](enumerationobject)
### enumeration object <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#enumerationObject`
Description | Specifies the object part of a triple pattern used to enumerate the members of a delegated register
Domain(s) |<a href="#DelegatedRegister">reg:DelegatedRegister</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](enumerationpredicate)
### enumeration predicate <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#enumerationPredicate`
Description | Specifies the predicate part of a triple pattern used to enumerate the members of a delegated register
Domain(s) |<a href="#DelegatedRegister">reg:DelegatedRegister</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](enumerationsubject)
### enumeration subject <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#enumerationSubject`
Description | Specifies the subject part of a triple pattern used to enumerate the members of a delegated register
Domain(s) |<a href="#DelegatedRegister">reg:DelegatedRegister</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](governancepolicy)
### governance policy <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#governancePolicy`
Description | A resource, such as a web accessible-document, which describes the governance policy applicable to this register.
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](inversemembershippredicate)
### inverse membership predicate <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#inverseMembershipPredicate`
Description | Indicates a property which links a member of a collection back to the collection itself, this is the reverse direction to the normal ldp:membershipPredicate
Domain(s) |<a href="http://www.w3.org/ns/ldp#Container">ldp:Container</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property">rdf:Property</a><sup class="sup-c" title="class">c</sup><br />
[](itemclass)
### item class <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#itemClass`
Description | The type of the entity that this record is about. Note that it may be possible to register a non-RDF resource in which case this property provides a way to state the intended class of the entity even though no direct RDF assertion of type is available.
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Class">rdfs:Class</a><sup class="sup-c" title="class">c</sup><br />
[](manager)
### manager <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#manager`
Description | The manager of the register, may be a person (foaf:Person) or an organization (org:Organization). Operates the register on behalf of the owner, makes day to day decisions on acceptance of entries based on agreed principles but it may be possible to appeal to the owner to override a decision by the manager.
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](operatinglanguage)
### operating language <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#operatingLanguage`
Description | Indicates a language supported by the register and the items within it. The language should be indicated by a resource within a well-maintained URI set such as the Library of Congress language URIs e.g. http://id.loc.gov/vocabulary/iso639-1/en
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](owner)
### owner <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#owner`
Description | The owner of the register, may be a person (foaf:Person) or an organization (org:Organization). The owner has final authority over the contents of the regster.
Super-properties |<a href="http://purl.org/dc/terms/publisher">dct:publisher</a><br />
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](predecessor)
### predecessor <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#predecessor`
Description | An item which has been replaced this one within the register. Should be asserted between hub resources (VersionedThing).
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
[](register)
### register <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#register`
Description | The register in which this item has been registered.
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
[](release)
### release <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#release`
Description | A tagged snapshot of a register
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/ns/prov#Collection">prov:Collection</a><sup class="sup-c" title="class">c</sup><br />
[](representationof)
### representation of <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#representationOf`
Description | A resource, typically a real-world object, which the registered entity is a representation for.
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
[](sourcedataset)
### source dataset <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#sourceDataset`
Description | Gives the source dataset in a Linkset, the other link target is assumed to be the destination
Domain(s) |<a href="http://rdfs.org/ns/void#Linkset">void:Linkset</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://rdfs.org/ns/void#Dataset">void:Dataset</a><sup class="sup-c" title="class">c</sup><br />
[](sourcegraph)
### source graph <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#sourceGraph`
Description | A resource representing an RDF graph (within the Registry's SPARQL dataset) containing the properties of the reference entity. If not present then assume default graph.
Domain(s) |<a href="#EntityReference">reg:EntityReference</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/ns/sparql-service-description#Graph">ssd:Graph</a><sup class="sup-c" title="class">c</sup><br />
[](status)
### status <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#status`
Description | The status of this register entry
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#Status">reg:Status</a><sup class="sup-c" title="class">c</sup><br />
[](submitter)
### submitter <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#submitter`
Description | The person or organization who originally submitted this register entry. Subsequent chages to the entry may have been made by other agents.
Super-properties |<a href="http://purl.org/dc/terms/publisher">dct:publisher</a><br />
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](subregister)
### subregister <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#subregister`
Description | Indicates a register that is itself an entry in this principle register.
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
[](successor)
### successor <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#successor`
Description | Indicates the replacement for a superseded item.
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
[](validationquery)
### validation query <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#validationQuery`
Description | A SPARQL ASK query which can be used to validate a proposed entry in this register. Returns true of an error is found.
Domain(s) |<a href="#Register">reg:Register</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#SPARQLASKquery">reg:SPARQLAskQuery</a><sup class="sup-c" title="class">c</sup><br />

## Datatype Properties
[forwarding code](forwardingcode),
[next state](nextstate),
[notation](notation),
[presentation](presentation),
[next state](priorState),
[query](query),
[tag](tag),
[](forwardingcode)
### forwarding code <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#forwardingCode`
Description | The HTTP status code to return the requester in order to forward the request.
Domain(s) |<a href="#NamespaceForward">reg:NamespaceForward</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#int">xsd:int</a><sup class="sup-c" title="class">c</sup><br />
[](nextstate)
### next state <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#nextState`
Description | Gives the label of a state which can follow from this state
Domain(s) |<a href="#Status">reg:Status</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](notation)
### notation <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#notation`
Description | A short text string which can be used to denote the register item. Must be unique within the register. If available it should be used as the path segment, relative to the parent register, for the RegisterItem (and for the item itself, if managed). Restricted to be a syntactically legal URI segment (i.e. *pchar).
Domain(s) |<a href="#RegisterItem">reg:RegisterItem</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](presentation)
### presentation <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#presentation`
Description | Presentational hint for showing items with this status
Domain(s) |<a href="#Status">reg:Status</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](priorState)
### next state <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#priorState`
Description | Gives the label of a state which can precede this state
Domain(s) |<a href="#Status">reg:Status</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](query)
### query <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#query`
Description | The source of a SPARQL query
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](tag)
### tag <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://purl.org/linked-data/registry#tag`
Description | The tag used to label a collection which snapshots the state of a register
Domain(s) |<a href="http://www.w3.org/ns/prov#Collection">prov:Collection</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />

## Namespaces
* **default (:)**
  * `http://purl.org/linked-data/registry#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
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
* **reg**
  * `http://purl.org/linked-data/registry#`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **ssd**
  * `http://www.w3.org/ns/sparql-service-description#`
* **version**
  * `http://purl.org/linked-data/version#`
* **void**
  * `http://rdfs.org/ns/void#`
* **vs**
  * `http://www.w3.org/2003/06/sw-vocab-status/ns#`
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