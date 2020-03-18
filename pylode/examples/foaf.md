# Friend of a Friend (FOAF) vocabulary
<sub>metadata by [pyLODE](http://github.com/rdflib/pyLODE)</sub>
## Metadata
* **IRI**
  * `http://xmlns.com/foaf/0.1/`
* **Ontology Source**
  * <a href="foaf.ttl">RDF (turtle)</a>
### Description
<p>The Friend of a Friend (FOAF) RDF vocabulary, described using W3C RDF Schema and the Web Ontology Language.</p>

## Table of Contents
* [Classes](#classes)
* [Object Properties](#objectproperties)
* [Functional Properties](#functionalproperties)
* [Datatype Properties](#datatypeproperties)
* [Annotation Properties](#annotationproperties)
* [Properties](#properties)
* [Namespaces](#namespaces)  
 
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
### Class <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/2000/01/rdf-schema#Class`
### Spatial Thing <sup>c</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing`
In domain of |<a href="http://xmlns.com/foaf/0.1/based_near">foaf:based_near</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="http://xmlns.com/foaf/0.1/based_near">foaf:based_near</a><sup class="sup-op" title="object property">op</sup><br />
### Agent <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Agent`
Description | An agent (eg. person, group, software or physical artifact).
In domain of |<a href="http://xmlns.com/foaf/0.1/tipjar">foaf:tipjar</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/interest">foaf:interest</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/mbox">foaf:mbox</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/openid">foaf:openid</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/gender">foaf:gender</a><sup class="sup-fp" title="functional property">fp</sup><br /><a href="http://xmlns.com/foaf/0.1/msnChatID">foaf:msnChatID</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/mbox_sha1sum">foaf:mbox_sha1sum</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/account">foaf:account</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/yahooChatID">foaf:yahooChatID</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/made">foaf:made</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/jabberID">foaf:jabberID</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/age">foaf:age</a><sup class="sup-fp" title="functional property">fp</sup><br /><a href="http://xmlns.com/foaf/0.1/holdsAccount">foaf:holdsAccount</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/icqChatID">foaf:icqChatID</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/aimChatID">foaf:aimChatID</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/birthday">foaf:birthday</a><sup class="sup-fp" title="functional property">fp</sup><br /><a href="http://xmlns.com/foaf/0.1/skypeID">foaf:skypeID</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/topic_interest">foaf:topic_interest</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/weblog">foaf:weblog</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/status">foaf:status</a><sup class="sup-dp" title="datatype property">dp</sup><br />
In range of |<a href="http://xmlns.com/foaf/0.1/member">foaf:member</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/maker">foaf:maker</a><sup class="sup-op" title="object property">op</sup><br />
### Document <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Document`
Description | A document.
In domain of |<a href="http://xmlns.com/foaf/0.1/topic">foaf:topic</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/sha1">foaf:sha1</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/primaryTopic">foaf:primaryTopic</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="http://xmlns.com/foaf/0.1/tipjar">foaf:tipjar</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/isPrimaryTopicOf">foaf:isPrimaryTopicOf</a><br /><a href="http://xmlns.com/foaf/0.1/homepage">foaf:homepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/interest">foaf:interest</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/workplaceHomepage">foaf:workplaceHomepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/workInfoHomepage">foaf:workInfoHomepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/accountServiceHomepage">foaf:accountServiceHomepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/page">foaf:page</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/weblog">foaf:weblog</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/publications">foaf:publications</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/openid">foaf:openid</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/schoolHomepage">foaf:schoolHomepage</a><sup class="sup-op" title="object property">op</sup><br />
### Group <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Group`
Description | A class of Agents.
Super-classes |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
In domain of |<a href="http://xmlns.com/foaf/0.1/member">foaf:member</a><sup class="sup-op" title="object property">op</sup><br />
### Image <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Image`
Description | An image.
Super-classes |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
In domain of |<a href="http://xmlns.com/foaf/0.1/thumbnail">foaf:thumbnail</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/depicts">foaf:depicts</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="http://xmlns.com/foaf/0.1/depiction">foaf:depiction</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/thumbnail">foaf:thumbnail</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/img">foaf:img</a><sup class="sup-op" title="object property">op</sup><br />
### Label Property <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/LabelProperty`
Description | A foaf:LabelProperty is any RDF property with texual values that serve as labels.
### Online Account <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/OnlineAccount`
Description | An online account.
Super-classes |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |<a href="http://xmlns.com/foaf/0.1/OnlineGamingAccount">foaf:OnlineGamingAccount</a><sup class="sup-c" title="class">c</sup><br /><a href="http://xmlns.com/foaf/0.1/OnlineEcommerceAccount">foaf:OnlineEcommerceAccount</a><sup class="sup-c" title="class">c</sup><br /><a href="http://xmlns.com/foaf/0.1/OnlineChatAccount">foaf:OnlineChatAccount</a><sup class="sup-c" title="class">c</sup><br />
In domain of |<a href="http://xmlns.com/foaf/0.1/accountServiceHomepage">foaf:accountServiceHomepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/accountName">foaf:accountName</a><sup class="sup-dp" title="datatype property">dp</sup><br />
In range of |<a href="http://xmlns.com/foaf/0.1/holdsAccount">foaf:holdsAccount</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/account">foaf:account</a><sup class="sup-op" title="object property">op</sup><br />
### Online Chat Account <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/OnlineChatAccount`
Description | An online chat account.
Super-classes |<a href="http://xmlns.com/foaf/0.1/OnlineAccount">foaf:OnlineAccount</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Online E-commerce Account <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/OnlineEcommerceAccount`
Description | An online e-commerce account.
Super-classes |<a href="http://xmlns.com/foaf/0.1/OnlineAccount">foaf:OnlineAccount</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Online Gaming Account <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/OnlineGamingAccount`
Description | An online gaming account.
Super-classes |<a href="http://xmlns.com/foaf/0.1/OnlineAccount">foaf:OnlineAccount</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Organization <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Organization`
Description | An organization.
Super-classes |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Person <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Person`
Description | A person.
Super-classes |<a href="http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing">http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing</a><sup class="sup-c" title="class">c</sup><br /><a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
In domain of |<a href="http://xmlns.com/foaf/0.1/publications">foaf:publications</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/currentProject">foaf:currentProject</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/firstName">foaf:firstName</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/workplaceHomepage">foaf:workplaceHomepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/workInfoHomepage">foaf:workInfoHomepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/myersBriggs">foaf:myersBriggs</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/geekcode">foaf:geekcode</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/knows">foaf:knows</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/img">foaf:img</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/surname">foaf:surname</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/schoolHomepage">foaf:schoolHomepage</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/plan">foaf:plan</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/lastName">foaf:lastName</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/familyName">foaf:familyName</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/family_name">foaf:family_name</a><sup class="sup-dp" title="datatype property">dp</sup><br /><a href="http://xmlns.com/foaf/0.1/pastProject">foaf:pastProject</a><sup class="sup-op" title="object property">op</sup><br />
In range of |<a href="http://xmlns.com/foaf/0.1/knows">foaf:knows</a><sup class="sup-op" title="object property">op</sup><br />
### PersonalProfileDocument <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/PersonalProfileDocument`
Description | A personal profile RDF document.
Super-classes |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Project <sup>c</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/Project`
Description | A project (a collective endeavour of some kind).

## Object Properties
[account](account),
[account service homepage](accountservicehomepage),
[based near](basednear),
[current project](currentproject),
[depiction](depiction),
[depicts](depicts),
[focus](focus),
[funded by](fundedby),
[account](holdsAccount),
[homepage](homepage),
[image](image),
[interest](interest),
[knows](knows),
[logo](logo),
[made](made),
[maker](maker),
[personal mailbox](personalmailbox),
[member](member),
[openid](openid),
[page](page),
[past project](pastproject),
[phone](phone),
[primary topic](primarytopic),
[publications](publications),
[schoolHomepage](schoolHomepage),
[theme](theme),
[thumbnail](thumbnail),
[tipjar](tipjar),
[topic](topic),
[topic_interest](topic_interest),
[weblog](weblog),
[work info homepage](workinfohomepage),
[workplace homepage](workplacehomepage),
[](account)
### account <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/account`
Description | Indicates an account held by this agent.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/OnlineAccount">foaf:OnlineAccount</a><sup class="sup-c" title="class">c</sup><br />
[](accountservicehomepage)
### account service homepage <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/accountServiceHomepage`
Description | Indicates a homepage of the service provide for this online account.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/OnlineAccount">foaf:OnlineAccount</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](basednear)
### based near <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/based_near`
Description | A location that something is based near, for some broadly human notion of near.
Domain(s) |<a href="http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing">http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing">http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing</a><sup class="sup-c" title="class">c</sup><br />
[](currentproject)
### current project <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/currentProject`
Description | A current project this person works on.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](depiction)
### depiction <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/depiction`
Description | A depiction of some thing.
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Image">foaf:Image</a><sup class="sup-c" title="class">c</sup><br />
[](depicts)
### depicts <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/depicts`
Description | A thing depicted in this representation.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Image">foaf:Image</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](focus)
### focus <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/focus`
Description | The underlying or 'focal' entity associated with some SKOS-described concept.
Domain(s) |<a href="http://www.w3.org/2004/02/skos/core#Concept">http://www.w3.org/2004/02/skos/core#Concept</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](fundedby)
### funded by <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/fundedBy`
Description | An organization funding a project or person.
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](holdsAccount)
### account <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/holdsAccount`
Description | Indicates an account held by this agent.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/OnlineAccount">foaf:OnlineAccount</a><sup class="sup-c" title="class">c</sup><br />
[](homepage)
### homepage <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/homepage`
Description | A homepage for some thing.
Super-properties |<a href="http://xmlns.com/foaf/0.1/page">foaf:page</a><sup class="sup-op" title="object property">op</sup><br /><a href="http://xmlns.com/foaf/0.1/isPrimaryTopicOf">foaf:isPrimaryTopicOf</a><br />
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](image)
### image <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/img`
Description | An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage).
Super-properties |<a href="http://xmlns.com/foaf/0.1/depiction">foaf:depiction</a><sup class="sup-op" title="object property">op</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Image">foaf:Image</a><sup class="sup-c" title="class">c</sup><br />
[](interest)
### interest <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/interest`
Description | A page about a topic of interest to this person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](knows)
### knows <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/knows`
Description | A person known by this person (indicating some level of reciprocated interaction between the parties).
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
[](logo)
### logo <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/logo`
Description | A logo representing some thing.
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](made)
### made <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/made`
Description | Something that was made by this agent.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](maker)
### maker <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/maker`
Description | An agent that  made this thing.
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](personalmailbox)
### personal mailbox <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/mbox`
Description | A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](member)
### member <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/member`
Description | Indicates a member of a Group
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Group">foaf:Group</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
[](openid)
### openid <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/openid`
Description | An OpenID for an Agent.
Super-properties |<a href="http://xmlns.com/foaf/0.1/isPrimaryTopicOf">foaf:isPrimaryTopicOf</a><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](page)
### page <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/page`
Description | A page or document about this thing.
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](pastproject)
### past project <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/pastProject`
Description | A project this person has previously worked on.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](phone)
### phone <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/phone`
Description | A phone,  specified using fully qualified tel: URI scheme (refs: http://www.w3.org/Addressing/schemes.html#tel).
[](primarytopic)
### primary topic <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/primaryTopic`
Description | The primary topic of some page or document.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](publications)
### publications <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/publications`
Description | A link to the publications of this person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](schoolHomepage)
### schoolHomepage <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/schoolHomepage`
Description | A homepage of a school attended by the person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](theme)
### theme <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/theme`
Description | A theme.
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](thumbnail)
### thumbnail <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/thumbnail`
Description | A derived thumbnail image.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Image">foaf:Image</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Image">foaf:Image</a><sup class="sup-c" title="class">c</sup><br />
[](tipjar)
### tipjar <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/tipjar`
Description | A tipjar document for this agent, describing means for payment and reward.
Super-properties |<a href="http://xmlns.com/foaf/0.1/page">foaf:page</a><sup class="sup-op" title="object property">op</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](topic)
### topic <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/topic`
Description | A topic of some page or document.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](topic_interest)
### topic_interest <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/topic_interest`
Description | A thing of interest to this person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
[](weblog)
### weblog <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/weblog`
Description | A weblog of some thing (whether person, group, company etc.).
Super-properties |<a href="http://xmlns.com/foaf/0.1/page">foaf:page</a><sup class="sup-op" title="object property">op</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](workinfohomepage)
### work info homepage <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/workInfoHomepage`
Description | A work info homepage of some person; a page about their work for some organization.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](workplacehomepage)
### workplace homepage <sup>op</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/workplaceHomepage`
Description | A workplace homepage of some person; the homepage of an organization they work for.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />

