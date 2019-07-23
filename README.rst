.. image:: https://badge.fury.io/py/pyLODE.svg
    :target: https://badge.fury.io/py/pyLODE

pyLODE
======
An OWL ontology documentation tool using Python and templating, based on
LODE.

The Live OWL Documentation Environment tool
(`LODE <https://github.com/essepuntato/LODE>`__) is a well-known (in
Semantic Web circles) Java & XSLT-based tool used to generate
human-readable HTML documents for OWL and RDF ontologies. That tool is
now a bit dated (old-style HTML, use of older technologies like XSLT)
and it's (`online version <www.essepuntato.it/lode>`__) is not always
online.

This tool is a complete re-implementation of LODE's functionality using
Python and Pythons RDF manipulation module,
`rdflib <https://pypi.org/project/rdflib/>`__. An ontology to be
documented is parsed and inspected using rdflib and HTML is generated
using basic Python scripting and Python's `Jinja2
templating <https://pypi.org/project/Jinja2/>`__.

Differences from LODE
^^^^^^^^^^^^^^^^^^^^^
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
      future so we will cater fro more and more things
   -  recent ontology documentation initiatives such as the `MOD
      Ontology <https://github.com/sifrproject/MOD-Ontology>`__ will be
      handled, if requested

Examples
--------
pyLODE has been tested with all of the ontologies in
`pylode/examples/ <pylode/examples/>`__ and we are trying to ensure it
captures all of their annotations. For each example, there is the
original RDF file and the corresponding output HTML.

Ontologies online using pyLODE:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-  `Geological Survey of
   Queensland <https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/gsq>`__'s
   **Boreholes Profile** - http://linked.data.gov.au/def/borehole
-  `Geoscience Australia <http://www.ga.gov.au/>`__'s **Place Names
   Profile** - http://linked.data.gov.au/def/placenames
-  `Epimorphic <https://www.epimorphics.com/>`__'s **Registry Ontology**
   - https://epimorphics.com/public/vocabulary/Registry.html

See pairs of RDF & HTML files in the
`pylode/examples/ <pylode/examples/>`__ directory for other,
preprocessed examples.

Installation
--------------
This tool can be used either as a command line utility (see below) or as a Python module in other Python code.

This tool is available on PyPI, the Python Package Index, at https://pypi.org/project/pyLODE/ and can be installed for use as a Python module via pip:

::

    pip install pylode

For desktop command line use, just clone this repository and either use Python or the provided BASH scrip (see below).

Use
---
Currently pyLODE presents as a Python & BASH command-line utility,
`pylode/cli.py <pylode/cli.py>`__ &
`pylode/bin/pylode <pylode/bin/pylode>`__ respectively. Windows scripts
may appear soon. All use the same command line arguments.

An online version of it will be available soon too, just as LODE is
(was) available online.

Command line arguments
^^^^^^^^^^^^^^^^^^^^^^
For the command line running of pyLODE, these are the command line
argument options:

-  ``-i`` or ``--inputfile``, *required if* ``-u`` *not used*
-  The RDF ontology file you wish to generate HTML for Must be in either
   Turtle, RDF/XML, JSON-LD or N-Triples formats indicated by the file
   type extensions .rdf, .owl, .ttl, .n3, .nt, .json respectively
-  ``-u`` or ``--url``, *required if* ``-i`` *not used*
-  The RDF ontology you wish to generate HTML for, online. Must be an
   absolute URL that can be resolved to RDF, preferably via Content
   Negotiation.
-  ``-c`` or ``--css``, *optional, default 'false'*
-  Whether (true) or not (false) to copy the default CSS file to the
   output directory.
-  ``-o`` or ``--outputfile``, *optional*
-  A name you wish to assign to the output file. Will be postfixed with
   .html. If not specified, the name of the input file or last segment
   of RDF URI will be used, + .html.

Example call
^^^^^^^^^^^^
This call to the BASH script in `pylode/bin/ <pylode/bin/>`__ will
create an HTML document for an ontology called ``placenames.html`` and
save it with a basic CSS file into
`pylode/output\_files/ <pylode/output_files/>`__:

::

    $ ./pylode -i ../example/prof.ttl --css true

Annotations
-----------

pyLODE understands the following ontology annotations:

