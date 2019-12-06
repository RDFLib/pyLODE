# Commonwealth Record Series Ontology
<sub>metadata by [pyLODE](http://github.com/rdflib/pyLODE)</sub>
## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/crs`
* **Publisher(s)**
  * <a href="http://catalogue.linked.data.gov.au/org/naa">National Archives of Australia</a>
* **Creators(s)**
  * <a href="http://orcid.org/0000-0002-8742-7730">Nicholas J. Car</a> (<a href="mailto:nicholas.car@csiro.au">nicholas.car@csiro.au</a>) of <a href="http://catalogue.linked.data.gov.au/org/csiro">CSIRO</a>
* **Contributor(s)**
  * David Hearder
  * Marco Wallenius
  * <a href="https://orcid.org/0000-0002-3884-3420">Simon J.D. Cox</a> (<a href="mailto:simon.cox@csiro.au">simon.cox@csiro.au</a>) of <a href="http://catalogue.linked.data.gov.au/org/csiro">CSIRO</a>
* **Created**
  * 2018-09-10
* **Modified**
  * 2019-05-31
* **Version Information**
  * Beta version
* **Version IRI**
  * <a href="http://linked.data.gov.au/def/crs#">http://linked.data.gov.au/def/crs#</a>
* **Imports**
  * <a href="http://www.w3.org/2006/time">http://www.w3.org/2006/time</a>
  * <a href="http://www.w3.org/ns/org#">org:</a>
  * <a href="http://purl.org/dc/elements/1.1/">dc:</a>
* **Ontology Source**
  * <a href="crs.ttl">RDF (turtle)</a>
### Description
<p>This ontology is an <a href="https://www.w3.org/OWL/">OWL</a> interpretation of the Commonwealth Record Series (CRS) system's data model that is maintained by the <a href="http://naa.gov.au">National Archives of Australia</a>.</p>
<p>This ontology specialises classes and properties from the <a href="https://www.w3.org/TR/vocab-org/">Organization Ontology</a> and other well-known ontologies such as <a href="http://dublincore.org/schemas/rdfs/">Dublin Core</a> &amp; <a href="https://www.w3.org/TR/prov-o/">PROV</a> to describe CRS things in specific terms but also in relation to well-known generic terms.</p>
<p>It also refers to components in other Australian government ontologies, particularly <a href="http://reference.data.gov.au/def/ont/agrif">AGRIF</a> - Australian government Functions &amp; Records</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Namespaces](#namespaces)  


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
### Administrative Arrangement Order <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#AdministrativeArrangementOrder`
Description | Administrative Arrangements Orders (AAOs) formally allocate executive responsibility among ministers. They set out which matters and legislation are administered by which department or portfolio. AAOs are re-issued or amended to take into account changes in the structure of government. The information hosted here is for historical purposes only
### Affiliation <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Affiliation`
Description | Affiliations are temporal associations between CRS Agents that indicate both the Agent-Agent relation and a Role.

For example John Howard was Associated with the House of Representatitves where he played the Role of Member of Parliament (among others).
Associations may be temporal, for example John Howard was Associated with the Department of Prime Minister & Cabinet where he played the Role of Prime Minister from 1996-2007.
Super-classes |<a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#hasagent">crs:hasAgent</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 2<br />
### Agent <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Agent`
Super-classes |<a href="http://www.w3.org/ns/prov#Agent">http://www.w3.org/ns/prov#Agent</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="https://schema.org/Person">sdo:Person</a><sup class="sup-c" title="class">c</sup><br /><a href="#CommonwealthAgency">crs:CommonwealthAgency</a><sup class="sup-c" title="class">c</sup><br /><a href="#CommonwealthOrganisation">crs:CommonwealthOrganisation</a><sup class="sup-c" title="class">c</sup><br />
In domain of |<a href="#Affiliatedwith">crs:affiliatedWith</a><sup class="sup-op" title="object property">op</sup><br /><a href="#created">crs:created</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="#hasagent">crs:hasAgent</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#hasMember">org:hasMember</a><sup class="sup-op" title="object property">op</sup><br /><a href="#creator">crs:creator</a><sup class="sup-op" title="object property">op</sup><br />
### Assistant Minister <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#AssistantMinister`
### Authority <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Authority`
Description | An authority or rule that define the functions and activities of a Government Entity
In range of |<a href="#mandatedby">crs:mandatedBy</a><sup class="sup-op" title="object property">op</sup><br />
### Commonwealth Agency <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#CommonwealthAgency`
Super-classes |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br /><a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#created">crs:created</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 1 <a href="#Series">crs:Series</a><sup class="sup-c" title="class">c</sup><br /><a href="#ispartof">crs:isPartOf</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#CommonwealthOrganisation">crs:CommonwealthOrganisation</a><sup class="sup-c" title="class">c</sup><br /><a href="#performs">crs:performs</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> (<a href="#GovernmentFunction">crs:Function</a><sup class="sup-c" title="class">c</sup> or <a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup>)<br />
In domain of |<a href="#performs">crs:performs</a><sup class="sup-op" title="object property">op</sup><br />
### Commonwealth Organisation <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#CommonwealthOrganisation`
Description | A whole government, learned society, church or company. The Archives registers organisations with a CO (Commonwealth Organisation) number
Super-classes |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br /><a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#haspart">crs:hasPart</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#CommonwealthAgency">crs:CommonwealthAgency</a><sup class="sup-c" title="class">c</sup><br />
### Commonwealth Person <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#CommonwealthPerson`
Description | Depositors of personal records collections. These persons have had a close association with the Commonwealth, such as Prime Ministers, senior public servants and the Governors-General. The Archives registers persons with a CP (Commonwealth Persons) number
Super-classes |<a href="https://schema.org/Person">sdo:Person</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#created">crs:created</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 0 <a href="#Series">crs:Series</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#ParliamentarySecretary">crs:ParliamentarySecretary</a><sup class="sup-c" title="class">c</sup><br /><a href="#Minister">crs:Minister</a><sup class="sup-c" title="class">c</sup><br />
### Deputy Prime Minister <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#DeputyPrimeMinister`
Description | The Deputy Prime Minister of Australia is the second-most senior officer in the Government of Australia. The office of Deputy Prime Minister was officially created as a ministerial portfolio in 1968, although the title had been used informally for many years previously. The Deputy Prime Minister is appointed by the Governor-General on the advice of the Prime Minister
Super-classes |<a href="#MinisterofState">crs:MinisterOfState</a><sup class="sup-c" title="class">c</sup><br />
### Government Function <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Function`
Description | A major function normally undertaken by an agency in its operations
Super-classes |<a href="http://linked.data.gov.au/def/agift#Function">agift:Function</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#isperformedby">crs:isPerformedBy</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> (<a href="#CommonwealthAgency">crs:CommonwealthAgency</a><sup class="sup-c" title="class">c</sup> or <a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup>)<br />
In domain of |<a href="#isperformedby">crs:isPerformedBy</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="#forFunction">crs:forFunction</a><sup class="sup-op" title="object property">op</sup><br />
### Item <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Item`
Description | Individual records in any format, such as files, volumes, maps, photographs or sound recordings. Items are identified by the number or symbol that the agency used when it created the item.

Items in the CRS are AGIFT Records.
Super-classes |<a href="http://linked.data.gov.au/def/agrif#Record">agrif:Record</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#ispartof">crs:isPartOf</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#Series">crs:Series</a><sup class="sup-c" title="class">c</sup><br />
### Member <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Member`
### Minister <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Minister`
Super-classes |<a href="#CommonwealthPerson">crs:CommonwealthPerson</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#MinisterofState">crs:MinisterOfState</a><sup class="sup-c" title="class">c</sup><br />
### Minister of State <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#MinisterOfState`
Super-classes |<a href="#Minister">crs:Minister</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#PrimeMinister">crs:PrimeMinister</a><sup class="sup-c" title="class">c</sup><br /><a href="#DeputyPrimeMinister">crs:DeputyPrimeMinister</a><sup class="sup-c" title="class">c</sup><br />
### Parliamentary Secretary <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#ParliamentarySecretary`
Super-classes |<a href="#CommonwealthPerson">crs:CommonwealthPerson</a><sup class="sup-c" title="class">c</sup><br />
### Prime Minister <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#PrimeMinister`
Description | The Prime Minister of Australia is the head of government of Australia. The individual who holds the office is the most senior Minister of State, the leader of the Federal Cabinet. The Prime Minister also has the responsibility of administering the Department of the Prime Minister and Cabinet, and is the chair of the National Security Committee and the Council of Australian Governments
Super-classes |<a href="#MinisterofState">crs:MinisterOfState</a><sup class="sup-c" title="class">c</sup><br />
### Relationship <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Relationship`
Description | Relationships are general associations between entities, agents and activities that allow a role, timing and other properties to be attached to a relationship.
Sub-classes |<a href="http://www.w3.org/ns/org#Membership">org:Membership</a><sup class="sup-c" title="class">c</sup><br /><a href="#Affiliation">crs:Affiliation</a><sup class="sup-c" title="class">c</sup><br />
In domain of |<a href="#forFunction">crs:forFunction</a><sup class="sup-op" title="object property">op</sup><br /><a href="#relatedduring">crs:relatedDuring</a><sup class="sup-op" title="object property">op</sup><br /><a href="#hasrole">crs:hasRole</a><sup class="sup-op" title="object property">op</sup><br /><a href="#hasagent">crs:hasAgent</a><sup class="sup-op" title="object property">op</sup><br />
### Role <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Role`
Description | The role played by one CRS Agent when associated with another via an Assotiation
Super-classes |<a href="http://www.w3.org/2004/02/skos/core#Concept">skos:Concept</a><sup class="sup-c" title="class">c</sup><br />
In range of |<a href="#hasrole">crs:hasRole</a><sup class="sup-op" title="object property">op</sup><br />
### Series <sup>c</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#Series`
Description | A group of records created or accumulated by the same agency or person. A series can be a single item or many items. The Archives identifies series with a series number
Super-classes |<a href="http://purl.org/dc/terms/Collection">dct:Collection</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |<a href="#creator">crs:creator</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 1<br /><a href="#haspart">crs:hasPart</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">min</span> 1<br /><a href="#creator">crs:creator</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> (<a href="#CommonwealthAgency">crs:CommonwealthAgency</a><sup class="sup-c" title="class">c</sup> or <a href="#CommonwealthPerson">crs:CommonwealthPerson</a><sup class="sup-c" title="class">c</sup>)<br /><a href="#haspart">crs:hasPart</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#Item">crs:Item</a><sup class="sup-c" title="class">c</sup><br />
### Interval <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/2006/time#Interval`
In range of |<a href="#relatedduring">crs:relatedDuring</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#memberDuring">org:memberDuring</a><sup class="sup-op" title="object property">op</sup><br />
### Membership <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#Membership`
Super-classes |<a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
### Organization <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#Organization`
Sub-classes |<a href="#CommonwealthOrganisation">crs:CommonwealthOrganisation</a><sup class="sup-c" title="class">c</sup><br /><a href="#CommonwealthAgency">crs:CommonwealthAgency</a><sup class="sup-c" title="class">c</sup><br />
In domain of |<a href="http://www.w3.org/ns/org#hasMember">org:hasMember</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#memberDuring">org:memberDuring</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#hasSubOrganization">org:hasSubOrganization</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#linkedTo">org:linkedTo</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="http://www.w3.org/ns/org#memberOf">org:memberOf</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#hasSubOrganization">org:hasSubOrganization</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#linkedTo">org:linkedTo</a><sup class="sup-op" title="object property">op</sup><br />
### Agent <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/prov#Agent`
Sub-classes |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
### Person <sup>c</sup>
Property | Value
--- | ---
IRI | `https://schema.org/Person`
Super-classes |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
Sub-classes |<a href="#CommonwealthPerson">crs:CommonwealthPerson</a><sup class="sup-c" title="class">c</sup><br />

## Object Properties
[Affiliated with](Affiliatedwith),
[created](created),
[creator](creator),
[for Function](forFunction),
[has agent](hasagent),
[has part](haspart),
[has role](hasrole),
[is part of](ispartof),
[is performed by](isperformedby),
[mandated by](mandatedby),
[performs](performs),
[previous agency](previousagency),
[related during](relatedduring),
[related to](relatedto),
[subordinate agency](subordinateagency),
[subsequent agency](subsequentagency),
[superior agency](superioragency),
[creator](creator1),
[has member](hasmember),
[has sub organization](hassuborganization),
[linked to](linkedto),
[member](member),
[member during](memberduring),
[member of](memberof),
[original organization](originalorganization),
[resulted from](resultedfrom),
[sub organization of](suborganizationof),
[](Affiliatedwith)
### Affiliated with <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#affiliatedWith`
Description | An Agent (Commonwealth Person, Agency, Organisation) is affiliated with another Agent
Domain(s) |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#Affiliation">crs:Affiliation</a><sup class="sup-c" title="class">c</sup><br /><a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](created)
### created <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#created`
Super-properties |<a href="http://purl.org/dc/terms/created">dct:created</a><br />
Domain(s) |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](creator)
### creator <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#creator`
Super-properties |<a href="http://purl.org/dc/terms/creator">dct:creator</a><sup class="sup-op" title="object property">op</sup><br />
Range(s) |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](forFunction)
### for Function <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#forFunction`
Super-properties |<a href="http://purl.org/dc/terms/relation">dct:relation</a><br />
Domain(s) |<a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#GovernmentFunction">crs:Function</a><sup class="sup-c" title="class">c</sup><br />
[](hasagent)
### has agent <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#hasAgent`
Description | Whan an Association object indicates an association between two Agents, this property is used to indicate the Agent the assocition is to, e.g. Agent_1 -> associatedWith -> Association_X, Association_X -> hasAgent -> Agent_2
Super-properties |<a href="http://purl.org/dc/terms/relation">dct:relation</a><br />
Domain(s) |<a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](haspart)
### has part <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#hasPart`
Super-properties |<a href="http://purl.org/dc/terms/hasPart">dct:hasPart</a><br />
[](hasrole)
### has role <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#hasRole`
Description | A character or part performed especially in a particular operation or process
Domain(s) |<a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#Role">crs:Role</a><sup class="sup-c" title="class">c</sup><br />
[](ispartof)
### is part of <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#isPartOf`
Super-properties |<a href="http://purl.org/dc/terms/isPartOf">dct:isPartOf</a><br />
[](isperformedby)
### is performed by <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#isPerformedBy`
Domain(s) |<a href="#GovernmentFunction">crs:Function</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#CommonwealthAgency">crs:CommonwealthAgency</a><sup class="sup-c" title="class">c</sup><br /><a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
[](mandatedby)
### mandated by <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#mandatedBy`
Description | mandate: A command or an authorization given by a political electorate to its representative
Range(s) |<a href="#Authority">crs:Authority</a><sup class="sup-c" title="class">c</sup><br />
[](performs)
### performs <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#performs`
Domain(s) |<a href="#CommonwealthAgency">crs:CommonwealthAgency</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#GovernmentFunction">crs:Function</a><sup class="sup-c" title="class">c</sup><br /><a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
[](previousagency)
### previous agency <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#previousAgency`
Super-properties |<a href="http://www.w3.org/ns/org#linkedTo">org:linkedTo</a><sup class="sup-op" title="object property">op</sup><br />
[](relatedduring)
### related during <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#relatedDuring`
Super-properties |<a href="http://purl.org/dc/terms/temporal">dct:temporal</a><br />
Domain(s) |<a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2006/time#Interval">http://www.w3.org/2006/time#Interval</a><sup class="sup-c" title="class">c</sup><br />
[](relatedto)
### related to <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#relatedTo`
Description | An Entity is related to another Entity
Range(s) |<a href="#Relationship">crs:Relationship</a><sup class="sup-c" title="class">c</sup><br /><a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](subordinateagency)
### subordinate agency <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#subordinateAgency`
Super-properties |<a href="http://www.w3.org/ns/org#hasSubOrganization">org:hasSubOrganization</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#linkedTo">org:linkedTo</a><sup class="sup-op" title="object property">op</sup><br />
[](subsequentagency)
### subsequent agency <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#subsequentAgency`
Super-properties |<a href="http://www.w3.org/ns/org#linkedTo">org:linkedTo</a><sup class="sup-op" title="object property">op</sup><br />
[](superioragency)
### superior agency <sup>op</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#superiorAgency`
Super-properties |<a href="http://www.w3.org/ns/org#linkedTo">org:linkedTo</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://www.w3.org/ns/org#subOrganizationOf">org:subOrganizationOf</a><sup class="sup-op" title="object property">op</sup><br />
[](creator1)
### creator <sup>op</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/terms/creator`
[](hasmember)
### has member <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#hasMember`
Super-properties |<a href="#Affiliatedwith">crs:affiliatedWith</a><sup class="sup-op" title="object property">op</sup><br />
Domain(s) |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="#Agent">crs:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](hassuborganization)
### has sub organization <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#hasSubOrganization`
Domain(s) |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
[](linkedto)
### linked to <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#linkedTo`
Domain(s) |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
[](member)
### member <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#member`
[](memberduring)
### member during <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#memberDuring`
Description | Property to indicate the interval for which the membership is/was valid
Super-properties |<a href="http://purl.org/dc/terms/temporal">dct:temporal</a><br />
Domain(s) |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2006/time#Interval">http://www.w3.org/2006/time#Interval</a><sup class="sup-c" title="class">c</sup><br />
[](memberof)
### member of <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#memberOf`
Super-properties |<a href="#Affiliatedwith">crs:affiliatedWith</a><sup class="sup-op" title="object property">op</sup><br />
Range(s) |<a href="http://www.w3.org/ns/org#Organization">org:Organization</a><sup class="sup-c" title="class">c</sup><br />
[](originalorganization)
### original organization <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#originalOrganization`
[](resultedfrom)
### resulted from <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#resultedFrom`
[](suborganizationof)
### sub organization of <sup>op</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#subOrganizationOf`

## Datatype Properties
[control number](controlnumber),
[identifier](identifier),
[](controlnumber)
### control number <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/crs#controlNumber`
Super-properties |<a href="http://www.w3.org/ns/org#identifier">org:identifier</a><sup class="sup-dp" title="datatype property">dp</sup><br />
Range(s) |<a href="http://www.w3.org/2001/XMLSchema#string">xsd:string</a><sup class="sup-c" title="class">c</sup><br />
[](identifier)
### identifier <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/ns/org#identifier`

## Annotation Properties
[comment](comment),
[None](None),
[altLabel](altLabel),
[](comment)
### comment <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/1999/02/22-rdf-syntax-ns#comment`
[](None)
### None <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/2000/01/rdf-schema#`
[](altLabel)
### altLabel <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/2004/02/skos/core#altLabel`

## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/crs#`
* **agift**
  * `http://linked.data.gov.au/def/agift#`
* **agrif**
  * `http://linked.data.gov.au/def/agrif#`
* **auorg**
  * `http://linked.data.gov.au/def/auorg/`
* **crs**
  * `http://linked.data.gov.au/def/crs#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **org**
  * `http://www.w3.org/ns/org#`
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
* **time**
  * `http://www.w3.org/2006/time`
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