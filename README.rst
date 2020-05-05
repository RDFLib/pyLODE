.. image:: img/pyLODE-250.png

.. image:: https://badge.fury.io/py/pyLODE.svg
    :target: https://badge.fury.io/py/pyLODE

pyLODE
******
An OWL ontology documentation tool using Python and templating, based on
LODE.

In addition to making human-readable forms of ontologies/taxonomies, pyLODE encourages ontology annotation *best
practice* by only producing good results for well documented inputs! pyLODe defines what it considers w'well documented'
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
8. `Releases roadmap`_
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
documented is parsed and inspected using rdflib and HTML or Markdown is generated
using basic Python scripting and Python's `Jinja2
templating <https://pypi.org/project/Jinja2/>`__.

The tool can be run as in these ways:

- Python command line
    - cli.py in the main folder
- BASH command line
    - bin/ directory, uses cli.py
- as-a-service locally
    - via the popular `Falcon framework <https://falconframework.org/>`__.
    - see server.py in the main folder
- as-a-service online
    - hosted at https://kurrawong.net/pylode-online


Examples
========
pyLODE has been tested with all of the 30+ ontologies in `pylode/examples/ <pylode/examples/>`_ and we are trying to
ensure it captures all of their annotations. For each example, there is the original RDF file and the corresponding
output, in HTML & Markdown.

For example, `Epimorphic's <https://www.epimorphics.com/>`__'s **Registry Ontology** is:

- **agrif.ttl** - source file
- **agrif.html** - HTML output
    - see this `rendered online by GitHack <https://raw.githack.com/RDFLib/pyLODE/master/pylode/examples/agrif.html>`__
    - see `the point-of-truth rendered online <https://linked.data.gov.au/def/agrif>`__
- **agrif.md** - Markdown output
    - see this `rendered online by GitHub <https://github.com/RDFLib/pyLODE/blob/master/pylode/examples/agrif.md>`__
- **agrif.skos.html** - HTMl output, "skosp" profile
    - see this `rendered online by GitHack <https://raw.githack.com/RDFLib/pyLODE/master/pylode/examples/agrif.skosp.html>`__

You can build all of the example outputs locally by running `pylode/examples/_make_examples.py <pylode/examples/_make_examples.py>`_
which also serves as a good demonstration of calling pyLODE from a Python file.


Ontologies online using pyLODE:
-------------------------------

- `Australia's Department of Finance's <https://www.finance.gov.au>`__'s **AGRIF ontology** - http://linked.data.gov.au/def/agrif
    - see the `Markdown version <https://github.com/AGLDWG/agrif-ont/blob/master/agrif.md>`__
- `National Archives of Australia <http://www.naa.gov.au>`__'s **Commonwealth Records Series ontology** - http://linked.data.gov.au/def/crs
    - see the `Markdown version <https://github.com/RDFLib/pyLODE/blob/master/src/pylode/examples/crs.md>`__
- `CSIRO's <https://www.csiro.au>`__'s **LocI ontology** - http://linked.data.gov.au/def/loci
-  `Geological Survey of
   Queensland <https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/gsq>`__'s
   **Boreholes Profile** - http://linked.data.gov.au/def/borehole
-  `Geoscience Australia <http://www.ga.gov.au/>`__'s **Place Names
   Profile** - http://linked.data.gov.au/def/placenames
-  `Epimorphic <https://www.epimorphics.com/>`__'s **Registry Ontology**
   - https://epimorphics.com/public/vocabulary/Registry.html
- `Semantic Web for Earth and Environmental Terminology <http://sweetontology.net>`__ (SWEET)

See pairs of RDF & HTML files in the
`pylode/examples/ <pylode/examples/>`__ directory for other,
preprocessed examples.


Installation
============
This tool can be used either as a command line utility (Linux, Mac or Windows, see below) or as a Python module in other Python code. It can also be used via an online API. This repo contains executable files for Mac & Windows (soon Linux!) that you can use without any installation too.

