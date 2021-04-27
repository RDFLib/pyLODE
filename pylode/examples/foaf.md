Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Friend of a Friend (FOAF) vocabulary

## Metadata
* **URI**
  * `http://xmlns.com/foaf/0.1/`
* **Ontology RDF**
  * RDF ([foaf.ttl](turtle))
### Description
<p>The Friend of a Friend (FOAF) RDF vocabulary, described using W3C RDF Schema and the Web Ontology Language.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Functional Properties](#functionalproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Annotation Properties](#annotationproperties)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Agent](#Agent),
[Class](#Class),
[Document](#Document),
[Group](#Group),
[Image](#Image),
[Label Property](#LabelProperty),
[Online Account](#OnlineAccount),
[Online Chat Account](#OnlineChatAccount),
[Online E-commerce Account](#OnlineE-commerceAccount),
[Online Gaming Account](#OnlineGamingAccount),
[Organization](#Organization),
[Person](#Person),
[PersonalProfileDocument](#PersonalProfileDocument),
[Project](#Project),
[Spatial Thing](#SpatialThing),
### Class
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#Class`
Has members |[foaf:LabelProperty](http://xmlns.com/foaf/0.1/LabelProperty)<br />[foaf:OnlineGamingAccount](http://xmlns.com/foaf/0.1/OnlineGamingAccount)<br />[foaf:PersonalProfileDocument](http://xmlns.com/foaf/0.1/PersonalProfileDocument)<br />[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount)<br />[foaf:Person](http://xmlns.com/foaf/0.1/Person)<br />[foaf:Image](http://xmlns.com/foaf/0.1/Image)<br />[geo:SpatialThing](http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing)<br />[foaf:Group](http://xmlns.com/foaf/0.1/Group)<br />[foaf:OnlineChatAccount](http://xmlns.com/foaf/0.1/OnlineChatAccount)<br />[foaf:OnlineEcommerceAccount](http://xmlns.com/foaf/0.1/OnlineEcommerceAccount)<br />[foaf:Agent](http://xmlns.com/foaf/0.1/Agent)<br />[foaf:Project](http://xmlns.com/foaf/0.1/Project)<br />[foaf:Organization](http://xmlns.com/foaf/0.1/Organization)<br />[rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class)<br />[foaf:Document](http://xmlns.com/foaf/0.1/Document)<br />
### Spatial Thing
Property | Value
--- | ---
URI | `http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing`
Sub-classes |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
In domain of |[foaf:based_near](http://xmlns.com/foaf/0.1/based_near) (op)<br />
In range of |[foaf:based_near](http://xmlns.com/foaf/0.1/based_near) (op)<br />
### Agent
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Agent`
Description | <p>An agent (eg. person, group, software or physical artifact).</p>
Sub-classes |[foaf:Group](http://xmlns.com/foaf/0.1/Group) (c)<br />[foaf:Organization](http://xmlns.com/foaf/0.1/Organization) (c)<br />[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
In domain of |[foaf:status](http://xmlns.com/foaf/0.1/status) (dp)<br />[foaf:gender](http://xmlns.com/foaf/0.1/gender) (fp)<br />[foaf:age](http://xmlns.com/foaf/0.1/age) (fp)<br />[foaf:skypeID](http://xmlns.com/foaf/0.1/skypeID) (dp)<br />[foaf:topic_interest](http://xmlns.com/foaf/0.1/topic_interest) (op)<br />[foaf:aimChatID](http://xmlns.com/foaf/0.1/aimChatID) (dp)<br />[foaf:yahooChatID](http://xmlns.com/foaf/0.1/yahooChatID) (dp)<br />[foaf:holdsAccount](http://xmlns.com/foaf/0.1/holdsAccount) (op)<br />[foaf:account](http://xmlns.com/foaf/0.1/account) (op)<br />[foaf:mbox_sha1sum](http://xmlns.com/foaf/0.1/mbox_sha1sum) (dp)<br />[foaf:interest](http://xmlns.com/foaf/0.1/interest) (op)<br />[foaf:birthday](http://xmlns.com/foaf/0.1/birthday) (fp)<br />[foaf:icqChatID](http://xmlns.com/foaf/0.1/icqChatID) (dp)<br />[foaf:jabberID](http://xmlns.com/foaf/0.1/jabberID) (dp)<br />[foaf:weblog](http://xmlns.com/foaf/0.1/weblog) (op)<br />[foaf:tipjar](http://xmlns.com/foaf/0.1/tipjar) (op)<br />[foaf:msnChatID](http://xmlns.com/foaf/0.1/msnChatID) (dp)<br />[foaf:mbox](http://xmlns.com/foaf/0.1/mbox) (op)<br />[foaf:openid](http://xmlns.com/foaf/0.1/openid) (op)<br />[foaf:made](http://xmlns.com/foaf/0.1/made) (op)<br />
In range of |[foaf:member](http://xmlns.com/foaf/0.1/member) (op)<br />[foaf:maker](http://xmlns.com/foaf/0.1/maker) (op)<br />
### Document
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Document`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>A document.</p>
Sub-classes |[foaf:Image](http://xmlns.com/foaf/0.1/Image) (c)<br />[foaf:PersonalProfileDocument](http://xmlns.com/foaf/0.1/PersonalProfileDocument) (c)<br />
In domain of |[foaf:primaryTopic](http://xmlns.com/foaf/0.1/primaryTopic) (op)<br />[foaf:sha1](http://xmlns.com/foaf/0.1/sha1) (dp)<br />[foaf:topic](http://xmlns.com/foaf/0.1/topic) (op)<br />
In range of |[foaf:tipjar](http://xmlns.com/foaf/0.1/tipjar) (op)<br />[foaf:workInfoHomepage](http://xmlns.com/foaf/0.1/workInfoHomepage) (op)<br />[foaf:homepage](http://xmlns.com/foaf/0.1/homepage) (op)<br />[foaf:openid](http://xmlns.com/foaf/0.1/openid) (op)<br />[foaf:page](http://xmlns.com/foaf/0.1/page) (op)<br />[foaf:isPrimaryTopicOf](http://xmlns.com/foaf/0.1/isPrimaryTopicOf)<br />[foaf:schoolHomepage](http://xmlns.com/foaf/0.1/schoolHomepage) (op)<br />[foaf:weblog](http://xmlns.com/foaf/0.1/weblog) (op)<br />[foaf:accountServiceHomepage](http://xmlns.com/foaf/0.1/accountServiceHomepage) (op)<br />[foaf:workplaceHomepage](http://xmlns.com/foaf/0.1/workplaceHomepage) (op)<br />[foaf:publications](http://xmlns.com/foaf/0.1/publications) (op)<br />[foaf:interest](http://xmlns.com/foaf/0.1/interest) (op)<br />
### Group
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Group`
Description | <p>A class of Agents.</p>
Super-classes |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
In domain of |[foaf:member](http://xmlns.com/foaf/0.1/member) (op)<br />
### Image
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Image`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>An image.</p>
Super-classes |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
In domain of |[foaf:depicts](http://xmlns.com/foaf/0.1/depicts) (op)<br />[foaf:thumbnail](http://xmlns.com/foaf/0.1/thumbnail) (op)<br />
In range of |[foaf:thumbnail](http://xmlns.com/foaf/0.1/thumbnail) (op)<br />[foaf:depiction](http://xmlns.com/foaf/0.1/depiction) (op)<br />[foaf:img](http://xmlns.com/foaf/0.1/img) (op)<br />
### Label Property
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/LabelProperty`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>A foaf:LabelProperty is any RDF property with texual values that serve as labels.</p>
### Online Account
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/OnlineAccount`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>An online account.</p>
Super-classes |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Sub-classes |[foaf:OnlineGamingAccount](http://xmlns.com/foaf/0.1/OnlineGamingAccount) (c)<br />[foaf:OnlineChatAccount](http://xmlns.com/foaf/0.1/OnlineChatAccount) (c)<br />[foaf:OnlineEcommerceAccount](http://xmlns.com/foaf/0.1/OnlineEcommerceAccount) (c)<br />
In domain of |[foaf:accountName](http://xmlns.com/foaf/0.1/accountName) (dp)<br />[foaf:accountServiceHomepage](http://xmlns.com/foaf/0.1/accountServiceHomepage) (op)<br />
In range of |[foaf:holdsAccount](http://xmlns.com/foaf/0.1/holdsAccount) (op)<br />[foaf:account](http://xmlns.com/foaf/0.1/account) (op)<br />
### Online Chat Account
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/OnlineChatAccount`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>An online chat account.</p>
Super-classes |[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount) (c)<br />
### Online E-commerce Account
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/OnlineEcommerceAccount`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>An online e-commerce account.</p>
Super-classes |[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount) (c)<br />
### Online Gaming Account
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/OnlineGamingAccount`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>An online gaming account.</p>
Super-classes |[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount) (c)<br />
### Organization
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Organization`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>An organization.</p>
Super-classes |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
### Person
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Person`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>A person.</p>
Super-classes |[geo:SpatialThing](http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing) (c)<br />[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
In domain of |[foaf:knows](http://xmlns.com/foaf/0.1/knows) (op)<br />[foaf:myersBriggs](http://xmlns.com/foaf/0.1/myersBriggs) (dp)<br />[foaf:firstName](http://xmlns.com/foaf/0.1/firstName) (dp)<br />[foaf:publications](http://xmlns.com/foaf/0.1/publications) (op)<br />[foaf:schoolHomepage](http://xmlns.com/foaf/0.1/schoolHomepage) (op)<br />[foaf:img](http://xmlns.com/foaf/0.1/img) (op)<br />[foaf:workplaceHomepage](http://xmlns.com/foaf/0.1/workplaceHomepage) (op)<br />[foaf:familyName](http://xmlns.com/foaf/0.1/familyName) (dp)<br />[foaf:plan](http://xmlns.com/foaf/0.1/plan) (dp)<br />[foaf:surname](http://xmlns.com/foaf/0.1/surname) (dp)<br />[foaf:family_name](http://xmlns.com/foaf/0.1/family_name) (dp)<br />[foaf:geekcode](http://xmlns.com/foaf/0.1/geekcode) (dp)<br />[foaf:currentProject](http://xmlns.com/foaf/0.1/currentProject) (op)<br />[foaf:pastProject](http://xmlns.com/foaf/0.1/pastProject) (op)<br />[foaf:lastName](http://xmlns.com/foaf/0.1/lastName) (dp)<br />[foaf:workInfoHomepage](http://xmlns.com/foaf/0.1/workInfoHomepage) (op)<br />
In range of |[foaf:knows](http://xmlns.com/foaf/0.1/knows) (op)<br />
### PersonalProfileDocument
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/PersonalProfileDocument`
Description | <p>A personal profile RDF document.</p>
Super-classes |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
### Project
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/Project`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | <p>A project (a collective endeavour of some kind).</p>

## Object Properties
[account](#account),
[account service homepage](#accountservicehomepage),
[based near](#basednear),
[current project](#currentproject),
[depiction](#depiction),
[depicts](#depicts),
[focus](#focus),
[funded by](#fundedby),
[account](#holdsAccount),
[homepage](#homepage),
[image](#image),
[interest](#interest),
[knows](#knows),
[logo](#logo),
[made](#made),
[maker](#maker),
[personal mailbox](#personalmailbox),
[member](#member),
[openid](#openid),
[page](#page),
[past project](#pastproject),
[phone](#phone),
[primary topic](#primarytopic),
[publications](#publications),
[schoolHomepage](#schoolHomepage),
[theme](#theme),
[thumbnail](#thumbnail),
[tipjar](#tipjar),
[topic](#topic),
[topic_interest](#topic_interest),
[weblog](#weblog),
[work info homepage](#workinfohomepage),
[workplace homepage](#workplacehomepage),
[](account)
### account
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/account`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Indicates an account held by this agent.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount) (c)<br />
[](accountservicehomepage)
### account service homepage
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/accountServiceHomepage`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Indicates a homepage of the service provide for this online account.
Domain(s) |[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](basednear)
### based near
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/based_near`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A location that something is based near, for some broadly human notion of near.
Domain(s) |[geo:SpatialThing](http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing) (c)<br />
Range(s) |[geo:SpatialThing](http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing) (c)<br />
[](currentproject)
### current project
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/currentProject`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A current project this person works on.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](depiction)
### depiction
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/depiction`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A depiction of some thing.
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[foaf:Image](http://xmlns.com/foaf/0.1/Image) (c)<br />
[](depicts)
### depicts
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/depicts`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A thing depicted in this representation.
Domain(s) |[foaf:Image](http://xmlns.com/foaf/0.1/Image) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](focus)
### focus
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/focus`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The underlying or 'focal' entity associated with some SKOS-described concept.
Domain(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](fundedby)
### funded by
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/fundedBy`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | An organization funding a project or person.
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](holdsAccount)
### account
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/holdsAccount`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Indicates an account held by this agent.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount) (c)<br />
[](homepage)
### homepage
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/homepage`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A homepage for some thing.
Super-properties |[foaf:isPrimaryTopicOf](http://xmlns.com/foaf/0.1/isPrimaryTopicOf)<br />[foaf:page](http://xmlns.com/foaf/0.1/page) (op)<br />
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](image)
### image
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/img`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage).
Super-properties |[foaf:depiction](http://xmlns.com/foaf/0.1/depiction) (op)<br />
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[foaf:Image](http://xmlns.com/foaf/0.1/Image) (c)<br />
[](interest)
### interest
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/interest`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A page about a topic of interest to this person.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](knows)
### knows
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/knows`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A person known by this person (indicating some level of reciprocated interaction between the parties).
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](logo)
### logo
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/logo`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A logo representing some thing.
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](made)
### made
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/made`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Something that was made by this agent.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](maker)
### maker
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/maker`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | An agent that  made this thing.
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
[](personalmailbox)
### personal mailbox
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/mbox`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](member)
### member
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/member`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Indicates a member of a Group
Domain(s) |[foaf:Group](http://xmlns.com/foaf/0.1/Group) (c)<br />
Range(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
[](openid)
### openid
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/openid`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | An OpenID for an Agent.
Super-properties |[foaf:isPrimaryTopicOf](http://xmlns.com/foaf/0.1/isPrimaryTopicOf)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](page)
### page
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/page`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A page or document about this thing.
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](pastproject)
### past project
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/pastProject`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A project this person has previously worked on.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](phone)
### phone
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/phone`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A phone,  specified using fully qualified tel: URI scheme (refs: http://www.w3.org/Addressing/schemes.html#tel).
[](primarytopic)
### primary topic
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/primaryTopic`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The primary topic of some page or document.
Domain(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](publications)
### publications
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/publications`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A link to the publications of this person.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](schoolHomepage)
### schoolHomepage
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/schoolHomepage`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A homepage of a school attended by the person.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](theme)
### theme
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/theme`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A theme.
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](thumbnail)
### thumbnail
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/thumbnail`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A derived thumbnail image.
Domain(s) |[foaf:Image](http://xmlns.com/foaf/0.1/Image) (c)<br />
Range(s) |[foaf:Image](http://xmlns.com/foaf/0.1/Image) (c)<br />
[](tipjar)
### tipjar
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/tipjar`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A tipjar document for this agent, describing means for payment and reward.
Super-properties |[foaf:page](http://xmlns.com/foaf/0.1/page) (op)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](topic)
### topic
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/topic`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A topic of some page or document.
Domain(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](topic_interest)
### topic_interest
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/topic_interest`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A thing of interest to this person.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
[](weblog)
### weblog
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/weblog`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A weblog of some thing (whether person, group, company etc.).
Super-properties |[foaf:page](http://xmlns.com/foaf/0.1/page) (op)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](workinfohomepage)
### work info homepage
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/workInfoHomepage`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A work info homepage of some person; a page about their work for some organization.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](workplacehomepage)
### workplace homepage
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/workplaceHomepage`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A workplace homepage of some person; the homepage of an organization they work for.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />

## Functional Properties
[age](#age),
[birthday](#birthday),
[gender](#gender),
[](age)
### age
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/age`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The age in years of some agent.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](birthday)
### birthday
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/birthday`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The birthday of this Agent, represented in mm-dd string form, eg. '12-31'.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](gender)
### gender
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/gender`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The gender of this Agent (typically but not necessarily 'male' or 'female').
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />

## Datatype Properties
[account name](#accountname),
[AIM chat ID](#AIMchatID),
[DNA checksum](#DNAchecksum),
[familyName](#familyName),
[family_name](#family_name),
[firstName](#firstName),
[geekcode](#geekcode),
[Given name](#Givenname),
[Given name](#givenname),
[ICQ chat ID](#ICQchatID),
[jabber ID](#jabberID),
[lastName](#lastName),
[sha1sum of a personal mailbox URI name](#sha1sumofapersonalmailboxURIname),
[MSN chat ID](#MSNchatID),
[myersBriggs](#myersBriggs),
[name](#name),
[nickname](#nickname),
[plan](#plan),
[sha1sum (hex)](#sha1sum(hex)),
[Skype ID](#SkypeID),
[status](#status),
[Surname](#Surname),
[title](#title1),
[Yahoo chat ID](#YahoochatID),
[](accountname)
### account name
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/accountName`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Indicates the name (identifier) associated with this online account.
Domain(s) |[foaf:OnlineAccount](http://xmlns.com/foaf/0.1/OnlineAccount) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](AIMchatID)
### AIM chat ID
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/aimChatID`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | An AIM chat ID
Super-properties |[foaf:nick](http://xmlns.com/foaf/0.1/nick) (dp)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](DNAchecksum)
### DNA checksum
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/dnaChecksum`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A checksum for the DNA of some thing. Joke.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](familyName)
### familyName
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/familyName`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The family name of some person.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](family_name)
### family_name
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/family_name`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The family name of some person.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](firstName)
### firstName
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/firstName`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The first name of a person.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](geekcode)
### geekcode
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/geekcode`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A textual geekcode for this person, see http://www.geekcode.com/geek.html
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](Givenname)
### Given name
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/givenName`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The given name of some person.
[](givenname)
### Given name
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/givenname`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The given name of some person.
[](ICQchatID)
### ICQ chat ID
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/icqChatID`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | An ICQ chat ID
Super-properties |[foaf:nick](http://xmlns.com/foaf/0.1/nick) (dp)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](jabberID)
### jabber ID
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/jabberID`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A jabber ID for something.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](lastName)
### lastName
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/lastName`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The last name of a person.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](sha1sumofapersonalmailboxURIname)
### sha1sum of a personal mailbox URI name
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/mbox_sha1sum`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](MSNchatID)
### MSN chat ID
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/msnChatID`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | An MSN chat ID
Super-properties |[foaf:nick](http://xmlns.com/foaf/0.1/nick) (dp)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](myersBriggs)
### myersBriggs
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/myersBriggs`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A Myers Briggs (MBTI) personality classification.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](name)
### name
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/name`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A name for some thing.
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](nickname)
### nickname
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/nick`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).
[](plan)
### plan
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/plan`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A .plan comment, in the tradition of finger and '.plan' files.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](sha1sum(hex))
### sha1sum (hex)
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/sha1`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A sha1sum hash, in hex.
Domain(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />
[](SkypeID)
### Skype ID
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/skypeID`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A Skype ID
Super-properties |[foaf:nick](http://xmlns.com/foaf/0.1/nick) (dp)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](status)
### status
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/status`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A string expressing what the user is happy for the general public (normally) to know about their current activity.
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](Surname)
### Surname
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/surname`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | The surname of some person.
Domain(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](title1)
### title
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/title`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Title (Mr, Mrs, Ms, Dr. etc)
[](YahoochatID)
### Yahoo chat ID
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/yahooChatID`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A Yahoo chat ID
Super-properties |[foaf:nick](http://xmlns.com/foaf/0.1/nick) (dp)<br />
Domain(s) |[foaf:Agent](http://xmlns.com/foaf/0.1/Agent) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />

## Annotation Properties
[date](#date),
[description](#description),
[title](#title),
[term_status](#term_status),
[membershipClass](#membershipClass),
[assurance](#assurance),
[src_assurance](#src_assurance),
[](date)
### date
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/date`
[](description)
### description
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/description`
[](title)
### title
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/title`
[](term_status)
### term_status
Property | Value
--- | ---
URI | `http://www.w3.org/2003/06/sw-vocab-status/ns#term_status`
[](membershipClass)
### membershipClass
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/membershipClass`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | Indicates the class of individuals that are a member of a Group
[](assurance)
### assurance
Property | Value
--- | ---
URI | `http://xmlns.com/wot/0.1/assurance`
[](src_assurance)
### src_assurance
Property | Value
--- | ---
URI | `http://xmlns.com/wot/0.1/src_assurance`

## Properties
[is primary topic of](#isprimarytopicof),
[](isprimarytopicof)
### is primary topic of
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/isPrimaryTopicOf`
Is Defined By | http://xmlns.com/foaf/0.1/
Description | A document that this thing is the primary topic of.
Super-properties |[foaf:page](http://xmlns.com/foaf/0.1/page) (op)<br />
Domain(s) |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Range(s) |[foaf:Document](http://xmlns.com/foaf/0.1/Document) (c)<br />

## Named Individuals
## Namespaces
* **con**
  * `http://www.w3.org/2000/10/swap/pim/contact#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
* **geo**
  * `http://www.w3.org/2003/01/geo/wgs84_pos#`
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
* **vs**
  * `http://www.w3.org/2003/06/sw-vocab-status/ns#`
* **wot**
  * `http://xmlns.com/wot/0.1/`
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