# Description of a Project (DOAP) vocabulary
<sub>metadata by [pyLODE](http://github.com/rdflib/pyLODE)</sub>
## Metadata
* **IRI**
  * `http://usefulinc.com/ns/doap#`
* **Creators(s)**
  * Edd Wilder-James
* **Imports**
  * <a href="http://xmlns.com/foaf/0.1/index.rdf">foaf</a>
* **Ontology Source**
  * <a href="doap.ttl">RDF (turtle)</a>
### Description
<p>VocabulÃ¡rio de descriÃ§Ã£o de um Projeto (DOAP - Description of a Project), descrito no esquema (schema) W3C RDF e na Web Ontology Language.</p>

## Table of Contents
1. [Classes](#classes)
1. [Properties](#properties)
1. [Namespaces](#namespaces)  
  
## Classes
[Bazaar Branch](#BazaarBranch),
[CVS Repository](#CVSRepository),
[DÃ©pÃ´t GNU Arch](#DptGNUArch),
[DÃ©pÃ´t darcs](#Dptdarcs),
[Git Branch](#GitBranch),
[Git Repository](#GitRepository),
[Mercurial Repository](#MercurialRepository),
[Projeto](#Projeto),
[Repositorio BitKeeper](#RepositorioBitKeeper),
[Repositorio Subversion](#RepositorioSubversion),
[Specification](#Specification),
[Version](#Version),
[ÃšloÅ¾iÅ¡tÄ›](#loit),
### DÃ©pÃ´t GNU Arch <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#ArchRepository`
Description | GNU Arch source code repository.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Repositorio BitKeeper <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BKRepository`
Description | Repositorio BitKeeper del cÃ³digo fuente.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Bazaar Branch <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#BazaarBranch`
Description | CÃ³digo fonte da ramificaÃ§Ã£o Bazaar.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### CVS Repository <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#CVSRepository`
Description | RepositÃ³rio CVS do cÃ³digo fonte.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### DÃ©pÃ´t darcs <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#DarcsRepository`
Description | RepositÃ³rio darcs do cÃ³digo fonte.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Git Branch <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#GitBranch`
Description | Git source code branch.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Git Repository <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#GitRepository`
Description | RepositÃ³rio Git do cÃ³digo fonte.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Mercurial Repository <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#HgRepository`
Description | RepositÃ³rio Mercurial do cÃ³digo fonte.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Projeto <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Project`
Description | Ein Projekt.
Super-classes |<a href="http://xmlns.com/wordnet/1.6/Project">http://xmlns.com/wordnet/1.6/Project</a><sup class="sup-c" title="class">c</sup><br /><a href="http://xmlns.com/foaf/0.1/Project">foaf:Project</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
In domain of |<a href="http://usefulinc.com/ns/doap#developer">doap:developer</a><br /><a href="http://usefulinc.com/ns/doap#language">doap:language</a><br /><a href="http://usefulinc.com/ns/doap#implements">doap:implements</a><br /><a href="http://usefulinc.com/ns/doap#developer-forum">doap:developer-forum</a><br /><a href="http://usefulinc.com/ns/doap#mailing-list">doap:mailing-list</a><br /><a href="http://usefulinc.com/ns/doap#documenter">doap:documenter</a><br /><a href="http://usefulinc.com/ns/doap#repository">doap:repository</a><br /><a href="http://usefulinc.com/ns/doap#tester">doap:tester</a><br /><a href="http://usefulinc.com/ns/doap#platform">doap:platform</a><br /><a href="http://usefulinc.com/ns/doap#download-mirror">doap:download-mirror</a><br /><a href="http://usefulinc.com/ns/doap#category">doap:category</a><br /><a href="http://usefulinc.com/ns/doap#blog">doap:blog</a><br /><a href="http://usefulinc.com/ns/doap#support-forum">doap:support-forum</a><br /><a href="http://usefulinc.com/ns/doap#homepage">doap:homepage</a><br /><a href="http://usefulinc.com/ns/doap#wiki">doap:wiki</a><br /><a href="http://usefulinc.com/ns/doap#vendor">doap:vendor</a><br /><a href="http://usefulinc.com/ns/doap#download-page">doap:download-page</a><br /><a href="http://usefulinc.com/ns/doap#audience">doap:audience</a><br /><a href="http://usefulinc.com/ns/doap#os">doap:os</a><br /><a href="http://usefulinc.com/ns/doap#screenshots">doap:screenshots</a><br /><a href="http://usefulinc.com/ns/doap#maintainer">doap:maintainer</a><br /><a href="http://usefulinc.com/ns/doap#old-homepage">doap:old-homepage</a><br /><a href="http://usefulinc.com/ns/doap#bug-database">doap:bug-database</a><br /><a href="http://usefulinc.com/ns/doap#service-endpoint">doap:service-endpoint</a><br /><a href="http://usefulinc.com/ns/doap#translator">doap:translator</a><br /><a href="http://usefulinc.com/ns/doap#release">doap:release</a><br /><a href="http://usefulinc.com/ns/doap#helper">doap:helper</a><br /><a href="http://usefulinc.com/ns/doap#programming-language">doap:programming-language</a><br />
In range of |<a href="http://usefulinc.com/ns/doap#repositoryOf">doap:repositoryOf</a><br />
### ÃšloÅ¾iÅ¡tÄ› <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Repository`
Description | Repositorio del cÃ³digo fuente.
In domain of |<a href="http://usefulinc.com/ns/doap#location">doap:location</a><br /><a href="http://usefulinc.com/ns/doap#anon-root">doap:anon-root</a><br /><a href="http://usefulinc.com/ns/doap#browse">doap:browse</a><br /><a href="http://usefulinc.com/ns/doap#repositoryOf">doap:repositoryOf</a><br />
In range of |<a href="http://usefulinc.com/ns/doap#repository">doap:repository</a><br />
### Repositorio Subversion <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#SVNRepository`
Description | ÃšloÅ¾iÅ¡tÄ› zdrojovÃ½ch kÃ³dÅ¯ Subversion.
Super-classes |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
### Specification <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Specification`
Description | A specification of a system's aspects, technical or otherwise.
Super-classes |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
Restrictions |
Sub-classes |
In range of |<a href="http://usefulinc.com/ns/doap#implements">doap:implements</a><br />
### Version <sup>c</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#Version`
Description | Informace o uvolnÄ›nÃ© verzi projektu.
In domain of |<a href="http://usefulinc.com/ns/doap#os">doap:os</a><br /><a href="http://usefulinc.com/ns/doap#file-release">doap:file-release</a><br /><a href="http://usefulinc.com/ns/doap#revision">doap:revision</a><br /><a href="http://usefulinc.com/ns/doap#platform">doap:platform</a><br />
In range of |<a href="http://usefulinc.com/ns/doap#release">doap:release</a><br />

## Properties
[anonymnÃ­ koÅ™en](anonymnkoen),
[audience](audience),
[blog](blog),
[navegar](navegar),
[bug database](bugdatabase),
[categoria](categoria),
[vytvoÅ™eno](vytvoeno),
[description](description),
[programador](programador),
[developer forum](developerforum),
[escritor de ayuda](escritordeayuda),
[miroir pour le tÃ©lÃ©chargement](miroirpourletlchargement),
[pÃ¡gina de descarga](pginadedescarga),
[publicaÃ§Ã£o do ficheiro](publicaodoficheiro),
[colaborador](colaborador),
[pÃ¡gina web](pginaweb),
[EspecificaÃ§Ãµes para implementaÃ§Ã£o](Especificaesparaimplementao),
[language](language),
[licencia](licencia),
[Repository Lokation](RepositoryLokation),
[lista de distribuiÃ§Ã£o de e-mail](listadedistribuiodee-mail),
[maintainer](maintainer),
[module](module),
[name](name),
[Alte Homepage](AlteHomepage),
[operating system](operatingsystem),
[plataforma](plataforma),
[programming language](programminglanguage),
[release](release),
[repositÃ³rio](repositrio),
[repository of](repositoryof),
[versiÃ³n](versin),
[capturas de ecrÃ£s](capturasdeecrs),
[service endpoint](serviceendpoint),
[short description](shortdescription),
[supporting forum](supportingforum),
[tester](tester),
[pÅ™ekladatel](pekladatel),
[vendor](vendor),
[wiki](wiki),
[](anonymnkoen)
### anonymnÃ­ koÅ™en <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#anon-root`
Description | Repositorio para acceso anÃ³nimo.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](audience)
### audience <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#audience`
Description | DescriÃ§Ã£o do utilizador base alvo
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](blog)
### blog <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#blog`
Description | URI de um blog relacionado com um projeto
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br /><a href="http://rdfs.org/sioc/types#Weblog">http://rdfs.org/sioc/types#Weblog</a><sup class="sup-c" title="class">c</sup><br />
[](navegar)
### navegar <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#browse`
Description | Interface web au dÃ©pÃ´t.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
[](bugdatabase)
### bug database <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#bug-database`
Description | SprÃ¡va chyb projektu.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](categoria)
### categoria <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#category`
Description | Eine Kategorie eines Projektes.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](vytvoeno)
### vytvoÅ™eno <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#created`
Description | Datum, kdy bylo nÄ›co vytvoÅ™eno ve formÃ¡tu RRRR-MM-DD, napÅ™. 2004-04-05
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](description)
### description <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#description`
Description | DescriÃ§Ã£o de um projeto em texto apenas, com 2 a 4 frases de comprimento.
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](programador)
### programador <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#developer`
Description | VÃ½vojÃ¡Å™ softwaru projektu.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
[](developerforum)
### developer forum <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#developer-forum`
Description | A forum or community for developers of this project.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://rdfs.org/sioc/ns#Container">http://rdfs.org/sioc/ns#Container</a><sup class="sup-c" title="class">c</sup><br />
[](escritordeayuda)
### escritor de ayuda <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#documenter`
Description | Contributor of documentation to the project.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
[](miroirpourletlchargement)
### miroir pour le tÃ©lÃ©chargement <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#download-mirror`
Description | Zrcadlo strÃ¡nky pro staÅ¾enÃ­ softwaru.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](pginadedescarga)
### pÃ¡gina de descarga <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#download-page`
Description | Page web Ã  partir de laquelle on peut tÃ©lÃ©charger le programme.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](publicaodoficheiro)
### publicaÃ§Ã£o do ficheiro <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#file-release`
Description | URI para download associado com a publicaÃ§Ã£o.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Version">doap:Version</a><sup class="sup-c" title="class">c</sup><br />
[](colaborador)
### colaborador <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#helper`
Description | Collaborateur au projet.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
[](pginaweb)
### pÃ¡gina web <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#homepage`
Description | URL adresa domovskÃ© strÃ¡nky projektu asociovanÃ© s prÃ¡vÄ› jednÃ­m projektem.
Super-properties |<a href="http://xmlns.com/foaf/0.1/homepage">foaf:homepage</a><br />
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](Especificaesparaimplementao)
### EspecificaÃ§Ãµes para implementaÃ§Ã£o <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#implements`
Description | A specification that a project implements. Could be a standard, API or legally defined level of conformance.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://usefulinc.com/ns/doap#Specification">doap:Specification</a><sup class="sup-c" title="class">c</sup><br />
[](language)
### language <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#language`
Description | CÃ³digo de idioma ISO do projeto para o qual foi traduzido
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](licencia)
### licencia <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#license`
Description | El URI de una descripciÃ³n RDF de la licencia bajo la cuÃ¡l se distribuye el software.
[](RepositoryLokation)
### Repository Lokation <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#location`
Description | lugar de un repositorio.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
[](listadedistribuiodee-mail)
### lista de distribuiÃ§Ã£o de e-mail <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#mailing-list`
Description | DomovskÃ¡ strÃ¡nka nebo eâ€“mailovÃ¡ adresa eâ€“mailovÃ© diskuse.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://rdfs.org/sioc/types#MailingList">http://rdfs.org/sioc/types#MailingList</a><sup class="sup-c" title="class">c</sup><br />
[](maintainer)
### maintainer <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#maintainer`
Description | SprÃ¡vce projektu, vedoucÃ­ projektu.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
[](module)
### module <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#module`
Description | Nom du module d'un dÃ©pÃ´t Subversion, CVS, BitKeeper ou Arch.
Domain(s) |(<a href="http://usefulinc.com/ns/doap#CVSRepository">doap:CVSRepository</a><sup class="sup-c" title="class">c</sup> or <a href="http://usefulinc.com/ns/doap#ArchRepository">doap:ArchRepository</a><sup class="sup-c" title="class">c</sup> or <a href="http://usefulinc.com/ns/doap#BKRepository">doap:BKRepository</a><sup class="sup-c" title="class">c</sup>)<br />
[](name)
### name <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#name`
Description | Der Name von Irgendwas
Super-properties |<a href="http://www.w3.org/2000/01/rdf-schema#label">rdfs:label</a><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](AlteHomepage)
### Alte Homepage <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#old-homepage`
Description | URL of a project's past homepage,
		associated with exactly one project.
Super-properties |<a href="http://xmlns.com/foaf/0.1/homepage">foaf:homepage</a><br />
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](operatingsystem)
### operating system <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#os`
Description | Operating system that a project is limited to.  Omit this property if the project is not OS-specific.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br /><a href="http://usefulinc.com/ns/doap#Version">doap:Version</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](plataforma)
### plataforma <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#platform`
Description | Indicator of software platform (non-OS specific), e.g. Java, Firefox, ECMA CLR
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br /><a href="http://usefulinc.com/ns/doap#Version">doap:Version</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](programminglanguage)
### programming language <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#programming-language`
Description | Programming language a project is implemented in or intended for use with.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](release)
### release <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#release`
Description | A publicaÃ§Ã£o de um projeto.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://usefulinc.com/ns/doap#Version">doap:Version</a><sup class="sup-c" title="class">c</sup><br />
[](repositrio)
### repositÃ³rio <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#repository`
Description | Quellcode-Versionierungssystem.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
[](repositoryof)
### repository of <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#repositoryOf`
Description | The project that uses a repository.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Repository">doap:Repository</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](versin)
### versiÃ³n <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#revision`
Description | Identifiant de rÃ©vision d'une release du programme.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Version">doap:Version</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](capturasdeecrs)
### capturas de ecrÃ£s <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#screenshots`
Description | Web page with screenshots of project.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
[](serviceendpoint)
### service endpoint <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#service-endpoint`
Description | The URI of a web service endpoint where software as a service may be accessed
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Resource">rdfs:Resource</a><sup class="sup-c" title="class">c</sup><br />
[](shortdescription)
### short description <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#shortdesc`
Description | Texte descriptif concis (8 ou 9 mots) d'un projet.
Range(s) |<a href="http://www.w3.org/2000/01/rdf-schema#Literal">rdfs:Literal</a><sup class="sup-c" title="class">c</sup><br />
[](supportingforum)
### supporting forum <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#support-forum`
Description | A forum or community that supports this project.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://rdfs.org/sioc/ns#Container">http://rdfs.org/sioc/ns#Container</a><sup class="sup-c" title="class">c</sup><br />
[](tester)
### tester <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#tester`
Description | Un tester u otro proveedor de control de calidad.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
[](pekladatel)
### pÅ™ekladatel <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#translator`
Description | Spoluautor pÅ™ekladu projektu.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Person">foaf:Person</a><sup class="sup-c" title="class">c</sup><br />
[](vendor)
### vendor <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#vendor`
Description | Vendor organization: commercial, free or otherwise
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://xmlns.com/foaf/0.1/Organization">foaf:Organization</a><sup class="sup-c" title="class">c</sup><br />
[](wiki)
### wiki <sup>p</sup>
Property | Value
--- | ---
IRI | `http://usefulinc.com/ns/doap#wiki`
Description | L'URL du Wiki pour la discussion collaborative sur le projet.
Domain(s) |<a href="http://usefulinc.com/ns/doap#Project">doap:Project</a><sup class="sup-c" title="class">c</sup><br />
Range(s) |<a href="http://rdfs.org/sioc/types#Wiki">http://rdfs.org/sioc/types#Wiki</a><sup class="sup-c" title="class">c</sup><br />

## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **doap**
  * `http://usefulinc.com/ns/doap#`
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