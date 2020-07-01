Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.6

# Description of a Project (DOAP) vocabulary

## Metadata
* **URI**
  * `http://usefulinc.com/ns/doap#`
* **Creators(s)**
  * Edd Wilder-James
* **Imports**
  * [foaf:index.rdf](http://xmlns.com/foaf/0.1/index.rdf)
* **Ontology RDF**
  * RDF ([doap.ttl](turtle))
### Description
<p>El vocabulario Description of a Project (DOAP, DescripciÃ³n de un Proyecto), descrito usando RDF Schema de W3C
        y Web Ontology Language.</p>

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[DÃ©pÃ´t BitKeeper](#DptBitKeeper),
[GNU Arch repository](#GNUArchrepository),
[Git Branch](#GitBranch),
[Mercurial Repository](#MercurialRepository),
[Projet](#Projet),
[RamificaÃ§Ã£o Bazaar](#RamificaoBazaar),
[Repositorio darcs](#Repositoriodarcs),
[Repository](#Repository),
[RepositÃ³rio CVS](#RepositrioCVS),
[RepositÃ³rio Git](#RepositrioGit),
[Specification](#Specification),
[Subversion Repository](#SubversionRepository),
[VersiÃ³n](#Versin),
### GNU Arch repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#ArchRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>ÃšloÅ¾iÅ¡tÄ› zdrojovÃ½ch kÃ³dÅ¯ GNU Arch.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### DÃ©pÃ´t BitKeeper
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#BKRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio BitKeeper do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RamificaÃ§Ã£o Bazaar
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#BazaarBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Bazaar source code branch.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio CVS
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#CVSRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio CVS do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Repositorio darcs
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#DarcsRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>DÃ©pÃ´t darcs du code source.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Git Branch
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#GitBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Git source code branch.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio Git
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#GitRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Git Quellcode-Versionierungssystem.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Mercurial Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#HgRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio Mercurial do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Projet
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Project`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Projekt.</p>
Super-classes |[foaf:Project](http://xmlns.com/foaf/0.1/Project) (c)<br />[http://xmlns.com/wordnet/1.6/Project](http://xmlns.com/wordnet/1.6/Project) (c)<br />
In domain of |[doap:developer](http://usefulinc.com/ns/doap#developer)<br />[doap:programming-language](http://usefulinc.com/ns/doap#programming-language)<br />[doap:translator](http://usefulinc.com/ns/doap#translator)<br />[doap:mailing-list](http://usefulinc.com/ns/doap#mailing-list)<br />[doap:old-homepage](http://usefulinc.com/ns/doap#old-homepage)<br />[doap:wiki](http://usefulinc.com/ns/doap#wiki)<br />[doap:vendor](http://usefulinc.com/ns/doap#vendor)<br />[doap:helper](http://usefulinc.com/ns/doap#helper)<br />[doap:category](http://usefulinc.com/ns/doap#category)<br />[doap:language](http://usefulinc.com/ns/doap#language)<br />[doap:implements](http://usefulinc.com/ns/doap#implements)<br />[doap:bug-database](http://usefulinc.com/ns/doap#bug-database)<br />[doap:tester](http://usefulinc.com/ns/doap#tester)<br />[doap:blog](http://usefulinc.com/ns/doap#blog)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:service-endpoint](http://usefulinc.com/ns/doap#service-endpoint)<br />[doap:audience](http://usefulinc.com/ns/doap#audience)<br />[doap:support-forum](http://usefulinc.com/ns/doap#support-forum)<br />[doap:developer-forum](http://usefulinc.com/ns/doap#developer-forum)<br />[doap:documenter](http://usefulinc.com/ns/doap#documenter)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:release](http://usefulinc.com/ns/doap#release)<br />[doap:maintainer](http://usefulinc.com/ns/doap#maintainer)<br />[doap:homepage](http://usefulinc.com/ns/doap#homepage)<br />[doap:download-page](http://usefulinc.com/ns/doap#download-page)<br />[doap:repository](http://usefulinc.com/ns/doap#repository)<br />[doap:download-mirror](http://usefulinc.com/ns/doap#download-mirror)<br />[doap:screenshots](http://usefulinc.com/ns/doap#screenshots)<br />
In range of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />
### Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio do cÃ³digo fonte.</p>
Sub-classes |[doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c)<br />[doap:GitRepository](http://usefulinc.com/ns/doap#GitRepository) (c)<br />[doap:SVNRepository](http://usefulinc.com/ns/doap#SVNRepository) (c)<br />[doap:DarcsRepository](http://usefulinc.com/ns/doap#DarcsRepository) (c)<br />[doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c)<br />[doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c)<br />[doap:HgRepository](http://usefulinc.com/ns/doap#HgRepository) (c)<br />[doap:GitBranch](http://usefulinc.com/ns/doap#GitBranch) (c)<br />[doap:BazaarBranch](http://usefulinc.com/ns/doap#BazaarBranch) (c)<br />
In domain of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />[doap:anon-root](http://usefulinc.com/ns/doap#anon-root)<br />[doap:browse](http://usefulinc.com/ns/doap#browse)<br />[doap:location](http://usefulinc.com/ns/doap#location)<br />
In range of |[doap:repository](http://usefulinc.com/ns/doap#repository)<br />
### Subversion Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#SVNRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Subversion Quellcode-Versionierungssystem.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Specification
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Specification`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>A specification of a system's aspects, technical or otherwise.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In range of |[doap:implements](http://usefulinc.com/ns/doap#implements)<br />
### VersiÃ³n
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Version`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>InformaÃ§Ã£o sobre a versÃ£o do projeto lanÃ§ado.</p>
In domain of |[doap:file-release](http://usefulinc.com/ns/doap#file-release)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:revision](http://usefulinc.com/ns/doap#revision)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />
In range of |[doap:release](http://usefulinc.com/ns/doap#release)<br />

## Properties
[anonymous root](#anonymousroot),
[audience](#audience),
[blog](#blog),
[visualiser](#visualiser),
[base de dados de bugs](#basededadosdebugs),
[Kategorie](#Kategorie),
[vytvoÅ™eno](#vytvoeno),
[description](#description),
[developer](#developer),
[developer forum](#developerforum),
[documenter](#documenter),
[mirror de descarga](#mirrordedescarga),
[pÃ¡gina para download](#pginaparadownload),
[publicaÃ§Ã£o do ficheiro](#publicaodoficheiro),
[spoluautor](#spoluautor),
[page web](#pageweb),
[EspecificaÃ§Ãµes para implementaÃ§Ã£o](#Especificaesparaimplementao),
[language](#language),
[license](#license),
[umÃ­stÄ›nÃ­ ÃºloÅ¾iÅ¡tÄ›](#umstnloit),
[eâ€“mailovÃ¡ diskuse](#emailovdiskuse),
[maintainer](#maintainer),
[module](#module),
[nombre](#nombre),
[pÃ¡gina web antiga](#pginawebantiga),
[sistema operativo](#sistemaoperativo),
[plataforma](#plataforma),
[langage de programmation](#langagedeprogrammation),
[release](#release),
[repository](#repository),
[repository of](#repositoryof),
[Version](#Version),
[capturas de ecrÃ£s](#capturasdeecrs),
[service endpoint](#serviceendpoint),
[Kurzbeschreibung](#Kurzbeschreibung),
[supporting forum](#supportingforum),
[tester](#tester),
[tradutor](#tradutor),
[vendor](#vendor),
[wiki](#wiki),
[](anonymousroot)
### anonymous root
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#anon-root`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Repositorio para acceso anÃ³nimo.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](audience)
### audience
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#audience`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Description of target user base
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](blog)
### blog
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#blog`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI de um blog relacionado com um projeto
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />[http://rdfs.org/sioc/types#Weblog](http://rdfs.org/sioc/types#Weblog) (c)<br />
[](visualiser)
### visualiser
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#browse`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Interface web au dÃ©pÃ´t.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](basededadosdebugs)
### base de dados de bugs
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#bug-database`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Bug tracker para un proyecto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](Kategorie)
### Kategorie
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#category`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A category of project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](vytvoeno)
### vytvoÅ™eno
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#created`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Erstellungsdatum von Irgendwas, angegeben im YYYY-MM-DD Format, z.B. 2004-04-05.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](description)
### description
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#description`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Texte descriptif d'un projet, long de 2 Ã  4 phrases.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](developer)
### developer
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#developer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DÃ©veloppeur pour le projet.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](developerforum)
### developer forum
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#developer-forum`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A forum or community for developers of this project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/ns#Container](http://rdfs.org/sioc/ns#Container) (c)<br />
[](documenter)
### documenter
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#documenter`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Mitarbeiter an der Dokumentation eines Projektes.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](mirrordedescarga)
### mirror de descarga
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#download-mirror`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Mirror da pÃ¡gina web para fazer download.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](pginaparadownload)
### pÃ¡gina para download
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#download-page`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Page web Ã  partir de laquelle on peut tÃ©lÃ©charger le programme.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](publicaodoficheiro)
### publicaÃ§Ã£o do ficheiro
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#file-release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI adresa staÅ¾enÃ­ asociovanÃ© s revizÃ­.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](spoluautor)
### spoluautor
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#helper`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Collaborateur au projet.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](pageweb)
### page web
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | El URL de la pÃ¡gina de un proyecto, 		asociada con exactamente un proyecto.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](Especificaesparaimplementao)
### EspecificaÃ§Ãµes para implementaÃ§Ã£o
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#implements`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A specification that a project implements. Could be a standard, API or legally defined level of conformance.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Specification](http://usefulinc.com/ns/doap#Specification) (c)<br />
[](language)
### language
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | CÃ³digo de idioma ISO do projeto para o qual foi traduzido
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](license)
### license
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#license`
Is Defined By | http://usefulinc.com/ns/doap#
Description | The URI of an RDF description of the license the software is distributed under. E.g. a SPDX reference
[](umstnloit)
### umÃ­stÄ›nÃ­ ÃºloÅ¾iÅ¡tÄ›
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#location`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Location of a repository.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](emailovdiskuse)
### eâ€“mailovÃ¡ diskuse
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#mailing-list`
Is Defined By | http://usefulinc.com/ns/doap#
Description | PÃ¡gina web de la lista de correo o direcciÃ³n de correo.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#MailingList](http://rdfs.org/sioc/types#MailingList) (c)<br />
[](maintainer)
### maintainer
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#maintainer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Maintainer of a project, a project leader.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](module)
### module
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#module`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Nom du module d'un dÃ©pÃ´t Subversion, CVS, BitKeeper ou Arch.
Domain(s) |([doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c) or [doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c) or [doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c))<br />
[](nombre)
### nombre
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#name`
Is Defined By | http://usefulinc.com/ns/doap#
Description | O nome de alguma coisa.
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](pginawebantiga)
### pÃ¡gina web antiga
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#old-homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URL der letzten Projekt-Homepage, 		verbunden mit genau einem Projekt.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](sistemaoperativo)
### sistema operativo
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#os`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Sistema operativo a que o projeto estÃ¡ limitado. Omita esta propriedade se o projeto nÃ£o Ã© condicionado pelo SO usado.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](plataforma)
### plataforma
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#platform`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indicator of software platform (non-OS specific), e.g. Java, Firefox, ECMA CLR
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](langagedeprogrammation)
### langage de programmation
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#programming-language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Linguagem de programaÃ§Ã£o que o projeto usa ou Ã© para ser utilizada.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](release)
### release
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Une release (rÃ©vision) d'un projet.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](repository)
### repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DÃ©pÃ´t du code source.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](repositoryof)
### repository of
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#repositoryOf`
Is Defined By | http://usefulinc.com/ns/doap#
Description | The project that uses a repository.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
Range(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](Version)
### Version
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#revision`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indentificador de la versiÃ³n de un release de software.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](capturasdeecrs)
### capturas de ecrÃ£s
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#screenshots`
Is Defined By | http://usefulinc.com/ns/doap#
Description | PÃ¡gina web com as capturas de ecrÃ£n do projeto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](serviceendpoint)
### service endpoint
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#service-endpoint`
Is Defined By | http://usefulinc.com/ns/doap#
Description | The URI of a web service endpoint where software as a service may be accessed
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](Kurzbeschreibung)
### Kurzbeschreibung
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#shortdesc`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Texte descriptif concis (8 ou 9 mots) d'un projet.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](supportingforum)
### supporting forum
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#support-forum`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A forum or community that supports this project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/ns#Container](http://rdfs.org/sioc/ns#Container) (c)<br />
[](tester)
### tester
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#tester`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A tester or other quality control contributor.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](tradutor)
### tradutor
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#translator`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Collaborateur Ã  la traduction du projet.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](vendor)
### vendor
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#vendor`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Vendor organization: commercial, free or otherwise
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Organization](http://xmlns.com/foaf/0.1/Organization) (c)<br />
[](wiki)
### wiki
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#wiki`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URL adresa wiki projektu pro spoleÄnÃ© diskuse.
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