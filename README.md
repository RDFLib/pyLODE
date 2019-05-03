# pyLODE
An OWL ontology documentation tool using Python and templating, based on LODE.


The Live OWL Documentation Environment tool ([LODE](https://github.com/essepuntato/LODE)) is a well-known (in Semantic Web circles) Java & XSLT-based tool used to generate human-readable HTML documents for OWL and RDF ontologies. That tool is now a bit dated (old-style, HTML, use of older technologies like XSLT) and it's ([online version](www.essepuntato.it/lode)) is not always online.

This tool is a complete re-implementation of LODE's functionality using Python & the Python [rdflib](https://pypi.org/project/rdflib/) RDF manipulation module. Additionally, the [OWL-RL](https://pypi.org/project/owlrl/) RDf inferencing tool is also used as well as simple [Jinja2 templating](https://pypi.org/project/Jinja2/).



## Use
Currently pyLODE presents as a (CURRENTLY INCOMPLETE!) Python command-line utility. Soon an online version of it will be available too, just as LODE is (was) available online.



## License
This code is licensed using the GPL v3 licence. See the [LICENSE file](LICENSE) for the deed.


## Contacts
*Author*:
**Nicholas Car**
*Senior Experimental Scientist*
CSIRO Land & Water, Environmental Informatics Group
<nicholas.car@csiro.au>