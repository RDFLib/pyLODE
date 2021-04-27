Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.8.10

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
[BitKeeper Repository](#BitKeeperRepository),
[CVS Repository](#CVSRepository),
[GNU Arch repository](#GNUArchrepository),
[Git Branch](#GitBranch),
[Git Repository](#GitRepository),
[Mercurial Repository](#MercurialRepository),
[Project](#Project),
[Repository](#Repository),
[Specification](#Specification),
[Subversion Repository](#SubversionRepository),
[Version](#Version),
[darcs Repository](#darcsRepository),
### GNU Arch repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#ArchRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>GNU Arch source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### BitKeeper Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#BKRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>BitKeeper source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Bazaar Branch
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#BazaarBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Bazaar source code branch.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### CVS Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#CVSRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>CVS source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### darcs Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#DarcsRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>darcs source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Git Branch
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#GitBranch`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Git source code branch.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Git Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#GitRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Git source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Mercurial Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#HgRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Mercurial source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Project
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Project`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>A project.</p>
Super-classes |[wn:Project](http://xmlns.com/wordnet/1.6/Project) (c)<br />[foaf:Project](http://xmlns.com/foaf/0.1/Project) (c)<br />
In domain of |[doap:audience](http://usefulinc.com/ns/doap#audience)<br />[doap:screenshots](http://usefulinc.com/ns/doap#screenshots)<br />[doap:wiki](http://usefulinc.com/ns/doap#wiki)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />[doap:translator](http://usefulinc.com/ns/doap#translator)<br />[doap:developer](http://usefulinc.com/ns/doap#developer)<br />[doap:download-page](http://usefulinc.com/ns/doap#download-page)<br />[doap:download-mirror](http://usefulinc.com/ns/doap#download-mirror)<br />[doap:tester](http://usefulinc.com/ns/doap#tester)<br />[doap:blog](http://usefulinc.com/ns/doap#blog)<br />[doap:repository](http://usefulinc.com/ns/doap#repository)<br />[doap:mailing-list](http://usefulinc.com/ns/doap#mailing-list)<br />[doap:helper](http://usefulinc.com/ns/doap#helper)<br />[doap:service-endpoint](http://usefulinc.com/ns/doap#service-endpoint)<br />[doap:release](http://usefulinc.com/ns/doap#release)<br />[doap:vendor](http://usefulinc.com/ns/doap#vendor)<br />[doap:documenter](http://usefulinc.com/ns/doap#documenter)<br />[doap:category](http://usefulinc.com/ns/doap#category)<br />[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:developer-forum](http://usefulinc.com/ns/doap#developer-forum)<br />[doap:language](http://usefulinc.com/ns/doap#language)<br />[doap:bug-database](http://usefulinc.com/ns/doap#bug-database)<br />[doap:homepage](http://usefulinc.com/ns/doap#homepage)<br />[doap:programming-language](http://usefulinc.com/ns/doap#programming-language)<br />[doap:maintainer](http://usefulinc.com/ns/doap#maintainer)<br />[doap:implements](http://usefulinc.com/ns/doap#implements)<br />[doap:old-homepage](http://usefulinc.com/ns/doap#old-homepage)<br />[doap:support-forum](http://usefulinc.com/ns/doap#support-forum)<br />
In range of |[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />
### Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Source code repository.</p>
Sub-classes |[doap:SVNRepository](http://usefulinc.com/ns/doap#SVNRepository) (c)<br />[doap:GitBranch](http://usefulinc.com/ns/doap#GitBranch) (c)<br />[doap:GitRepository](http://usefulinc.com/ns/doap#GitRepository) (c)<br />[doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c)<br />[doap:DarcsRepository](http://usefulinc.com/ns/doap#DarcsRepository) (c)<br />[doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c)<br />[doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c)<br />[doap:HgRepository](http://usefulinc.com/ns/doap#HgRepository) (c)<br />[doap:BazaarBranch](http://usefulinc.com/ns/doap#BazaarBranch) (c)<br />
In domain of |[doap:location](http://usefulinc.com/ns/doap#location)<br />[doap:browse](http://usefulinc.com/ns/doap#browse)<br />[doap:repositoryOf](http://usefulinc.com/ns/doap#repositoryOf)<br />[doap:anon-root](http://usefulinc.com/ns/doap#anon-root)<br />
In range of |[doap:repository](http://usefulinc.com/ns/doap#repository)<br />
### Subversion Repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#SVNRepository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Subversion source code repository.</p>
Super-classes |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
### Specification
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Specification`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>A specification of a system's aspects, technical or otherwise.</p>
Super-classes |[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
In range of |[doap:implements](http://usefulinc.com/ns/doap#implements)<br />
### Version
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#Version`
Is Defined By | http://usefulinc.com/ns/doap#
Description | <p>Version information of a project release.</p>
In domain of |[doap:platform](http://usefulinc.com/ns/doap#platform)<br />[doap:file-release](http://usefulinc.com/ns/doap#file-release)<br />[doap:revision](http://usefulinc.com/ns/doap#revision)<br />[doap:os](http://usefulinc.com/ns/doap#os)<br />
In range of |[doap:release](http://usefulinc.com/ns/doap#release)<br />

## Properties
[anonymous root](#anonymousroot),
[audience](#audience),
[blog](#blog),
[browse](#browse),
[bug database](#bugdatabase),
[category](#category),
[created](#created),
[description](#description),
[developer](#developer),
[developer forum](#developerforum),
[documenter](#documenter),
[download mirror](#downloadmirror),
[download page](#downloadpage),
[file-release](#file-release),
[helper](#helper),
[homepage](#homepage),
[Implements specification](#Implementsspecification),
[language](#language),
[license](#license),
[repository location](#repositorylocation),
[mailing list](#mailinglist),
[maintainer](#maintainer),
[module](#module),
[name](#name),
[old homepage](#oldhomepage),
[operating system](#operatingsystem),
[platform](#platform),
[programming language](#programminglanguage),
[release](#release),
[repository](#repository),
[repository of](#repositoryof),
[revision](#revision),
[screenshots](#screenshots),
[service endpoint](#serviceendpoint),
[short description](#shortdescription),
[supporting forum](#supportingforum),
[tester](#tester),
[translator](#translator),
[vendor](#vendor),
[wiki](#wiki),
[](anonymousroot)
### anonymous root
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#anon-root`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Repository for anonymous access.
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
Description | URI of a blog related to a project
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[sioct:Weblog](http://rdfs.org/sioc/types#Weblog) (c)<br />[rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource) (c)<br />
[](browse)
### browse
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#browse`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web browser interface to repository.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](bugdatabase)
### bug database
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#bug-database`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Bug tracker for a project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](category)
### category
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#category`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A category of project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](created)
### created
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#created`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Date when something was created, in YYYY-MM-DD form. e.g. 2004-04-05
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](description)
### description
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#description`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Plain text description of a project, of 2-4 sentences in length.
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
Range(s) |[sioc:Container](http://rdfs.org/sioc/ns#Container) (c)<br />
[](documenter)
### documenter
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#documenter`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Contributor of documentation to the project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](downloadmirror)
### download mirror
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#download-mirror`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Mirror of software download web page.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](downloadpage)
### download page
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#download-page`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web page from which the project software can be downloaded.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](file-release)
### file-release
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#file-release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URI of download associated with this release.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](helper)
### helper
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#helper`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Project contributor.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](homepage)
### homepage
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
Description | ISO language code a project has been translated into
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](license)
### license
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#license`
Is Defined By | http://usefulinc.com/ns/doap#
Description | The URI of an RDF description of the license the software is distributed under. E.g. a SPDX reference
[](repositorylocation)
### repository location
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#location`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Location of a repository.
Domain(s) |[doap:Repository](http://usefulinc.com/ns/doap#Repository) (c)<br />
[](mailinglist)
### mailing list
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#mailing-list`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Mailing list home page or email address.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[sioct:MailingList](http://rdfs.org/sioc/types#MailingList) (c)<br />
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
Description | Module name of a Subversion, CVS, BitKeeper or Arch repository.
Domain(s) |([doap:CVSRepository](http://usefulinc.com/ns/doap#CVSRepository) (c) or [doap:ArchRepository](http://usefulinc.com/ns/doap#ArchRepository) (c) or [doap:BKRepository](http://usefulinc.com/ns/doap#BKRepository) (c))<br />
[](name)
### name
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#name`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A name of something.
Super-properties |[rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](oldhomepage)
### old homepage
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#old-homepage`
Is Defined By | http://usefulinc.com/ns/doap#
Description | URL of a project's past homepage, 		associated with exactly one project.
Super-properties |[foaf:homepage](http://xmlns.com/foaf/0.1/homepage)<br />
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
[](operatingsystem)
### operating system
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#os`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Operating system that a project is limited to.  Omit this property if the project is not OS-specific.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](platform)
### platform
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#platform`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Indicator of software platform (non-OS specific), e.g. Java, Firefox, ECMA CLR
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](programminglanguage)
### programming language
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#programming-language`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Programming language a project is implemented in or intended for use with.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](release)
### release
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#release`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A project release.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
[](repository)
### repository
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#repository`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Source code repository.
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
[](revision)
### revision
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#revision`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Revision identifier of a software release.
Domain(s) |[doap:Version](http://usefulinc.com/ns/doap#Version) (c)<br />
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](screenshots)
### screenshots
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#screenshots`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Web page with screenshots of project.
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
[](shortdescription)
### short description
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#shortdesc`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Short (8 or 9 words) plain text description of a project.
Range(s) |[rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal) (c)<br />
[](supportingforum)
### supporting forum
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#support-forum`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A forum or community that supports this project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[sioc:Container](http://rdfs.org/sioc/ns#Container) (c)<br />
[](tester)
### tester
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#tester`
Is Defined By | http://usefulinc.com/ns/doap#
Description | A tester or other quality control contributor.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[foaf:Person](http://xmlns.com/foaf/0.1/Person) (c)<br />
[](translator)
### translator
Property | Value
--- | ---
URI | `http://usefulinc.com/ns/doap#translator`
Is Defined By | http://usefulinc.com/ns/doap#
Description | Contributor of translations to the project.
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
Description | URL of Wiki for collaborative discussion of project.
Domain(s) |[doap:Project](http://usefulinc.com/ns/doap#Project) (c)<br />
Range(s) |[sioct:Wiki](http://rdfs.org/sioc/types#Wiki) (c)<br />

## Named Individuals
## Namespaces
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
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
* **sioc**
  * `http://rdfs.org/sioc/ns#`
* **sioct**
  * `http://rdfs.org/sioc/types#`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **wn**
  * `http://xmlns.com/wordnet/1.6/`
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