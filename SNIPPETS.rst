pyLODE Snippets
===============
Small snippets of RDF and corresponding HTML to indicate good ontology documentation.

Contents
--------
1. Agents_
2. Provenance_


Agents
------
Agents, individual persons or organisations, should be associated with ontologies to indicate *authors*, *creators*, *publishers* etc. There are 2 ways to do this that pyLODE understands: datatype & object type.

Datatype - not preferred
~~~~~~~~~~~~~~~~~~~~~~~~
A simple literal value for an agent that a human can read but not a machine can't understand:

* ``<ONTOLOGY_URI> dc:creator "AGENT NAME" .``
   * the range value is a string literal, either string typed (``^^xsd:string``) or language typed (``@en`` or ``@de``)
   * the following `Dublin Core Elements 1.1 <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-3>`__ properties may be used: 
      * ``dc:contributor``
      * ``dc:creator``
      * ``dc:publisher``
   * the following `schema.org <https://schema.org>`__ properties may be used:
      * ``schema:author``
      * ``schema:contributor``
      * ``schema:creator``
      * ``schema:editor``
      * ``schema:funder``
      * ``schema:publisher``
      * ``schema:translator``

::

    <ontology_x>
        dc:creator "Nicholas J. Car" ;

Object type - preferred
~~~~~~~~~~~~~~~~~~~~~~~
An RDF object is used for the agent and can contain multiple details. A Blank Node or a URI can be used. Best case, a persistent agent URI!

.. figure:: img/contributor-object.png
    :align: center
    :figclass: figure-eg

.....

* ``<ONTOLOGY_URI> dct:creator [...] .``

or

* ``<ONTOLOGY_URI> dct:creator <SOME_URI> .``
   * the range value is a Blank Node or a URI of type:
      * ``schema:Person``
      * ``schema:Organization``
      * ``foaf:Person``
      * ``foaf:Organization``
   * the properties of the Blank Node or the URI are as below
   * the following `Dublin Core Terms <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-2>`__ properties may be used:
      * ``dct:contributor``
      * ``dct:creator``
      * ``dct:publisher``
      * ``dct:rightsHolder``
   * the following `schema.org <https://schema.org>`__ properties may be used:
      * ``schema:author``
      * ``schema:contributor``
      * ``schema:creator``
      * ``schema:editor``
      * ``schema:funder``
      * ``schema:publisher`` 
      * ``schema:translator``
   * the following `FOAF <http://xmlns.com/foaf/spec/>`__ properties may be used:
      * ``foaf:maker``

e.g. (Blank Node):

::

    <ontology_x>
        schema:editor [
            a schema:Organization ;
            ...
        ] ;

or (URI):

::

    <ontology_x>
        schema:editor <https://orcid.org/0000-0002-8742-7730> ;
        ...

    <https://orcid.org/0000-0002-8742-7730>
        a foaf:Person ;
        ...


Agent properties
^^^^^^^^^^^^^^^^

* ``foaf:name`` / ``schema:name``
* ``foaf:mbox`` / ``schema:email``
* ``foaf:homepage`` / ``schema:url``
* ``schema:identifier``


e.g.:

::

    <ontology_x>
        dct:creator [
            schema:name "Nicholas J. Car" ;
            schema:identifier <http://orcid.org/0000-0002-8742-7730> ;
            schema:email <mailto:nicholas.car@surroundaustralia.com> ;
        ] ;


Linking a Person to an Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``schema:member``, ``schema:affiliation`` (there is no FOAF Person -> Group/Org property):

e.g.:

::

    <ontology_x>
        dct:creator [
            schema:name "Nicholas J. Car" ;
            schema:identifier <http://orcid.org/0000-0002-8742-7730> ;
            schema:email <mailto:nicholas.car@surroundaustralia.com> ;
            schema:affiliation [
                schema:name "SURROUND Australia Pty Ltd" ;
                schema:url <https://surroundaustralia.com> ;
            ] ;
        ] ;


Provenance
----------

Ontology Source
~~~~~~~~~~~~~~~
The ontology's HTML representation linking back to the RDF: generated automatically

.. figure:: img/source.png
    :align: center
    :figclass: figure-eg

.....

Code Repositories
~~~~~~~~~~~~~~~~~
Indicating to readers where the 'live' version of the ontology is managed:

.. figure:: img/code-repository.png
    :align: center
    :figclass: figure-eg

.....

Code repositories that house an ontology can be indicated either using `schema.org's codeRepository property <https://schema.org/codeRepository>`__ or a combination of the `Description of a Project <https://github.com/ewilderj/doap>`__ and PROV:

::

    @prefix schema: <https://schema.org/> .

    <ONTOLOGY_URI>
        schema:codeRepository <REPO_URI> ;
        ...

or

::

    @prefix doap: <http://usefulinc.com/ns/doap#> .
    @prefix prov: <http://www.w3.org/ns/prov#> .

    <ONTOLOGY_URI>
        prov:wasGeneratedBy [
            a doap:Project , prov:Activity ;
            doap:repository <REPO_URI>
        ]
        ...

e.g., for the `ontology version on ISO 19160-1 <http://linked.data.gov.au/def/iso19160-1-address>`__:

::

    <http://linked.data.gov.au/def/iso19160-1-address>
        prov:wasGeneratedBy [
            a doap:Project , prov:Activity ;
            doap:repository <https://github.com/AGLDWG/iso19160-1-address-ont>
        ] ;
        ...
