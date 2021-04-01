Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 

# Collection item format
### A taxonomy

## Metadata
* **URI**
  * `http://linked.data.gov.au/def/collection-item-format`
* **Publisher(s)**
  * [Australian Government Linked Data Working Group](http://www.linked.data.gov.au/org/agldwg)
* **Creators(s)**
  * [Tessa Elieff](http://linked.data.gov.au/def/collection-item-format/tessa)
    (<not@given.com></a>)
* **Contributor(s)**
  * Nicholas J. Car
* **Created**
  * 2020-03-03
* **Modified**
  * 2020-03-29
* **Source**
  * [http://colsearch.nfsa.gov.au/nfsa/search/search.w3p;adv=yes](http://colsearch.nfsa.gov.au/nfsa/search/search.w3p;adv=yes)

* **Taxonomy RDF**
  * RDF ([collection-item-format.ttl](turtle))
### Description
<p>The format of an item within a collection describes its physical presence at the highest level.</p>

**History Note**  
<p>This vocabulary has been developed by referencing publicly available information from select libraries and archives about their FORMAT cataloguing terms.</p>

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
URI | `http://linked.data.gov.au/def/collection-item-format/national-film-and-sound-archive`
Preferred Labels |National Film and Sound Archive's Formats (en)<br />
Alternate Labels |N (F)<br />
Source | https://www.nfsa.gov.au/
Members |[Documentation](Documentation) (cp)<br />[Film](Film) (cp)<br />[Object](Object) (cp)<br />[Disk](Disk) (cp)<br />[Disc](Disc) (cp)<br />[Digital](Digital) (cp)<br />[Tape](Tape) (cp)<br />

### State Library New South Wales' Formats
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/state-library-new-south-wales`
Preferred Labels |State Library New South Wales' Formats (en)<br />
Alternate Labels |S (L)<br />
Source | https://www.sl.nsw.gov.au/
Members |[Map](Map) (cp)<br />[Picture](Picture) (cp)<br />[Object-SLNSW](Object-SLNSW) (cp)<br />[Manuscript](Manuscript) (cp)<br />[Book](Book) (cp)<br />[Audio](Audio) (cp)<br />[Eresource](Eresource) (cp)<br />[Newspaper](Newspaper) (cp)<br />[Video & film](Videofilm) (cp)<br />[Journal & magazine](Journalmagazine) (cp)<br />

## Concepts
* [Audio](http://linked.data.gov.au/def/collection-item-format/audio)
* [Book](http://linked.data.gov.au/def/collection-item-format/book)
* [Digital](http://linked.data.gov.au/def/collection-item-format/digital)
	* [Disk](http://linked.data.gov.au/def/collection-item-format/disk)
	* [Digital Versatile Disc](http://linked.data.gov.au/def/collection-item-format/dvd)
	* [Eresource](http://linked.data.gov.au/def/collection-item-format/eresource)
* [Disc](http://linked.data.gov.au/def/collection-item-format/disc)
* [Disk](http://linked.data.gov.au/def/collection-item-format/disk)
* [Documentation](http://linked.data.gov.au/def/collection-item-format/documentation)
	* [Manuscript](http://linked.data.gov.au/def/collection-item-format/manuscript)
	* [Map](http://linked.data.gov.au/def/collection-item-format/map)
	* [Newspaper](http://linked.data.gov.au/def/collection-item-format/newspaper)
	* [Picture](http://linked.data.gov.au/def/collection-item-format/picture)
* [Digital Versatile Disc](http://linked.data.gov.au/def/collection-item-format/dvd)
* [Eresource](http://linked.data.gov.au/def/collection-item-format/eresource)
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
URI | `http://linked.data.gov.au/def/collection-item-format/audio`
Preferred Labels |Audio (en)<br />
Definitions |['Musical sound recordings and audio books.']<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
### Book
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/book`
Preferred Labels |Book (en)<br />
Definitions |['A written text that can be published in printed or electronic form.']<br />
Source | https://dictionary.cambridge.org/dictionary/english/book
### Digital
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/digital`
Preferred Labels |Digital (en)<br />Mamati (mi)<br />Cyfrowy (pl)<br />
Alternate Labels |Digital Storage<br />
Definitions |['A physical device for storing digital content.']<br />
Narrower Concepts |[Disk](Disk) (cp)<br />[Eresource](Eresource) (cp)<br />[Digital Versatile Disc](DigitalVersatileDisc) (cp)<br />
### Disc
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/disc`
Preferred Labels |Disc (en)<br />
Definitions |['A sound recording on a thin, flat circular object, usually made of shellac, vinyl, or various laminates. The signal may be either analogue or digital, and recorded/played using acoustical, electrical, magnetic or optical technology.']<br />
Source | https://www.iasa-web.org/cataloguing-rules/appendix-d-glossary
### Disk
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/disk`
Preferred Labels |Disk (en)<br />
Alternate Labels |HDD<br />Hard Drive<br />
Definitions |['A round magnetic device for storing information and programmes accessible by computer; may be either a rigid platter (hard disk) or a sheet of flexible plastic (floppy disk or diskette). The disk base is coated with a magnetizable material on which data can be recorded or stored along concentric tracks as small magnetic areas forming patterns of binary digits or bits. Information is written onto the disk, and read from it in a disk drive, by read/write heads mounted on arms which move rapidly across the disk.']<br />
Source | https://www.iasa-web.org/cataloguing-rules/appendix-d-glossary
Broader Concepts |[Digital](Digital) (cp)<br />
### Documentation
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/documentation`
Preferred Labels |Documentation (en)<br />
Definitions |['Photographs and paper collection items.']<br />
Source | http://colsearch.nfsa.gov.au/nfsa/search/search.w3p;adv=yes
Narrower Concepts |[Newspaper](Newspaper) (cp)<br />[Map](Map) (cp)<br />[Picture](Picture) (cp)<br />[Manuscript](Manuscript) (cp)<br />
### Digital Versatile Disc
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/dvd`
Preferred Labels |Digital Versatile Disc (en)<br />
Definitions |['A round plastic, partly metal-coated disc used to store digital data which can be written and read by laser.']<br />
Source | https://en.wikipedia.org/wiki/DVD
Broader Concepts |[Digital](Digital) (cp)<br />
### Eresource
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/eresource`
Preferred Labels |Eresource (en)<br />
Definitions |['Website, database and software collection items.']<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Broader Concepts |[Digital](Digital) (cp)<br />
### Film
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/film`
Preferred Labels |Film (en)<br />
Definitions |['A series of still images collected onto a flexible and transparent piece of film so that they can be projected in a rapid sequence so as to give the illusion of motion.']<br />
Source | https://www.iasa-web.org/cataloguing-rules/appendix-d-glossary
Broader Concepts |[Video & film](Videofilm) (cp)<br />
### Journal & magazine
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/journal-magazine`
Preferred Labels |Journal & magazine (en)<br />
Definitions |['Journal and magazine collection items.']<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
### Manuscript
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/manuscript`
Preferred Labels |Manuscript (en)<br />
Definitions |['The original copy of a book or article.']<br />
Source | https://dictionary.cambridge.org/dictionary/english/manuscript
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Map
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/map`
Preferred Labels |Map (en)<br />
Definitions |["A drawing of the earth's surface, or part of that surface, showing the shape and position of different countries, political borders, natural features such as rivers and mountains, and artificial features such as roads and buildings."]<br />
Source | https://dictionary.cambridge.org/dictionary/english/map
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Newspaper
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/newspaper`
Preferred Labels |Newspaper (en)<br />
Definitions |['A regularly printed document consisting of large sheets of paper that are folded together, or a website, containing news reports, articles, photographs, and advertisements.']<br />
Source | https://dictionary.cambridge.org/dictionary/english/newspaper
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Object
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/object`
Preferred Labels |Object (en)<br />
Definitions |['A thing that you can see or touch but that is not usually a living animal, plant, or person.']<br />
Source | https://dictionary.cambridge.org/dictionary/english/object
Narrower Concepts |[Object-SLNSW](Object-SLNSW) (cp)<br />
### Object-SLNSW
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/object-slnsw`
Preferred Labels |Object-SLNSW (en)<br />
Definitions |['Objects, stamps and ephemera collection items.']<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Broader Concepts |[Object](Object) (cp)<br />
### Picture
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/picture`
Preferred Labels |Picture (en)<br />
Definitions |['photographs, prints, drawings, paintings, posters.']<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Broader Concepts |[Documentation](Documentation) (cp)<br />
### Tape
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/tape`
Preferred Labels |Tape (en)<br />
Definitions |['A plastic strip covered with a magnetic substance on which sound, images, or computer information can be recorded.']<br />
Source | https://dictionary.cambridge.org/dictionary/english/magnetic-tape
Broader Concepts |[Video & film](Videofilm) (cp)<br />
### Video & film
Property | Value
--- | ---
URI | `http://linked.data.gov.au/def/collection-item-format/video-film`
Preferred Labels |Video & film (en)<br />
Definitions |['Video and film collection items.']<br />
Source | https://collection.sl.nsw.gov.au/search?offset=0
Narrower Concepts |[Film](Film) (cp)<br />[Tape](Tape) (cp)<br />

## Namespaces
* **cif**
  * `http://linked.data.gov.au/def/collection-item-format/`
* **cs**
  * `http://linked.data.gov.au/def/collection-item-format`
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
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Collections: cl
* Concepts: cp