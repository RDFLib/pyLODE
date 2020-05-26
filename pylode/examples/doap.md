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
<p>SlovnÃ­k Description of a Project (DOAP, Popis projektu), popsanÃ½ pouÅ¾itÃ­m W3C RDF Schema a Web Ontology Language.</p>

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Bazaar Branch](#BazaarBranch),
[CVS Repository](#CVSRepository),
[DÃ©pÃ´t darcs](#Dptdarcs),
[Git Branch](#GitBranch),
[Git Repository](#GitRepository),
[Proyecto](#Proyecto),
[Repositorio](#Repositorio),
[Repositorio BitKeeper](#RepositorioBitKeeper),
[Repositorio Subversion](#RepositorioSubversion),
[RepositÃ³rio GNU Arch](#RepositrioGNUArch),
[RepositÃ³rio Mercurial](#RepositrioMercurial),
[Specification](#Specification),
[VersiÃ³n](#Versin),
### RepositÃ³rio GNU Arch
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#ArchRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio GNU Arch do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Repositorio BitKeeper
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BKRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio BitKeeper do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Bazaar Branch
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BazaarBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>CÃ³digo fonte da ramificaÃ§Ã£o Bazaar.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### CVS Repository
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#CVSRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>CVS source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### DÃ©pÃ´t darcs
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
### Git Repository
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#GitRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio Git do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### RepositÃ³rio Mercurial
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#HgRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>RepositÃ³rio Mercurial do cÃ³digo fonte.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Proyecto
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Project`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Un projet.</p>
Super-classes |[foaf:Project](http://xmlns.com/foaf/0.1/Project) (c)<br />[http://xmlns.com/wordnet/1.6/Project](http://xmlns.com/wordnet/1.6/Project) (c)<br />
In domain of |[doap:maintainer](http://usefulinc.com/ns/doap#maintainer)<br />[doap:documenter](http://usefulinc.com/ns/doap#documenter)<br />[doap:bug-database](http://usefulinc.com/ns/doap#bug-database)<br />[doap:developer-forum](http://usefulinc.com/ns/doap#developer-forum)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:vendor](http://usefulinc.com/ns/doap#vendor)<br />[doap:download-mirror](http://usefulinc.com/ns/doap#download-mirror)<br />[doap:old-homepage](http://usefulinc.com/ns/doap#old-homepage)<br />[doap:implements](http://usefulinc.com/ns/doap#implements)<br />[doap:release](http://usefulinc.com/ns/doap#release)<br />[doap:programming-language](http://usefulinc.com/ns/doap#programming-language)<br />[doap:category](http://usefulinc.com/ns/doap#category)<br />[doap:audience](http://usefulinc.com/ns/doap#audience)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:translator](http://usefulinc.com/ns/doap#translator)<br />[doap:mailing-list](http://usefulinc.com/ns/doap#mailing-list)<br />[doap:service-endpoint](http://usefulinc.com/ns/doap#service-endpoint)<br />[doap:download-page](http://usefulinc.com/ns/doap#download-page)<br />[doap:tester](http://usefulinc.com/ns/doap#tester)<br />[doap:blog](http://usefulinc.com/ns/doap#blog)<br />[doap:language](http://usefulinc.com/ns/doap#language)<br />[doap:helper](http://usefulinc.com/ns/doap#helper)<br />[doap:screenshots](http://usefulinc.com/ns/doap#screenshots)<br />[doap:wiki](http://usefulinc.com/ns/doap#wiki)<br />[doap:repository](http://usefulinc.com/ns/doap#repository)<br />[doap:support-forum](http://usefulinc.com/ns/doap#support-forum)<br />[doap:developer](http://usefulinc.com/ns/doap#developer)<br />[doap:homepage](http://usefulinc.com/ns/doap#homepage)<br />
In range of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />
### Repositorio
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Repositorio del cÃ³digo fuente.</p>
Sub-classes |[doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c)<br />[doap:SVNRepository](http://usefulinc.com/ns/doap#SVNRepository) (c)<br />[doap:BazaarBranch](http://usefulinc.com/ns/doap#BazaarBranch) (c)<br />[doap:DarcsRepository](http://usefulinc.com/ns/doap#DarcsRepository) (c)<br />[doap:GitRepository](http://usefulinc.com/ns/doap#GitRepository) (c)<br />[doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c)<br />[doap:HgRepository](http://usefulinc.com/ns/doap#HgRepository) (c)<br />[doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c)<br />[doap:GitBranch](http://usefulinc.com/ns/doap#GitBranch) (c)<br />
In domain of |[doap:browse](http://usefulinc.com/ns/doap#browse)<br />[doap:location](http://usefulinc.com/ns/doap#location)<br />[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />[doap:anon-root](http://usefulinc.com/ns/doap#anon-root)<br />
In range of |[doap:repository](http://usefulinc.com/ns/doap#repository)<br />
### Repositorio Subversion
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
Description | <p>A specification of a system's aspects, technical or otherwise.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In range of |[doap:implements](http://usefulinc.com/ns/doap#implements)<br />
### VersiÃ³n
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Version`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>InformaÃ§Ã£o sobre a versÃ£o do projeto lanÃ§ado.</p>
In domain of |[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:revision](http://usefulinc.com/ns/doap#revision)<br />[doap:file-release](http://usefulinc.com/ns/doap#file-release)<br />
In range of |[doap:release](http://usefulinc.com/ns/doap#release)<br />

## Properties
[raÃ­z anÃ³nima](#razannima),
[audiÃªncia](#audincia),
[blog](#blog),
[visualiser](#visualiser),
[base de dados de bugs](#basededadosdebugs),
[category](#category),
[created](#created),
[descripciÃ³n](#descripcin),
[desarrollador](#desarrollador),
[developer forum](#developerforum),
[rÃ©dacteur de l'aide](#rdacteurdel'aide),
[mirror para download](#mirrorparadownload),
[strÃ¡nka pro staÅ¾enÃ­](#strnkaprostaen),
[publicaÃ§Ã£o do ficheiro](#publicaodoficheiro),
[Helfer](#Helfer),
[homepage](#homepage),
[EspecificaÃ§Ãµes para implementaÃ§Ã£o](#Especificaesparaimplementao),
[idioma](#idioma),
[licenÃ§a](#licena),
[localizaÃ§Ã£o do respositÃ³rio](#localizaodorespositrio),
[liste de diffusion](#listedediffusion),
[Projektverantwortlicher](#Projektverantwortlicher),
[modul](#modul),
[nombre](#nombre),
[pÃ¡gina web antigua](#pginawebantigua),
[operaÄnÃ­ systÃ©m](#operansystm),
[platform](#platform),
[programovacÃ­ jazyk](#programovacjazyk),
[release](#release),
[ÃºloÅ¾iÅ¡tÄ›](#loit),
[repository of](#repositoryof),
[versiÃ³n](#versin),
[screenshots](#screenshots),
[service endpoint](#serviceendpoint),
[descripciÃ³n corta](#descripcincorta),
[supporting forum](#supportingforum),
[Tester](#Tester),
[translator](#translator),
[vendor](#vendor),
[wiki](#wiki),
[](razannima)
### raÃ­z anÃ³nima
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#anon-root`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Repositorio para acceso anÃ³nimo.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](audincia)
### audiÃªncia
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#audience`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DescriÃ§Ã£o do utilizador base alvo
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
Range(s) |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />[http://rdfs.org/sioc/types#Weblog](http://rdfs.org/sioc/types#Weblog) (c)<br />
[](visualiser)
### visualiser
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#browse`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web browser interface to repository.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](basededadosdebugs)
### base de dados de bugs
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#bug-database`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Bug tracker para un proyecto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](category)
### category
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#category`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A category of project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](created)
### created
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#created`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Fecha en la que algo fue creado, en formato AAAA-MM-DD. e.g. 2004-04-05
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](descripcin)
### descripciÃ³n
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#description`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DescriÃ§Ã£o de um projeto em texto apenas, com 2 a 4 frases de comprimento.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](desarrollador)
### desarrollador
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#developer`
Is Defined By | http://usefulinc.com/ns/doap#
Description | DÃ©veloppeur pour le projet.
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
[](rdacteurdel'aide)
### rÃ©dacteur de l'aide
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#documenter`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Collaborateur Ã  la documentation du projet.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](mirrorparadownload)
### mirror para download
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#download-mirror`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Spiegel der Seite von die Projekt-Software heruntergeladen werden kann.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](strnkaprostaen)
### strÃ¡nka pro staÅ¾enÃ­
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#download-page`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web page from which the project software can be downloaded.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](publicaodoficheiro)
### publicaÃ§Ã£o do ficheiro
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#file-release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI of download associated with this release.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](Helfer)
### Helfer
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#helper`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Colaborador del proyecto.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](homepage)
### homepage
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | O URL da pÃ¡gina de um projeto, 		asociada com exactamente um projeto.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](Especificaesparaimplementao)
### EspecificaÃ§Ãµes para implementaÃ§Ã£o
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#implements`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Uma especificaÃ§Ã£o que um projeto implementa. Pode ser uma padrÃ£o, API ou um nÃ­vel de conformidade definida legalmente.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Specification](http://usefulinc.com/ns/doap#Specification) (c)<br />
[](idioma)
### idioma
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | ISO language code a project has been translated into
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](licena)
### licenÃ§a
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#license`
Is Defined By | http://usefulinc.com/ns/doap#
Description | El URI de una descripciÃ³n RDF de la licencia bajo la cuÃ¡l se distribuye el software.
[](localizaodorespositrio)
### localizaÃ§Ã£o do respositÃ³rio
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#location`
Is Defined By | http://usefulinc.com/ns/doap#
Description | lugar de un repositorio.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](listedediffusion)
### liste de diffusion
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#mailing-list`
Is Defined By | http://usefulinc.com/ns/doap#
Description | PÃ¡gina web de la lista de correo o direcciÃ³n de correo.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[http://rdfs.org/sioc/types#MailingList](http://rdfs.org/sioc/types#MailingList) (c)<br />
[](Projektverantwortlicher)
### Projektverantwortlicher
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
[](nombre)
### nombre
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#name`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Der Name von Irgendwas
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](pginawebantigua)
### pÃ¡gina web antigua
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#old-homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | L'URL d'une ancienne page web d'un 		projet, associÃ©e avec un unique projet.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](operansystm)
### operaÄnÃ­ systÃ©m
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#os`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Sistema opertivo al cuÃ¡l estÃ¡ limitado el proyecto.  Omita esta propiedad si el proyecto no es especÃ­fico 		de un sistema opertaivo en particular.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](platform)
### platform
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#platform`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indicator of software platform (non-OS specific), e.g. Java, Firefox, ECMA CLR
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](programovacjazyk)
### programovacÃ­ jazyk
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#programming-language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Programming language a project is implemented in or intended for use with.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](release)
### release
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Relase (verze) projektu.
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
[](versin)
### versiÃ³n
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#revision`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indentificador de la versiÃ³n de un release de software.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](screenshots)
### screenshots
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#screenshots`
Is Defined By | http://usefulinc.com/ns/doap#
Description | PÃ¡gina web con capturas de pantalla del proyecto.
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
[](descripcincorta)
### descripciÃ³n corta
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#shortdesc`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Short (8 or 9 words) plain text description of a project.
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
Description | Ein Tester oder anderer Mitarbeiter der QualitÃ¤tskontrolle.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](translator)
### translator
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#translator`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Contributor of translations to the project.
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