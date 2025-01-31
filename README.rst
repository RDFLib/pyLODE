.. image:: https://rawcdn.githack.com/RDFLib/pyLODE/master/img/pyLODE-250.png
.. image:: https://badge.fury.io/py/pyLODE.svg
    :target: https://badge.fury.io/py/pyLODE

pyLODE
******

An OWL ontology documentation tool using Python, based on LODE.

In addition to making web page, human-readable forms of ontologies, pyLODE encourages ontology annotation *best
practice* by only producing good results for well documented inputs! pyLODE defines what it considers 'well documented'
in sections below, e.g. `What pyLODE understands`_.

**New mode**: In v3.1.0, pyLODE now has a new mode called ``supermodel``, in addition to the existing ``ontpub`` mode. This new mode allows for documenting **profiles and modules** of multi-part models. See `supermodel.md <supermodel.md>`_ for more information.

----

**A note on the v 3.x change**

This is pyLODE version 3.0.1 and it's vastly different from pyLODE 2.x. It doesn't yet handle all the various "profiles" that pyLODE 2.13.2 does, such as SKOS 'vocabularies' & Profiles Vocabulary 'profiles', it only handles OWL 'ontologies', nor all the special data types, such as JSON literals, BUT, it generates HTML in a much more straightforward manner and the code is both more efficient and much more maintainable, which is why it's been made.

v 3.x will eventually catch up to all of v 2.13.2's features.

To access v 2.13.2 of pyLODE, either `download it from PyPI <https://pypi.org/project/pylode/2.13.2/>`_ , `check it out from GitHub <https://github.com/RDFLib/pyLODE/releases/tag/2.13.2>`_ or access it via the `online service <http://pylode.surroundaustralia.com/>`_ .

----

Contents
========

1. `Quick Intro`_
2. Use_
3. `What pyLODE understands`_
4. Examples_
5. Installation_
6. Testing_
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
and its (`online version <https://essepuntato.it/lode>`__) is not always
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

- BASH command line script
    - pyLODE.sh in bin/
- Windows EXE
    - pyLODE.exe in bin/
- Mac executable
    - pyLODE in bin/
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

.. code-block:: text

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

Basic Use
^^^^^^^^^

* as a Python script
* executed in this directory

::

    python pylode examples/ontpub/minimal.ttl -o minimal.html

This will produce the file ``minimal.html`` in this directory which should
match exactly the file ``examples/minimal.html``.

* as a docker container

build the docker image:

.. code-block:: bash

    docker build -t pylode:latest .

copy the example directory, mount it to the container and run cli.py in the container:

.. code-block:: bash

    docker  run  --mount 'type=bind,src=<ttl_directory>,target=/app/pylode/data' pylode:latest  python3.10 pylode/cli.py data/<ttl_file> -o data/<html_file>

Note: ``<ttl_directory>`` must be absolute

Module Use
^^^^^^^^^^

for OWL:

.. code-block:: python

    from pylode.profiles.ontpub import OntPub

    # initialise
    od = OntPub(ontology="some-ontology-file.ttl")

    # produce HTML
    html = od.make_html()

    # or save HTML to a file
    od.make_html(destination="some-resulting-html-file.html")

for SKOS:

.. code-block:: python

    from pylode.profiles.vocpub import VocPub

    # initialise
    od = VocPub(ontology="some-ontology-file.ttl")

    # produce HTML
    html = od.make_html()

    # or save HTML to a file
    od.make_html(destination="some-resulting-html-file.html")

This will read from ``some-ontology-file.ttl`` to produce the file ``some-resulting-html-file.html`` in this directory.

Examples
========

The `examples/ directory <https://github.com/RDFLib/pyLODE/tree/master/examples>`_
contains multiple pairs of RDF & HTML files generated from them using this
version of pyLODE.

You can also see rendered versions of these example files online too:

* `minimal.html <https://rdflib.dev/pyLODE/examples/ontpub/minimal.html>`_
* `agift.html <https://rdflib.dev/pyLODE/examples/ontpub/agrif.html>`_
* `alternates.html <https://rdflib.dev/pyLODE/examples/ontpub/alternates.html>`_
* `asgs.html <https://rdflib.dev/pyLODE/examples/ontpub/asgs.html>`_

What pyLODE understands
=======================

pyLODE knows about definitional ontologies (``owl:Ontology``) and the major
elements usually found in them, such as classes (``owl:Class`` or ``rdf:Class``)
and properties (``rdf:Property`` & ``owl:ObjectProperty`` etc.).

To see what properties for ontology, class and RDF property documentation
pyLODE currently supports, just look in the ``rdf_elements.py`` file. All
elements' properties supported are given in property lists there.

pyLODES won't just translate everything that you can describe in RDF into
HTML! This is a conscious design choice to ensure that a certain conventional
style of documented ontology is produced. However, support for new
properties and ontology patterns can be made - just create an Issue on
`this project's Issue tracker <https://github.com/RDFLib/pyLODE/issues>`__.

While it *does* know about instance data, such as Named Individuals, it's
not really designed to document large ontologies containing class instances.

Notes on Agents
---------------

pyLODE can understand both simple and complex Agent objects. You can use
simple string properties like ``dc:contributor "Nicholas J. Car"`` too if
you really must but better would be to take advantage of real Linked Data
representation, e.g. complex Agent objects with web addresses, emails,
affiliations, ORCIDs and so on, e.g.:

