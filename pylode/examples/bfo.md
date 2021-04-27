Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

# Basic Formal Ontology version 2

## Metadata
* **URI**
  * `http://purl.obolibrary.org/obo/bfo.owl`
* **Contributor(s)**
  * Alan Ruttenberg
  * Albert Goldfain
  * Barry Smith
  * Bill Duncan
  * Bjoern Peters
  * Chris Mungall
  * David Osumi-Sutherland
  * Fabian Neuhaus
  * James A. Overton
  * Janna Hastings
  * Jie Zheng
  * Jonathan Bona
  * Larry Hunter
  * Leonard Jacuzzo
  * Ludger Jansen
  * Mark Ressler
  * Mathias Brochhausen
  * Mauricio Almeida
  * Melanie Courtot
  * Pierre Grenon
  * Randall Dipert
  * Robert Rovetto
  * Ron Rudnicki
  * Stefan Schulz
  * Thomas Bittner
  * Werner Ceusters
* **Ontology RDF**
  * RDF ([bfo.ttl](turtle))
### Description
<p>This is an early version of BFO version 2 and has not yet been extensively reviewed by the project team members. Please see the project site http://code.google.com/p/bfo/ , the bfo2 owl discussion group http://groups.google.com/group/bfo-owl-devel , the bfo2 discussion group http://groups.google.com/group/bfo-devel, the tracking google doc http://goo.gl/IlrEE, and the current version of the bfo2 reference http://purl.obolibrary.org/obo/bfo/dev/bfo2-reference.docx . This ontology is generated from a specification at http://bfo.googlecode.com/svn/trunk/src/ontology/owl-group/specification/ and with the code that generates the OWL version in http://bfo.googlecode.com/svn/trunk/src/tools/. A very early version of BFO version 2 in CLIF is at http://purl.obolibrary.org/obo/bfo/dev/bfo.clif</p>

## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Annotation Properties](#annotationproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[continuant](#continuant),
[continuant fiat boundary](#continuantfiatboundary),
[disposition](#disposition),
[entity](#entity),
[fiat object](#fiatobject),
[function](#function),
[generically dependent continuant](#genericallydependentcontinuant),
[history](#history),
[immaterial entity](#immaterialentity),
[independent continuant](#independentcontinuant),
[material entity](#materialentity),
[object](#object),
[object aggregate](#objectaggregate),
[occurrent](#occurrent),
[one-dimensional continuant fiat boundary](#one-dimensionalcontinuantfiatboundary),
[one-dimensional spatial region](#one-dimensionalspatialregion),
[one-dimensional temporal region](#one-dimensionaltemporalregion),
[process](#process),
[process boundary](#processboundary),
[process profile](#processprofile),
[quality](#quality),
[realizable entity](#realizableentity),
[relational quality](#relationalquality),
[role](#role),
[site](#site),
[spatial region](#spatialregion),
[spatiotemporal region](#spatiotemporalregion),
[specifically dependent continuant](#specificallydependentcontinuant),
[temporal region](#temporalregion),
[three-dimensional spatial region](#three-dimensionalspatialregion),
[two-dimensional continuant fiat boundary](#two-dimensionalcontinuantfiatboundary),
[two-dimensional spatial region](#two-dimensionalspatialregion),
[zero-dimensional continuant fiat boundary](#zero-dimensionalcontinuantfiatboundary),
[zero-dimensional spatial region](#zero-dimensionalspatialregion),
[zero-dimensional temporal region](#zero-dimensionaltemporalregion),
### entity
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000001`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Restrictions |[cdao:BFO_0000108](http://purl.obolibrary.org/obo/BFO_0000108) (op) **some** [cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
Sub-classes |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
In domain of |[cdao:BFO_0000108](http://purl.obolibrary.org/obo/BFO_0000108) (op)<br />
In range of |[cdao:BFO_0000157](http://purl.obolibrary.org/obo/BFO_0000157) (op)<br />
### continuant
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000002`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000001](http://purl.obolibrary.org/obo/BFO_0000001) (c)<br />
Sub-classes |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />[cdao:BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031) (c)<br />[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
In domain of |[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op)<br />[cdao:BFO_0000175](http://purl.obolibrary.org/obo/BFO_0000175) (op)<br />[cdao:BFO_0000129](http://purl.obolibrary.org/obo/BFO_0000129) (op)<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op)<br />[cdao:BFO_0000115](http://purl.obolibrary.org/obo/BFO_0000115) (op)<br />[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op)<br />[cdao:BFO_0000174](http://purl.obolibrary.org/obo/BFO_0000174) (op)<br />[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op)<br />
In range of |[cdao:BFO_0000115](http://purl.obolibrary.org/obo/BFO_0000115) (op)<br />[cdao:BFO_0000175](http://purl.obolibrary.org/obo/BFO_0000175) (op)<br />[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op)<br />[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op)<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op)<br />[cdao:BFO_0000174](http://purl.obolibrary.org/obo/BFO_0000174) (op)<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op)<br />[cdao:BFO_0000129](http://purl.obolibrary.org/obo/BFO_0000129) (op)<br />
### occurrent
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000003`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000001](http://purl.obolibrary.org/obo/BFO_0000001) (c)<br />
Sub-classes |[cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />[cdao:BFO_0000035](http://purl.obolibrary.org/obo/BFO_0000035) (c)<br />
In domain of |[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op)<br />[cdao:BFO_0000130](http://purl.obolibrary.org/obo/BFO_0000130) (op)<br />[cdao:BFO_0000136](http://purl.obolibrary.org/obo/BFO_0000136) (op)<br />[cdao:BFO_0000155](http://purl.obolibrary.org/obo/BFO_0000155) (op)<br />[cdao:BFO_0000181](http://purl.obolibrary.org/obo/BFO_0000181) (op)<br />[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op)<br />[cdao:BFO_0000138](http://purl.obolibrary.org/obo/BFO_0000138) (op)<br />[cdao:BFO_0000118](http://purl.obolibrary.org/obo/BFO_0000118) (op)<br />[cdao:BFO_0000121](http://purl.obolibrary.org/obo/BFO_0000121) (op)<br />[cdao:BFO_0000139](http://purl.obolibrary.org/obo/BFO_0000139) (op)<br />
In range of |[cdao:BFO_0000118](http://purl.obolibrary.org/obo/BFO_0000118) (op)<br />[cdao:BFO_0000136](http://purl.obolibrary.org/obo/BFO_0000136) (op)<br />[cdao:BFO_0000121](http://purl.obolibrary.org/obo/BFO_0000121) (op)<br />[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op)<br />[cdao:BFO_0000126](http://purl.obolibrary.org/obo/BFO_0000126) (op)<br />[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op)<br />[cdao:BFO_0000138](http://purl.obolibrary.org/obo/BFO_0000138) (op)<br />[cdao:BFO_0000139](http://purl.obolibrary.org/obo/BFO_0000139) (op)<br />[cdao:BFO_0000156](http://purl.obolibrary.org/obo/BFO_0000156) (op)<br />[cdao:BFO_0000181](http://purl.obolibrary.org/obo/BFO_0000181) (op)<br />
### independent continuant
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000004`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Restrictions |[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ()<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ()<br />[cdao:BFO_0000169](http://purl.obolibrary.org/obo/BFO_0000169) (op) **only** [owl:Nothing](http://www.w3.org/2002/07/owl#Nothing) (c)<br />[cdao:BFO_0000083](http://purl.obolibrary.org/obo/BFO_0000083) (op) **some** [cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
Sub-classes |[cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c)<br />[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
In domain of |[cdao:BFO_0000083](http://purl.obolibrary.org/obo/BFO_0000083) (op)<br />[cdao:BFO_0000171](http://purl.obolibrary.org/obo/BFO_0000171) (op)<br />[cdao:BFO_0000124](http://purl.obolibrary.org/obo/BFO_0000124) (op)<br />
In range of |[cdao:BFO_0000124](http://purl.obolibrary.org/obo/BFO_0000124) (op)<br />[cdao:BFO_0000123](http://purl.obolibrary.org/obo/BFO_0000123) (op)<br />[cdao:BFO_0000171](http://purl.obolibrary.org/obo/BFO_0000171) (op)<br />
### spatial region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000006`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c)<br />
Restrictions |[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** [cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />[cdao:BFO_0000123](http://purl.obolibrary.org/obo/BFO_0000123) (op)<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** [cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />[cdao:BFO_0000083](http://purl.obolibrary.org/obo/BFO_0000083) (op)<br />[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** [cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** [cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
Sub-classes |[cdao:BFO_0000026](http://purl.obolibrary.org/obo/BFO_0000026) (c)<br />[cdao:BFO_0000018](http://purl.obolibrary.org/obo/BFO_0000018) (c)<br />[cdao:BFO_0000009](http://purl.obolibrary.org/obo/BFO_0000009) (c)<br />[cdao:BFO_0000028](http://purl.obolibrary.org/obo/BFO_0000028) (c)<br />
In domain of |[cdao:BFO_0000152](http://purl.obolibrary.org/obo/BFO_0000152) (op)<br />[cdao:BFO_0000123](http://purl.obolibrary.org/obo/BFO_0000123) (op)<br />
In range of |[cdao:BFO_0000151](http://purl.obolibrary.org/obo/BFO_0000151) (op)<br />[cdao:BFO_0000083](http://purl.obolibrary.org/obo/BFO_0000083) (op)<br />
### temporal region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000008`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Restrictions |[cdao:BFO_0000156](http://purl.obolibrary.org/obo/BFO_0000156) (op)<br />[cdao:BFO_0000155](http://purl.obolibrary.org/obo/BFO_0000155) (op)<br />[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op) **only** [cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op) **only** [cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
Sub-classes |[cdao:BFO_0000148](http://purl.obolibrary.org/obo/BFO_0000148) (c)<br />[cdao:BFO_0000038](http://purl.obolibrary.org/obo/BFO_0000038) (c)<br />
In domain of |[cdao:BFO_0000154](http://purl.obolibrary.org/obo/BFO_0000154) (op)<br />[cdao:BFO_0000156](http://purl.obolibrary.org/obo/BFO_0000156) (op)<br />[cdao:BFO_0000157](http://purl.obolibrary.org/obo/BFO_0000157) (op)<br />
In range of |[cdao:BFO_0000153](http://purl.obolibrary.org/obo/BFO_0000153) (op)<br />[cdao:BFO_0000108](http://purl.obolibrary.org/obo/BFO_0000108) (op)<br />[cdao:BFO_0000155](http://purl.obolibrary.org/obo/BFO_0000155) (op)<br />
### two-dimensional spatial region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000009`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
Restrictions |[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** ()<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** ()<br />
### spatiotemporal region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000011`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Restrictions |[cdao:BFO_0000130](http://purl.obolibrary.org/obo/BFO_0000130) (op)<br />[cdao:BFO_0000151](http://purl.obolibrary.org/obo/BFO_0000151) (op) **some** [cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />[cdao:BFO_0000126](http://purl.obolibrary.org/obo/BFO_0000126) (op)<br />[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op) **only** [cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op) **only** [cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />[cdao:BFO_0000153](http://purl.obolibrary.org/obo/BFO_0000153) (op) **some** [cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
In domain of |[cdao:BFO_0000151](http://purl.obolibrary.org/obo/BFO_0000151) (op)<br />[cdao:BFO_0000126](http://purl.obolibrary.org/obo/BFO_0000126) (op)<br />[cdao:BFO_0000153](http://purl.obolibrary.org/obo/BFO_0000153) (op)<br />
In range of |[cdao:BFO_0000154](http://purl.obolibrary.org/obo/BFO_0000154) (op)<br />[cdao:BFO_0000152](http://purl.obolibrary.org/obo/BFO_0000152) (op)<br />[cdao:BFO_0000130](http://purl.obolibrary.org/obo/BFO_0000130) (op)<br />
### process
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000015`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Restrictions |[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op) **only** [cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />[cdao:BFO_0000169](http://purl.obolibrary.org/obo/BFO_0000169) (op) **some** [cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op) **only** ([cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c) or [cdao:BFO_0000035](http://purl.obolibrary.org/obo/BFO_0000035) (c))<br />
Sub-classes |[cdao:BFO_0000144](http://purl.obolibrary.org/obo/BFO_0000144) (c)<br />[cdao:BFO_0000182](http://purl.obolibrary.org/obo/BFO_0000182) (c)<br />
In domain of |[cdao:BFO_0000057](http://purl.obolibrary.org/obo/BFO_0000057) (op)<br />[cdao:BFO_0000119](http://purl.obolibrary.org/obo/BFO_0000119) (op)<br />[cdao:BFO_0000167](http://purl.obolibrary.org/obo/BFO_0000167) (op)<br />[cdao:BFO_0000055](http://purl.obolibrary.org/obo/BFO_0000055) (op)<br />[cdao:BFO_0000184](http://purl.obolibrary.org/obo/BFO_0000184) (op)<br />
In range of |[cdao:BFO_0000056](http://purl.obolibrary.org/obo/BFO_0000056) (op)<br />[cdao:BFO_0000185](http://purl.obolibrary.org/obo/BFO_0000185) (op)<br />[cdao:BFO_0000133](http://purl.obolibrary.org/obo/BFO_0000133) (op)<br />[cdao:BFO_0000054](http://purl.obolibrary.org/obo/BFO_0000054) (op)<br />
### disposition
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000016`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000017](http://purl.obolibrary.org/obo/BFO_0000017) (c)<br />
Restrictions |[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ()<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ()<br />
Sub-classes |[cdao:BFO_0000034](http://purl.obolibrary.org/obo/BFO_0000034) (c)<br />
In domain of |[cdao:BFO_0000107](http://purl.obolibrary.org/obo/BFO_0000107) (op)<br />[cdao:BFO_0000113](http://purl.obolibrary.org/obo/BFO_0000113) (op)<br />
In range of |[cdao:BFO_0000112](http://purl.obolibrary.org/obo/BFO_0000112) (op)<br />[cdao:BFO_0000127](http://purl.obolibrary.org/obo/BFO_0000127) (op)<br />[cdao:BFO_0000162](http://purl.obolibrary.org/obo/BFO_0000162) (op)<br />[cdao:BFO_0000163](http://purl.obolibrary.org/obo/BFO_0000163) (op)<br />
### realizable entity
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000017`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
Restrictions |[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ()<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ()<br />
Sub-classes |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />[cdao:BFO_0000023](http://purl.obolibrary.org/obo/BFO_0000023) (c)<br />
In domain of |[cdao:BFO_0000054](http://purl.obolibrary.org/obo/BFO_0000054) (op)<br />
In range of |[cdao:BFO_0000055](http://purl.obolibrary.org/obo/BFO_0000055) (op)<br />
### zero-dimensional spatial region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000018`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
Restrictions |[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** ()<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** ()<br />
### quality
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000019`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
Restrictions |[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ()<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ()<br />
Sub-classes |[cdao:BFO_0000145](http://purl.obolibrary.org/obo/BFO_0000145) (c)<br />
In domain of |[cdao:BFO_0000080](http://purl.obolibrary.org/obo/BFO_0000080) (op)<br />
In range of |[cdao:BFO_0000159](http://purl.obolibrary.org/obo/BFO_0000159) (op)<br />[cdao:BFO_0000086](http://purl.obolibrary.org/obo/BFO_0000086) (op)<br />
### specifically dependent continuant
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000020`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Restrictions |[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ([cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c) and [ub10bL2217C58](ub10bL2217C58) (c))<br />[cdao:BFO_0000052](http://purl.obolibrary.org/obo/BFO_0000052) (op) **some** ([cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c) and [ub10bL2217C58](ub10bL2217C58) (c))<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ([cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c) and [ub10bL2217C58](ub10bL2217C58) (c))<br />
Sub-classes |[cdao:BFO_0000019](http://purl.obolibrary.org/obo/BFO_0000019) (c)<br />[cdao:BFO_0000017](http://purl.obolibrary.org/obo/BFO_0000017) (c)<br />
In domain of |[cdao:BFO_0000059](http://purl.obolibrary.org/obo/BFO_0000059) (op)<br />[cdao:BFO_0000052](http://purl.obolibrary.org/obo/BFO_0000052) (op)<br />
In range of |[cdao:BFO_0000053](http://purl.obolibrary.org/obo/BFO_0000053) (op)<br />[cdao:BFO_0000158](http://purl.obolibrary.org/obo/BFO_0000158) (op)<br />[cdao:BFO_0000058](http://purl.obolibrary.org/obo/BFO_0000058) (op)<br />
### role
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000023`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000017](http://purl.obolibrary.org/obo/BFO_0000017) (c)<br />
Restrictions |[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ()<br />[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ()<br />
In domain of |[cdao:BFO_0000081](http://purl.obolibrary.org/obo/BFO_0000081) (op)<br />
In range of |[cdao:BFO_0000161](http://purl.obolibrary.org/obo/BFO_0000161) (op)<br />[cdao:BFO_0000087](http://purl.obolibrary.org/obo/BFO_0000087) (op)<br />
### fiat object
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000024`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
### one-dimensional spatial region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000026`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
Restrictions |[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** ()<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** ()<br />
### object aggregate
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000027`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
### three-dimensional spatial region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000028`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
### site
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000029`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c)<br />
### object
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000030`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
### generically dependent continuant
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000031`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Restrictions |[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ()<br />[cdao:BFO_0000058](http://purl.obolibrary.org/obo/BFO_0000058) (op) **some** [cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ()<br />
In domain of |[cdao:BFO_0000084](http://purl.obolibrary.org/obo/BFO_0000084) (op)<br />[cdao:BFO_0000058](http://purl.obolibrary.org/obo/BFO_0000058) (op)<br />
In range of |[cdao:BFO_0000059](http://purl.obolibrary.org/obo/BFO_0000059) (op)<br />[cdao:BFO_0000101](http://purl.obolibrary.org/obo/BFO_0000101) (op)<br />
### function
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000034`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />
In domain of |[cdao:BFO_0000079](http://purl.obolibrary.org/obo/BFO_0000079) (op)<br />
In range of |[cdao:BFO_0000085](http://purl.obolibrary.org/obo/BFO_0000085) (op)<br />[cdao:BFO_0000160](http://purl.obolibrary.org/obo/BFO_0000160) (op)<br />
### process boundary
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000035`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Restrictions |[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op) **only** [cdao:BFO_0000035](http://purl.obolibrary.org/obo/BFO_0000035) (c)<br />[cdao:BFO_0000130](http://purl.obolibrary.org/obo/BFO_0000130) (op) **only** ([cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c) and [cdao:BFO_0000035](http://purl.obolibrary.org/obo/BFO_0000035) (c) and [cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c) and [ub10bL1760C58](ub10bL1760C58) (c))<br />[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op) **only** ([cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c) and [cdao:BFO_0000035](http://purl.obolibrary.org/obo/BFO_0000035) (c) and [cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c) and [ub10bL1760C58](ub10bL1760C58) (c))<br />[cdao:BFO_0000108](http://purl.obolibrary.org/obo/BFO_0000108) (op) **only** [cdao:BFO_0000148](http://purl.obolibrary.org/obo/BFO_0000148) (c)<br />
### one-dimensional temporal region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000038`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
### material entity
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000040`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
Restrictions |[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** ([cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c) or [cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c) or [cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c) or [cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c))<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** [cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />[cdao:BFO_0000083](http://purl.obolibrary.org/obo/BFO_0000083) (op) **only** [cdao:BFO_0000028](http://purl.obolibrary.org/obo/BFO_0000028) (c)<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** ([cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c) or [cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c) or [cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c) or [cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c))<br />[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** [cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
Sub-classes |[cdao:BFO_0000024](http://purl.obolibrary.org/obo/BFO_0000024) (c)<br />[cdao:BFO_0000027](http://purl.obolibrary.org/obo/BFO_0000027) (c)<br />[cdao:BFO_0000030](http://purl.obolibrary.org/obo/BFO_0000030) (c)<br />
In domain of |[cdao:BFO_0000127](http://purl.obolibrary.org/obo/BFO_0000127) (op)<br />[cdao:BFO_0000185](http://purl.obolibrary.org/obo/BFO_0000185) (op)<br />[cdao:BFO_0000163](http://purl.obolibrary.org/obo/BFO_0000163) (op)<br />
In range of |[cdao:BFO_0000113](http://purl.obolibrary.org/obo/BFO_0000113) (op)<br />[cdao:BFO_0000184](http://purl.obolibrary.org/obo/BFO_0000184) (op)<br />
### continuant fiat boundary
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000140`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c)<br />
Restrictions |[cdao:BFO_0000083](http://purl.obolibrary.org/obo/BFO_0000083) (op) **only** ([cdao:BFO_0000009](http://purl.obolibrary.org/obo/BFO_0000009) (c) or [cdao:BFO_0000018](http://purl.obolibrary.org/obo/BFO_0000018) (c) or [cdao:BFO_0000026](http://purl.obolibrary.org/obo/BFO_0000026) (c))<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op) **only** ([cdao:BFO_0000009](http://purl.obolibrary.org/obo/BFO_0000009) (c) or [cdao:BFO_0000018](http://purl.obolibrary.org/obo/BFO_0000018) (c) or [cdao:BFO_0000026](http://purl.obolibrary.org/obo/BFO_0000026) (c))<br />[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** [cdao:BFO_0000140](http://purl.obolibrary.org/obo/BFO_0000140) (c)<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** [cdao:BFO_0000140](http://purl.obolibrary.org/obo/BFO_0000140) (c)<br />[cdao:BFO_0000186](http://purl.obolibrary.org/obo/BFO_0000186) (op) **only** ([cdao:BFO_0000009](http://purl.obolibrary.org/obo/BFO_0000009) (c) or [cdao:BFO_0000018](http://purl.obolibrary.org/obo/BFO_0000018) (c) or [cdao:BFO_0000026](http://purl.obolibrary.org/obo/BFO_0000026) (c))<br />
Sub-classes |[cdao:BFO_0000142](http://purl.obolibrary.org/obo/BFO_0000142) (c)<br />[cdao:BFO_0000146](http://purl.obolibrary.org/obo/BFO_0000146) (c)<br />[cdao:BFO_0000147](http://purl.obolibrary.org/obo/BFO_0000147) (c)<br />
### immaterial entity
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000141`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
Restrictions |[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** ()<br />[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** [cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c)<br />[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** ()<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** [cdao:BFO_0000141](http://purl.obolibrary.org/obo/BFO_0000141) (c)<br />
Sub-classes |[cdao:BFO_0000029](http://purl.obolibrary.org/obo/BFO_0000029) (c)<br />[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />[cdao:BFO_0000140](http://purl.obolibrary.org/obo/BFO_0000140) (c)<br />
### one-dimensional continuant fiat boundary
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000142`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000140](http://purl.obolibrary.org/obo/BFO_0000140) (c)<br />
Restrictions |[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** ()<br />[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** ()<br />
### process profile
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000144`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
Restrictions |[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op) **some** [cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
In domain of |[cdao:BFO_0000133](http://purl.obolibrary.org/obo/BFO_0000133) (op)<br />
In range of |[cdao:BFO_0000119](http://purl.obolibrary.org/obo/BFO_0000119) (op)<br />
### relational quality
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000145`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000019](http://purl.obolibrary.org/obo/BFO_0000019) (c)<br />
### two-dimensional continuant fiat boundary
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000146`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000140](http://purl.obolibrary.org/obo/BFO_0000140) (c)<br />
### zero-dimensional continuant fiat boundary
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000147`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000140](http://purl.obolibrary.org/obo/BFO_0000140) (c)<br />
Restrictions |[cdao:BFO_0000187](http://purl.obolibrary.org/obo/BFO_0000187) (op) **only** ()<br />[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op) **only** ()<br />
### zero-dimensional temporal region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000148`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
Restrictions |[cdao:BFO_0000118](http://purl.obolibrary.org/obo/BFO_0000118) (op) **only** [owl:Nothing](http://www.w3.org/2002/07/owl#Nothing) (c)<br />
### history
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000182`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-classes |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
Restrictions |[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op) **only** ()<br />[cdao:BFO_0000184](http://purl.obolibrary.org/obo/BFO_0000184) (op) **some** [cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />

## Object Properties
[inheres in at all times](#inheresinatalltimes),
[bearer of at some time](#bearerofatsometime),
[realized in](#realizedin),
[realizes](#realizes),
[participates in at some time](#participatesinatsometime),
[has participant at some time](#hasparticipantatsometime),
[concretized by at some time](#concretizedbyatsometime),
[concretizes at some time](#concretizesatsometime),
[occurs in](#occursin),
[contains process](#containsprocess),
[specifically depends on at all times](#specificallydependsonatalltimes),
[function of at all times](#functionofatalltimes),
[quality of at all times](#qualityofatalltimes),
[role of at all times](#roleofatalltimes),
[located in at all times](#locatedinatalltimes),
[occupies spatial region at some time](#occupiesspatialregionatsometime),
[generically depends on at some time](#genericallydependsonatsometime),
[has function at some time](#hasfunctionatsometime),
[has quality at some time](#hasqualityatsometime),
[has role at some time](#hasroleatsometime),
[has generic dependent at some time](#hasgenericdependentatsometime),
[disposition of at all times](#dispositionofatalltimes),
[exists at](#existsat),
[has continuant part at all times](#hascontinuantpartatalltimes),
[has proper continuant part at all times](#haspropercontinuantpartatalltimes),
[has disposition at some time](#hasdispositionatsometime),
[has material basis at all times](#hasmaterialbasisatalltimes),
[has member part at some time](#hasmemberpartatsometime),
[has occurrent part](#hasoccurrentpart),
[has proper occurrent part](#hasproperoccurrentpart),
[has profile](#hasprofile),
[has temporal part](#hastemporalpart),
[has spatial occupant at some time](#hasspatialoccupantatsometime),
[has location at some time](#haslocationatsometime),
[has specific dependent at some time](#hasspecificdependentatsometime),
[has spatiotemporal occupant](#hasspatiotemporaloccupant),
[material basis of at some time](#materialbasisofatsometime),
[member part of at some time](#memberpartofatsometime),
[occupies spatiotemporal region](#occupiesspatiotemporalregion),
[part of occurrent](#partofoccurrent),
[process profile of](#processprofileof),
[proper temporal part of](#propertemporalpartof),
[proper part of continuant at all times](#properpartofcontinuantatalltimes),
[proper part of occurrent](#properpartofoccurrent),
[temporal part of](#temporalpartof),
[projects onto spatial region at some time](#projectsontospatialregionatsometime),
[spatial projection of spatiotemporal at some time](#spatialprojectionofspatiotemporalatsometime),
[projects onto temporal region](#projectsontotemporalregion),
[temporal projection of spatiotemporal](#temporalprojectionofspatiotemporal),
[occupies temporal region](#occupiestemporalregion),
[has temporal occupant](#hastemporaloccupant),
[during which exists](#duringwhichexists),
[bearer of at all times](#bearerofatalltimes),
[has quality at all times](#hasqualityatalltimes),
[has function at all times](#hasfunctionatalltimes),
[has role at all times](#hasroleatalltimes),
[has disposition at all times](#hasdispositionatalltimes),
[material basis of at all times](#materialbasisofatalltimes),
[concretizes at all times](#concretizesatalltimes),
[concretized by at all times](#concretizedbyatalltimes),
[participates in at all times](#participatesinatalltimes),
[has participant at all times](#hasparticipantatalltimes),
[has specific dependent at all times](#hasspecificdependentatalltimes),
[specifically depends on at some time](#specificallydependsonatsometime),
[has location at all times](#haslocationatalltimes),
[located in at some time](#locatedinatsometime),
[has member part at all times](#hasmemberpartatalltimes),
[member part of at all times](#memberpartofatalltimes),
[has proper continuant part at some time](#haspropercontinuantpartatsometime),
[proper part of continuant at some time](#properpartofcontinuantatsometime),
[part of continuant at some time](#partofcontinuantatsometime),
[part of continuant at all times](#partofcontinuantatalltimes),
[has continuant part at some time](#hascontinuantpartatsometime),
[has proper temporal part](#haspropertemporalpart),
[history of](#historyof),
[has history](#hashistory),
[part of continuant at all times that whole exists](#partofcontinuantatalltimesthatwholeexists),
[has continuant part at all times that part exists](#hascontinuantpartatalltimesthatpartexists),
[](inheresinatalltimes)
### inheres in at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000052`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000070](http://purl.obolibrary.org/obo/BFO_0000070) (op)<br />
Domain(s) |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
Range(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />[ub10bL1733C50](ub10bL1733C50) (c)<br />
[](bearerofatsometime)
### bearer of at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000053`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000125](http://purl.obolibrary.org/obo/BFO_0000125) (op)<br />
Domain(s) |([cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c) and [ub10bL1301C50](ub10bL1301C50) (c))<br />
Range(s) |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
[](realizedin)
### realized in
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000054`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000017](http://purl.obolibrary.org/obo/BFO_0000017) (c)<br />
Range(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
[](realizes)
### realizes
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000055`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
Range(s) |[cdao:BFO_0000017](http://purl.obolibrary.org/obo/BFO_0000017) (c)<br />
[](participatesinatsometime)
### participates in at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000056`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |([cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c) and [ub10bL350C50](ub10bL350C50) (c))<br />
Range(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
[](hasparticipantatsometime)
### has participant at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000057`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />[ub10bL1490C50](ub10bL1490C50) (c)<br />
[](concretizedbyatsometime)
### concretized by at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000058`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031) (c)<br />
Range(s) |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
[](concretizesatsometime)
### concretizes at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000059`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
Range(s) |[cdao:BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031) (c)<br />
[](occursin)
### occurs in
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000066`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |([cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c) or [cdao:BFO_0000035](http://purl.obolibrary.org/obo/BFO_0000035) (c))<br />
Range(s) |[cdao:BFO_0000029](http://purl.obolibrary.org/obo/BFO_0000029) (c)<br />[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
[](containsprocess)
### contains process
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000067`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |([cdao:BFO_0000029](http://purl.obolibrary.org/obo/BFO_0000029) (c) or [cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c))<br />
Range(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />[cdao:BFO_0000035](http://purl.obolibrary.org/obo/BFO_0000035) (c)<br />
[](specificallydependsonatalltimes)
### specifically depends on at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000070`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000169](http://purl.obolibrary.org/obo/BFO_0000169) (op)<br />
[](functionofatalltimes)
### function of at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000079`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000052](http://purl.obolibrary.org/obo/BFO_0000052) (op)<br />
Domain(s) |[cdao:BFO_0000034](http://purl.obolibrary.org/obo/BFO_0000034) (c)<br />
[](qualityofatalltimes)
### quality of at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000080`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000052](http://purl.obolibrary.org/obo/BFO_0000052) (op)<br />
Domain(s) |[cdao:BFO_0000019](http://purl.obolibrary.org/obo/BFO_0000019) (c)<br />
[](roleofatalltimes)
### role of at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000081`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000052](http://purl.obolibrary.org/obo/BFO_0000052) (op)<br />
Domain(s) |[cdao:BFO_0000023](http://purl.obolibrary.org/obo/BFO_0000023) (c)<br />
[](locatedinatalltimes)
### located in at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000082`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000171](http://purl.obolibrary.org/obo/BFO_0000171) (op)<br />
[](occupiesspatialregionatsometime)
### occupies spatial region at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000083`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
Range(s) |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
[](genericallydependsonatsometime)
### generically depends on at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000084`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031) (c)<br />
Range(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />[ub10bL605C50](ub10bL605C50) (c)<br />
[](hasfunctionatsometime)
### has function at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000085`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000053](http://purl.obolibrary.org/obo/BFO_0000053) (op)<br />
Range(s) |[cdao:BFO_0000034](http://purl.obolibrary.org/obo/BFO_0000034) (c)<br />
[](hasqualityatsometime)
### has quality at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000086`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000053](http://purl.obolibrary.org/obo/BFO_0000053) (op)<br />
Range(s) |[cdao:BFO_0000019](http://purl.obolibrary.org/obo/BFO_0000019) (c)<br />
[](hasroleatsometime)
### has role at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000087`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000053](http://purl.obolibrary.org/obo/BFO_0000053) (op)<br />
Range(s) |[cdao:BFO_0000023](http://purl.obolibrary.org/obo/BFO_0000023) (c)<br />
[](hasgenericdependentatsometime)
### has generic dependent at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000101`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |([cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c) and [ub10bL387C50](ub10bL387C50) (c))<br />
Range(s) |[cdao:BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031) (c)<br />
[](dispositionofatalltimes)
### disposition of at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000107`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000052](http://purl.obolibrary.org/obo/BFO_0000052) (op)<br />
Domain(s) |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />
[](existsat)
### exists at
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000108`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000001](http://purl.obolibrary.org/obo/BFO_0000001) (c)<br />
Range(s) |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
[](hascontinuantpartatalltimes)
### has continuant part at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000110`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op)<br />
[](haspropercontinuantpartatalltimes)
### has proper continuant part at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000111`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000110](http://purl.obolibrary.org/obo/BFO_0000110) (op)<br />[cdao:BFO_0000174](http://purl.obolibrary.org/obo/BFO_0000174) (op)<br />
[](hasdispositionatsometime)
### has disposition at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000112`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000053](http://purl.obolibrary.org/obo/BFO_0000053) (op)<br />
Range(s) |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />
[](hasmaterialbasisatalltimes)
### has material basis at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000113`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />
Range(s) |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
[](hasmemberpartatsometime)
### has member part at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000115`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op)<br />
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
[](hasoccurrentpart)
### has occurrent part
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000117`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](hasproperoccurrentpart)
### has proper occurrent part
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000118`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op)<br />
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](hasprofile)
### has profile
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000119`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
Range(s) |[cdao:BFO_0000144](http://purl.obolibrary.org/obo/BFO_0000144) (c)<br />
[](hastemporalpart)
### has temporal part
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000121`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000117](http://purl.obolibrary.org/obo/BFO_0000117) (op)<br />
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](hasspatialoccupantatsometime)
### has spatial occupant at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000123`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
Range(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
[](haslocationatsometime)
### has location at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000124`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
Range(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
[](hasspecificdependentatsometime)
### has specific dependent at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000125`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |([cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c) or [cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c) or [ub10bL1053C59](ub10bL1053C59) (c))<br />
Range(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
[](hasspatiotemporaloccupant)
### has spatiotemporal occupant
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000126`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](materialbasisofatsometime)
### material basis of at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000127`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
Range(s) |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />
[](memberpartofatsometime)
### member part of at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000129`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000175](http://purl.obolibrary.org/obo/BFO_0000175) (op)<br />[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op)<br />
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
[](occupiesspatiotemporalregion)
### occupies spatiotemporal region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000130`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />
[](partofoccurrent)
### part of occurrent
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000132`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](processprofileof)
### process profile of
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000133`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000144](http://purl.obolibrary.org/obo/BFO_0000144) (c)<br />
Range(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
[](propertemporalpartof)
### proper temporal part of
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000136`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000138](http://purl.obolibrary.org/obo/BFO_0000138) (op)<br />[cdao:BFO_0000139](http://purl.obolibrary.org/obo/BFO_0000139) (op)<br />
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](properpartofcontinuantatalltimes)
### proper part of continuant at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000137`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000175](http://purl.obolibrary.org/obo/BFO_0000175) (op)<br />[cdao:BFO_0000177](http://purl.obolibrary.org/obo/BFO_0000177) (op)<br />
[](properpartofoccurrent)
### proper part of occurrent
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000138`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op)<br />
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](temporalpartof)
### temporal part of
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000139`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000132](http://purl.obolibrary.org/obo/BFO_0000132) (op)<br />
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](projectsontospatialregionatsometime)
### projects onto spatial region at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000151`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />
Range(s) |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
[](spatialprojectionofspatiotemporalatsometime)
### spatial projection of spatiotemporal at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000152`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000006](http://purl.obolibrary.org/obo/BFO_0000006) (c)<br />
Range(s) |[cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />
[](projectsontotemporalregion)
### projects onto temporal region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000153`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000108](http://purl.obolibrary.org/obo/BFO_0000108) (op)<br />
Domain(s) |[cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />
Range(s) |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
[](temporalprojectionofspatiotemporal)
### temporal projection of spatiotemporal
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000154`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000157](http://purl.obolibrary.org/obo/BFO_0000157) (op)<br />
Domain(s) |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
Range(s) |[cdao:BFO_0000011](http://purl.obolibrary.org/obo/BFO_0000011) (c)<br />
[](occupiestemporalregion)
### occupies temporal region
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000155`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000108](http://purl.obolibrary.org/obo/BFO_0000108) (op)<br />
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
[](hastemporaloccupant)
### has temporal occupant
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000156`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000157](http://purl.obolibrary.org/obo/BFO_0000157) (op)<br />
Domain(s) |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](duringwhichexists)
### during which exists
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000157`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000008](http://purl.obolibrary.org/obo/BFO_0000008) (c)<br />
Range(s) |[cdao:BFO_0000001](http://purl.obolibrary.org/obo/BFO_0000001) (c)<br />
[](bearerofatalltimes)
### bearer of at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000158`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000168](http://purl.obolibrary.org/obo/BFO_0000168) (op)<br />
Domain(s) |([cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c) and [ub10bL1416C50](ub10bL1416C50) (c))<br />
Range(s) |[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />
[](hasqualityatalltimes)
### has quality at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000159`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000158](http://purl.obolibrary.org/obo/BFO_0000158) (op)<br />
Range(s) |[cdao:BFO_0000019](http://purl.obolibrary.org/obo/BFO_0000019) (c)<br />
[](hasfunctionatalltimes)
### has function at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000160`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000158](http://purl.obolibrary.org/obo/BFO_0000158) (op)<br />
Range(s) |[cdao:BFO_0000034](http://purl.obolibrary.org/obo/BFO_0000034) (c)<br />
[](hasroleatalltimes)
### has role at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000161`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000158](http://purl.obolibrary.org/obo/BFO_0000158) (op)<br />
Range(s) |[cdao:BFO_0000023](http://purl.obolibrary.org/obo/BFO_0000023) (c)<br />
[](hasdispositionatalltimes)
### has disposition at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000162`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000158](http://purl.obolibrary.org/obo/BFO_0000158) (op)<br />
Range(s) |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />
[](materialbasisofatalltimes)
### material basis of at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000163`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000127](http://purl.obolibrary.org/obo/BFO_0000127) (op)<br />
Domain(s) |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
Range(s) |[cdao:BFO_0000016](http://purl.obolibrary.org/obo/BFO_0000016) (c)<br />
[](concretizesatalltimes)
### concretizes at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000164`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000059](http://purl.obolibrary.org/obo/BFO_0000059) (op)<br />
[](concretizedbyatalltimes)
### concretized by at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000165`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000058](http://purl.obolibrary.org/obo/BFO_0000058) (op)<br />
[](participatesinatalltimes)
### participates in at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000166`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000056](http://purl.obolibrary.org/obo/BFO_0000056) (op)<br />
[](hasparticipantatalltimes)
### has participant at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000167`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000057](http://purl.obolibrary.org/obo/BFO_0000057) (op)<br />
Domain(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />[ub10bL1251C50](ub10bL1251C50) (c)<br />
[](hasspecificdependentatalltimes)
### has specific dependent at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000168`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000125](http://purl.obolibrary.org/obo/BFO_0000125) (op)<br />
[](specificallydependsonatsometime)
### specifically depends on at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000169`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |([cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c) or [cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c))<br />
Range(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />[cdao:BFO_0000020](http://purl.obolibrary.org/obo/BFO_0000020) (c)<br />[ub10bL1712C59](ub10bL1712C59) (c)<br />
[](haslocationatalltimes)
### has location at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000170`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000124](http://purl.obolibrary.org/obo/BFO_0000124) (op)<br />
[](locatedinatsometime)
### located in at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000171`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
Range(s) |[cdao:BFO_0000004](http://purl.obolibrary.org/obo/BFO_0000004) (c)<br />
[](hasmemberpartatalltimes)
### has member part at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000172`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000110](http://purl.obolibrary.org/obo/BFO_0000110) (op)<br />[cdao:BFO_0000115](http://purl.obolibrary.org/obo/BFO_0000115) (op)<br />[cdao:BFO_0000111](http://purl.obolibrary.org/obo/BFO_0000111) (op)<br />
[](memberpartofatalltimes)
### member part of at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000173`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000129](http://purl.obolibrary.org/obo/BFO_0000129) (op)<br />[cdao:BFO_0000177](http://purl.obolibrary.org/obo/BFO_0000177) (op)<br />[cdao:BFO_0000137](http://purl.obolibrary.org/obo/BFO_0000137) (op)<br />
[](haspropercontinuantpartatsometime)
### has proper continuant part at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000174`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op)<br />
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
[](properpartofcontinuantatsometime)
### proper part of continuant at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000175`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op)<br />
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
[](partofcontinuantatsometime)
### part of continuant at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000176`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
[](partofcontinuantatalltimes)
### part of continuant at all times
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000177`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op)<br />
[](hascontinuantpartatsometime)
### has continuant part at some time
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000178`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
[](haspropertemporalpart)
### has proper temporal part
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000181`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000118](http://purl.obolibrary.org/obo/BFO_0000118) (op)<br />[cdao:BFO_0000121](http://purl.obolibrary.org/obo/BFO_0000121) (op)<br />
Domain(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
Range(s) |[cdao:BFO_0000003](http://purl.obolibrary.org/obo/BFO_0000003) (c)<br />
[](historyof)
### history of
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000184`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000066](http://purl.obolibrary.org/obo/BFO_0000066) (op)<br />[cdao:BFO_0000070](http://purl.obolibrary.org/obo/BFO_0000070) (op)<br />
Domain(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
Range(s) |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
[](hashistory)
### has history
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000185`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000067](http://purl.obolibrary.org/obo/BFO_0000067) (op)<br />[cdao:BFO_0000166](http://purl.obolibrary.org/obo/BFO_0000166) (op)<br />
Domain(s) |[cdao:BFO_0000040](http://purl.obolibrary.org/obo/BFO_0000040) (c)<br />
Range(s) |[cdao:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015) (c)<br />
[](partofcontinuantatalltimesthatwholeexists)
### part of continuant at all times that whole exists
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000186`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000176](http://purl.obolibrary.org/obo/BFO_0000176) (op)<br />
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
[](hascontinuantpartatalltimesthatpartexists)
### has continuant part at all times that part exists
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000187`
Is Defined By | http://purl.obolibrary.org/obo/bfo.owl
Super-properties |[cdao:BFO_0000178](http://purl.obolibrary.org/obo/BFO_0000178) (op)<br />
Domain(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />
Range(s) |[cdao:BFO_0000002](http://purl.obolibrary.org/obo/BFO_0000002) (c)<br />

## Annotation Properties
[BFO OWL specification label](#BFOOWLspecificationlabel),
[BFO CLIF specification label](#BFOCLIFspecificationlabel),
[editor preferred term](#editorpreferredterm),
[example of usage](#exampleofusage),
[definition](#definition),
[editor note](#editornote),
[term editor](#termeditor),
[alternative term](#alternativeterm),
[definition source](#definitionsource),
[curator note](#curatornote),
[imported from](#importedfrom),
[elucidation](#elucidation),
[has associated axiom(nl)](#hasassociatedaxiom(nl)),
[has associated axiom(fol)](#hasassociatedaxiom(fol)),
[has axiom label](#hasaxiomlabel),
[contributor](#contributor),
[member](#member),
[isDefinedBy](#isDefinedBy),
[seeAlso](#seeAlso),
[homepage](#homepage),
[](BFOOWLspecificationlabel)
### BFO OWL specification label
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000179`
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
[](BFOCLIFspecificationlabel)
### BFO CLIF specification label
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/BFO_0000180`
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
[](editorpreferredterm)
### editor preferred term
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000111`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](exampleofusage)
### example of usage
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000112`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](definition)
### definition
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000115`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](editornote)
### editor note
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000116`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](termeditor)
### term editor
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000117`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](alternativeterm)
### alternative term
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000118`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](definitionsource)
### definition source
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000119`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](curatornote)
### curator note
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000232`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](importedfrom)
### imported from
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000412`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](elucidation)
### elucidation
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000600`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](hasassociatedaxiom(nl))
### has associated axiom(nl)
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000601`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](hasassociatedaxiom(fol))
### has associated axiom(fol)
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0000602`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](hasaxiomlabel)
### has axiom label
Property | Value
--- | ---
URI | `http://purl.obolibrary.org/obo/IAO_0010000`
Is Defined By | http://purl.obolibrary.org/obo/iao.owl
[](contributor)
### contributor
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/contributor`
[](member)
### member
Property | Value
--- | ---
URI | `http://purl.org/dc/elements/1.1/member`
[](isDefinedBy)
### isDefinedBy
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#isDefinedBy`
[](seeAlso)
### seeAlso
Property | Value
--- | ---
URI | `http://www.w3.org/2000/01/rdf-schema#seeAlso`
[](homepage)
### homepage
Property | Value
--- | ---
URI | `http://xmlns.com/foaf/0.1/homepage`

## Named Individuals
## Namespaces
* **cdao**
  * `http://purl.obolibrary.org/obo/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
* **meat**
  * `http://example.com/`
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