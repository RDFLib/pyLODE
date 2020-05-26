Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.4

# Description of a Project (DOAP) vocabulary

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
<p>Le vocabulaire Description Of A Project (DOAP, Description D'Un Projet),
        dÃ©crit en utilisant RDF Schema du W3C et OWL.</p>

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Bazaar Branch](#BazaarBranch),
[Git Branch](#GitBranch),
[Project](#Project),
[Repositorio Git](#RepositorioGit),
[Repository](#Repository),
[RepositÃ³rio CVS](#RepositrioCVS),
[RepositÃ³rio Mercurial](#RepositrioMercurial),
[RepositÃ³rio darcs](#Repositriodarcs),
[Specification](#Specification),
[Subversion Repository](#SubversionRepository),
[Verze](#Verze),
[ÃšloÅ¾iÅ¡tÄ› BitKeeper](#loitBitKeeper),
[ÃšloÅ¾iÅ¡tÄ› GNU Arch](#loitGNUArch),
### ÃšloÅ¾iÅ¡tÄ› GNU Arch
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#ArchRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>GNU Arch Quellcode-Versionierungssystem.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### ÃšloÅ¾iÅ¡tÄ› BitKeeper
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BKRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>BitKeeper source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Bazaar Branch
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BazaarBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Bazaar source code branch.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio CVS
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#CVSRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio CVS do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio darcs
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#DarcsRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>darcs source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Git Branch
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#GitBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>CÃ³digo fonte da ramificaÃ§Ã£o Git.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Repositorio Git
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#GitRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Git source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio Mercurial
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#HgRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio Mercurial do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Project
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Project`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Un proyecto.</p>
Super-classes |[http://xmlns.com/wordnet/1.6/Project](http://xmlns.com/wordnet/1.6/Project) (c)<br />[foaf:Project](http://xmlns.com/foaf/0.1/Project) (c)<br />
In domain of |[doap:bug-database](http://usefulinc.com/ns/doap#bug-database)<br />[doap:support-forum](http://usefulinc.com/ns/doap#support-forum)<br />[doap:vendor](http://usefulinc.com/ns/doap#vendor)<br />[doap:documenter](http://usefulinc.com/ns/doap#documenter)<br />[doap:language](http://usefulinc.com/ns/doap#language)<br />[doap:service-endpoint](http://usefulinc.com/ns/doap#service-endpoint)<br />[doap:developer-forum](http://usefulinc.com/ns/doap#developer-forum)<br />[doap:developer](http://usefulinc.com/ns/doap#developer)<br />[doap:maintainer](http://usefulinc.com/ns/doap#maintainer)<br />[doap:screenshots](http://usefulinc.com/ns/doap#screenshots)<br />[doap:download-page](http://usefulinc.com/ns/doap#download-page)<br />[doap:release](http://usefulinc.com/ns/doap#release)<br />[doap:category](http://usefulinc.com/ns/doap#category)<br />[doap:programming-language](http://usefulinc.com/ns/doap#programming-language)<br />[doap:wiki](http://usefulinc.com/ns/doap#wiki)<br />[doap:old-homepage](http://usefulinc.com/ns/doap#old-homepage)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:repository](http://usefulinc.com/ns/doap#repository)<br />[doap:implements](http://usefulinc.com/ns/doap#implements)<br />[doap:blog](http://usefulinc.com/ns/doap#blog)<br />[doap:mailing-list](http://usefulinc.com/ns/doap#mailing-list)<br />[doap:homepage](http://usefulinc.com/ns/doap#homepage)<br />[doap:audience](http://usefulinc.com/ns/doap#audience)<br />[doap:download-mirror](http://usefulinc.com/ns/doap#download-mirror)<br />[doap:translator](http://usefulinc.com/ns/doap#translator)<br />[doap:tester](http://usefulinc.com/ns/doap#tester)<br />[doap:helper](http://usefulinc.com/ns/doap#helper)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />
In range of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />
### Repository
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>ÃšloÅ¾iÅ¡tÄ› zdrojovÃ½ch kÃ³dÅ¯.</p>
Sub-classes |[doap:DarcsRepository](http://usefulinc.com/ns/doap#DarcsRepository) (c)<br />[doap:BazaarBranch](http://usefulinc.com/ns/doap#BazaarBranch) (c)<br />[doap:GitBranch](http://usefulinc.com/ns/doap#GitBranch) (c)<br />[doap:HgRepository](http://usefulinc.com/ns/doap#HgRepository) (c)<br />[doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c)<br />[doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c)<br />[doap:GitRepository](http://usefulinc.com/ns/doap#GitRepository) (c)<br />[doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c)<br />[doap:SVNRepository](http://usefulinc.com/ns/doap#SVNRepository) (c)<br />
In domain of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />[doap:browse](http://usefulinc.com/ns/doap#browse)<br />[doap:location](http://usefulinc.com/ns/doap#location)<br />[doap:anon-root](http://usefulinc.com/ns/doap#anon-root)<br />
In range of |[doap:repository](http://usefulinc.com/ns/doap#repository)<br />
### Subversion Repository
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#SVNRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Subversion source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Specification
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Specification`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>A especificaÃ§Ã£o de aspetos, tÃ©cnicas ou outros do sistema.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In range of |[doap:implements](http://usefulinc.com/ns/doap#implements)<br />
### Verze
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Version`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Versionsinformation eines Projekt Releases.</p>
In domain of |[doap:revision](http://usefulinc.com/ns/doap#revision)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:file-release](http://usefulinc.com/ns/doap#file-release)<br />
In range of |[doap:release](http://usefulinc.com/ns/doap#release)<br />

## Properties
[anonymnÃ­ koÅ™en](#anonymnkoen),
[audience](#audience),
[blog](#blog),
[navegar](#navegar),
[bug database](#bugdatabase),
[categoria](#categoria),
[crÃ©Ã©](#cr),
[Beschreibung](#Beschreibung),
[vÃ½vojÃ¡Å™](#vvoj),
[developer forum](#developerforum),
[documentador](#documentador),
[download mirror](#downloadmirror),
[Seite zum Herunterladen](#SeitezumHerunterladen),
[file-release](#file-release),
[Helfer](#Helfer),
[homepage](#homepage),
[Implements specification](#Implementsspecification),
[language](#language),
[licence](#licence),
[umÃ­stÄ›nÃ­ ÃºloÅ¾iÅ¡tÄ›](#umstnloit),
[eâ€“mailovÃ¡ diskuse](#emailovdiskuse),
[desarrollador principal](#desarrolladorprincipal),
[modul](#modul),
[name](#name),
[pÃ¡gina web antiga](#pginawebantiga),
[systÃ¨me d'exploitation](#systmed'exploitation),
[platform](#platform),
[programovacÃ­ jazyk](#programovacjazyk),
[release](#release),
[dÃ©pÃ´t](#dpt),
[repository of](#repositoryof),
[rÃ©vision](#rvision),
[Screenshots](#Screenshots),
[service endpoint](#serviceendpoint),
[short description](#shortdescription),
[supporting forum](#supportingforum),
[controlador](#controlador),
[translator](#translator),
[vendor](#vendor),
[wiki](#wiki),
[](anonymnkoen)
### anonymnÃ­ koÅ™en
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#anon-root`
Is Defined By | http://usefulinc.com/ns/doap#
Description | RepositÃ³rio para acesso anÃ³nimo.
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
Description | URI de um blog relacionado com um projeto
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#Weblog](http://rdfs.org/sioc/types#Weblog) (c)<br />[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](navegar)
### navegar
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#browse`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Interface web au dÃ©pÃ´t.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](bugdatabase)
### bug database
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#bug-database`
Is Defined By | http://usefulinc.com/ns/doap#
Description | SprÃ¡va chyb projektu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](categoria)
### categoria
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#category`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Kategorie projektu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](cr)
### crÃ©Ã©
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#created`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Fecha en la que algo fue creado, en formato AAAA-MM-DD. e.g. 2004-04-05
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](Beschreibung)
### Beschreibung
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#description`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Beschreibung eines Projekts als einfacher Text mit der LÃ¤nge von 2 bis 4 SÃ¤tzen.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](vvoj)
### vÃ½vojÃ¡Å™
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#developer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Desarrollador de software para el proyecto.
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
[](documentador)
### documentador
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#documenter`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Mitarbeiter an der Dokumentation eines Projektes.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](downloadmirror)
### download mirror
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
[](Helfer)
### Helfer
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#helper`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Project contributor.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](homepage)
### homepage
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | El URL de la pÃ¡gina de un proyecto, 		asociada con exactamente un proyecto.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](Implementsspecification)
### Implements specification
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#implements`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Uma especificaÃ§Ã£o que um projeto implementa. Pode ser uma padrÃ£o, API ou um nÃ­vel de conformidade definida legalmente.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Specification](http://usefulinc.com/ns/doap#Specification) (c)<br />
[](language)
### language
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | CÃ³digo de idioma ISO do projeto para o qual foi traduzido
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](licence)
### licence
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#license`
Is Defined By | http://usefulinc.com/ns/doap#
Description | El URI de una descripciÃ³n RDF de la licencia bajo la cuÃ¡l se distribuye el software.
[](umstnloit)
### umÃ­stÄ›nÃ­ ÃºloÅ¾iÅ¡tÄ›
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#location`
Is Defined By | http://usefulinc.com/ns/doap#
Description | lugar de un repositorio.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](emailovdiskuse)
### eâ€“mailovÃ¡ diskuse
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#mailing-list`
Is Defined By | http://usefulinc.com/ns/doap#
Description | PÃ¡gina web de la lista de correo o direcciÃ³n de correo.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#MailingList](http://rdfs.org/sioc/types#MailingList) (c)<br />
[](desarrolladorprincipal)
### desarrollador principal
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#maintainer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Maintainer of a project, a project leader.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](modul)
### modul
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#module`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Module name of a Subversion, CVS, BitKeeper or Arch repository.
Domain(s) |([doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c) or [doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c) or [doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c))<br />
[](name)
### name
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#name`
Is Defined By | http://usefulinc.com/ns/doap#
Description | El nombre de algo.
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](pginawebantiga)
### pÃ¡gina web antiga
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#old-homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | L'URL d'une ancienne page web d'un 		projet, associÃ©e avec un unique projet.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](systmed'exploitation)
### systÃ¨me d'exploitation
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#os`
Is Defined By | http://usefulinc.com/ns/doap#
Description | OperaÄnÃ­ systÃ©m, na jehoÅ¾ pouÅ¾itÃ­ je projekt limitovÃ¡n. Vynechejte tuto vlastnost, pokud je projekt nezÃ¡vislÃ½ na operaÄnÃ­m systÃ©mu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](platform)
### platform
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#platform`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indicador da plataforma do software (nÃ£o especÃ­fico a nenhum SO), ex.: Java, Firefox, ECMA CLR
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](programovacjazyk)
### programovacÃ­ jazyk
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#programming-language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Langage de programmation avec lequel un projet est implÃ©mentÃ©, 		ou avec lequel il est prÃ©vu de l'utiliser.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](release)
### release
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A project release.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](dpt)
### dÃ©pÃ´t
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DÃ©pÃ´t du code source.
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
[](rvision)
### rÃ©vision
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#revision`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Identificador do lanÃ§amento da revisÃ£o do software.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](Screenshots)
### Screenshots
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#screenshots`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web page with screenshots of project.
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
[](shortdescription)
### short description
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#shortdesc`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DescripciÃ³n corta (8 o 9 palabras) en texto plano de un proyecto.
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
[](controlador)
### controlador
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#tester`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A tester or other quality control contributor.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](translator)
### translator
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
[](wiki)
### wiki
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#wiki`
Is Defined By | http://usefulinc.com/ns/doap#
Description | L'URL du Wiki pour la discussion collaborative sur le projet.
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