.. code-block:: turtle

    <ontology_x>
        dct:creator [
            sdo:name "Nicholas J. Car" ;
            sdo:identifier <http://orcid.org/0000-0002-8742-7730> ;
            sdo:affiliation [
                sdo:name "SURROUND Australia Pty Ldt." ;
                sdo:url "https://surroundaustralia.com"^^xsd:anyURI ;
            ] ;
        ] ;
    .

See all the properties in ``rdf_elements.py:AGENT_PROPS`` for a list of
all the Agent properties pyLODE can handle.

Installation
============

pyLODE is `on PyPI <https://pypi.org/project/pyLODE/>`_, so you can install
it using `pip <https://pypi.org/project/pip/>`_ as normal:

::

    pip install pylode

Testing
=======

It's best to disable warnings to hide pointless warnings from the RDFLib library.

::

    python -m pytest tests --disable-warnings

Differences from LODE
=====================

-  command line access

   -  you can use this on your own desktop so you don't need me to
      maintain a live service for use

-  use of modern simple HTML

   - no JavaScript: pyLODE generates static HTML pages

-  catering for a wider range of ontology options such as:

   -  schema.org ``domainIncludes`` & ``rangeIncludes`` for properties

-  better Agent representation

   - see the `Notes on Agents`_ section above

-  smarter CURIES

   -  pyLODE caches and looks up well-known prefixes to make more/better
      CURIES
   -  it tries to be smart with CURIE presentation by CURIE-ising all
      URIs it finds, rather than printing them

-  reference ontologies property labels

   - pyLODE caches ~ 10 well-known ontologies (RDFS, SKOS etc), properties from which people often use for their ontology documentation. Where these properties are used, the background ontology's labels are use

-  **active development**

   -  pyLODE has been under active development since mid-2019 and is
      still very much actively developed - it's not just staying still
   -  it will be improved in foreseeable to cater for more and more things
   -  recent ontology documentation initiatives such as the `MOD
      Ontology <https://github.com/FAIR-IMPACT/MOD>`__ will be
      handled, if requested


Releases
========

pyLODE is under continual and constant development. The current developers have a roadmap for enhancements in mind,
which is given here, however, since this is an open source project, new developers may join the pyLODE dev community
and change/add development priorities.

Current Release
---------------

The current release is **3.2.1**.

Release Schedule
----------------

.. csv-table:: **pyLODE Release Schedule**
   :header: "Version", "Date", "Description"
   :widths: 15, 10, 30

   3.2.1, 31 January 2025, "Fix version number in version.py"
   3.2.0, 27 July 2024, "dependency updates and merged multiple small PRs"
   3.1.4, 6 April 2024, "Fix load_ontology function's detection of data input"
   3.1.3, 18 March 2024, "Relax rdflib version constraint"
   3.1.2, 18 March 2024, "Relax httpx version constraint"
   3.1.1, 19 February 2024, "Fix release"
   3.1.0, 19 February 2024, "Add supermodel mode - supports documenting profiles and modules"
   3.0.5, 27 April 2023, "Minor patching"
   3.0.4, 24 May 2022, "Use of Poetry"
   3.0.2, 24 May 2022, "Support for preformatted skos:example literals"
   3.0.1, 6 Jan 2022, "Direct HTML generation using dominate; easier to maintain and extend"
   2.13.2, 21 December 2021, "Updated RDFlib to 6.1.1, improved test to properly use pytest"
   2.10.0, 24 May 2021, "Update Windows EXE build process, simplified versioning"
   2.9.1, 28 Apr 2021, "Support for ASCIIDOC format (OntDoc profile only)"
   2.8.11, 28 Apr 2021, "Further changes for PyPI only"
   2.8.10, 27 Apr 2021, "Further changes for PyPI only"
   2.8.9, 27 Apr 2021, "PyPI enhancements only"
   2.8.8, 27 Apr 2021, "Several small bugs fixed, auto-generation of version no. from Git tag"
   2.8.6, 23 Feb 2021, "Fixing char encoding issues, updated examples, new test files style - per issue"
   2.8.5, 5 Jan 2021, "Small enhancements to the Falcon server deployment option"
   2.8.3, 3 July 2020, "Packaging bugfixes only"
   2.7, 1 July 2020, "Much refactoring for new profile creation ease"
   2.6, June 2020, "Supports PROF profiles as well as taxonomies & ontologies"
   2.4, 27 May 2020, "Small improvements over 2.0"
   2.0, 18 Apr 2020, "Includes multiple profiles - OWP & vocpub"
   1.0, 15 Dec 2019, "Initial working release"

License
=======

This code is licensed using the BSD 3-Clause licence. See the `LICENSE
file <LICENSE>`_ for the deed. Note *Citation* below though for
attribution.

Citation
========

If you use pyLODE, please leave the pyLODE logo with a hyperlink back
here in the top left of published HTML pages.

Collaboration
=============

The maintainers welcome any collaboration.

If you have suggestions, please email the contacts below or leave Issues
in this repository's `Issue tracker <https://github.com/rdflib/pyLODE/issues>`_.

But the very best thing you could do is create a Pull Request for us to
action!

Contacts
========

| *Author*:
| **Nicholas Car**
| *Data Architect*
| `Kurrawong AI <https://kurrawong.ai>`_
| nick@kurrawong.ai