The most import dependency to get correct when using this as a Python script of a command line program is the package ``rdflib`` which must be v5.0.0 or greater (see requirements.txt).

Python
------
Do this to use pyLODE as a Python command line program.

This tool is available on PyPI, the Python Package Index, at https://pypi.org/project/pyLODE/ and can be installed for use as a Python module via pip:

::

    pip install pylode

For desktop command line use, just clone this repository and either use ``cli.py`` as per the command line instructions below or use makedocco.py as a Python script directly.


Use
===
pyLODE presents natively as a Python command-line utility,
`pylode/cli.py <pylode/cli.py>`__ and there are also a BASH, Windows & Mac OS options available for command line use:

* `pylode/bin/pylode.sh <pylode/bin/pylode.sh>`__ - BASH script
* Linux executable coming soon!
* `pylode/bin/pylode.app <pylode/bin/pylode.app>`__ - MAC OS command line executable script
* `pylode/bin/pylode.exe <pylode/bin/pylode.exe>`__ - Windows command line executable

Additionally, there is a `Falcon framework <https://falconframework.org/>`__ local HTTP server option.

All use the same command line arguments.

Command line arguments
----------------------
These are the command line arguments to run pyLODE as a BASH or Python script on Linux, Mac etc. or via the Windows executable:

-  ``-i`` or ``--inputfile``, *required if* ``-u`` *not used*
    -  The RDF ontology file you wish to generate HTML for Must be in either Turtle, RDF/XML, JSON-LD or N-Triples formats indicated by the file type extensions .rdf, .owl, .ttl, .n3, .nt, .json respectively
-  ``-u`` or ``--url``, *required if* ``-i`` *not used*
    -  The RDF ontology you wish to generate HTML for, online. Must be an absolute URL that can be resolved to RDF, preferably via Content Negotiation.
-  ``-c`` or ``--css``, *optional, default 'false'*
    -  Whether (true) or not (false) to copy the default CSS file to the output directory.
-  ``-o`` or ``--outputfile``, *optional*
    -  A name you wish to assign to the output file. Will be postfixed with .html or .md. If not specified, the name of the input file or last segment of RDF URI will be used, + .html/.md.
-  ``-f`` or ``--outputformat``, *optional, default 'html'*
    - The output format of the documentation. 'html' or 'md' accepted.
-  ``-p`` or ``--profile``, *optional, default 'owl'*
    - The profile (specification) for ontology documentation used. This has been "owl" (for OWL Ontology) only until the recent introduction of "skosp" (according to the `Simple Knowledge Organization System (SKOS) <https://www.w3.org/TR/skos-reference/>`__). See ``-lp`` for all profiles supported.
-  ``-lp`` or ``--listprofiles``, *optional, no arguments*
    - Lists all the profiles (specifications) for ontology documentation supported by pyLODE

Example call
------------
This call to the BASH script in `pylode/bin/ <pylode/bin/>`__ will
create an HTML document for an ontology called ``placenames.html`` and
save it with a basic CSS file into
`pylode/output\_files/ <pylode/output_files/>`__:

::

    $ ./pylode -i ../example/prof.ttl --css true

Online API
----------
An online API to access pyLODE is now available in test mode at https://kurrawong.net/pylode-online.

Local server - Falcon
---------------------
You can run pyLODE using your own, local, HTTP server like this:
::
        cd pylode && gunicorn --chdir /path/to/pyLODE/pylode server:api

Then, in another terminal:
::
        curl localhost:8000/lode?url=http://sweetontology.net/sweetAll.ttl

Windows - create EXE from source
--------------------------------
`Pyinstaller <https://www.pyinstaller.org/>`__ can be 
`used <https://pyinstaller.readthedocs.io/en/stable/usage.html>`__ to create an 
executable for Windows that has the same characteristics as the Linux/Mac 
CLI program. 
The necessary ``.spec`` file is already included in ``pylode-cli.spec``.
The ``pylode-cli.spec`` PyInstaller spec file creates a ``.exe`` for the 
pyLODE Command Line utility. See above for the pyLODE command line util usage instructions.

