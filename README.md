# pyLODE
An OWL ontology documentation tool using Python and templating, based on LODE.


The Live OWL Documentation Environment tool ([LODE](https://github.com/essepuntato/LODE)) is a well-known (in Semantic Web circles) Java & XSLT-based tool used to generate human-readable HTML documents for OWL and RDF ontologies. That tool is now a bit dated (old-style HTML, use of older technologies like XSLT) and it's ([online version](www.essepuntato.it/lode)) is not always online.

This tool is a complete re-implementation of LODE's functionality using Python and Pythons RDF manipulation module, [rdflib](https://pypi.org/project/rdflib/). An ontology to be documented is parsed and inspected using rdflib and HTML is generated using basic Python scripting and Python's [Jinja2 templating](https://pypi.org/project/Jinja2/).


### Differences from LODE
* command line access
    * you can use this on your own desktop so you don't need me to maintain a live service for use
* use of more modern & simpler HTML
* catering for a wider range of ontology options such as:
    * schema.org `domainIncludes` & `rangeIncludes` for properties
    * `foaf:Agent` or `schema:Person` objects for creators, contributors & publishers
* smarter CURIES - pyLODE looks up well-known prefixes to make more/better CURIES
* **active development**
    * this software is in use and will be improved for the foreseeable future so we will cater fro more and more things
    * recent ontology documentation initiatives such as the [MOD Ontology](https://github.com/sifrproject/MOD-Ontology) will be handled, if requested


## Use
Currently pyLODE presents as a Python & BASH command-line utility, [pylode/cli.py](pylode/cli.py) & [pylode/bin/pylode](pylode/bin/pylode) respectively. Windows scripts may appear soon. All use the same command line arguments.

An online version of it will be available soon too, just as LODE is (was) available online.


### Command line arguments
For the command line running of pyLODE, these are the command line argument options:

* `-i` or `--inputfile`, *required if `-u` not used*
  * The RDF ontology file you wish to generate HTML for Must be in either Turtle, RDF/XML, JSON-LD or N-Triples formats indicated by the file type extensions .rdf, .owl, .ttl, .n3, .nt, .json respectively
* `-u` or `--url`, *required if `-1` not used*
  * The RDF ontology you wish to generate HTML for, onlin. Must be an absolute URL that can be resolved to RDF, preferably via Content Negotiation.
* `-c` or `--css`, *optional, default 'false'*
  * Whether (true) or not (false) to copy the default CSS file to the output directory.
* `-o` or `--outputfile`, *optional*
  * A name you wish to assign to the output file. Will be postfixed with .html. If not specified, the name of the input file or last segment of RDF URI will be used, + .html.

#### Example call
This call to the BASH script in [pylode/bin/](pylode/bin/) will create an HTML document for an ontology called `doc.html` and save it with a basic CSS file into [pylode/output_files/](pylode/output_files/):

```
$ ./pylode -i ../example/prof.ttl --css true
```


## Annotations understood
pyLODE understands the following ontology annotations:

* **ontology metadata**
    * imports - `owl:imports`
    * title - `rdfs:label` or `skos:prefLabel` or `dct:title`
    * version_uri - `owl:versionIRI`
    * publishers, creators, contributors
        * either `dc:publisher` etc. as a string or `dct:publisher` etc. as a `foaf:Agent` or `schema:Person` with `foaf:name` & `foaf:homepage` or `schema:name` & `schema:identifier` properties respectively
    * created, modified, issued - `dct:created` etc., all as `xsd:date` or `xsd:dateTime` datatype properties
    * description - `rdf:comment` or `skos:definition` or `dct:description`
    * versionInfo - `owl:versionInfo` as a string

* **classes**
    * per `rdfs:Class` or `owl:Class`
    * title - `rdfs:label` or `skos:prefLabel` or `dct:title`
    * description - `rdf:comment` or `skos:definition` or `dct:description`
    * usage note - a `skos:scopeNote` string
    * super classes - by declaring a class to be `owl:subClassOf` something
    * sub classes - pyLODE will work these out itself
    * restrictions - by declaring a class to be `owl:subClassOf` of an `owl:Restriction` with any of the normal cardinality or property existence etc. restrictions

* **properties**
    * per `owl:ObjectProperty`, `owl:DatatypeProperty` or `owl:AnnotationProperty`
    * title - `rdfs:label` or `skos:prefLabel` or `dct:title`
    * description - `rdf:comment` or `skos:definition` or `dct:description`
    * usage note - a `skos:scopeNote` string
    * super properties - by declaring a class to be `owl:subPropertyOf` something
    * sub properties - pyLODE will work these out itself
    * domains - `rdfs:domain` or `schema:domainIncludes`
    * ranges - `rdfs:range` or `schema:rangeIncludes`

* **namespaces**
    * pyLODE will honour any namespace prefixes you set and look up others in [http://prefix.cc](http://prefix.cc/)
    * it will either read your ontology's default/base URI in annotations or guess it using a number of methods

* **named individuals**
    * *coming!*

To help pyLODE understand more annotations, see **Suggestions** below.


## Styling
This tool generates HTML that is shamelessly similar to LODE's styling. That's because we want things to look familiar and LODE's outputs look great.

Feel free to extend your styling with your own CSS.


## License
This code is licensed using the GPL v3 licence. See the [LICENSE file](LICENSE) for the deed.


## Citation
If you use pyLODE, please leave the pyLODE logo in the top left of published HTML pages.


## Suggestions
If you have suggestions, please email the contacts below or leave Issues in this repositories [Issue tracker](https://github.com/rdflib/pyLODE/issues).

But the very best thing you could do is create a Pull Request for us to action!


## Examples
pyLODE has been tested with all of the ontologies in [pylode/examples/](pylode/examples/) and we are trying to ensure it captures all of their annotations.

As ontologies' HTML, generated by pyLODE, appears online, it will be linked to here, if we know about it.


## Contacts
*Author*:  
**Nicholas Car**  
*Senior Experimental Scientist*  
CSIRO Land & Water, Environmental Informatics Group  
<nicholas.car@csiro.au>  