-  **ontology metadata**

   -  *imports* - ``owl:imports``
   -  *title* - ``rdfs:label`` or ``skos:prefLabel`` or ``dct:title``
   -  *version URI* - ``owl:versionIRI`` as a URI
   -  *version info* - ``owl:versionInfo`` as a string
   -  *publishers*, *creators*, *contributors*

      -  either the DC versions of properties (``dc:publisher`` etc.) or
         the DCT versions (``dct:publisher`` etc.)
      -  if using the DC form, the range should just be a string, e.g.
         \`dc:publisher "Geoscience Australia" .
      -  if using the DCT form, range should be a ``foaf:Agent`` or
         ``schema:Person`` Blank Node with the following properties: ``foaf:name``/``sdo:name``, ``foaf:mbox``/``sdo:email`` or
         ``foaf:homepage``/``schema:identifier`` properties
      -  see the `pylode/examples/ <pylode/examples/>`__ directory for
         examples!

   -  *created*, modified, issued - ``dct:created`` etc., all as
      ``xsd:date`` or ``xsd:dateTime`` datatype properties
   -  *description* - ``rdf:comment`` or ``skos:definition`` or
      ``dct:description``
   -  *license* - ``dct:license`` as a URI
   -  *rights* - ``dct:rights`` as a string

-  **classes**

   -  per ``rdfs:Class`` or ``owl:Class``
   -  *title* - ``rdfs:label`` or ``skos:prefLabel`` or ``dct:title``
   -  *description* - ``rdf:comment`` or ``skos:definition`` or
      ``dct:description`` as a string or using
      `Markdown <https://daringfireball.net/projects/markdown/>`__ or
      HTML
   -  *usage note* - a ``skos:scopeNote`` string
   -  *super classes* - by declaring a class to be ``owl:subClassOf``
      something
   -  *sub classes* - pyLODE will work these out itself
   -  *restrictions* - by declaring a class to be ``owl:subClassOf`` of
      an ``owl:Restriction`` with any of the normal cardinality or
      property existence etc. restrictions
   -  *in domain/range of* - pyLODE will auto-calculate these

-  **properties**

   -  per ``owl:ObjectProperty``, ``owl:DatatypeProperty`` or
      ``owl:AnnotationProperty``
   -  *title* - ``rdfs:label`` or ``skos:prefLabel`` or ``dct:title``
   -  *description* - ``rdf:comment`` or ``skos:definition`` or
      ``dct:description``
   -  *usage note* - a ``skos:scopeNote`` string
   -  *super properties* - by declaring a class to be
      ``owl:subPropertyOf`` something
   -  *sub properties* - pyLODE will work these out itself
   -  *domains* - ``rdfs:domain`` or ``schema:domainIncludes``
   -  *ranges* - ``rdfs:range`` or ``schema:rangeIncludes``

-  **namespaces**

   -  pyLODE will honour any namespace prefixes you set and look up
      others in `http://prefix.cc <http://prefix.cc/>`__
   -  it will either read your ontology's default/base URI in
      annotations or guess it using a number of methods

-  **named individuals**

   -  *coming!*

To help pyLODE understand more annotations, see **Suggestions** below.

Styling
-------

This tool generates HTML that is shamelessly similar to LODE's styling.
That's because we want things to look familiar and LODE's outputs look
great.

Also, pyLODE generates and uses only static HTML + CSS, no JavaScript,
live loading Google Fonts etc. This is to ensure that all you nned for
nice display is within a couple of static, easy to use and maintain,
files. Prevents documentation breaking over time.

Feel free to extend your styling with your own CSS.

Online use
----------

Soon (July 2019?) an online, hosted, version of this tool will be
implemented so you can use it live, online.

License
-------

This code is licensed using the GPL v3 licence. See the `LICENSE
file <LICENSE>`__ for the deed. Note *Citation* below though for
attribution.

Citation
--------

If you use pyLODE, please leave the pyLODE logo with a hyperlink back
here in the top left of published HTML pages.

Suggestions
-----------

If you have suggestions, please email the contacts below or leave Issues
in this repositories `Issue
tracker <https://github.com/rdflib/pyLODE/issues>`__.

But the very best thing you could do is create a Pull Request for us to
action!

Contacts
--------

| *Author*:
| **Nicholas Car**
| *Data System Architect*
| SURROUND Australia Pty Ltd
| nicholas.car@surround.com