See `the PyInstaller installation guide <https://pyinstaller.readthedocs.io/en/stable/installation.html#installing-in-windows>`__
for info on how to install PyInstaller for Windows.

Once you have pyinstaller, use pyinstaller to generate the ``pyLODE.exe`` CLI file like so:

::

    $ cd src/pylode
    $ pyinstaller pylode-cli.spec

This will output ``pylode.exe`` in the ``dist`` directory in ``src/pylode``.

You can now run the pyLODE Command Line utility via ``pylode.exe``. 
See above for the pyLODE command line util usage instructions.

Mac OS - create APP from source
-------------------------------
As per instructions for PyInstaller use on Windows, just do it on a Mac!

What pyLODE understands
=======================

Annotations
-----------
pyLODE understands the following ontology constructs:

-  **ontology metadata**
    -  *imports* - ``owl:imports``
    -  *title* - ``rdfs:label`` or ``skos:prefLabel`` or ``dct:title`` or ``dc:title``
    -  *description* - ``rdfs:comment`` or ``skos:definition`` or ``dct:description`` or ``dc:description``
        - Markdown is supported
    -  *historyNote* - ``skos:historyNote``
        - Markdown is supported
    -  *version URI* - ``owl:versionIRI`` as a URI
    -  *version info* - ``owl:versionInfo`` as a string
        - *preferred namespace prefix* - ``vann:preferredNamespacePrefix`` as a token
        - *preferred namespace URI* - ``vann:preferredNamespaceUri`` as a URI
    -  **agents**: *publishers*, *creators*, *contributors*
        - see **Agent Formatting** below for details
        - see the `pylode/examples/ <pylode/examples/>`__ directory for examples!
    -  **dates**: *created*, *modified*, *issued* - ``dct:created`` etc., all as ``xsd:date`` or ``xsd:dateTime`` datatype properties
    -  **rights**: *license* - ``dct:license`` as a URI & *rights* - ``dct:rights`` as a string
    -  *code respository* - ``schema:codeRepository`` as a URI
    -  *source* - ``dcterms:source`` as a URI or text
-  **classes**
    -  per ``rdfs:Class`` or ``owl:Class``
    -  *title* - ``rdfs:label`` or ``skos:prefLabel`` or ``dct:title``
    -  *description* - ``rdf:comment`` or ``skos:definition`` or ``dct:description`` as a string or using `Markdown <https://daringfireball.net/projects/markdown/>`__ or HTML
    -  *usage note* - a ``skos:scopeNote`` string
    -  *example* - a ``skos:example`` string containing RDF
    -  *super classes* - by declaring a class to be ``owl:subClassOf`` something
    -  *sub classes* - pyLODE will work these out itself
    -  *restrictions* - by declaring a class to be ``owl:subClassOf`` of an ``owl:Restriction`` with any of the normal cardinality or property existence etc. restrictions
    -  *in domain/range of* - pyLODE will auto-calculate these
-  **properties**
    -  per ``owl:ObjectProperty``, ``owl:DatatypeProperty`` or ``owl:AnnotationProperty``
    -  *title* - ``rdfs:label`` or ``skos:prefLabel`` or ``dct:title``
    -  *description* - ``rdf:comment`` or ``skos:definition`` or ``dct:description``
    -  *usage note* - a ``skos:scopeNote`` string
    -  *example* - a ``skos:example`` string containing RDF
    -  *super properties* - by declaring a class to be ``owl:subPropertyOf`` something
    -  *sub properties* - pyLODE will work these out itself
    -  *equivalent properties* - by declaring a class to be ``owl:equivalentProperty`` something
    -  *inverse of* - by declaring a class to be ``owl:inverseOf`` something
    -  *domains* - ``rdfs:domain`` or ``schema:domainIncludes``
    -  *ranges* - ``rdfs:range`` or ``schema:rangeIncludes``
-  **namespaces**
    -  pyLODE will honour any namespace prefixes you set and look up others in `http://prefix.cc <http://prefix.cc/>`__
    -  it will either read your ontology's default/base URI in annotations or guess it using a number of methods
