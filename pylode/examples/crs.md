Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Commonwealth Record Series Ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/crs`
* **Publisher(s)**
  * [National Archives of Australia](http://catalogue.linked.data.gov.au/org/naa)
* **Creators(s)**
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[ORCID]](http://orcid.org/0000-0002-8742-7730)
    (<nicholas.car@csiro.au></a>) of [CSIRO](http://catalogue.linked.data.gov.au/org/csiro)
* **Contributor(s)**
  * David Hearder
  * Marco Wallenius
  * [Simon J.D. Cox](https://orcid.org/0000-0002-3884-3420)
    [[ORCID]](https://orcid.org/0000-0002-3884-3420)
    (<simon.cox@csiro.au></a>) of [CSIRO](http://catalogue.linked.data.gov.au/org/csiro)
* **Created**
  * 2018-09-10
* **Modified**
  * 2019-05-31
* **Version Information**
  * Beta version
* **Version URI**
  * [http://linked.data.gov.au/def/crs#](http://linked.data.gov.au/def/crs#)
* **Imports**
  * [http://purl.org/dc/elements/1.1/](http://purl.org/dc/elements/1.1/)
  * [http://www.w3.org/2006/time](http://www.w3.org/2006/time)
  * [org:](http://www.w3.org/ns/org#)
* **Ontology RDF**
  * RDF ([crs.ttl](turtle))
### Description
<p>This ontology is an <a href="https://www.w3.org/OWL/">OWL</a> interpretation of the Commonwealth Record Series (CRS) system's data model that is maintained by the <a href="http://naa.gov.au">National Archives of Australia</a>.</p>
<p>This ontology specialises classes and properties from the <a href="https://www.w3.org/TR/vocab-org/">Organization Ontology</a> and other well-known ontologies such as <a href="http://dublincore.org/schemas/rdfs/">Dublin Core</a> &amp; <a href="https://www.w3.org/TR/prov-o/">PROV</a> to describe CRS things in specific terms but also in relation to well-known generic terms.</p>
<p>It also refers to components in other Australian government ontologies, particularly <a href="http://reference.data.gov.au/def/ont/agrif">AGRIF</a> - Australian government Functions &amp; Records</p>

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
[Administrative Arrangement Order](#AdministrativeArrangementOrder),
[Affiliation](#Affiliation),
[Agent](#Agent),
[Agent](#Agent1),
[Assistant Minister](#AssistantMinister),
[Authority](#Authority),
[Commonwealth Agency](#CommonwealthAgency),
[Commonwealth Organisation](#CommonwealthOrganisation),
[Commonwealth Person](#CommonwealthPerson),
[Deputy Prime Minister](#DeputyPrimeMinister),
[Government Function](#GovernmentFunction),
[Interval](#Interval),
[Item](#Item),
[Member](#Member),
[Membership](#Membership),
[Minister](#Minister),
[Minister of State](#MinisterofState),
[Organization](#Organization),
[Parliamentary Secretary](#ParliamentarySecretary),
[Person](#Person),
[Prime Minister](#PrimeMinister),
[Relationship](#Relationship),
[Role](#Role),
[Series](#Series),
### Administrative Arrangement Order
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#AdministrativeArrangementOrder`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>Administrative Arrangements Orders (AAOs) formally allocate executive responsibility among ministers. They set out which matters and legislation are administered by which department or portfolio. AAOs are re-issued or amended to take into account changes in the structure of government. The information hosted here is for historical purposes only</p>
### Affiliation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Affiliation`
Description | <p>Affiliations are temporal associations between CRS Agents that indicate both the Agent-Agent relation and a Role.</p> <p>For example John Howard was Associated with the House of Representatitves where he played the Role of Member of Parliament (among others). Associations may be temporal, for example John Howard was Associated with the Department of Prime Minister &amp; Cabinet where he played the Role of Prime Minister from 1996-2007.</p>
Super-classes |[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
Restrictions |[http://linked.data.gov.au/def/crs#hasAgent](http://linked.data.gov.au/def/crs#hasAgent) (op) **min** 2<br />
### Agent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Agent`
Super-classes |[prov:Agent](http://www.w3.org/ns/prov#Agent) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/crs#CommonwealthOrganisation](http://linked.data.gov.au/def/crs#CommonwealthOrganisation) (c)<br />[http://linked.data.gov.au/def/crs#CommonwealthAgency](http://linked.data.gov.au/def/crs#CommonwealthAgency) (c)<br />[sdo:Person](https://schema.org/Person) (c)<br />
In domain of |[http://linked.data.gov.au/def/crs#affiliatedWith](http://linked.data.gov.au/def/crs#affiliatedWith) (op)<br />[http://linked.data.gov.au/def/crs#created](http://linked.data.gov.au/def/crs#created) (op)<br />
In range of |[http://linked.data.gov.au/def/crs#hasAgent](http://linked.data.gov.au/def/crs#hasAgent) (op)<br />[http://linked.data.gov.au/def/crs#creator](http://linked.data.gov.au/def/crs#creator) (op)<br />[org:hasMember](http://www.w3.org/ns/org#hasMember) (op)<br />
### Assistant Minister
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#AssistantMinister`
### Authority
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Authority`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>An authority or rule that define the functions and activities of a Government Entity</p>
In range of |[http://linked.data.gov.au/def/crs#mandatedBy](http://linked.data.gov.au/def/crs#mandatedBy) (op)<br />
### Commonwealth Agency
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#CommonwealthAgency`
Super-classes |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
Restrictions |[http://linked.data.gov.au/def/crs#created](http://linked.data.gov.au/def/crs#created) (op) **min** 1 [http://linked.data.gov.au/def/crs#Series](http://linked.data.gov.au/def/crs#Series) (c)<br />[http://linked.data.gov.au/def/crs#isPartOf](http://linked.data.gov.au/def/crs#isPartOf) (op) **only** [http://linked.data.gov.au/def/crs#CommonwealthOrganisation](http://linked.data.gov.au/def/crs#CommonwealthOrganisation) (c)<br />[http://linked.data.gov.au/def/crs#performs](http://linked.data.gov.au/def/crs#performs) (op) **only** ([http://linked.data.gov.au/def/crs#Function](http://linked.data.gov.au/def/crs#Function) (c) or [http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c))<br />
In domain of |[http://linked.data.gov.au/def/crs#performs](http://linked.data.gov.au/def/crs#performs) (op)<br />
### Commonwealth Organisation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#CommonwealthOrganisation`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>A whole government, learned society, church or company. The Archives registers organisations with a CO (Commonwealth Organisation) number</p>
Super-classes |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
Restrictions |[http://linked.data.gov.au/def/crs#hasPart](http://linked.data.gov.au/def/crs#hasPart) (op) **only** [http://linked.data.gov.au/def/crs#CommonwealthAgency](http://linked.data.gov.au/def/crs#CommonwealthAgency) (c)<br />
### Commonwealth Person
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#CommonwealthPerson`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>Depositors of personal records collections. These persons have had a close association with the Commonwealth, such as Prime Ministers, senior public servants and the Governors-General. The Archives registers persons with a CP (Commonwealth Persons) number</p>
Super-classes |[sdo:Person](https://schema.org/Person) (c)<br />
Restrictions |[http://linked.data.gov.au/def/crs#created](http://linked.data.gov.au/def/crs#created) (op) **min** 0 [http://linked.data.gov.au/def/crs#Series](http://linked.data.gov.au/def/crs#Series) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/crs#Minister](http://linked.data.gov.au/def/crs#Minister) (c)<br />[http://linked.data.gov.au/def/crs#ParliamentarySecretary](http://linked.data.gov.au/def/crs#ParliamentarySecretary) (c)<br />
### Deputy Prime Minister
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#DeputyPrimeMinister`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>The Deputy Prime Minister of Australia is the second-most senior officer in the Government of Australia. The office of Deputy Prime Minister was officially created as a ministerial portfolio in 1968, although the title had been used informally for many years previously. The Deputy Prime Minister is appointed by the Governor-General on the advice of the Prime Minister</p>
Super-classes |[http://linked.data.gov.au/def/crs#MinisterOfState](http://linked.data.gov.au/def/crs#MinisterOfState) (c)<br />
### Government Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Function`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>A major function normally undertaken by an agency in its operations</p>
Super-classes |[http://linked.data.gov.au/def/agift#Function](http://linked.data.gov.au/def/agift#Function) (c)<br />
Restrictions |[http://linked.data.gov.au/def/crs#isPerformedBy](http://linked.data.gov.au/def/crs#isPerformedBy) (op) **only** ([http://linked.data.gov.au/def/crs#CommonwealthAgency](http://linked.data.gov.au/def/crs#CommonwealthAgency) (c) or [http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c))<br />
In domain of |[http://linked.data.gov.au/def/crs#isPerformedBy](http://linked.data.gov.au/def/crs#isPerformedBy) (op)<br />
In range of |[http://linked.data.gov.au/def/crs#forFunction](http://linked.data.gov.au/def/crs#forFunction) (op)<br />
### Item
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Item`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>Individual records in any format, such as files, volumes, maps, photographs or sound recordings. Items are identified by the number or symbol that the agency used when it created the item.</p> <p>Items in the CRS are AGIFT Records.</p>
Super-classes |[http://linked.data.gov.au/def/agrif#Record](http://linked.data.gov.au/def/agrif#Record) (c)<br />
Restrictions |[http://linked.data.gov.au/def/crs#isPartOf](http://linked.data.gov.au/def/crs#isPartOf) (op) **only** [http://linked.data.gov.au/def/crs#Series](http://linked.data.gov.au/def/crs#Series) (c)<br />
### Member
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Member`
Is Defined By | http://linked.data.gov.au/def/crs
### Minister
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Minister`
Is Defined By | http://linked.data.gov.au/def/crs
Super-classes |[http://linked.data.gov.au/def/crs#CommonwealthPerson](http://linked.data.gov.au/def/crs#CommonwealthPerson) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/crs#MinisterOfState](http://linked.data.gov.au/def/crs#MinisterOfState) (c)<br />
### Minister of State
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#MinisterOfState`
Super-classes |[http://linked.data.gov.au/def/crs#Minister](http://linked.data.gov.au/def/crs#Minister) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/crs#PrimeMinister](http://linked.data.gov.au/def/crs#PrimeMinister) (c)<br />[http://linked.data.gov.au/def/crs#DeputyPrimeMinister](http://linked.data.gov.au/def/crs#DeputyPrimeMinister) (c)<br />
### Parliamentary Secretary
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#ParliamentarySecretary`
Is Defined By | http://linked.data.gov.au/def/crs
Super-classes |[http://linked.data.gov.au/def/crs#CommonwealthPerson](http://linked.data.gov.au/def/crs#CommonwealthPerson) (c)<br />
### Prime Minister
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#PrimeMinister`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>The Prime Minister of Australia is the head of government of Australia. The individual who holds the office is the most senior Minister of State, the leader of the Federal Cabinet. The Prime Minister also has the responsibility of administering the Department of the Prime Minister and Cabinet, and is the chair of the National Security Committee and the Council of Australian Governments</p>
Super-classes |[http://linked.data.gov.au/def/crs#MinisterOfState](http://linked.data.gov.au/def/crs#MinisterOfState) (c)<br />
### Relationship
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Relationship`
Description | <p>Relationships are general associations between entities, agents and activities that allow a role, timing and other properties to be attached to a relationship.</p>
Sub-classes |[org:Membership](http://www.w3.org/ns/org#Membership) (c)<br />[http://linked.data.gov.au/def/crs#Affiliation](http://linked.data.gov.au/def/crs#Affiliation) (c)<br />
In domain of |[http://linked.data.gov.au/def/crs#hasRole](http://linked.data.gov.au/def/crs#hasRole) (op)<br />[http://linked.data.gov.au/def/crs#forFunction](http://linked.data.gov.au/def/crs#forFunction) (op)<br />[http://linked.data.gov.au/def/crs#relatedDuring](http://linked.data.gov.au/def/crs#relatedDuring) (op)<br />[http://linked.data.gov.au/def/crs#hasAgent](http://linked.data.gov.au/def/crs#hasAgent) (op)<br />
### Role
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Role`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>The role played by one CRS Agent when associated with another via an Assotiation</p>
Super-classes |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
In range of |[http://linked.data.gov.au/def/crs#hasRole](http://linked.data.gov.au/def/crs#hasRole) (op)<br />
### Series
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#Series`
Is Defined By | http://linked.data.gov.au/def/crs
Description | <p>A group of records created or accumulated by the same agency or person. A series can be a single item or many items. The Archives identifies series with a series number</p>
Super-classes |[dct:Collection](http://purl.org/dc/terms/Collection) (c)<br />
Restrictions |[http://linked.data.gov.au/def/crs#hasPart](http://linked.data.gov.au/def/crs#hasPart) (op) **min** 1<br />[http://linked.data.gov.au/def/crs#creator](http://linked.data.gov.au/def/crs#creator) (op) **min** 1<br />[http://linked.data.gov.au/def/crs#creator](http://linked.data.gov.au/def/crs#creator) (op) **only** ([http://linked.data.gov.au/def/crs#CommonwealthAgency](http://linked.data.gov.au/def/crs#CommonwealthAgency) (c) or [http://linked.data.gov.au/def/crs#CommonwealthPerson](http://linked.data.gov.au/def/crs#CommonwealthPerson) (c))<br />[http://linked.data.gov.au/def/crs#hasPart](http://linked.data.gov.au/def/crs#hasPart) (op) **only** [http://linked.data.gov.au/def/crs#Item](http://linked.data.gov.au/def/crs#Item) (c)<br />
### Interval
Property | Value
--- | ---
URI | `http://www.w3.org/2006/time#Interval`
In range of |[org:memberDuring](http://www.w3.org/ns/org#memberDuring) (op)<br />[http://linked.data.gov.au/def/crs#relatedDuring](http://linked.data.gov.au/def/crs#relatedDuring) (op)<br />
### Membership
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#Membership`
Super-classes |[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
### Organization
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#Organization`
Sub-classes |[http://linked.data.gov.au/def/crs#CommonwealthOrganisation](http://linked.data.gov.au/def/crs#CommonwealthOrganisation) (c)<br />[http://linked.data.gov.au/def/crs#CommonwealthAgency](http://linked.data.gov.au/def/crs#CommonwealthAgency) (c)<br />
In domain of |[org:hasMember](http://www.w3.org/ns/org#hasMember) (op)<br />[org:memberDuring](http://www.w3.org/ns/org#memberDuring) (op)<br />[org:linkedTo](http://www.w3.org/ns/org#linkedTo) (op)<br />[org:hasSubOrganization](http://www.w3.org/ns/org#hasSubOrganization) (op)<br />
In range of |[org:memberOf](http://www.w3.org/ns/org#memberOf) (op)<br />[org:hasSubOrganization](http://www.w3.org/ns/org#hasSubOrganization) (op)<br />[org:linkedTo](http://www.w3.org/ns/org#linkedTo) (op)<br />
### Agent
Property | Value
--- | ---
URI | `http://www.w3.org/ns/prov#Agent`
Sub-classes |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
### Person
Property | Value
--- | ---
URI | `https://schema.org/Person`
Super-classes |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
Sub-classes |[http://linked.data.gov.au/def/crs#CommonwealthPerson](http://linked.data.gov.au/def/crs#CommonwealthPerson) (c)<br />

## Object Properties
[Affiliated with](#Affiliatedwith),
[created](#created),
[creator](#creator),
[for Function](#forFunction),
[has agent](#hasagent),
[has part](#haspart),
[has role](#hasrole),
[is part of](#ispartof),
[is performed by](#isperformedby),
[mandated by](#mandatedby),
[performs](#performs),
[previous agency](#previousagency),
[related during](#relatedduring),
[related to](#relatedto),
[subordinate agency](#subordinateagency),
[subsequent agency](#subsequentagency),
[superior agency](#superioragency),
[creator](#creator1),
[has member](#hasmember),
[has sub organization](#hassuborganization),
[linked to](#linkedto),
[member](#member),
[member during](#memberduring),
[member of](#memberof),
[original organization](#originalorganization),
[resulted from](#resultedfrom),
[sub organization of](#suborganizationof),
[](Affiliatedwith)
### Affiliated with
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#affiliatedWith`
Is Defined By | http://linked.data.gov.au/def/crs
Description | An Agent (Commonwealth Person, Agency, Organisation) is affiliated with another Agent
Domain(s) |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
Range(s) |[http://linked.data.gov.au/def/crs#Affiliation](http://linked.data.gov.au/def/crs#Affiliation) (c)<br />[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
[](created)
### created
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#created`
Super-properties |[dct:created](http://purl.org/dc/terms/created)<br />
Domain(s) |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
[](creator)
### creator
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#creator`
Super-properties |[dct:creator](http://purl.org/dc/terms/creator) (op)<br />
Range(s) |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
[](forFunction)
### for Function
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#forFunction`
Is Defined By | http://linked.data.gov.au/def/crs
Super-properties |[dct:relation](http://purl.org/dc/terms/relation)<br />
Domain(s) |[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
Range(s) |[http://linked.data.gov.au/def/crs#Function](http://linked.data.gov.au/def/crs#Function) (c)<br />
[](hasagent)
### has agent
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#hasAgent`
Is Defined By | http://linked.data.gov.au/def/crs
Description | Whan an Association object indicates an association between two Agents, this property is used to indicate the Agent the assocition is to, e.g. Agent_1 -> associatedWith -> Association_X, Association_X -> hasAgent -> Agent_2
Super-properties |[dct:relation](http://purl.org/dc/terms/relation)<br />
Domain(s) |[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
Range(s) |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
[](haspart)
### has part
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#hasPart`
Super-properties |[dct:hasPart](http://purl.org/dc/terms/hasPart)<br />
[](hasrole)
### has role
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#hasRole`
Is Defined By | http://linked.data.gov.au/def/crs
Description | A character or part performed especially in a particular operation or process
Domain(s) |[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
Range(s) |[http://linked.data.gov.au/def/crs#Role](http://linked.data.gov.au/def/crs#Role) (c)<br />
[](ispartof)
### is part of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#isPartOf`
Super-properties |[dct:isPartOf](http://purl.org/dc/terms/isPartOf)<br />
[](isperformedby)
### is performed by
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#isPerformedBy`
Domain(s) |[http://linked.data.gov.au/def/crs#Function](http://linked.data.gov.au/def/crs#Function) (c)<br />
Range(s) |[http://linked.data.gov.au/def/crs#CommonwealthAgency](http://linked.data.gov.au/def/crs#CommonwealthAgency) (c)<br />[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
[](mandatedby)
### mandated by
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#mandatedBy`
Is Defined By | http://linked.data.gov.au/def/crs
Description | mandate: A command or an authorization given by a political electorate to its representative
Range(s) |[http://linked.data.gov.au/def/crs#Authority](http://linked.data.gov.au/def/crs#Authority) (c)<br />
[](performs)
### performs
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#performs`
Is Defined By | http://linked.data.gov.au/def/crs
Domain(s) |[http://linked.data.gov.au/def/crs#CommonwealthAgency](http://linked.data.gov.au/def/crs#CommonwealthAgency) (c)<br />
Range(s) |[http://linked.data.gov.au/def/crs#Function](http://linked.data.gov.au/def/crs#Function) (c)<br />[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
[](previousagency)
### previous agency
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#previousAgency`
Is Defined By | http://linked.data.gov.au/def/crs
Super-properties |[org:linkedTo](http://www.w3.org/ns/org#linkedTo) (op)<br />
[](relatedduring)
### related during
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#relatedDuring`
Super-properties |[dct:temporal](http://purl.org/dc/terms/temporal)<br />
Domain(s) |[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />
Range(s) |[time:Interval](http://www.w3.org/2006/time#Interval) (c)<br />
[](relatedto)
### related to
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#relatedTo`
Is Defined By | http://linked.data.gov.au/def/crs
Description | An Entity is related to another Entity
Range(s) |[http://linked.data.gov.au/def/crs#Relationship](http://linked.data.gov.au/def/crs#Relationship) (c)<br />[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](subordinateagency)
### subordinate agency
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#subordinateAgency`
Is Defined By | http://linked.data.gov.au/def/crs
Super-properties |[org:linkedTo](http://www.w3.org/ns/org#linkedTo) (op)<br />[org:hasSubOrganization](http://www.w3.org/ns/org#hasSubOrganization) (op)<br />
[](subsequentagency)
### subsequent agency
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#subsequentAgency`
Is Defined By | http://linked.data.gov.au/def/crs
Super-properties |[org:linkedTo](http://www.w3.org/ns/org#linkedTo) (op)<br />
[](superioragency)
### superior agency
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#superiorAgency`
Is Defined By | http://linked.data.gov.au/def/crs
Super-properties |[org:subOrganizationOf](http://www.w3.org/ns/org#subOrganizationOf) (op)<br />[org:linkedTo](http://www.w3.org/ns/org#linkedTo) (op)<br />
[](creator1)
### creator
Property | Value
--- | ---
URI | `http://purl.org/dc/terms/creator`
[](hasmember)
### has member
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#hasMember`
Is Defined By | http://www.w3.org/ns/org
Super-properties |[http://linked.data.gov.au/def/crs#affiliatedWith](http://linked.data.gov.au/def/crs#affiliatedWith) (op)<br />
Domain(s) |[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
Range(s) |[http://linked.data.gov.au/def/crs#Agent](http://linked.data.gov.au/def/crs#Agent) (c)<br />
[](hassuborganization)
### has sub organization
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#hasSubOrganization`
Is Defined By | http://www.w3.org/ns/org
Domain(s) |[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
Range(s) |[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
[](linkedto)
### linked to
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#linkedTo`
Is Defined By | http://www.w3.org/ns/org
Domain(s) |[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
Range(s) |[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
[](member)
### member
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#member`
[](memberduring)
### member during
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#memberDuring`
Is Defined By | http://www.w3.org/ns/org
Description | Property to indicate the interval for which the membership is/was valid
Super-properties |[dct:temporal](http://purl.org/dc/terms/temporal)<br />
Domain(s) |[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
Range(s) |[time:Interval](http://www.w3.org/2006/time#Interval) (c)<br />
[](memberof)
### member of
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#memberOf`
Is Defined By | http://www.w3.org/ns/org
Super-properties |[http://linked.data.gov.au/def/crs#affiliatedWith](http://linked.data.gov.au/def/crs#affiliatedWith) (op)<br />
Range(s) |[org:Organization](http://www.w3.org/ns/org#Organization) (c)<br />
[](originalorganization)
### original organization
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#originalOrganization`
Is Defined By | http://www.w3.org/ns/org
[](resultedfrom)
### resulted from
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#resultedFrom`
Is Defined By | http://www.w3.org/ns/org
[](suborganizationof)
### sub organization of
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#subOrganizationOf`
Is Defined By | http://www.w3.org/ns/org

## Datatype Properties
[control number](#controlnumber),
[identifier](#identifier),
[](controlnumber)
### control number
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs#controlNumber`
Is Defined By | http://linked.data.gov.au/def/crs
Super-properties |[org:identifier](http://www.w3.org/ns/org#identifier) (dp)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](identifier)
### identifier
Property | Value
--- | ---
URI | `http://www.w3.org/ns/org#identifier`

## Annotation Properties
[comment](#comment),
[None](#None),
[altLabel](#altLabel),
[](comment)
### comment
Property | Value
--- | ---
URI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#comment`
[](None)
### None
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#`
[](altLabel)
### altLabel
Property | Value
--- | ---
URI | `http://www.w3.org/2004/02/skos/core#altLabel`

## Named Individuals
[Commonwealth Record Series Ontology](#CommonwealthRecordSeriesOntology),
[Nicholas J. Car](#NicholasJ.Car),
### Commonwealth Record Series Ontology <sup>c</sup>
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/crs`
* **Contributor(s)**
  * [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology)
Description | This ontology is an [OWL](https://www.w3.org/OWL/) interpretation of the Commonwealth Record Series (CRS) system's data model that is maintained by the [National Archives of Australia](http://naa.gov.au).

This ontology specialises classes and properties from the [Organization Ontology](https://www.w3.org/TR/vocab-org/) and other well-known ontologies such as [Dublin Core](http://dublincore.org/schemas/rdfs/) & [PROV](https://www.w3.org/TR/prov-o/) to describe CRS things in specific terms but also in relation to well-known generic terms.

It also refers to components in other Australian government ontologies, particularly [AGRIF](http://reference.data.gov.au/def/ont/agrif) - Australian government Functions & Records
See Also | [The GitHub repository containing addition documentation: http://github.com/CSIRO-enviro-informatics/crs-ont/](The GitHub repository containing addition documentation: http://github.com/CSIRO-enviro-informatics/crs-ont/)
### Nicholas J. Car <sup>c</sup>
Property | Value
--- | ---
URI | `http://orcid.org/0000-0002-8742-7730`
## Namespaces
* **dct**
  * `http://purl.org/dc/terms/`
* **orcid**
  * `http://orcid.org/`
* **org**
  * `http://www.w3.org/ns/org#`
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
* **time**
  * `http://www.w3.org/2006/time#`
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