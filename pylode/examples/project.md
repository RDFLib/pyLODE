Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# A Project ontology

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/project`
* **Creators(s)**
  * [None](https://orcid.org/0000-0002-3884-3420)
    [[ORCID]](https://orcid.org/0000-0002-3884-3420)
* **Contributor(s)**
  * Peter Brenton, CSIRO
* **Created**
  * 2017-08-14
* **Modified**
  * 2020-04-24
* **Imports**
  * [dct:](http://purl.org/dc/terms/)
  * [http://www.w3.org/2004/02/skos/core](http://www.w3.org/2004/02/skos/core)
  * [http://www.w3.org/ns/prov](http://www.w3.org/ns/prov)
  * [https://www.w3.org/ns/dx/prof](https://www.w3.org/ns/dx/prof)
* **License**
  * [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
* **Ontology RDF**
  * RDF ([project.ttl](turtle))
### Description
<p>The PROJECT ontology is designed to enable publication of information describing projects, including research projects. It is not designed to support project management, though sub-activities are included. As far as possible PROJECT is intended to be domain-neutral, and it is expected that domains and applications will specialize or extend this ontology for more specific purposes.</p>
<p>The ontology gives terms to support the representation of:</p>
<ul>
<li>project planning, funding, goals</li>
<li>project stakeholders and relationships</li>
<li>project activities and timeline</li>
</ul>
<p>One specialization is included - the <strong>Research Project</strong> - which has been the subject of several predecessor designs that have informed the design of this ontology.</p>
<p>PROJECT extends the W3C PROV-O ontology. Otherwise, it has no dependencies except for the normal RDF/OWL infrastructure (RDF [rdf11-concepts], RDFS [rdf-schema], OWL [owl2-quick-reference]), Dublin Core [dc-terms] for some ontology metadata, and SKOS [skos-reference] to support some relationships between Role values, and project classification.</p>
<p>A summary of the main classes and relationships in PROJECT is shown in the diagram below, including the key superclass <code>prov:Activity</code>.</p>
<p><img alt="summary of PROJECT ontology" src="../images/Project-overview.png" /></p>
<p>Core classes from PROJECT vocabulary.</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Funding association](#Fundingassociation),
[Project](#Project),
[Research Project](#ResearchProject),
[Sum of money](#Sumofmoney),
### Funding association
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#FundingAssociation`
Description | <p>Association to a funder and a sum of money</p> <p><img alt="Project funding association" src="../images/Project-funding.png" /></p>
Example | `ex:FA3`<br />`  rdf:type proj:FundingAssociation ;`<br />`  rdfs:label "Level crossing removal project phase 1 funding arrangement" ;`<br />`  rdfs:seeAlso <http://www.premier.vic.gov.au/contract-awarded-for-first-four-level-crossing-removals/> ;`<br />`  proj:fundsProvided [`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`  ] ;`<br />`  prov:agent <http://www.vic.gov.au/> ;`<br />` .`<br />
Super-classes |[prov:Association](http://www.w3.org/ns/prov#Association) (c)<br />
Restrictions |[http://linked.data.gov.au/def/project#fundsProvided](http://linked.data.gov.au/def/project#fundsProvided) (op) **min** 1<br />[prov:agent](http://www.w3.org/ns/prov#agent) **exactly** 1<br />[prov:hadRole](http://www.w3.org/ns/prov#hadRole) **value** [http://linked.data.gov.au/def/project/Funder](http://linked.data.gov.au/def/project/Funder) (c)<br />
In domain of |[http://linked.data.gov.au/def/project#fundingScheme](http://linked.data.gov.au/def/project#fundingScheme) (op)<br />[http://linked.data.gov.au/def/project#grantNumber](http://linked.data.gov.au/def/project#grantNumber) (dp)<br />
In range of |[http://linked.data.gov.au/def/project#wasFundedThrough](http://linked.data.gov.au/def/project#wasFundedThrough) (op)<br />
### Project
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#Project`
Description | <p>A Project is a planned activity with a budget, a sponsor, and a leader.</p> <p>Project stakeholders are indicated using <code>prov:wasAssociatedWith</code> or the <code>prov:qualifiedAssociation</code> structure which allows their role to be catpured. Some special stakeholders have specific sub-properties with the roles fixed, including project-leader, project-participant, and project-funder.</p> <p>Activities within a project are indicated using the <code>proj:hasSubActivity</code> (simple) or <code>proj:subActivityAssociation</code> properties - the latter allowing the nature of the relationshp to be described as well.</p> <p><img alt="Project details" src="../images/Project.png" /></p>
Example | `ex:Project1`<br />`rdf:type proj:Project ;`<br />`rdfs:label "Victoria level-crossing removal - phase 1" ;`<br />`proj:hadBudgetTotal [`<br />`  rdf:type proj:SumOfMoney ;`<br />`  rdfs:label "Level crossing removal phase 1 budget" ;`<br />`  proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`  proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`] ;`<br />`proj:hadLeader ex:johnholland-kbr ;`<br />`proj:hadSponsor <http://levelcrossings.vic.gov.au/about/about-the-authority> ;`<br />`proj:hadSubActivity ex:BentleighLevelCrossingRemoval ;`<br />`proj:hadSubActivity ex:BurkeRoadLevelCrossingRemoval ;`<br />`proj:hadSubActivity ex:McKinnonRoadLevelCrossingRemoval ;`<br />`proj:hadSubActivity ex:NorthRoadLevelCrossingRemoval ;`<br />`proj:wasFundedThrough [`<br />`  rdf:type proj:FundingAssociation ;`<br />`  rdfs:label "Level crossing removal project phase 1 funding arrangement" ;`<br />`  rdfs:seeAlso <http://www.premier.vic.gov.au/contract-awarded-for-first-four-level-crossing-removals/> ;`<br />`  proj:fundsProvided [`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`  ] ;`<br />`  prov:agent <http://www.vic.gov.au/> ;`<br />`] ;`<br />`rdfs:label "Victoria level-crossing removal - phase 1" ;`<br />`proj:plannedEnd "2017-03-31"^^xsd:date ;`<br />`proj:plannedStart "2015-10-01"^^xsd:date ;`<br />`prov:atLocation <https://dbpedia.org/resource/Melbourne> ;`<br />`prov:endedAtTime "2016-10-31T00:00:00"^^xsd:dateTime ;`<br />`prov:startedAtTime "2015-10-01T00:00:00"^^xsd:dateTime ;`<br />`.`<br />
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Restrictions |[http://linked.data.gov.au/def/project#plannedEnd](http://linked.data.gov.au/def/project#plannedEnd) (dp) **exactly** 1<br />[http://linked.data.gov.au/def/project#hadSponsor](http://linked.data.gov.au/def/project#hadSponsor) (op) **min** 1<br />[http://linked.data.gov.au/def/project#hadPlan](http://linked.data.gov.au/def/project#hadPlan) (op) **min** 1<br />[http://linked.data.gov.au/def/project#plannedStart](http://linked.data.gov.au/def/project#plannedStart) (dp) **exactly** 1<br />[http://linked.data.gov.au/def/project#hadLeader](http://linked.data.gov.au/def/project#hadLeader) (op) **min** 1<br />[http://linked.data.gov.au/def/project#hadBudgetTotal](http://linked.data.gov.au/def/project#hadBudgetTotal) (op) **exactly** 1<br />
Sub-classes |[http://linked.data.gov.au/def/project#ResearchProject](http://linked.data.gov.au/def/project#ResearchProject) (c)<br />
In domain of |[http://linked.data.gov.au/def/project#hadBudgetTotal](http://linked.data.gov.au/def/project#hadBudgetTotal) (op)<br />[http://linked.data.gov.au/def/project#hadAreaOfInterest](http://linked.data.gov.au/def/project#hadAreaOfInterest) (op)<br />[http://linked.data.gov.au/def/project#hadObjective](http://linked.data.gov.au/def/project#hadObjective) (dp)<br />[http://linked.data.gov.au/def/project#hadPlan](http://linked.data.gov.au/def/project#hadPlan) (op)<br />[http://linked.data.gov.au/def/project#wasFundedThrough](http://linked.data.gov.au/def/project#wasFundedThrough) (op)<br />[http://linked.data.gov.au/def/project#hadSponsor](http://linked.data.gov.au/def/project#hadSponsor) (op)<br />
### Research Project
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#ResearchProject`
Description | <p>A research project is a project that has</p> <ul> <li>one or more PIs who are individual persons, and</li> <li>should be classified according to standard research classification, such as the Australian Bureau of Statistics ANZSRC-FOR or NASA's Global Change Master Directory - Science Keywords.</li> </ul>
Example | `ex:Project2`<br />`rdf:type proj:Project ;`<br />`rdf:type proj:ResearchProject ;`<br />`rdfs:label "Improved management of feral animals in remote tropical Australia" ;`<br />`proj:budgetTotal [`<br />`  rdf:type proj:SumOfMoney ;`<br />`  proj:moneyAmount 0 ;`<br />`  proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`] ;`<br />`proj:hadFieldOfResearch <http://purl.org/au-research/vocabulary/anzsrc-for/2008/050202> ;`<br />`proj:hadPrincipalInvestigator <http://orcid.org/0000-0002-5823-7364> ;`<br />`proj:hadSponsor <http://dbpedia.org/resource/Commonwealth_Scientific_and_Industrial_Research_Organisation> ;`<br />`proj:hadSubActivity ex:Aerial ;`<br />`proj:wasSubActivityOf <http://www.environment.gov.au/science/nesp> ;`<br />`rdfs:label "Improved management of feral animals in remote tropical Australia" ;`<br />`proj:hadObjective "To develop a robust understanding of the costs and benefits of selected feral animal control programs on reducing impacts to natural and cultural values." ;`<br />`proj:plannedEnd "2022-12-31"^^xsd:date ;`<br />`proj:plannedStart "2012-12-31"^^xsd:date ;`<br />`proj:projectParticipant <mailto:peter.brenton@csiro.au> ;`<br />`proj:hadPlan ex:FCY-project-plan ;`<br />`proj:wasFundedThrough [`<br />`  rdf:type proj:FundingAssociation ;`<br />`  proj:fundsProvided [`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount 0 ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`  ] ;`<br />`  prov:agent <http://dbpedia.org/resource/Government_of_Australia> ;`<br />`] ;`<br />`prov:atLocation <http://dbpedia.org/resource/Archer_River,_Queensland> ;`<br />`prov:generated <https://doi.org/10.1071/WF15133> ;`<br />`prov:startedAtTime "2012-12-31T00:00:00"^^xsd:dateTime ;`<br />`.`<br />
Super-classes |[http://linked.data.gov.au/def/project#Project](http://linked.data.gov.au/def/project#Project) (c)<br />
Restrictions |[http://linked.data.gov.au/def/project#hadFieldOfResearch](http://linked.data.gov.au/def/project#hadFieldOfResearch) (op) **min** 1<br />
In domain of |[http://linked.data.gov.au/def/project#hadFieldOfResearch](http://linked.data.gov.au/def/project#hadFieldOfResearch) (op)<br />[http://linked.data.gov.au/def/project#hadPrincipalInvestigator](http://linked.data.gov.au/def/project#hadPrincipalInvestigator) (op)<br />
### Sum of money
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#SumOfMoney`
Description | <p>A sum of money, expressed as an amount and a specified currency</p>
Example | `ex:SM4`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />` .`<br />
Super-classes |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (c)<br />
Restrictions |[http://linked.data.gov.au/def/project#moneyCurrency](http://linked.data.gov.au/def/project#moneyCurrency) (op) **exactly** 1<br />[http://linked.data.gov.au/def/project#moneyAmount](http://linked.data.gov.au/def/project#moneyAmount) (dp) **exactly** 1<br />
In domain of |[http://linked.data.gov.au/def/project#moneyAmount](http://linked.data.gov.au/def/project#moneyAmount) (dp)<br />[http://linked.data.gov.au/def/project#moneyCurrency](http://linked.data.gov.au/def/project#moneyCurrency) (op)<br />
In range of |[http://linked.data.gov.au/def/project#hadBudgetTotal](http://linked.data.gov.au/def/project#hadBudgetTotal) (op)<br />[http://linked.data.gov.au/def/project#fundsProvided](http://linked.data.gov.au/def/project#fundsProvided) (op)<br />

## Object Properties
[pointer to funding-scheme](#pointertofunding-scheme),
[funding provided](#fundingprovided),
[has area of interest](#hasareaofinterest),
[total project budget](#totalprojectbudget),
[field of research](#fieldofresearch),
[leader](#leader),
[Project plan](#Projectplan),
[principal investigator](#principalinvestigator),
[had related activity](#hadrelatedactivity),
[activity sponsor](#activitysponsor),
[has sub-activity](#hassub-activity),
[currency of a sum of money](#currencyofasumofmoney),
[had funding association](#hadfundingassociation),
[is sub-activity of](#issub-activityof),
[](pointertofunding-scheme)
### pointer to funding-scheme
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#fundingScheme`
Description |  Link to description of funding scheme, e.g.  - [European Commission Horizon 2020](https://ec.europa.eu/programmes/horizon2020/) - [Australian National Collaborative Research Infrastructure Strategy](https://www.education.gov.au/national-collaborative-research-infrastructure-strategy-ncris) 
Domain(s) |[http://linked.data.gov.au/def/project#FundingAssociation](http://linked.data.gov.au/def/project#FundingAssociation) (c)<br />
[](fundingprovided)
### funding provided
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#fundsProvided`
Description | Link to a sum of money.
Range(s) |[http://linked.data.gov.au/def/project#SumOfMoney](http://linked.data.gov.au/def/project#SumOfMoney) (c)<br />
[](hasareaofinterest)
### has area of interest
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadAreaOfInterest`
Description |  Address, place, locality, location, etc 
Super-properties |[prov:atLocation](http://www.w3.org/ns/prov#atLocation)<br />
Domain(s) |[http://linked.data.gov.au/def/project#Project](http://linked.data.gov.au/def/project#Project) (c)<br />
Range(s) |[dct:Location](http://purl.org/dc/terms/Location) (c)<br />
[](totalprojectbudget)
### total project budget
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadBudgetTotal`
Description |  Basic funding arrangements are captured through the `proj:hadSponsor` and `proj:hadBudgetTotal` properties.  More complex arrangements, for example if multiple funders are involved, can be captured through the `proj:wasFundedThrough` property, which links a funding agent with a funding amount in the context of a project. 
Domain(s) |[http://linked.data.gov.au/def/project#Project](http://linked.data.gov.au/def/project#Project) (c)<br />
Range(s) |[http://linked.data.gov.au/def/project#SumOfMoney](http://linked.data.gov.au/def/project#SumOfMoney) (c)<br />
[](fieldofresearch)
### field of research
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadFieldOfResearch`
Description |  The field of research of the research project. 
Scope Notes | The value is usually taken from a curated vocabulary, such as [ANZSRC Fields of Research](http://www.abs.gov.au/ausstats/abs@.nsf/0/6BB427AB9696C225CA2574180004463E), [Re3data subjects](http://www.re3data.org/browse/by-subject/), [EDAM Topic](http://edamontology.org/topic_0003) or [Scigraph subjects](https://github.com/springernature/scigraph/wiki)
Super-properties |[dct:subject](http://purl.org/dc/terms/subject)<br />
Domain(s) |[http://linked.data.gov.au/def/project#ResearchProject](http://linked.data.gov.au/def/project#ResearchProject) (c)<br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />
[](leader)
### leader
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadLeader`
Description |  There are a number of distinctive stakeholders in a project, in particular: a leader who is accountable for the delivery of project outcomes; a sponsor under whose authority the project is undertaken; funders; and project staff or participants. In some cases it is useful to provide specific details of a participant's role in the project. PROJECT provides a number of ways to represent the relationships of stakeholders to projects and activities.  The standard role of _leader_ is implemented as a directly named property from an `prov:Activity` to a `prov:Agent`, and _sponsor_ as a directly named property from a `proj:Project` to a `prov:Agent`.  We distinguish one sub-class, the `proj:ResearchProject`, in which the leader(s) is known as a _Principal Investigator_, and which is classified according to its _field of research_.  
Super-properties |[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />
Range(s) |[prov:Person](http://www.w3.org/ns/prov#Person) (c)<br />
[](Projectplan)
### Project plan
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadPlan`
Description | The project plan.
Super-properties |[prov:used](http://www.w3.org/ns/prov#used)<br />
Domain(s) |[http://linked.data.gov.au/def/project#Project](http://linked.data.gov.au/def/project#Project) (c)<br />
Range(s) |[prov:Plan](http://www.w3.org/ns/prov#Plan) (c)<br />
[](principalinvestigator)
### principal investigator
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadPrincipalInvestigator`
Description |  The person who acts as principal investigator on the research project. 
Super-properties |[http://linked.data.gov.au/def/project#hadLeader](http://linked.data.gov.au/def/project#hadLeader) (op)<br />
Domain(s) |[http://linked.data.gov.au/def/project#ResearchProject](http://linked.data.gov.au/def/project#ResearchProject) (c)<br />
[](hadrelatedactivity)
### had related activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadRelatedActivity`
Description |  Link from an activity to a related activity. 
Super-properties |[prov:qualifiedInfluence](http://www.w3.org/ns/prov#qualifiedInfluence)<br />
Domain(s) |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Range(s) |[prov:ActivityInfluence](http://www.w3.org/ns/prov#ActivityInfluence) (c)<br />
[](activitysponsor)
### activity sponsor
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadSponsor`
Description |  There are a number of distinctive stakeholders in a project, in particular: a leader who is accountable for the delivery of project outcomes; a sponsor under whose authority the project is undertaken; funders; and project staff or participants. In some cases it is useful to provide specific details of a participant's role in the project. PROJECT provides a number of ways to represent the relationships of stakeholders to projects and activities.  Basic funding arrangements are captured through the `proj:hadSponsor` and `proj:hadBudgetTotal` properties. More complex arrangements, for example if multiple funders are involved, can be captured through the `proj:wasFundedThrough` property, which links a funding agent with a funding amount in the context of a project.  ![Project funding association](../images/Project-funding.png)  
Super-properties |[prov:wasAssociatedWith](http://www.w3.org/ns/prov#wasAssociatedWith)<br />
Domain(s) |[http://linked.data.gov.au/def/project#Project](http://linked.data.gov.au/def/project#Project) (c)<br />
[](hassub-activity)
### has sub-activity
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadSubActivity`
Description |  Relationship from an activity to a subsidiary activity. 
Domain(s) |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Range(s) |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
[](currencyofasumofmoney)
### currency of a sum of money
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#moneyCurrency`
Domain(s) |[http://linked.data.gov.au/def/project#SumOfMoney](http://linked.data.gov.au/def/project#SumOfMoney) (c)<br />
[](hadfundingassociation)
### had funding association
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#wasFundedThrough`
Description |  Basic funding arrangements are captured through the `proj:hadSponsor` and `proj:hadBudgetTotal` properties. More complex arrangements, for example if multiple funders are involved, can be captured through the `proj:wasFundedThrough` property, which links a funding agent with a funding amount in the context of a project.  ![Project funding association](../images/Project-funding.png)  
Domain(s) |[http://linked.data.gov.au/def/project#Project](http://linked.data.gov.au/def/project#Project) (c)<br />
Range(s) |[http://linked.data.gov.au/def/project#FundingAssociation](http://linked.data.gov.au/def/project#FundingAssociation) (c)<br />
[](issub-activityof)
### is sub-activity of
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#wasSubActivityOf`
Description |  Relationship from an activity to its parent activity or project. 
Super-properties |[prov:wasInformedBy](http://www.w3.org/ns/prov#wasInformedBy)<br />

## Datatype Properties
[grant or contract number](#grantorcontractnumber),
[project objective](#projectobjective),
[Money amount](#Moneyamount),
[planned end-date|time](#plannedend-date|time),
[planned start-date|time](#plannedstart-date|time),
[](grantorcontractnumber)
### grant or contract number
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#grantNumber`
Description | The grant or contract number assigned to the funding arrangement by the funder.  'Grant number' is common for research or charitable projects, 'Contract number' in a commercial context.
Domain(s) |[http://linked.data.gov.au/def/project#FundingAssociation](http://linked.data.gov.au/def/project#FundingAssociation) (c)<br />
Range(s) |[xsd:string](http://www.w3.org/2001/XMLSchema#string) (c)<br />
[](projectobjective)
### project objective
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#hadObjective`
Description | Textual description of project objective.
Domain(s) |[http://linked.data.gov.au/def/project#Project](http://linked.data.gov.au/def/project#Project) (c)<br />
[](Moneyamount)
### Money amount
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#moneyAmount`
Description | Numeric value of a sum of money, which must be scaled by a specified currency to get the actual value
Domain(s) |[http://linked.data.gov.au/def/project#SumOfMoney](http://linked.data.gov.au/def/project#SumOfMoney) (c)<br />
Range(s) |[xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) (c)<br />
[](plannedend-date|time)
### planned end-date|time
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#plannedEnd`
Description | The date and time at which an activity was planned to end. See also project:plannedStart.
Scope Notes | Usually an xsd:date or xsd:dateTime
[](plannedstart-date|time)
### planned start-date|time
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/project#plannedStart`
Description | The date and time at which an activity was planned to start. See also project:plannedEnd.
Scope Notes | Usually an xsd:date or xsd:dateTime

## Named Individuals
## Namespaces
* **dct**
  * `http://purl.org/dc/terms/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prof**
  * `http://www.w3.org/ns/dx/prof/`
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