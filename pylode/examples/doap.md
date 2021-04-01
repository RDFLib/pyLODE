Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.6

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
<p>VocabulÃ¡rio de descriÃ§Ã£o de um Projeto (DOAP - Description of a Project), descrito no esquema (schema) W3C RDF e na Web Ontology Language.</p>

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[DÃ©pÃ´t GNU Arch](#DptGNUArch),
[Git Repository](#GitRepository),
[Projekt](#Projekt),
[RamificaÃ§Ã£o Bazaar](#RamificaoBazaar),
[RamificaÃ§Ã£o Git](#RamificaoGit),
[Repository](#Repository),
[RepositÃ³rio Bitkeeper](#RepositrioBitkeeper),
[RepositÃ³rio CVS](#RepositrioCVS),
[RepositÃ³rio Mercurial](#RepositrioMercurial),
[RepositÃ³rio Subversion](#RepositrioSubversion),
[Specification](#Specification),
[Verze](#Verze),
[darcs Repository](#darcsRepository),
### DÃ©pÃ´t GNU Arch
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#ArchRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>GNU Arch Quellcode-Versionierungssystem.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio Bitkeeper
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#BKRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>BitKeeper Quellcode-Versionierungssystem.</p>
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
Description | <p>Repositorio CVS del cÃ³digo fuente.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### darcs Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#DarcsRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>DÃ©pÃ´t darcs du code source.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RamificaÃ§Ã£o Git
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#GitBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>CÃ³digo fonte da ramificaÃ§Ã£o Git.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Git Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#GitRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>DÃ©pÃ´t Git du code source.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio Mercurial
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#HgRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio Mercurial do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Projekt
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Project`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Ein Projekt.</p>
Super-classes |[http://xmlns.com/wordnet/1.6/Project](http://xmlns.com/wordnet/1.6/Project) (c)<br />[foaf:Project](http://xmlns.com/foaf/0.1/Project) (c)<br />
In domain of |[doap:blog](http://usefulinc.com/ns/doap#blog)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:audience](http://usefulinc.com/ns/doap#audience)<br />[doap:repository](http://usefulinc.com/ns/doap#repository)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:screenshots](http://usefulinc.com/ns/doap#screenshots)<br />[doap:homepage](http://usefulinc.com/ns/doap#homepage)<br />[doap:tester](http://usefulinc.com/ns/doap#tester)<br />[doap:implements](http://usefulinc.com/ns/doap#implements)<br />[doap:service-endpoint](http://usefulinc.com/ns/doap#service-endpoint)<br />[doap:category](http://usefulinc.com/ns/doap#category)<br />[doap:old-homepage](http://usefulinc.com/ns/doap#old-homepage)<br />[doap:download-page](http://usefulinc.com/ns/doap#download-page)<br />[doap:bug-database](http://usefulinc.com/ns/doap#bug-database)<br />[doap:mailing-list](http://usefulinc.com/ns/doap#mailing-list)<br />[doap:developer](http://usefulinc.com/ns/doap#developer)<br />[doap:download-mirror](http://usefulinc.com/ns/doap#download-mirror)<br />[doap:language](http://usefulinc.com/ns/doap#language)<br />[doap:documenter](http://usefulinc.com/ns/doap#documenter)<br />[doap:vendor](http://usefulinc.com/ns/doap#vendor)<br />[doap:helper](http://usefulinc.com/ns/doap#helper)<br />[doap:developer-forum](http://usefulinc.com/ns/doap#developer-forum)<br />[doap:maintainer](http://usefulinc.com/ns/doap#maintainer)<br />[doap:wiki](http://usefulinc.com/ns/doap#wiki)<br />[doap:translator](http://usefulinc.com/ns/doap#translator)<br />[doap:release](http://usefulinc.com/ns/doap#release)<br />[doap:support-forum](http://usefulinc.com/ns/doap#support-forum)<br />[doap:programming-language](http://usefulinc.com/ns/doap#programming-language)<br />
In range of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />
### Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Repositorio del cÃ³digo fuente.</p>
Sub-classes |[doap:GitBranch](http://usefulinc.com/ns/doap#GitBranch) (c)<br />[doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c)<br />[doap:DarcsRepository](http://usefulinc.com/ns/doap#DarcsRepository) (c)<br />[doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c)<br />[doap:BazaarBranch](http://usefulinc.com/ns/doap#BazaarBranch) (c)<br />[doap:HgRepository](http://usefulinc.com/ns/doap#HgRepository) (c)<br />[doap:SVNRepository](http://usefulinc.com/ns/doap#SVNRepository) (c)<br />[doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c)<br />[doap:GitRepository](http://usefulinc.com/ns/doap#GitRepository) (c)<br />
In domain of |[doap:browse](http://usefulinc.com/ns/doap#browse)<br />[doap:location](http://usefulinc.com/ns/doap#location)<br />[doap:anon-root](http://usefulinc.com/ns/doap#anon-root)<br />[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />
In range of |[doap:repository](http://usefulinc.com/ns/doap#repository)<br />
### RepositÃ³rio Subversion
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#SVNRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>DÃ©pÃ´t Subversion du code source.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Specification
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Specification`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>A especificaÃ§Ã£o de aspetos, tÃ©cnicas ou outros do sistema.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In range of |[doap:implements](http://usefulinc.com/ns/doap#implements)<br />
### Verze
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Version`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>InformaÃ§Ã£o sobre a versÃ£o do projeto lanÃ§ado.</p>
In domain of |[doap:file-release](http://usefulinc.com/ns/doap#file-release)<br />[doap:revision](http://usefulinc.com/ns/doap#revision)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />
In range of |[doap:release](http://usefulinc.com/ns/doap#release)<br />

## Properties
[Anonymes Root](#AnonymesRoot),
[audiÃªncia](#audincia),
[blog](#blog),
[navegar](#navegar),
[base de datos de bugs](#basededatosdebugs),
[categoria](#categoria),
[creado](#creado),
[descriÃ§Ã£o](#descrio),
[developer](#developer),
[developer forum](#developerforum),
[documenter](#documenter),
[Spiegel der Seite zum Herunterladen](#SpiegelderSeitezumHerunterladen),
[Seite zum Herunterladen](#SeitezumHerunterladen),
[soubor revize](#souborrevize),
[helper](#helper),
[pÃ¡gina web](#pginaweb),
[Implements specification](#Implementsspecification),
[language](#language),
[licence](#licence),
[localizaÃ§Ã£o do respositÃ³rio](#localizaodorespositrio),
[liste de diffusion](#listedediffusion),
[programador principal](#programadorprincipal),
[Modul](#Modul),
[nombre](#nombre),
[Alte Homepage](#AlteHomepage),
[sistema operativo](#sistemaoperativo),
[plataforma](#plataforma),
[lenguaje de programaciÃ³n](#lenguajedeprogramacin),
[release](#release),
[repositÃ³rio](#repositrio),
[repository of](#repositoryof),
[rÃ©vision](#rvision),
[snÃ­mek obrazovky](#snmekobrazovky),
[service endpoint](#serviceendpoint),
[description courte](#descriptioncourte),
[supporting forum](#supportingforum),
[tester](#tester),
[pÅ™ekladatel](#pekladatel),
[vendor](#vendor),
[wiki](#wiki),
[](AnonymesRoot)
### Anonymes Root
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#anon-root`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Repository fÃ¼r anonymen Zugriff
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](audincia)
### audiÃªncia
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
Description | URI of a blog related to a project
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />[http://rdfs.org/sioc/types#Weblog](http://rdfs.org/sioc/types#Weblog) (c)<br />
[](navegar)
### navegar
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#browse`
Is Defined By | http://usefulinc.com/ns/doap#
Description | WebovÃ© rozhranÃ­ pro prohlÃ­Å¾enÃ­ ÃºloÅ¾iÅ¡tÄ›.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](basededatosdebugs)
### base de datos de bugs
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#bug-database`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Bug tracker para um projeto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](categoria)
### categoria
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#category`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Kategorie projektu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](creado)
### creado
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#created`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Erstellungsdatum von Irgendwas, angegeben im YYYY-MM-DD Format, z.B. 2004-04-05.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](descrio)
### descriÃ§Ã£o
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#description`
Is Defined By | http://usefulinc.com/ns/doap#
Description | ÄŒistÄ› textovÃ½, 2 aÅ¾ 4 vÄ›ty dlouhÃ½ popis projektu.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](developer)
### developer
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#developer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Developer of software for the project.
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
[](SpiegelderSeitezumHerunterladen)
### Spiegel der Seite zum Herunterladen
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#download-mirror`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Miroir de la page de tÃ©lÃ©chargement du programme.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](SeitezumHerunterladen)
### Seite zum Herunterladen
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#download-page`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web-Seite von der die Projekt-Software heruntergeladen werden kann.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](souborrevize)
### soubor revize
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#file-release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI adresa staÅ¾enÃ­ asociovanÃ© s revizÃ­.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](helper)
### helper
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#helper`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Spoluautor projektu.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](pginaweb)
### pÃ¡gina web
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URL of a project's homepage, 		associated with exactly one project.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](Implementsspecification)
### Implements specification
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
[](licence)
### licence
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#license`
Is Defined By | http://usefulinc.com/ns/doap#
Description | El URI de una descripciÃ³n RDF de la licencia bajo la cuÃ¡l se distribuye el software.
[](localizaodorespositrio)
### localizaÃ§Ã£o do respositÃ³rio
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#location`
Is Defined By | http://usefulinc.com/ns/doap#
Description | lugar de un repositorio.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](listedediffusion)
### liste de diffusion
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#mailing-list`
Is Defined By | http://usefulinc.com/ns/doap#
Description | PÃ¡gina web de la lista de correo o direcciÃ³n de correo.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#MailingList](http://rdfs.org/sioc/types#MailingList) (c)<br />
[](programadorprincipal)
### programador principal
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#maintainer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Maintainer of a project, a project leader.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](Modul)
### Modul
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#module`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Module name of a Subversion, CVS, BitKeeper or Arch repository.
Domain(s) |([doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c) or [doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c) or [doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c))<br />
[](nombre)
### nombre
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#name`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Le nom de quelque chose.
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](AlteHomepage)
### Alte Homepage
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#old-homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URL of a project's past homepage, 		associated with exactly one project.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](sistemaoperativo)
### sistema operativo
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#os`
Is Defined By | http://usefulinc.com/ns/doap#
Description | SystÃ¨me d'exploitation auquel est limitÃ© le projet. Omettez cette propriÃ©tÃ© si le 		projet n'est pas limitÃ© Ã  un systÃ¨me d'exploitation.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](plataforma)
### plataforma
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#platform`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indicador da plataforma do software (nÃ£o especÃ­fico a nenhum SO), ex.: Java, Firefox, ECMA CLR
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](lenguajedeprogramacin)
### lenguaje de programaciÃ³n
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#programming-language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Langage de programmation avec lequel un projet est implÃ©mentÃ©, 		ou avec lequel il est prÃ©vu de l'utiliser.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](release)
### release
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Ein Release (Version) eines Projekts.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](repositrio)
### repositÃ³rio
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | RepositÃ³rio do cÃ³digo fonte.
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
[](rvision)
### rÃ©vision
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#revision`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Revision identifier of a software release.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](snmekobrazovky)
### snÃ­mek obrazovky
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
[](descriptioncourte)
### description courte
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#shortdesc`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Kurzbeschreibung (8 oder 9 WÃ¶rter) eines Projects als einfacher Text.
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
[](pekladatel)
### pÅ™ekladatel
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#translator`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Mitarbeiter an den Ãœbersetzungen eines Projektes.
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
Description | Wiki-URL fÃ¼r die kollaborative Dikussion eines Projektes.
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