## Functional Properties
[age](age),
[birthday](birthday),
[gender](gender),
[](age)
### age <sup>fp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/age`
Description | The age in years of some agent.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](birthday)
### birthday <sup>fp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/birthday`
Description | The birthday of this Agent, represented in mm-dd string form, eg. '12-31'.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](gender)
### gender <sup>fp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/gender`
Description | The gender of this Agent (typically but not necessarily 'male' or 'female').
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />

## Datatype Properties
[account name](accountname),
[AIM chat ID](AIMchatID),
[DNA checksum](DNAchecksum),
[familyName](familyName),
[family_name](family_name),
[firstName](firstName),
[geekcode](geekcode),
[Given name](Givenname),
[Given name](givenname),
[ICQ chat ID](ICQchatID),
[jabber ID](jabberID),
[lastName](lastName),
[sha1sum of a personal mailbox URI name](sha1sumofapersonalmailboxURIname),
[MSN chat ID](MSNchatID),
[myersBriggs](myersBriggs),
[name](name),
[nickname](nickname),
[plan](plan),
[sha1sum (hex)](sha1sum(hex)),
[Skype ID](SkypeID),
[status](status),
[Surname](Surname),
[title](title1),
[Yahoo chat ID](YahoochatID),
[](accountname)
### account name <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/accountName`
Description | Indicates the name (identifier) associated with this online account.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/OnlineAccount">foaf:OnlineAccount</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](AIMchatID)
### AIM chat ID <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/aimChatID`
Description | An AIM chat ID
Super-properties |<a href="http://xmlns.com/foaf/0.1/nick">foaf:nick</a><sup class="sup-dp" title="datatype property">dp</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](DNAchecksum)
### DNA checksum <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/dnaChecksum`
Description | A checksum for the DNA of some thing. Joke.
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](familyName)
### familyName <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/familyName`
Description | The family name of some person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](family_name)
### family_name <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/family_name`
Description | The family name of some person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](firstName)
### firstName <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/firstName`
Description | The first name of a person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](geekcode)
### geekcode <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/geekcode`
Description | A textual geekcode for this person, see http://www.geekcode.com/geek.html
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](Givenname)
### Given name <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/givenName`
Description | The given name of some person.
[](givenname)
### Given name <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/givenname`
Description | The given name of some person.
[](ICQchatID)
### ICQ chat ID <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/icqChatID`
Description | An ICQ chat ID
Super-properties |<a href="http://xmlns.com/foaf/0.1/nick">foaf:nick</a><sup class="sup-dp" title="datatype property">dp</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](jabberID)
### jabber ID <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/jabberID`
Description | A jabber ID for something.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](lastName)
### lastName <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/lastName`
Description | The last name of a person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](sha1sumofapersonalmailboxURIname)
### sha1sum of a personal mailbox URI name <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/mbox_sha1sum`
Description | The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](MSNchatID)
### MSN chat ID <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/msnChatID`
Description | An MSN chat ID
Super-properties |<a href="http://xmlns.com/foaf/0.1/nick">foaf:nick</a><sup class="sup-dp" title="datatype property">dp</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](myersBriggs)
### myersBriggs <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/myersBriggs`
Description | A Myers Briggs (MBTI) personality classification.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](name)
### name <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/name`
Description | A name for some thing.
Super-properties |<a href="http://www.w3.org/2000/01/rdf-schema#label">rdfs:label</a><br />
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](nickname)
### nickname <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/nick`
Description | A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).
[](plan)
### plan <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/plan`
Description | A .plan comment, in the tradition of finger and '.plan' files.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](sha1sum(hex))
### sha1sum (hex) <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/sha1`
Description | A sha1sum hash, in hex.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />
[](SkypeID)
### Skype ID <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/skypeID`
Description | A Skype ID
Super-properties |<a href="http://xmlns.com/foaf/0.1/nick">foaf:nick</a><sup class="sup-dp" title="datatype property">dp</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](status)
### status <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/status`
Description | A string expressing what the user is happy for the general public (normally) to know about their current activity.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](Surname)
### Surname <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/surname`
Description | The surname of some person.
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](title1)
### title <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/title`
Description | Title (Mr, Mrs, Ms, Dr. etc)
[](YahoochatID)
### Yahoo chat ID <sup>dp</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/yahooChatID`
Description | A Yahoo chat ID
Super-properties |<a href="http://xmlns.com/foaf/0.1/nick">foaf:nick</a><sup class="sup-dp" title="datatype property">dp</sup><br />
Domain(s) |<a href="http://xmlns.com/foaf/0.1/Agent">foaf:Agent</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />

