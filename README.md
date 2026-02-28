![pyLODE logo](https://raw.githubusercontent.com/RDFLib/pyLODE/master/img/pyLODE-250.png)
[![PyPI version](https://badge.fury.io/py/pyLODE.svg)](https://badge.fury.io/py/pyLODE)

# pyLODE

An OWL ontology documentation tool using Python, based on LODE.

In addition to making web page, human-readable forms of ontologies, pyLODE encourages ontology annotation *best practice* by only producing good results for well documented inputs! pyLODE defines what it considers “well documented” in sections below, e.g. [What pyLODE understands](#what-pylode-understands).

**New mode**: In v3.1.0, pyLODE now has a new mode called `supermodel`, in addition to the existing `ontpub` mode. This new mode allows for documenting **profiles and modules** of multipart models. See [supermodel.md](supermodel.md) for more information.

---

## A note on the v 3.x change

This is pyLODE version 3.0.1 and it’s vastly different from pyLODE 2.x. It doesn’t yet handle all the various “profiles” that pyLODE 2.13.2 does, such as SKOS “vocabularies” & Profiles Vocabulary “profiles”, it only handles OWL “ontologies”, nor all the special data types, such as JSON literals.

However, it generates HTML in a much more straightforward manner and the code is both more efficient and much more maintainable, which is why it’s been made.

v 3.x will eventually catch up to all of v 2.13.2’s features.

To access v 2.13.2 of pyLODE, either:

- [Download it from PyPI](https://pypi.org/project/pylode/2.13.2/)
- [Check it out from GitHub](https://github.com/RDFLib/pyLODE/releases/tag/2.13.2)
- Access it via the [online service](http://tools.kurrawong.ai/pylode)

---

## Contents

1. [Quick Intro](#quick-intro)
2. [Use](#use)
3. [What pyLODE understands](#what-pylode-understands)
4. [Examples](#examples)
5. [Installation](#installation)
6. [Testing](#testing)
7. [Differences from LODE](#differences-from-lode)
8. [Releases](#releases)
9. [License](#license)
10. [Citation](#citation)
11. [Collaboration](#collaboration)
12. [Contacts](#contacts)

## Quick Intro

The Live OWL Documentation Environment tool  
([LODE](https://github.com/essepuntato/LODE)) is a well-known (in Semantic Web circles) Java & XSLT-based tool used to generate human-readable HTML documents for OWL and RDF ontologies. That tool is now a bit dated and its [online version](https://essepuntato.it/lode) is not always online.

This tool is a complete re-implementation of LODE’s functionality using Python and Python’s RDF manipulation module, [rdflib](https://pypi.org/project/rdflib/). An ontology to be documented is parsed and inspected using rdflib and HTML is generated directly using Python’s [dominate](https://pypi.org/project/dominate/) package.

## Use

The tool can be used in multiple ways:

- BASH command line script  
  - `pyLODE.sh` in `bin/`
- Windows EXE  
  - `pyLODE.exe` in `bin/`
- Mac executable  
  - `pyLODE` in `bin/`
- Python script  
  - `cli.py` or module
- As-a-service locally  
  - via the [Falcon framework](https://falconframework.org/)
  - see `server.py`
- As-a-service online  
  - https://tools.kurrawong.ai/pylode

### Command line arguments

```text
usage: cli.py [-h] [-v] [-o OUTPUTFILE] [-c {true,false}] input

positional arguments:
    input                 Input file location or URL

optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -o OUTPUTFILE,
    --outputfile OUTPUTFILE
                          Output file name (postfixed with .html if needed)
    -c {true,false},
    --css {true,false}
                          Include CSS in the output HTML
```

### Basic Use

#### As a Python script

```bash
python pylode examples/ontpub/minimal.ttl -o minimal.html
```

#### As a Docker container

```bash
docker build -t pylode:latest .
```

```bash
docker run --mount 'type=bind,src=<ttl_directory>,target=/app/pylode/data' \
  pylode:latest python3.10 pylode/cli.py data/<ttl_file> -o data/<html_file>
```

> Note: `<ttl_directory>` must be absolute

#### Via a stand-alone server

The pyLODE server uses the popular [Falcon framework](https://falconframework.org/) to implement a lightweight web api.

It can be run standalone as a single-thread, single process HTTP server, or more robustly as a WSGI application with
[GUnicorn](https://gunicorn.org/).

In all launch methods listed here, the server will be available at http://localhost:8000 for the landing page and http://localhost:8000/pylode for the active endpoint.

The active endpoint accepts the following querystring parameters:

* `url` for the absolute URL of the ontology document that you wish to render. The server hosting that ontology document must be capable of responding to Content Negotiation,
i.e. it must supply RDF according to an HTTP `Accept` request for `text/turtle`, `application/rdf+xml` etc.
* `profile` for the profile to use to generate HTML. Must be one of:
    * `ontpub` (https://w3id.org/profile/ontpub) for ontologies. This is the default if no ``profile`` is provided.
    * `vocpub` (https://w3id.org/profile/vocpub) for SKOS vocabularies
    * `supermodel` for profiles of profiles
* `sort` to indicate whether subjects should be sorted in the rendered output. Must be one of:
    * `true` to sort the subjects (this is the default)
    * `false` to NOT sort the subjects

Here's an example of use with the [AGIF Ontology](https://linked.data.gov.au/def/agrif) using the source in this repository:

```bash
http://localhost:8000/pylode?url=https://raw.githubusercontent.com/RDFLib/pyLODE/refs/heads/master/examples/ontpub/agrif.ttl
```

The LODE responses generated by the server can be globally customised by setting the following optional environment variables:

* `CSS_URL` can be set to the absolute URL of a CSS stylesheet hosted elsewhere that should be referenced by pyLODE documents
* `FAVICON_URL` can be set to the absolute URL of a favicon image hosted elsewhere that should be referenced by pyLODE documents
* `FAVICON_MIME` should be set to the MIME type of the resource at ``FAVICON_URL`` if that has been configured (e.g. ``image/png`)
* `GTAGID` can be set to a Google Analytics Tag ID that you would like to use for tracking requests to your server.

**Launch the pyLODE server standalone from your local directory:**

You will need a few extra python modules installed locally:

```
pip install bs4 falcon validators
```

You can then run the pyLODE Server in standalone mode like this:

```
python -m pylode.server
```

**Build and run the docker image for the pyLODE Standalone Server:**

```
docker build --target=pylode-server -t pylode-server:latest .
docker run --rm -p 8000:8000 pylode-server:latest
```

**Build and run the docker image for the pyLODE GUnicorn Server:**

```
docker build --target=pylode-gunicorn -t pylode-gunicorn:latest .
docker run --rm -p 8000:8000 pylode-gunicorn:latest
```

### Module Use

#### For OWL

```python
from pylode.profiles.ontpub import OntPub

od = OntPub(ontology="some-ontology-file.ttl")
html = od.make_html()
od.make_html(destination="some-resulting-html-file.html")
```

#### For SKOS

```python
from pylode.profiles.vocpub import VocPub

od = VocPub(ontology="some-ontology-file.ttl")
html = od.make_html()
od.make_html(destination="some-resulting-html-file.html")
```

## Examples

The [`examples/` directory](https://github.com/RDFLib/pyLODE/tree/master/examples) contains multiple RDF & HTML pairs.

Rendered examples:

- [minimal.html](https://rdflib.dev/pyLODE/examples/ontpub/minimal.html)
- [agift.html](https://rdflib.dev/pyLODE/examples/ontpub/agrif.html)
- [alternates.html](https://rdflib.dev/pyLODE/examples/ontpub/alternates.html)
- [asgs.html](https://rdflib.dev/pyLODE/examples/ontpub/asgs.html)

## What pyLODE understands

pyLODE understands definitional ontologies (`owl:Ontology`), classes, and properties.

Supported properties can be found in `rdf_elements.py`.

pyLODE deliberately does **not** translate everything in RDF to HTML, enforcing a conventional ontology documentation style. Support for new patterns can be requested via the [issue tracker](https://github.com/RDFLib/pyLODE/issues).

### Notes on Agents

pyLODE supports simple and complex Agent objects, including ORCIDs, affiliations, and contact details.

```turtle
<ontology_x>
    schema:creator [
        schema:name "Nicholas J. Car" ;
        schema:identifier <http://orcid.org/0000-0002-8742-7730> ;
        schema:email "nick@kurrawong.ai"^^xsd:anyURI ;
        schema:affiliation [
            schema:name "KurrawongAI" ;
            schema:url "https://kurrawong.ai"^^xsd:anyURI ;
        ] ;
    ] ;
.
```

## Installation

pyLODE is available on [PyPI](https://pypi.org/project/pyLODE/):

```bash
pip install pylode
```

## Testing

```bash
python -m pytest tests --disable-warnings
```

## Differences from LODE

-  command line access
   -  you can use this on your own desktop so you don't need me to maintain a live service for use
-  use of modern simple HTML
   - no JavaScript: pyLODE generates static HTML pages
-  catering for a wider range of ontology options such as:
   -  schema.org ``domainIncludes`` & ``rangeIncludes`` for properties
-  better Agent representation
   - see the [Notes on Agents](#notes-on-agents) section above
-  smarter CURIES
   -  pyLODE caches and looks up well-known prefixes to make more/better CURIES
   -  it tries to be smart with CURIE presentation by CURIE-ising all URIs it finds, rather than printing them
-  reference ontologies property labels
   - pyLODE caches ~ 10 well-known ontologies (RDFS, SKOS etc), properties from which people often use for their ontology documentation. Where these properties are used, the background ontology's labels are use
-  **active development**
   -  pyLODE has been under active development since mid-2019 and is
      still very much actively developed - it's not just staying still
   -  it will be improved in foreseeable to cater for more and more things
   -  recent ontology documentation initiatives such as the [MOD Ontology](https://github.com/FAIR-IMPACT/MOD) will be handled, if requested

## Releases

Since version 3.0.1, we have moved to documenting releases in GitHub: https://github.com/RDFLib/pyLODE/releases

Older releasese

| Version | Date             | Description                                                                     |
|---------|------------------|---------------------------------------------------------------------------------|
| 3.0.5   | 27 April 2023    | Minor patching                                                                  |
| 3.0.4   | 24 May 2022      | Use of Poetry                                                                   |
| 3.0.2   | 24 May 2022      | Support for preformatted skos:example literals                                  |
| 3.0.1   | 6 Jan 2022       | Direct HTML generation using dominate; easier to maintain and extend            |
| 2.13.2  | 21 December 2021 | Updated RDFlib to 6.1.1, improved test to properly use pytest                   |
| 2.10.0  | 24 May 2021      | Update Windows EXE build process, simplified versioning                         |
| 2.9.1   | 28 Apr 2021      | Support for ASCIIDOC format (OntDoc profile only)                               |
| 2.8.11  | 28 Apr 2021      | Further changes for PyPI only                                                   |
| 2.8.10  | 27 Apr 2021      | Further changes for PyPI only                                                   |
| 2.8.9   | 27 Apr 2021      | PyPI enhancements only                                                          |
| 2.8.8   | 27 Apr 2021      | Several small bugs fixed, auto-generation of version no. from Git tag           |
| 2.8.6   | 23 Feb 2021      | Fixing char encoding issues, updated examples, new test files style - per issue |
| 2.8.5   | 5 Jan 2021       | Small enhancements to the Falcon server deployment option                       |
| 2.8.3   | 3 July 2020      | Packaging bugfixes only                                                         |
| 2.7     | 1 July 2020      | Much refactoring for new profile creation ease                                  |
| 2.6     | 15 June 2020     | Supports PROF profiles as well as taxonomies & ontologies                       |
| 2.4     | 27 May 2020      | Small improvements over 2.0                                                     |
| 2.0     | 18 Apr 2020      | Includes multiple profiles - OWP & vocpub                                       |
| 1.0     | 15 Dec 2019      | Initial working release                                                         |

## License

This code is licensed using the BSD 3-Clause licence. See the [LICENSE](LICENSE)  file for the deed. Note Citation below though for attribution.

## Citation

If you use pyLODE, please leave the pyLODE logo with a hyperlink back here in the top left of published HTML pages.

## Collaboration

Contributions are welcome!  

Please submit issues or pull requests via the [issue tracker](https://github.com/rdflib/pyLODE/issues).  

But the very best thing you could do is create a Pull Request for us to action!

## Contacts

**Author:**  
Nicholas Car  
*Data Architect*  
[KurrawongAI](https://kurrawong.ai)  
<nick@kurrawong.ai>

## Release Procedure

1. tidy code: `$ task format`
2. pass all tests: `$ task test`
3. increment version number in `pyproject.toml`
4. commit all changes `$ git commit -a "..."`
5. tag with version number: `$git tag ...`
6. push changes `$ git push`
7. push version `git push --tags`
8make a GitHub release
    * PyPI release is automated from this in `pypi.yml`
9. increment version number to next release alpha in `pyproject.toml`
10. commit all changes `$ git commit -a "..."`
1push changes `$ git push`