-  **named individuals**
    -  *coming!*

Agent Formatting
&&&&&&&&&&&&&&&&&
-  Use either the DC versions of properties (``dc:publisher`` etc.) or the DCT versions (``dct:publisher`` etc.)
-  if using the DC form, the range should just be a string, e.g. ``dc:publisher "Geoscience Australia" .`` or ``dc:creator "Nicholas J. Car" .``
-  if using the DCT form, the range should be a ``foaf:Agent`` or ``schema:Person`` Blank Node or URI (if details are given elsewhere in the ontology) with the following properties:
    - ``foaf:name``/``sdo:name``
    - ``foaf:mbox``/``sdo:email``
    - ``foaf:homepage``/``schema:identifier`` / ``sdo:url``
- Affiliation of people to organisation can be made if schem.aorg is used using ``sdo:member`` or ``sdo:affiliation`` (latter preferred)
    - e.g.

::

    <ontology_x>
        dct:creator [
            sdo:name "Nicholas J. Car" ;
            sdo:identifier <http://orcid.org/0000-0002-8742-7730> ;
            schema:email <mailto:nicholas.car@surroundaustralia.com> ;
            sdo:affiliation [
                sdo:name "SURROUND Australia Pty Ltd" ;
                sdo:url <https://surroundaustralia.com> ;
            ] ;
        ] ;

Additions
&&&&&&&&&&&&&&&&&
To help pyLODE understand more annotations, see **Suggestions** below.


schema.org
&&&&&&&&&&&
When an HTML document is generated, i.e. not Markdown or other format,
`schema.org <https://schema.org>`__ metadata is added to the HTML
header in the form of properties of a ``DigitalDocument`` subject.
The schema.org properties catered for are:

- ``name``
- ``dateCreated``
- ``dateModified``
- ``description``
- ``license``
- ``copyrightYear``
- ``repository``

Not yet handled, but will be soon, are:

- ``publisher``
- ``creator``
- ``copyrightHolder``

See `SNIPPETS <SNIPPETS.rst>`__ for detailed examples on what pyLODE knows about Agents Provenance etc.

Please suggest any more required schema.org annotations!

Styling
-------
This tool generates HTML that is shamelessly similar to LODE's styling.
That's because we want things to look familiar and LODE's outputs look
great. The Markdown's pretty vanilla.

Also, pyLODE generates and uses only static HTML + CSS, no JavaScript,
live loading Google Fonts etc. This is to ensure that all you need for
nice display is within a couple of static, easy to use and maintain,
files. Prevents documentation breaking over time.

Feel free to extend your styling with your own CSS.


Profiles
========
pyLODE can document ontologies and other taxonomies according to different *profiles* which are specifications. The
basic, default, profile is pyLODE's OWL Profile, which means documentation is generated according to OWL properties
and classes and the various annotation properties listed here in the `What pyLODE understands`_ section.

pyLODE can tell you what profiles it supports: just run ``~$ pylode -lp`` ("list profiles") or, if calling from Python:

::

    m = MakeDocco(input_data_file="examples/data-access-rights.ttl", profile="skosp")
    print(m.list_profiles())


Supported Profiles
------------------
Currently pyLODE supports its OWL profile, as described above, and a profile of SKOS. For full details of what the
profiles include, see the profiles' definitions at:

========= ==========================================
**Token** **URI**
========= ==========================================
owlp      `<https://w3id.org/profile/pylode-owl>`_
skosp     `<https://w3id.org/profile/pylode-skos>`_
========= ==========================================


Transformation by Profile
-------------------------
You can, of course, document an OWL ontology using the *owlp* profile or a SKOS taxonomy using the *skosp* profile
however, you can also document an OWL ontology using the *skosp* profile! This is because SKOS is conceptually a subset
of OWL - whatever you can express in SKOS you can express in OWL.

pyLODE performs an OWL > SKOS transformation on OWL ontologies to produce a taxonomy document. The following
conversions are made:

