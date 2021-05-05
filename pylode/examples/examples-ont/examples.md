Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.9.1

# Examples Ontology

## Metadata
* **URI**
  * `https://example.com`
* **Publisher(s)**
  * None
* **Creators(s)**
  * [Nicholas J. Car](http://orcid.org/0000-0002-8742-7730)
    [[0000-0002-8742-7730](http://orcid.org/0000-0002-8742-7730)]
* **Contributor(s)**
  * Santa Clause
* **Created**
  * 2021-05-05
* **Modified**
  * 2019-10-21
* **Version Information**
  * 0.9
* **License &amp; Rights**
  * [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
  * &copy; SURROUND Australia Pty Ltd
* **Ontology RDF**
  * RDF ([examples.ttl](turtle))
### Description
This ontology contains several simple classes and properties about animals that are defined only to show off pyLODE's ability to represent different forms of example rendering.

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Datatype Properties](#datatypeproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Creature](#Creature)
[Fish](#Fish)
[Fish food](#Fishfood)
[Food](#Food)
### Creature
Property | Value
--- | ---
URI | `https://example.com#Creature`
Description | A Creature is a living animal
Scope Notes | class with link example
Example(s) |[https://example.com/individuals/creature-x](https://example.com/individuals/creature-x) <br />
Restrictions |[born or hatched date](#bornorhatcheddate) (dp) **exactly** 1<br />
Sub-classes |[Fish](#Fish) (c)<br />
In domain of |[born or hatched date](#bornorhatcheddate) (dp)<br />
### Fish
Property | Value
--- | ---
URI | `https://example.com#Fish`
Description | Fish are aquatic, craniate, gill-bearing animals that lack limbs with digits. They form a sister group to the tunicates, together forming the olfactores. Included in this definition are the living hagfish, lampreys, and cartilaginous and bony fish as well as various extinct related groups. Around 99% of living fish species are ray-finned fish, belonging to the class Actinopterygii, with over 95% belonging to the teleost subgrouping.
Scope Notes | class with example in inline JSON-LD
Example(s) |`{` <br /> `  "@id": "https://example.com#flipper",` <br /> `  "@type": "https://example.com#Fish",` <br /> `  "http://www.w3.org/2004/02/skos/core#definition": "Flipper is the fish that lives in Nick's fish tank",` <br /> `  "http://www.w3.org/2004/02/skos/core#prefLabel": "Flipper the Fish",` <br /> `  "https://example.com#hasScaleColour": {` <br /> `    "@id": "http://example-voc.com/concept/Orange"` <br /> `  },` <br /> `  "https://example.com#livesInFreshWater": true,` <br /> `  "https://example.com#livesInSaltWater": false` <br /> `}` <br /> <br />
Super-classes |[Creature](#Creature) (c)<br />
Restrictions |[eats](#eats) (op) **min** 1<br />[lives in fresh water](#livesinfreshwater) (dp) **exactly** 1<br />[lives in salt water](#livesinsaltwater) (dp) **exactly** 1<br />[lives in estuarine water](#livesinestuarinewater) (dp) **exactly** 1<br />
In domain of |[lives in estuarine water](#livesinestuarinewater) (dp)<br />[lives in fresh water](#livesinfreshwater) (dp)<br />[lives in salt water](#livesinsaltwater) (dp)<br />
### Fish food
Property | Value
--- | ---
URI | `https://example.com#FishFood`
Description | Fish food is food primarily eaten by fish. It may also be eaten by other Creatures too
Scope Notes | class with a local image example
Example(s) |![](fish-food.png) <br />
Super-classes |[Food](#Food) (c)<br />
### Food
Property | Value
--- | ---
URI | `https://example.com#Food`
Description | Food is consumed by Creatures to give them energy
Scope Notes | class with an external URI example
Example(s) |[http://fake.com/thing/food-x](http://fake.com/thing/food-x) <br />
Sub-classes |[Fish food](#Fishfood) (c)<br />
In range of |[eats](#eats) (op)<br />

## Object Properties
[eats](#eats),
[has scale colour](#hasscalecolour),
[](eats)
### eats
Property | Value
--- | ---
URI | `https://example.com#eats`
Description | A creature eats a kind of food
Scope Notes | property with two Resource Descriptor example in same file, conforms to this ontology and something else (http://other.com)
Example(s) |`<x> a :Creature ;` <br /> `    :eats <y> ;` <br /> `.` <br /> `<y> a :Food .` <br /> 

Conforms to: [https://example.com](https://example.com)<br />`<?xml version="1.0" encoding="UTF-8"?>` <br /> `<rdf:RDF` <br /> `   xmlns="https://example.com"` <br /> `   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"` <br /> `>` <br /> `  <rdf:Description rdf:about="file:///Users/nick/Work/rdflib/pyLODE/pylode/examples/examples-ont/y2">` <br /> `    <rdf:type rdf:resource="https://example.comFood"/>` <br /> `  </rdf:Description>` <br /> `  <rdf:Description rdf:about="file:///Users/nick/Work/rdflib/pyLODE/pylode/examples/examples-ont/x2">` <br /> `    <rdf:type rdf:resource="https://example.comCreature"/>` <br /> `    <eats rdf:resource="file:///Users/nick/Work/rdflib/pyLODE/pylode/examples/examples-ont/y2"/>` <br /> `  </rdf:Description>` <br /> `</rdf:RDF>` <br /> 

Conforms to: [https://other.com](https://other.com)<br />
Range(s) |[Food](https://example.com#Food) (c)<br />
[](hasscalecolour)
### has scale colour
Property | Value
--- | ---
URI | `https://example.com#hasScaleColour`
Description | A colour of the fish's scales. Can have multiple colours.
Scope Notes | property with example in inline HTML
Example(s) |<strong><em>scale colour</em></strong>:<ul><li>blue</li><li>orange</li><li>white</li></ul><br />
Range(s) |[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) (c)<br />

## Datatype Properties
[born or hatched date](#bornorhatcheddate),
[lives in estuarine water](#livesinestuarinewater),
[lives in fresh water](#livesinfreshwater),
[lives in salt water](#livesinsaltwater),
[](bornorhatcheddate)
### born or hatched date
Property | Value
--- | ---
URI | `https://example.com#bornOrHatchedDate`
Description | The Gregorian calendar date on which this Creature was born or hatched
Scope Notes | property with example in inline XML
Example(s) |`<?xml version="1.0" encoding="UTF-8"?>` <br /> `<rdf:RDF` <br /> `   xmlns="https://example.com#"` <br /> `   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"` <br /> `>` <br /> `  <rdf:Description rdf:about="https://example.com#flipper">` <br /> `    <rdf:type rdf:resource="https://example.com#Fish"/>` <br /> `    <bornOrHatchedDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-05-11</bornOrHatchedDate>` <br /> `  </rdf:Description>` <br /> `</rdf:RDF>` <br /> <br />
Domain(s) |[Creature](#Creature) (c)<br />
Range(s) |[xsd:date](http://www.w3.org/2001/XMLSchema#date) (c)<br />
[](livesinestuarinewater)
### lives in estuarine water
Property | Value
--- | ---
URI | `https://example.com#livesInEstuarineWater`
Description | True if the fish lives in estuarine water. It may also live in other water
Scope Notes | property with example using Resource Descriptor for inline Markdown
Example(s) |<br />
Domain(s) |[Fish](#Fish) (c)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />
[](livesinfreshwater)
### lives in fresh water
Property | Value
--- | ---
URI | `https://example.com#livesInFreshWater`
Description | True if the fish lives in fresh water. It may also live in other water
Scope Notes | property with example in inline RDF
Example(s) |`<x> a eg:Fish ;` <br /> `    skos:prefLabel "Fish X"@en ;` <br /> `    eg:livesInFreshWater true ;` <br /> `    ...` <br /> `.` <br /> <br />
Domain(s) |[Fish](#Fish) (c)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />
[](livesinsaltwater)
### lives in salt water
Property | Value
--- | ---
URI | `https://example.com#livesInSaltWater`
Description | True if the fish lives in salt water. It may also live in other water
Scope Notes | property with an remote-hosted image example
Example(s) |![](https://raw.githubusercontent.com/RDFLib/pyLODE/master/pylode/examples/examples-ont/toothy.png) <br />
Domain(s) |[Fish](#Fish) (c)<br />
Range(s) |[xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) (c)<br />

## Named Individuals
## Namespaces
* **default (eggs)**
  * `https://example.com#`
* **dcterms**
  * `http://purl.org/dc/terms/`
* **orcid**
  * `http://orcid.org/`
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
* **sdo**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **vann**
  * `http://purl.org/vocab/vann/`
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