Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 

# Data Access Rights
### A taxonomy

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/data-access-rights`
* **Publisher(s)**
  * [Geological Survey of Queensland](http://linked.data.gov.au/org/gsq)
* **Creators(s)**
  * [Geological Survey of Queensland](http://linked.data.gov.au/org/gsq)
* **Created**
  * 2019-04-03
* **Modified**
  * 2019-09-10
* **Source**
  * [http://vocabularies.coar-repositories.org/documentation/access_rights/](http://vocabularies.coar-repositories.org/documentation/access_rights/)

* **Taxonomy RDF**
  * RDF ([data-access-rights.ttl](turtle))
### Description
<p>Data access rights control how users and systems access a data resource.</p>

**History Note**  
<p>This vocabulary is taken from the COAR Controlled Vocabularies Interest Group (http://vocabularies.coar-repositories.org/documentation/access_rights/) but is redelivered as that vocabulary isn't well presented online.</p>

## Table of Contents
1. [Collections](#collections)
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Collections
* [Closed data access rights](#Closeddataaccessrights)
* [Open data access rights](#Opendataaccessrights)
### Closed data access rights
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/data-access-rights/closed-access-rights`
Preferred Labels |Closed data access rights (en)<br />
Members |[Metadata only access](Metadataonlyaccess) (cp)<br />[Embargoed access](Embargoedaccess) (cp)<br />[Protected access](Protectedaccess) (cp)<br />[Restricted access](Restrictedaccess) (cp)<br />

### Open data access rights
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/data-access-rights/open-access-rights`
Preferred Labels |Open data access rights (en)<br />
Members |[Open access](Openaccess) (cp)<br />

## Concepts
* [Embargoed access](http://linked.data.gov.au/def/data-access-rights/embargoed)
* [Metadata only access](http://linked.data.gov.au/def/data-access-rights/metadata-only)
* [Open access](http://linked.data.gov.au/def/data-access-rights/open)
* [Protected access](http://linked.data.gov.au/def/data-access-rights/protected)
* [Restricted access](http://linked.data.gov.au/def/data-access-rights/restricted)
	* [Embargoed access](http://linked.data.gov.au/def/data-access-rights/embargoed)
	* [Metadata only access](http://linked.data.gov.au/def/data-access-rights/metadata-only)
	* [Protected access](http://linked.data.gov.au/def/data-access-rights/protected)

### Embargoed access
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/data-access-rights/embargoed`
Preferred Labels |Embargoed access (en)<br />
Definitions |['Embargoed access refers to a resource accessible as metadata only until released for open access on a specified date.']<br />
Broader Concepts |[Restricted access](Restrictedaccess) (cp)<br />
### Metadata only access
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/data-access-rights/metadata-only`
Preferred Labels |Metadata only access (en)<br />
Definitions |['Metadata only access refers to a resource in which access is limited to metadata only. Access to the resource requires granting of access rights.']<br />
Broader Concepts |[Restricted access](Restrictedaccess) (cp)<br />
### Open access
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/data-access-rights/open`
Preferred Labels |Open access (en)<br />
Alternate Labels |Open file<br />
Definitions |['Open access refers to a resource that is immediately and permanently online, and free for all on the Web, without financial and technical barriers.']<br />
### Protected access
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/data-access-rights/protected`
Preferred Labels |Protected access (en)<br />
Definitions |['Protected access refers to a resource that is stored in a system but is not freely accessible due to specific legal or policy decisions, such as active legal proceedings or ministerial discretion. Access is limited to specific personnel or user groups. ']<br />
Broader Concepts |[Restricted access](Restrictedaccess) (cp)<br />
### Restricted access
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/data-access-rights/restricted`
Preferred Labels |Restricted access (en)<br />
Definitions |['Restricted access refers to a resource that is stored in a system but is not freely accessible. Access is limited to specific personnel or user groups.']<br />
Narrower Concepts |[Metadata only access](Metadataonlyaccess) (cp)<br />[Embargoed access](Embargoedaccess) (cp)<br />[Protected access](Protectedaccess) (cp)<br />

## Namespaces
* **da**
  * `http://linked.data.gov.au/def/data-access-rights/`
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
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Collections: cl
* Concepts: cp