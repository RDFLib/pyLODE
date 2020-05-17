# A Project ontology
### A taxonomy

Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)

## Metadata
* **IRI**
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
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes

### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/project#FundingAssociation`
Preferred Labels |Funding association (None)<br />
Examples |`ex:FA3`<br />`  rdf:type proj:FundingAssociation ;`<br />`  rdfs:label "Level crossing removal project phase 1 funding arrangement" ;`<br />`  rdfs:seeAlso <http://www.premier.vic.gov.au/contract-awarded-for-first-four-level-crossing-removals/> ;`<br />`  proj:fundsProvided [`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`  ] ;`<br />`  prov:agent <http://www.vic.gov.au/> ;`<br />` .`<br /><br />
Broader Concepts |[prov:Association](http://www.w3.org/ns/prov#Association) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/project#Project`
Preferred Labels |Project (None)<br />
Examples |`ex:Project1`<br />`rdf:type proj:Project ;`<br />`rdfs:label "Victoria level-crossing removal - phase 1" ;`<br />`proj:hadBudgetTotal [`<br />`  rdf:type proj:SumOfMoney ;`<br />`  rdfs:label "Level crossing removal phase 1 budget" ;`<br />`  proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`  proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`] ;`<br />`proj:hadLeader ex:johnholland-kbr ;`<br />`proj:hadSponsor <http://levelcrossings.vic.gov.au/about/about-the-authority> ;`<br />`proj:hadSubActivity ex:BentleighLevelCrossingRemoval ;`<br />`proj:hadSubActivity ex:BurkeRoadLevelCrossingRemoval ;`<br />`proj:hadSubActivity ex:McKinnonRoadLevelCrossingRemoval ;`<br />`proj:hadSubActivity ex:NorthRoadLevelCrossingRemoval ;`<br />`proj:wasFundedThrough [`<br />`  rdf:type proj:FundingAssociation ;`<br />`  rdfs:label "Level crossing removal project phase 1 funding arrangement" ;`<br />`  rdfs:seeAlso <http://www.premier.vic.gov.au/contract-awarded-for-first-four-level-crossing-removals/> ;`<br />`  proj:fundsProvided [`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`  ] ;`<br />`  prov:agent <http://www.vic.gov.au/> ;`<br />`] ;`<br />`rdfs:label "Victoria level-crossing removal - phase 1" ;`<br />`proj:plannedEnd "2017-03-31"^^xsd:date ;`<br />`proj:plannedStart "2015-10-01"^^xsd:date ;`<br />`prov:atLocation <https://dbpedia.org/resource/Melbourne> ;`<br />`prov:endedAtTime "2016-10-31T00:00:00"^^xsd:dateTime ;`<br />`prov:startedAtTime "2015-10-01T00:00:00"^^xsd:dateTime ;`<br />`.`<br /><br />
Broader Concepts |[prov:Activity](http://www.w3.org/ns/prov#Activity) (cp)<br />
Narrower Concepts |[proj:ResearchProject](http://linked.data.gov.au/def/project#ResearchProject) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/project#ResearchProject`
Preferred Labels |Research Project (None)<br />
Examples |`ex:Project2`<br />`rdf:type proj:Project ;`<br />`rdf:type proj:ResearchProject ;`<br />`rdfs:label "Improved management of feral animals in remote tropical Australia" ;`<br />`proj:budgetTotal [`<br />`  rdf:type proj:SumOfMoney ;`<br />`  proj:moneyAmount 0 ;`<br />`  proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`] ;`<br />`proj:hadFieldOfResearch <http://purl.org/au-research/vocabulary/anzsrc-for/2008/050202> ;`<br />`proj:hadPrincipalInvestigator <http://orcid.org/0000-0002-5823-7364> ;`<br />`proj:hadSponsor <http://dbpedia.org/resource/Commonwealth_Scientific_and_Industrial_Research_Organisation> ;`<br />`proj:hadSubActivity ex:Aerial ;`<br />`proj:wasSubActivityOf <http://www.environment.gov.au/science/nesp> ;`<br />`rdfs:label "Improved management of feral animals in remote tropical Australia" ;`<br />`proj:hadObjective "To develop a robust understanding of the costs and benefits of selected feral animal control programs on reducing impacts to natural and cultural values." ;`<br />`proj:plannedEnd "2022-12-31"^^xsd:date ;`<br />`proj:plannedStart "2012-12-31"^^xsd:date ;`<br />`proj:projectParticipant <mailto:peter.brenton@csiro.au> ;`<br />`proj:hadPlan ex:FCY-project-plan ;`<br />`proj:wasFundedThrough [`<br />`  rdf:type proj:FundingAssociation ;`<br />`  proj:fundsProvided [`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount 0 ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />`  ] ;`<br />`  prov:agent <http://dbpedia.org/resource/Government_of_Australia> ;`<br />`] ;`<br />`prov:atLocation <http://dbpedia.org/resource/Archer_River,_Queensland> ;`<br />`prov:generated <https://doi.org/10.1071/WF15133> ;`<br />`prov:startedAtTime "2012-12-31T00:00:00"^^xsd:dateTime ;`<br />`.`<br /><br />
Broader Concepts |[proj:Project](http://linked.data.gov.au/def/project#Project) (cp)<br />
### None
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/project#SumOfMoney`
Preferred Labels |Sum of money (None)<br />
Examples |`ex:SM4`<br />`    rdf:type proj:SumOfMoney ;`<br />`    proj:moneyAmount "524000000"^^xsd:decimal ;`<br />`    proj:moneyCurrency <https://dbpedia.org/resource/Australian_dollar> ;`<br />` .`<br /><br />
Broader Concepts |[owl:Thing](http://www.w3.org/2002/07/owl#Thing) (cp)<br />

## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/project/`
* **dcterms**
  * `http://purl.org/dc/terms/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prof**
  * `http://www.w3.org/ns/dx/prof/`
* **proj**
  * `http://linked.data.gov.au/def/project#`
* **proji**
  * `http://linked.data.gov.au/def/project/`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `http://schema.org/`
* **sdo1**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Collections: cl
* Concepts: cp