# Collection item format
### A taxonomy

Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)

## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/collection-item-format`
* **Publisher(s)**
  * [Australian Government Linked Data Working Group](http://www.linked.data.gov.au/org/agldwg)
* **Creators(s)**
  * Tessa Elieff
* **Created**
  * 2020-03-03
* **Modified**
  * 2020-03-29
* **Source**
  * [https://collection.sl.nsw.gov.au/search?offset=0](https://collection.sl.nsw.gov.au/search?offset=0)
* **Ontology RDF**
  * RDF ([collection-item-format.ttl](turtle))
### Description
<p>The format of an item within a collection describes its physical presence at the highest level.</p>

**History Note**  
This vocabulary has been developed by referencing publicly available information from select libraries and archives about their FORMAT cataloguing terms.

## Table of Contents
1. [Collections](#collections)
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Collections
* [National Film and Sound Archive's Formats](#NationalFilmandSoundArchive'sFormats)
* [State Library New South Wales' Formats](#StateLibraryNewSouthWales'Formats)
### National Film and Sound Archive's Formats
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/national-film-and-sound-archive`
Preferred Labels |National Film and Sound Archive's Formats (en)<br />
Alternate Labels |N (F)<br />
Source | https://www.nfsa.gov.au/
Members |[Disk](Disk) (cp)<br />[Digital](Digital) (cp)<br />[Documentation](Documentation) (cp)<br />[Tape](Tape) (cp)<br />[Disc](Disc) (cp)<br />[Film](Film) (cp)<br />[Object](Object) (cp)<br />

### State Library New South Wales' Formats
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/state-library-new-south-wales`
Preferred Labels |State Library New South Wales' Formats (en)<br />
Alternate Labels |S (L)<br />
Source | https://www.sl.nsw.gov.au/
Members |[Newspaper](Newspaper) (cp)<br />[Manuscript](Manuscript) (cp)<br />[cif:eresource](http://linked.data.gov.au/def/collection-item-format/eresource) (cp)<br />[Map](Map) (cp)<br />[Book](Book) (cp)<br />[Object-SLNSW](Object-SLNSW) (cp)<br />[Journal & magazine](Journalmagazine) (cp)<br />[Picture](Picture) (cp)<br />[Audio](Audio) (cp)<br />[Video & film](Videofilm) (cp)<br />

## Classes
* [Audio](http://linked.data.gov.au/def/collection-item-format/audio)
* [Book](http://linked.data.gov.au/def/collection-item-format/book)
* [Digital](http://linked.data.gov.au/def/collection-item-format/digital)
	* [Disk](http://linked.data.gov.au/def/collection-item-format/disk)
	* [Digital Versatile Disc](http://linked.data.gov.au/def/collection-item-format/dvd)
	* [Eresources](http://linked.data.gov.au/def/collection-item-format/eresources)
* [Disc](http://linked.data.gov.au/def/collection-item-format/disc)
* [Disk](http://linked.data.gov.au/def/collection-item-format/disk)
* [Documentation](http://linked.data.gov.au/def/collection-item-format/documentation)
	* [Manuscript](http://linked.data.gov.au/def/collection-item-format/manuscript)
	* [Map](http://linked.data.gov.au/def/collection-item-format/map)
	* [Newspaper](http://linked.data.gov.au/def/collection-item-format/newspaper)
	* [Picture](http://linked.data.gov.au/def/collection-item-format/picture)
* [Eresources](http://linked.data.gov.au/def/collection-item-format/eresources)
* [Film](http://linked.data.gov.au/def/collection-item-format/film)
* [Journal & magazine](http://linked.data.gov.au/def/collection-item-format/journal-magazine)
* [Manuscript](http://linked.data.gov.au/def/collection-item-format/manuscript)
* [Map](http://linked.data.gov.au/def/collection-item-format/map)
* [Newspaper](http://linked.data.gov.au/def/collection-item-format/newspaper)
* [Object](http://linked.data.gov.au/def/collection-item-format/object)
	* [Object-SLNSW](http://linked.data.gov.au/def/collection-item-format/object-slnsw)
* [Object-SLNSW](http://linked.data.gov.au/def/collection-item-format/object-slnsw)
* [Picture](http://linked.data.gov.au/def/collection-item-format/picture)
* [Tape](http://linked.data.gov.au/def/collection-item-format/tape)
* [Video & film](http://linked.data.gov.au/def/collection-item-format/video-film)
	* [Film](http://linked.data.gov.au/def/collection-item-format/film)
	* [Tape](http://linked.data.gov.au/def/collection-item-format/tape)

### Audio
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/audio`
Preferred Labels |Audio (en)<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
### Book
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/book`
Preferred Labels |Book (en)<br />
Source | https://dictionary.cambridge.org/dictionary/english/book
### Digital
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/digital`
Preferred Labels |Mamati (mi)<br />Digital (en)<br />Cyfrowy (pl)<br />
Alternate Labels |Digital Storage<br />
Narrower Concepts |[Disk](Disk) (cp)<br />[Digital Versatile Disc](DigitalVersatileDisc) (cp)<br />[Eresources](Eresources) (cp)<br />
### Disc
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/disc`
Preferred Labels |Disc (en)<br />
Source | https://www.iasa-web.org/cataloguing-rules/appendix-d-glossary
### Disk
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/disk`
Preferred Labels |Disk (en)<br />
Alternate Labels |Hard Drive<br />HDD<br />
Source | https://www.iasa-web.org/cataloguing-rules/appendix-d-glossary
Broader Concepts |[Digital](Digital) (cp)<br />
### Documentation
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/documentation`
Preferred Labels |Documentation (en)<br />
Source | http://colsearch.nfsa.gov.au/nfsa/search/search.w3p;adv=yes
Narrower Concepts |[Newspaper](Newspaper) (cp)<br />[Picture](Picture) (cp)<br />[Manuscript](Manuscript) (cp)<br />[Map](Map) (cp)<br />
### Digital Versatile Disc
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/dvd`
Preferred Labels |Digital Versatile Disc (en)<br />
Source | https://en.wikipedia.org/wiki/DVD
Broader Concepts |[Digital](Digital) (cp)<br />
### Eresources
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/eresources`
Preferred Labels |Eresources (en)<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Broader Concepts |[Digital](Digital) (cp)<br />
### Film
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/film`
Preferred Labels |Film (en)<br />
Source | https://www.iasa-web.org/cataloguing-rules/appendix-d-glossary
Broader Concepts |[Video & film](Videofilm) (cp)<br />
### Journal & magazine
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/journal-magazine`
Preferred Labels |Journal & magazine (en)<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
### Manuscript
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/manuscript`
Preferred Labels |Manuscript (en)<br />
Source | https://dictionary.cambridge.org/dictionary/english/manuscript
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Map
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/map`
Preferred Labels |Map (en)<br />
Source | https://dictionary.cambridge.org/dictionary/english/map
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Newspaper
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/newspaper`
Preferred Labels |Newspaper (en)<br />
Source | https://dictionary.cambridge.org/dictionary/english/newspaper
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Object
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/object`
Preferred Labels |Object (en)<br />
Source | https://dictionary.cambridge.org/dictionary/english/object
Narrower Concepts |[Object-SLNSW](Object-SLNSW) (cp)<br />
### Object-SLNSW
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/object-slnsw`
Preferred Labels |Object-SLNSW (en)<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Broader Concepts |[Object](Object) (cp)<br />
### Picture
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/picture`
Preferred Labels |Picture (en)<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Tape
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/tape`
Preferred Labels |Tape (en)<br />
Source | https://dictionary.cambridge.org/dictionary/english/magnetic-tape
Broader Concepts |[Video & film](Videofilm) (cp)<br />
### Video & film
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/collection-item-format/video-film`
Preferred Labels |Video & film (en)<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Narrower Concepts |[Film](Film) (cp)<br />[Tape](Tape) (cp)<br />

## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/collection-item-format/`
* **cif**
  * `http://linked.data.gov.au/def/collection-item-format/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
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