## Annotation Properties
[date](date),
[description](description),
[title](title),
[term_status](term_status),
[membershipClass](membershipClass),
[assurance](assurance),
[src_assurance](src_assurance),
[](date)
### date <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/date`
[](description)
### description <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/description`
[](title)
### title <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://purl.org/dc/elements/1.1/title`
[](term_status)
### term_status <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://www.w3.org/2003/06/sw-vocab-status/ns#term_status`
[](membershipClass)
### membershipClass <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/membershipClass`
Description | Indicates the class of individuals that are a member of a Group
[](assurance)
### assurance <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/wot/0.1/assurance`
[](src_assurance)
### src_assurance <sup>ap</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/wot/0.1/src_assurance`

## Properties
[is primary topic of](isprimarytopicof),
[](isprimarytopicof)
### is primary topic of <sup>p</sup>
Property | Value
--- | ---
IRI | `http://xmlns.com/foaf/0.1/isPrimaryTopicOf`
Description | A document that this thing is the primary topic of.
Super-properties |<a href="http://xmlns.com/foaf/0.1/page">foaf:page</a><sup class="sup-op" title="object property">op</sup><br />
Domain(s) |<a href="http://www.w3.org/2002/07/owl#Thing">owl:Thing</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Document">foaf:Document</a><sup class="sup-c" title="class">c</sup><br />

## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **vs**
  * `http://www.w3.org/2003/06/sw-vocab-status/ns#`
* **wot**
  * `http://xmlns.com/wot/0.1/`
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