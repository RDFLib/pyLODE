.. image:: https://rawcdn.githack.com/RDFLib/pyLODE/b1ff1b1e19262cdc21ee28c7362b1690ca18e30b/img/pyLODE-250.png

.. image:: https://badge.fury.io/py/pyLODE.svg
    :target: https://badge.fury.io/py/pyLODE

pyLODE
******
An OWL ontology documentation tool using Python, based on LODE.

In addition to making web page, human-readable forms of ontologies, pyLODE encourages ontology annotation *best
practice* by only producing good results for well documented inputs! pyLODE defines what it considers 'well documented'
in sections below, such as `Profiles`_ & `What pyLODE understands`_.

.. note:: This is pyLODE version 3.0.0 and it's vastly different from pyLODE < 3.0.0. It doesn't yet handle all the various "profiles" that pyLODE 2.13.2 does, such as SKOS _vocabularies_ & Profiles Vocabulary _profiles, it only handles OWL _ontologies_. BUT, it handles ontologies much better and the code is both more efficient and much more maintainable, which is why it's been made. v 3.1.0 and so on will catch up to all of v 2.13.2's features.


Contents
========
1. `Quick Intro`_
2. Use_
3. `What pyLODE understands`_
4. Examples_
5. Installation_
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

Use
===

The tool can be used in multiple ways:

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

Command line arguments
----------------------

The BASH, Windows EXE and Python Script methods all use the same command line
arguments:

::

    usage: cli.py [-h] [-v] [-o OUTPUTFILE] [-c {true,false}] input

    positional arguments:
        input                 Input file location or URL

    optional arguments:
        -h, --help          show this help message and exit
        -v, --version       show program's version number and exit
        -o OUTPUTFILE,
        --outputfile OUTPUTFILE
                            A name you wish to assign to the output file. Will be
                            postfixed with .html if not already added. If no
                            output file is given, output will be printed to screen
        -c {true,false},
        --css {true,false}
                            Whether (true) or not (false) to include CSS within an
                            output HTML file.

Examples
========

Basic

* as a Python script
* executed in this directory

::

    python pylode examples/minimal.ttl -o minimal.html

This will produce the file ``minimal.html`` in this directory which should
match exactly the file ``examples/minimal.html``.

What pyLODE understands
=======================

pyLODE knows about definitional ontologies (``owl:Ontology``) and the major
elements usually fount in them, such as classes (``owl:Class`` or ``rdf:Class)
and properties (``rdf:Property`` & ``owl:ObjectProperty`` etc.).

To see what properties for ontology, class and RDF property documentation
pyLODE currently supports, just look in the ``rdf_elements.py`` file. All
elements' properties supported are given in property lists there.

pyLODES won't just translate everything that you can describe in RDF into
HTML! This is a conscious design choice to ensure that a certain conventional
style of documented ontology is produced. However, surrport for new
properties and ontology patterns can be made - just create an Issue on
`this project's Issue tracker <https://github.com/RDFLib/pyLODE/issues>`__.

While it *does* know about instance data, such as Named Individuals, it's
not really designed to document large ontologies containing class instances.


Installation
============