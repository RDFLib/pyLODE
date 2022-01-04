.. image:: https://rawcdn.githack.com/RDFLib/pyLODE/b1ff1b1e19262cdc21ee28c7362b1690ca18e30b/img/pyLODE-250.png

.. image:: https://badge.fury.io/py/pyLODE.svg
    :target: https://badge.fury.io/py/pyLODE

pyLODE
******
An OWL ontology documentation tool using Python and templating, based on
LODE.

In addition to making human-readable forms of ontologies/taxonomies, pyLODE encourages ontology annotation *best
practice* by only producing good results for well documented inputs! pyLODE defines what it considers 'well documented'
in sections below, such as `Profiles`_ & `What pyLODE understands`_.


Contents
========
1. `Quick Intro`_
2. Examples_
3. Installation_
4. Use_
5. `What pyLODE understands`_
6. `Profiles`_
7. `Differences from LODE`_
8. `Releases`_
9. License_
10. Citation_
11. Collaboration_
12. Contacts_


Quick Intro
===========
The Live OWL Documentation Environment tool
(`LODE <https://github.com/essepuntato/LODE>`__) is a well-known (in
Semantic Web circles) Java & XSLT-based tool used to generate
human-readable HTML documents for OWL and RDF ontologies. That tool is
now a bit dated (old-style HTML, use of older technologies like XSLT)
and it's (`online version <https://www.essepuntato.it/lode>`__) is not always
online.

This tool is a complete re-implementation of LODE's functionality using
Python and Python's RDF manipulation module,
`rdflib <https://pypi.org/project/rdflib/>`__. An ontology to be
documented is parsed and inspected using rdflib and HTML is generated
directly, using Python's `dominate <https://pypi.org/project/dominate/>`__
package.

The tool can be run as in multiple ways:

- BASH command line
    - pylode.sh, pylode.bat in bin/
- Windows EXE
    - pylode.exe in bin/
- Python Script
    - cli.py or module
- as-a-service locally
    - via the popular `Falcon framework <https://falconframework.org/>`__.
    - see server.py in the main folder
- as-a-service online
    - hosted at https://pylode.surroundaustralia.com

The BASH, Windows EXE and Python Script methods all use the same command line arguments.


Examples
========