- ``owl:Ontology`` > ``skos:ConceptScheme``
    - and all the ontology metadata is used with the ConceptScheme
- ``owl:Class`` > ``skos:Concept``
    - and other class annotation properties used with Concept
- ``owl:subClassOf`` > ``skos:broader``
   - and the inverses, ``skos:narrower``

To see the full list of transformations, see the function ``_expand_graph_for_skos()`` in *makedocco.py*.

Examples of a small taxonomies documented using the *skosp* profile are:

- `Data Access Rights <https://raw.githack.com/RDFLib/pyLODE/master/pylode/examples/data-access-rights.skos.html>`_
- `ISO 19115-1's RoleCodes <https://raw.githack.com/RDFLib/pyLODE/master/pylode/examples/iso19115-1-RoleCodes.skos.html>`_

An example of a large one:

- `Earth Science Data Category <https://raw.githack.com/RDFLib/pyLODE/master/pylode/examples/earth-science-data-category.skos.html>`_

An example of a *skosp*-documented OWL ontology and the corresponding *owlp* original is AGRIF:

- `AGRIF as skosp <https://raw.githack.com/RDFLib/pyLODE/master/pylode/examples/agrif.skos.html>`_
- `AGRIF as owlp <https://raw.githack.com/RDFLib/pyLODE/master/pylode/examples/agrif.html>`_


Differences from LODE
=====================
-  command line access

   -  you can use this on your own desktop so you don't need me to
      maintain a live service for use

-  use of more modern & simpler HTML
-  catering for a wider range of ontology options such as:

   -  schema.org ``domainIncludes`` & ``rangeIncludes`` for properties

-  better Agent linking

   -  ``foaf:Agent`` or ``schema:Person`` objects for creators,
      contributors & publishers
   -  you can still use simple string peoperties like
      ``dc:contributor "Nicholas J. Car"`` too if you really must!

::

    <ontology_x>
        dct:creator [
            sdo:name "Nicholas J. Car" ;
            sdo:identifier <http://orcid.org/0000-0002-8742-7730> ;
        ] ;

-  smarter CURIES

   -  pyLODE caches and looks up well-known prefixes to make more/better
      CURIES
   -  it tries to be smart with CURIE presentation by CURIE-ising all
      URIs it finds, rather than printing them

-  **active development**

   -  this software is in use and will be improved for the foreseeable
      future so we will cater for more and more things
   -  recent ontology documentation initiatives such as the `MOD
      Ontology <https://github.com/sifrproject/MOD-Ontology>`__ will be
      handled, if requested


Releases Roadmap
================
pyLODE is under continual and constant development. The current developers have a roadmap for enhancements in mind,
which is given here, however, since this is an open source project, new developers may join the pyLODE dev community
and change/add development priorities.

The current release, as of April 2020, is 2.0.

.. csv-table:: **pyLODE Releas Schedule**
   :header: "Version", "Date", "Description"
   :widths: 15, 10, 30

   3.0, *June 2020*, "Will include pre-testing inputs with SHACL"
   2.0, 18 Apr 2020, "Includes multiple profiles - OWP & SKOSP"
   1.0, 15 Dec 2019, "Initial working release"

Release notes
-------------

3.0
---
Expected to handle

- pre-documentation graph shape testing using SHACL
    - you will be able to see what pyLODE-recommended annotation and design patterns your inputs do/don't handle
- "modp", a documentation profile based on the `MOD Ontology <https://github.com/sifrproject/MOD-Ontology>`_

2.0
---
- handles Named Individuals in OWL ontologies
- implements "owlp" & "skosp" documentation profiles for OWL, SKOS and OWL-as-SKOS results

1.0
---
Initial pyLODE release. Generated HTML documentation for OWL ontologies, missed quite a few expected ontology elements,
such as Named Individuals.

License
=======
This code is licensed using the GPL v3 licence. See the `LICENSE
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
| *Data System Architect*
| `SURROUND Australia Pty Ltd <https://surroundaustralia.com>`_
| nicholas.car@surroundaustralia.com
