# Description of a Project (DOAP) vocabulary
Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)


## Metadata
* **IRI**
  * `http://usefulinc.com/ns/doap#`
* **Creators(s)**
  * Edd Wilder-James
* **Imports**
  * [foaf:index.rdf](http://xmlns.com/foaf/0.1/index.rdf)
* **Ontology RDF**
  * RDF ([doap.ttl](turtle))
### Description
<p>The Description of a Project (DOAP) vocabulary, described using W3C RDF Schema and the Web Ontology Language.</p>

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Bazaar Branch](#BazaarBranch),
[EspecificaÃ§Ã£o](#Especificao),
[GNU Arch repository](#GNUArchrepository),
[Git Branch](#GitBranch),
[Projekt](#Projekt),
[Repositorio](#Repositorio),
[Repositorio Git](#RepositorioGit),
[Repositorio Subversion](#RepositorioSubversion),
[Repositorio darcs](#Repositoriodarcs),
[RepositÃ³rio Bitkeeper](#RepositrioBitkeeper),
[RepositÃ³rio CVS](#RepositrioCVS),
[RepositÃ³rio Mercurial](#RepositrioMercurial),
[VersiÃ³n](#Versin),
### GNU Arch repository
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#ArchRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Repositorio GNU Arch del cÃ³digo fuente.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio Bitkeeper
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BKRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Repositorio BitKeeper del cÃ³digo fuente.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Bazaar Branch
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BazaarBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>CÃ³digo fonte da ramificaÃ§Ã£o Bazaar.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio CVS
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#CVSRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio CVS do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Repositorio darcs
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#DarcsRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>DÃ©pÃ´t darcs du code source.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Git Branch
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#GitBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Git source code branch.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Repositorio Git
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#GitRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>DÃ©pÃ´t Git du code source.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio Mercurial
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#HgRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Mercurial source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Projekt
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Project`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Un proyecto.</p>
Super-classes |[http://xmlns.com/wordnet/1.6/Project](http://xmlns.com/wordnet/1.6/Project) (c)<br />[foaf:Project](http://xmlns.com/foaf/0.1/Project) (c)<br />
In domain of |[doap:service-endpoint](http://usefulinc.com/ns/doap#service-endpoint)<br />[doap:download-mirror](http://usefulinc.com/ns/doap#download-mirror)<br />[doap:developer-forum](http://usefulinc.com/ns/doap#developer-forum)<br />[doap:developer](http://usefulinc.com/ns/doap#developer)<br />[doap:tester](http://usefulinc.com/ns/doap#tester)<br />[doap:language](http://usefulinc.com/ns/doap#language)<br />[doap:implements](http://usefulinc.com/ns/doap#implements)<br />[doap:maintainer](http://usefulinc.com/ns/doap#maintainer)<br />[doap:screenshots](http://usefulinc.com/ns/doap#screenshots)<br />[doap:wiki](http://usefulinc.com/ns/doap#wiki)<br />[doap:repository](http://usefulinc.com/ns/doap#repository)<br />[doap:helper](http://usefulinc.com/ns/doap#helper)<br />[doap:translator](http://usefulinc.com/ns/doap#translator)<br />[doap:mailing-list](http://usefulinc.com/ns/doap#mailing-list)<br />[doap:bug-database](http://usefulinc.com/ns/doap#bug-database)<br />[doap:vendor](http://usefulinc.com/ns/doap#vendor)<br />[doap:audience](http://usefulinc.com/ns/doap#audience)<br />[doap:programming-language](http://usefulinc.com/ns/doap#programming-language)<br />[doap:blog](http://usefulinc.com/ns/doap#blog)<br />[doap:homepage](http://usefulinc.com/ns/doap#homepage)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:download-page](http://usefulinc.com/ns/doap#download-page)<br />[doap:release](http://usefulinc.com/ns/doap#release)<br />[doap:documenter](http://usefulinc.com/ns/doap#documenter)<br />[doap:category](http://usefulinc.com/ns/doap#category)<br />[doap:old-homepage](http://usefulinc.com/ns/doap#old-homepage)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:support-forum](http://usefulinc.com/ns/doap#support-forum)<br />
In range of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />
### Repositorio
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Quellcode-Versionierungssystem.</p>
Sub-classes |[doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c)<br />[doap:BazaarBranch](http://usefulinc.com/ns/doap#BazaarBranch) (c)<br />[doap:HgRepository](http://usefulinc.com/ns/doap#HgRepository) (c)<br />[doap:DarcsRepository](http://usefulinc.com/ns/doap#DarcsRepository) (c)<br />[doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c)<br />[doap:GitBranch](http://usefulinc.com/ns/doap#GitBranch) (c)<br />[doap:SVNRepository](http://usefulinc.com/ns/doap#SVNRepository) (c)<br />[doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c)<br />[doap:GitRepository](http://usefulinc.com/ns/doap#GitRepository) (c)<br />
In domain of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />[doap:location](http://usefulinc.com/ns/doap#location)<br />[doap:browse](http://usefulinc.com/ns/doap#browse)<br />[doap:anon-root](http://usefulinc.com/ns/doap#anon-root)<br />
In range of |[doap:repository](http://usefulinc.com/ns/doap#repository)<br />
### Repositorio Subversion
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#SVNRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>ÃšloÅ¾iÅ¡tÄ› zdrojovÃ½ch kÃ³dÅ¯ Subversion.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### EspecificaÃ§Ã£o
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Specification`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>A especificaÃ§Ã£o de aspetos, tÃ©cnicas ou outros do sistema.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In range of |[doap:implements](http://usefulinc.com/ns/doap#implements)<br />
### VersiÃ³n
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Version`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Version information of a project release.</p>
In domain of |[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:revision](http://usefulinc.com/ns/doap#revision)<br />[doap:file-release](http://usefulinc.com/ns/doap#file-release)<br />
In range of |[doap:release](http://usefulinc.com/ns/doap#release)<br />

## Properties
[raÃ­z anÃ³nima](#razannima),
[audience](#audience),
[blog](#blog),
[browse](#browse),
[suivi des bugs](#suividesbugs),
[categorÃ­a](#categora),
[criado](#criado),
[description](#description),
[developer](#developer),
[developer forum](#developerforum),
[Dokumentator](#Dokumentator),
[mirror de descarga](#mirrordedescarga),
[Seite zum Herunterladen](#SeitezumHerunterladen),
[file-release](#file-release),
[colaborador](#colaborador),
[domovskÃ¡ strÃ¡nka](#domovskstrnka),
[EspecificaÃ§Ãµes para implementaÃ§Ã£o](#Especificaesparaimplementao),
[idioma](#idioma),
[Lizenz](#Lizenz),
[umÃ­stÄ›nÃ­ ÃºloÅ¾iÅ¡tÄ›](#umstnloit),
[liste de diffusion](#listedediffusion),
[maintainer](#maintainer),
[module](#module),
[nom](#nom),
[Alte Homepage](#AlteHomepage),
[systÃ¨me d'exploitation](#systmed'exploitation),
[plataforma](#plataforma),
[linguagem de programaÃ§Ã£o](#linguagemdeprogramao),
[release](#release),
[ÃºloÅ¾iÅ¡tÄ›](#loit),
[repository of](#repositoryof),
[verze](#verze),
[screenshots](#screenshots),
[service endpoint](#serviceendpoint),
[description courte](#descriptioncourte),
[supporting forum](#supportingforum),
[Tester](#Tester),
[tradutor](#tradutor),
[vendor](#vendor),
[Wiki](#Wiki),
[](razannima)
### raÃ­z anÃ³nima
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#anon-root`
Is Defined By | http://usefulinc.com/ns/doap#
Description | ÃšloÅ¾iÅ¡tÄ› pro anonymnÃ­ pÅ™Ã­stup.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](audience)
### audience
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#audience`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Description of target user base
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](blog)
### blog
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#blog`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI of a blog related to a project
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#Weblog](http://rdfs.org/sioc/types#Weblog) (c)<br />[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](browse)
### browse
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#browse`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Interface web del repositorio.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](suividesbugs)
### suivi des bugs
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#bug-database`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Suivi des bugs pour un projet.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](categora)
### categorÃ­a
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#category`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Kategorie projektu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](criado)
### criado
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#created`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Erstellungsdatum von Irgendwas, angegeben im YYYY-MM-DD Format, z.B. 2004-04-05.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](description)
### description
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#description`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DescriÃ§Ã£o de um projeto em texto apenas, com 2 a 4 frases de comprimento.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](developer)
### developer
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#developer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Developer of software for the project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](developerforum)
### developer forum
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#developer-forum`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A forum or community for developers of this project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/ns#Container](http://rdfs.org/sioc/ns#Container) (c)<br />
[](Dokumentator)
### Dokumentator
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#documenter`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Contributor of documentation to the project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](mirrordedescarga)
### mirror de descarga
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#download-mirror`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Mirror of software download web page.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](SeitezumHerunterladen)
### Seite zum Herunterladen
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#download-page`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web-Seite von der die Projekt-Software heruntergeladen werden kann.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](file-release)
### file-release
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#file-release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI adresa staÅ¾enÃ­ asociovanÃ© s revizÃ­.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](colaborador)
### colaborador
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#helper`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Spoluautor projektu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](domovskstrnka)
### domovskÃ¡ strÃ¡nka
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | O URL da pÃ¡gina de um projeto,
		asociada com exactamente um projeto.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](Especificaesparaimplementao)
### EspecificaÃ§Ãµes para implementaÃ§Ã£o
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#implements`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A specification that a project implements. Could be a standard, API or legally defined level of conformance.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Specification](http://usefulinc.com/ns/doap#Specification) (c)<br />
[](idioma)
### idioma
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | CÃ³digo de idioma ISO do projeto para o qual foi traduzido
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](Lizenz)
### Lizenz
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#license`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI adresa RDF popisu licence, pod kterou je software distribuovÃ¡n.
[](umstnloit)
### umÃ­stÄ›nÃ­ ÃºloÅ¾iÅ¡tÄ›
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#location`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Emplacement d'un dÃ©pÃ´t.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](listedediffusion)
### liste de diffusion
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#mailing-list`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Page web de la liste de diffusion, ou adresse de courriel.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#MailingList](http://rdfs.org/sioc/types#MailingList) (c)<br />
[](maintainer)
### maintainer
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#maintainer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Hauptentwickler eines Projektes, der Projektleiter
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](module)
### module
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#module`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Nome do mÃ³dulo de um repositÃ³rio Subversion, CVS, BitKeeper ou Arch.
Domain(s) |([doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c) or [doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c) or [doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c))<br />
[](nom)
### nom
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#name`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A name of something.
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](AlteHomepage)
### Alte Homepage
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#old-homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | L'URL d'une ancienne page web d'un
		projet, associÃ©e avec un unique projet.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](systmed'exploitation)
### systÃ¨me d'exploitation
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#os`
Is Defined By | http://usefulinc.com/ns/doap#
Description | SystÃ¨me d'exploitation auquel est limitÃ© le projet. Omettez cette propriÃ©tÃ© si le
		projet n'est pas limitÃ© Ã  un systÃ¨me d'exploitation.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](plataforma)
### plataforma
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#platform`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indicator of software platform (non-OS specific), e.g. Java, Firefox, ECMA CLR
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](linguagemdeprogramao)
### linguagem de programaÃ§Ã£o
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#programming-language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Langage de programmation avec lequel un projet est implÃ©mentÃ©,
		ou avec lequel il est prÃ©vu de l'utiliser.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](release)
### release
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Un release (versiÃ³n) de un proyecto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](loit)
### ÃºloÅ¾iÅ¡tÄ›
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | RepositÃ³rio do cÃ³digo fonte.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](repositoryof)
### repository of
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#repositoryOf`
Is Defined By | http://usefulinc.com/ns/doap#
Description | The project that uses a repository.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
Range(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](verze)
### verze
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#revision`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Versionsidentifikator eines Software-Releases.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](screenshots)
### screenshots
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#screenshots`
Is Defined By | http://usefulinc.com/ns/doap#
Description | PÃ¡gina web com as capturas de ecrÃ£n do projeto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](serviceendpoint)
### service endpoint
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#service-endpoint`
Is Defined By | http://usefulinc.com/ns/doap#
Description | The URI of a web service endpoint where software as a service may be accessed
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](descriptioncourte)
### description courte
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#shortdesc`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Texte descriptif concis (8 ou 9 mots) d'un projet.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](supportingforum)
### supporting forum
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#support-forum`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A forum or community that supports this project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/ns#Container](http://rdfs.org/sioc/ns#Container) (c)<br />
[](Tester)
### Tester
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#tester`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A tester or other quality control contributor.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](tradutor)
### tradutor
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#translator`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Spoluautor pÅ™ekladu projektu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](vendor)
### vendor
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#vendor`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Vendor organization: commercial, free or otherwise
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Organization](http://xmlns.com/foaf/0.1/Organization) (c)<br />
[](Wiki)
### Wiki
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#wiki`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URL da Wiki para discussÃ£o em grupo do projeto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#Wiki](http://rdfs.org/sioc/types#Wiki) (c)<br />

## Named Individuals
## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
* **foaf**
  * `http://xmlns.com/foaf/0.1/`
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
* **vs**
  * `http://www.w3.org/2003/06/sw-vocab-status/ns#`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
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