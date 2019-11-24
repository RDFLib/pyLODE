.. role:: raw-html(raw)
   :format: html

:raw-html:`<style>.figure-eg {border: solid 1px black;}</style>`


pyLODE Snippets
===============
Small snippets of RDF and corresponding HTML to indicate good ontology documentation.

Agents
------
There are 2 ways to associate agents - *authors*, *creators*, *publishers* etc. - with ontologies using pyLODE for good documentation results: datatype & object type.

Datatype
~~~~~~~~
A simple literal value for an agent.

* ``<ONTOLOGY_URI> dc:creator "AGENT NAME" .``
   * the range value is a string literal
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

Object type
~~~~~~~~~~~
.. figure:: img/contributor-object.png
    :align: center
    :figclass: figure-eg

* ``<ONTOLOGY_URI> dct:creator [...] .``
   * the range value is a Blank Node or a URI of type:
      * ``schema:Person``
      * ``schema:Organization``
      * ``foaf:Person``
      * ``foaf:Organization``
   * the properties of the Blank Node or the URI are as below
   * the following `Dublin Core Terms <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-2>`__ properties may be used:
      * ``dc:contributor``
      * ``dct:creator``
      * ``dct:publisher``
      * ``dc:rightsHolder``
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

e.g.:

::

    <ontology_x>
        schema:editor [
            a schema:Organization ;
            ...
        ] ;

or

::

    <ontology_x>
        schema:editor <https://orcid.org/0000-0002-8742-7730> ;
        ...

    <https://orcid.org/0000-0002-8742-7730>
        a foaf:Person ;
        ...


Object type agent properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``foaf:name`` / ``schema:name``
* ``foaf:mbox`` / ``schema:email``
* ``foaf:homepage`` / ``schema:identifier`` / ``schema:url``


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


Additional Resources
--------------------

Ontology Source
~~~~~~~~~~~~~~~
.. figure:: img/source.png
    :align: center
    :figclass: figure-eg

This is generated automatically

Code Repositories
~~~~~~~~~~~~~~~~~

.. figure:: img/code-repository.png
    :align: center
    :figclass: figure-eg


Code repositories that house an ontology can be indicated using the `Description of a Project <https://github.com/ewilderj/doap>`__ like this:

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
