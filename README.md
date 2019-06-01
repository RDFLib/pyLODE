# pyLODE

# WARNING: not working yet! Do Not use!

An OWL ontology documentation tool using Python and templating, based on LODE.


The Live OWL Documentation Environment tool ([LODE](https://github.com/essepuntato/LODE)) is a well-known (in Semantic Web circles) Java & XSLT-based tool used to generate human-readable HTML documents for OWL and RDF ontologies. That tool is now a bit dated (old-style, HTML, use of older technologies like XSLT) and it's ([online version](www.essepuntato.it/lode)) is not always online.

This tool is a complete re-implementation of LODE's functionality using Python & the Python [rdflib](https://pypi.org/project/rdflib/) RDF manipulation module. Additionally, the [OWL-RL](https://pypi.org/project/owlrl/) RDf inferencing tool is also used as well as simple [Jinja2 templating](https://pypi.org/project/Jinja2/).



## Use
Currently pyLODE presents as a Python command-line utility, [pylode.py](pylode.py), and Bash and Windows scripts for it are available in the [bin/](bin/) directory. All use the same command line arguments.

Soon an online version of it will be available too, just as LODE is (was) available online.


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
This call will create an HTML document for an ontology

## License
This code is licensed using the GPL v3 licence. See the [LICENSE file](LICENSE) for the deed.


## Contacts
*Author*:  
**Nicholas Car**  
*Senior Experimental Scientist*  
CSIRO Land & Water, Environmental Informatics Group  
<nicholas.car@csiro.au>  
