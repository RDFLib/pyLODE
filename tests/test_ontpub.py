import re
from pathlib import Path
from textwrap import dedent

import pytest
from rdflib import Graph

from pylode import __version__
from pylode.profiles import OntPub
from pylode.utils import de_space_html


# scope="session" so that this is reused
# without regeneration in this testing session
@pytest.fixture(scope="session")
def fix_html():
    od = OntPub(Path(__file__).parent / "data" / "prof.ttl")
    return od.make_html()


def test_sdo(fix_html):
    sdo_expected = """{
          "@graph": [
            {
              "@id": "http://www.w3.org/ns/dx/prof",
              "@type": "https://schema.org/DefinedTermSet",
              "https://schema.org/contributor": [
                "Antoine Isaac",
                "Simon Cox",
                "Alejandra Gonzalez-Beltran",
                "Makx Dekkers"
              ],
              "https://schema.org/creator": [
                {
                  "@id": "_:n8685fd29ed2c4ee3b3341a0f43e2c4c9b1"
                },
                {
                  "@id": "_:n8685fd29ed2c4ee3b3341a0f43e2c4c9b3"
                }
              ],
              "https://schema.org/dateCreated": {
                "@type": "http://www.w3.org/2001/XMLSchema#date",
                "@value": "2018-02-16"
              },
              "https://schema.org/dateModified": {
                "@type": "http://www.w3.org/2001/XMLSchema#date",
                "@value": "2019-10-25"
              },
              "https://schema.org/description": {
                "@language": "en",
                "@value": "This vocabulary is for describing relationships between standards/specifications, profiles of them and supporting artifacts such as validating resources.\\n\\nThis model starts with [http://dublincore.org/2012/06/14/dcterms#Standard](dct:Standard) entities which can either be Base Specifications (a standard not profiling any other Standard) or Profiles (Standards which do profile others). Base Specifications or Profiles can have Resource Descriptors associated with them that defines implementing rules for the it. Resource Descriptors must indicate the role they play (to guide, to validate etc.) and the formalism they adhere to (dct:format) to allow for content negotiation. A vocabulary of Resource Roles are provided alongside this vocabulary but that list is extensible."
              },
              "https://schema.org/name": "Profiles Vocabulary"
            },
            {
              "@id": "_:n8685fd29ed2c4ee3b3341a0f43e2c4c9b1",
              "https://schema.org/affiliation": {
                "@id": "_:n8685fd29ed2c4ee3b3341a0f43e2c4c9b2"
              },
              "https://schema.org/email": {
                "@type": "http://www.w3.org/2001/XMLSchema#anyURI",
                "@value": "nicholas.car@surroundaustralia.com"
              },
              "https://schema.org/identifier": {
                "@id": "http://orcid.org/0000-0002-8742-7730"
              },
              "https://schema.org/name": "Nicholas J. Car"
            },
            {
              "@id": "_:n8685fd29ed2c4ee3b3341a0f43e2c4c9b3",
              "https://schema.org/affiliation": [
                {
                  "@id": "_:n8685fd29ed2c4ee3b3341a0f43e2c4c9b4"
                },
                {
                  "@id": "_:n8685fd29ed2c4ee3b3341a0f43e2c4c9b5"
                }
              ],
              "https://schema.org/email": {
                "@id": "mailto:rob@metalinkage.com.au"
              },
              "https://schema.org/identifier": {
                "@id": "http://orcid.org/0000-0002-7878-2693"
              },
              "https://schema.org/name": "Rob Atkinson"
            }
          ]
        }"""
    g_expected = Graph().parse(data=sdo_expected, format="json-ld")
    sdo_actual = re.findall(
        r"<script([^>]*)>([^<]*)<\/script>", de_space_html(fix_html)
    )[0][1]
    g_actual = Graph().parse(data=sdo_actual, format="json-ld")

    assert g_actual.isomorphic(g_expected)


def test_logo(fix_html):
    html = fix_html
    actual = dedent(f"""
    <div id="pylode">
      <p>made by 
        <a href="https://github.com/rdflib/pyLODE">
          <span id="p">p</span>
          <span id="y">y</span>
          <span>LODE</span>
        </a>
        <a href="https://github.com/rdflib/pyLODE/release/{__version__}" id="version">{__version__}</a>
        <span> with the </span>
        <a href="https://linked.data.gov.au/def/ontpub" id="profile">OntPub</a>
        <span>profile</span>
      </p>
    </div>""")

    assert de_space_html(actual).strip() in de_space_html(html), (
        "pyLODE logo not generated correctly"
    )


def test_metadata(fix_html):
    assert (
        de_space_html(
            """
        <dl>
          <div>
            <dt>
              <strong>IRI</strong>
            </dt>
            <dd>
              <code>http://www.w3.org/ns/dx/prof</code>
            </dd>
          </div>
          <div>
            <dt>
              <a class="hover_property" href="http://purl.org/dc/terms/title" title="A name given to the resource. Defined in DCMI Metadata Terms">Title</a>
            </dt>
            <dd><p>Profiles Vocabulary</p></dd>
          </div>
          <div>
            <dt>
              <a class="hover_property" href="http://purl.org/dc/terms/creator" title="An entity responsible for making the resource. Defined in DCMI Metadata Terms">Creator</a>
            </dt>
            <dd>
        """
        )
        in de_space_html(fix_html)
    ), "Metadata section not generated correctly"


def test_classes_hierarchy(fix_html):
    assert (
        de_space_html(
            """
        <h3 id="class-hierarchy">Class Hierarchy</h3>
        <div class="hierarchy">
            <ul class="hierarchy">
              <li>
                <a href="#Profile">Profile</a>
              </li>
              <li>
                <a href="#ResourceDescriptor">Resource Descriptor</a>
              </li>
              <li>
                <a href="#ResourceRole">Resource Role</a>
              </li>
            </ul>
        </div>
            """
        )
        in de_space_html(fix_html)
    ), "Classes hierarchy section not generated correctly"


def test_classes_definitions(fix_html):
    assert (
        de_space_html(
            """
        <h3 id="class-definitions">Class Definitions</h3>
        <div class="property entity" id="ResourceDescriptor">
          <h3>Resource Descriptor
            <sup class="sup-c" title="OWL/RDFS Class">c</sup>
          </h3>
          <table>
            <tr>
              <th>IRI</th>
              <td>
                <code>http://www.w3.org/ns/dx/prof/ResourceDescriptor</code>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://purl.org/dc/terms/description" title="An account of the resource. Defined in DCMI Metadata Terms">Description</a>
              </th>
              <td><p>A description of a resource that defines an aspect - a particular part, feature or role - of a Profile</p></td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="https://w3id.org/profile/ontdoc/inDomainOf" title="Inverse of rdfs:domain. Defined in Ontology Documentation Profile">In Domain Of</a>
              </th>
              <td>
                <ul class="pylodelitlist">
                  <li>
                    <span>
                      <a href="#hasArtifact">has artifact</a>
                      <sup class="sup-op" title="OWL Object Property">op</sup>
                    </span>
                  </li>
                  <li>
                    <span>
                      <a href="#isInheritedFrom">is inherited from</a>
                      <sup class="sup-op" title="OWL Object Property">op</sup>
                    </span>
                  </li>
                  <li>
                    <span>
                      <a href="#hasRole">has role</a>
                      <sup class="sup-op" title="OWL Object Property">op</sup>
                    </span>
                  </li>
                </ul>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="https://w3id.org/profile/ontdoc/inRangeOf" title="Inverse of rdfs:range. Defined in Ontology Documentation Profile">In Range Of</a>
              </th>
              <td>
                <span>
                  <a href="#hasResource">has resource</a>
                  <sup class="sup-op" title="OWL Object Property">op</sup>
                </span>
              </td>
            </tr>
          </table>
        </div>
        <div class="property entity" id="ResourceRole">
          <h3>Resource Role
            <sup class="sup-c" title="OWL/RDFS Class">c</sup>
          </h3>
          <table>
            <tr>
              <th>IRI</th>
              <td>
                <code>http://www.w3.org/ns/dx/prof/ResourceRole</code>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://purl.org/dc/terms/description" title="An account of the resource. Defined in DCMI Metadata Terms">Description</a>
              </th>
              <td><p>A role that an profile resource, described by a Resource Descriptor, plays</p></td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://www.w3.org/2000/01/rdf-schema#subClassOf" title="The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)">Sub Class Of</a>
              </th>
              <td>
                <span>
                  <a href="http://www.w3.org/2004/02/skos/core#Concept">Concept</a>
                  <sup class="sup-c" title="OWL/RDFS Class">c</sup>
                </span>
              </td>
            </tr>
          </table>
        </div>
        <div class="property entity" id="Profile">
          <h3>Profile
            <sup class="sup-c" title="OWL/RDFS Class">c</sup>
          </h3>
          <table>
            <tr>
              <th>IRI</th>
              <td>
                <code>http://www.w3.org/ns/dx/prof/Profile</code>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://purl.org/dc/terms/description" title="An account of the resource. Defined in DCMI Metadata Terms">Description</a>
              </th>
              <td><p>A specification that constrains, extends, combines, or provides guidance or explanation about the usage of other specifications.</p>
<p>This definition includes what are often called "application profiles", "metadata application profiles", or "metadata profiles".</p></td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://purl.org/dc/terms/source" title="A related resource from which the described resource is derived. Defined in DCMI Metadata Terms">Source</a>
              </th>
              <td>
                <a href="https://www.w3.org/2017/dxwg/wiki/ProfileContext">https://www.w3.org/2017/dxwg/wiki/ProfileContext</a>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="http://www.w3.org/2000/01/rdf-schema#subClassOf" title="The subject is a subclass of a class. Defined in The RDF Schema vocabulary (RDFS)">Sub Class Of</a>
              </th>
              <td>
                <a href="http://purl.org/dc/terms/Standard">Standard</a>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="https://w3id.org/profile/ontdoc/inDomainOf" title="Inverse of rdfs:domain. Defined in Ontology Documentation Profile">In Domain Of</a>
              </th>
              <td>
                <ul class="pylodelitlist">
                  <li>
                    <span>
                      <a href="#isProfileOf">is profile of</a>
                      <sup class="sup-op" title="OWL Object Property">op</sup>
                    </span>
                  </li>
                  <li>
                    <span>
                      <a href="#isTransitiveProfileOf">is transitive profile of</a>
                      <sup class="sup-op" title="OWL Object Property">op</sup>
                    </span>
                  </li>
                  <li>
                    <span>
                      <a href="#hasToken">has token</a>
                      <sup class="sup-dp" title="OWL Datatype Property">dp</sup>
                    </span>
                  </li>
                </ul>
              </td>
            </tr>
            <tr>
              <th>
                <a class="hover_property" href="https://w3id.org/profile/ontdoc/inRangeOf" title="Inverse of rdfs:range. Defined in Ontology Documentation Profile">In Range Of</a>
              </th>
              <td>
                <span>
                  <a href="#isInheritedFrom">is inherited from</a>
                  <sup class="sup-op" title="OWL Object Property">op</sup>
                </span>
              </td>
            </tr>
          </table>
        </div>         
            """
        )
        in de_space_html(fix_html)
    ), "Classes definitions section not generated correctly"


def test_object_properties_hierarchy(fix_html):
    open("prof.html", "w").write(fix_html)
    assert (
        de_space_html(
            """
            <div class="hierarchy">
              <ul class="hierarchy">
                <li>
                  <a href="#hasArtifact">has artifact</a>
                </li>
                <li>
                  <a href="#hasResource">has resource</a>
                </li>
                <li>
                  <a href="#hasRole">has role</a>
                </li>
                <li>
                  <a href="#isInheritedFrom">is inherited from</a>
                </li>
                <li>
                  <a href="#isTransitiveProfileOf">is transitive profile of</a>
                  <ul class="hierarchy">
                    <li>
                      <a href="#isProfileOf">is profile of</a>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>            
            """
        )
        in de_space_html(fix_html)
    ), "Object properties hierarchy section not generated correctly"


def test_namespaces(fix_html):
    assert (
        de_space_html(
            """
            <div id="namespaces">
                <h2>Namespaces</h2>
                <dl>
                  <dt id=":">:</dt>
                  <dd>
                    <code>http://www.w3.org/ns/dx/prof/</code>
                  </dd>
                  <dt id="dc">dc</dt>
                  <dd>
                    <code>http://purl.org/dc/elements/1.1/</code>
                  </dd>
                  <dt id="dct">dct</dt>
                  <dd>
                    <code>http://purl.org/dc/terms/</code>
                  </dd>
                  <dt id="ns1">ns1</dt>
                  <dd>
                    <code>http://www.w3.org/ns/dx/</code>
                  </dd>
                  <dt id="owl">owl</dt>
                  <dd>
                    <code>http://www.w3.org/2002/07/owl#</code>
                  </dd>
                  <dt id="rdf">rdf</dt>
                  <dd>
                    <code>http://www.w3.org/1999/02/22-rdf-syntax-ns#</code>
                  </dd>
                  <dt id="rdfs">rdfs</dt>
                  <dd>
                    <code>http://www.w3.org/2000/01/rdf-schema#</code>
                  </dd>
                  <dt id="sdo">sdo</dt>
                  <dd>
                    <code>https://schema.org/</code>
                  </dd>
                  <dt id="skos">skos</dt>
                  <dd>
                    <code>http://www.w3.org/2004/02/skos/core#</code>
                  </dd>
                  <dt id="xsd">xsd</dt>
                  <dd>
                    <code>http://www.w3.org/2001/XMLSchema#</code>
                  </dd>
                </dl>
              </div>
            """
        )
        in de_space_html(fix_html)
    ), "Namespaces section not generated correctly"


def test_legend(fix_html):
    assert (
        de_space_html(
            """      <div id="legend">
        <h2>Legend</h2>
        <table class="entity">
          <tr>
            <td>
              <sup class="sup-c" title="OWL/RDFS Class">c</sup>
            </td>
            <td>Classes</td>
          </tr>
          <tr>
            <td>
              <sup class="sup-op" title="OWL Object Property">op</sup>
            </td>
            <td>Object Properties</td>
          </tr>
          <tr>
            <td>
              <sup class="sup-dp" title="OWL Datatype Property">dp</sup>
            </td>
            <td>Datatype Properties</td>
          </tr>
          <tr>
            <td>
              <sup class="sup-ap" title="OWL Annotation Property">ap</sup>
            </td>
            <td>Annotation Properties</td>
          </tr>
        </table>
      </div>"""
        )
        in de_space_html(fix_html)
    ), "Legend section not generated correctly"


def test_toc(fix_html):
    assert (
        de_space_html(
            """
    <div id="toc">
      <h3>Table of Contents</h3>
      <ul class="first">
        <li>
          <h4>
            <a href="#metadata">Metadata</a>
          </h4>
        </li>
        <li>
          <h4>
            <a href="#classes">Classes</a>
          </h4>
          <h5>
            <a href="#class-hierarchy" style="margin-left:10px;">Class Hierarchy</a>
          </h5>
          <h5>
            <a href="#class-definitions" style="margin-left:10px;">Class Definitions</a>
          </h5>
          <ul class="second">
            <li style="margin-left:10px;">
              <a href="#ResourceDescriptor">Resource Descriptor</a>
            </li>
            <li style="margin-left:10px;">
              <a href="#ResourceRole">Resource Role</a>
            </li>
            <li style="margin-left:10px;">
              <a href="#Profile">Profile</a>
            </li>
          </ul>
        </li>
        <li>
          <h4>
            <a href="#objectproperties">Object Properties</a>
          </h4>
          <h5>
            <a href="#object-property-hierarchy" style="margin-left:10px;">Object Property Hierarchy</a>
          </h5>
          <h5>
            <a href="#object-property-definitions" style="margin-left:10px;">Object Property Definitions</a>
          </h5>
          <ul class="second">
            <li style="margin-left:10px;">
              <a href="#hasArtifact">has artifact</a>
            </li>
            <li style="margin-left:10px;">
              <a href="#isInheritedFrom">is inherited from</a>
            </li>
            <li style="margin-left:10px;">
              <a href="#isProfileOf">is profile of</a>
            </li>
            <li style="margin-left:10px;">
              <a href="#isTransitiveProfileOf">is transitive profile of</a>
            </li>
            <li style="margin-left:10px;">
              <a href="#hasResource">has resource</a>
            </li>
            <li style="margin-left:10px;">
              <a href="#hasRole">has role</a>
            </li>
          </ul>
        </li>
        <li>
          <h4>
            <a href="#datatypeproperties">Datatype Properties</a>
          </h4>
          <ul class="second">
            <li>
              <a href="#hasToken">has token</a>
            </li>
          </ul>
        </li>
        <li>
          <h4>
            <a href="#annotationproperties">Annotation Properties</a>
          </h4>
          <ul class="second">
            <li>
              <a href="#conformsto">conforms to</a>
            </li>
            <li>
              <a href="#format">format</a>
            </li>
          </ul>
        </li>
        <li>
          <h4>
            <a href="#namespaces">Namespaces</a>
          </h4>
          <ul class="second">
            <li>
              <a href="#"></a>
            </li>
            <li>
              <a href="#dc">dc</a>
            </li>
            <li>
              <a href="#dct">dct</a>
            </li>
            <li>
              <a href="#ns1">ns1</a>
            </li>
            <li>
              <a href="#owl">owl</a>
            </li>
            <li>
              <a href="#rdf">rdf</a>
            </li>
            <li>
              <a href="#rdfs">rdfs</a>
            </li>
            <li>
              <a href="#sdo">sdo</a>
            </li>
            <li>
              <a href="#skos">skos</a>
            </li>
            <li>
              <a href="#xsd">xsd</a>
            </li>
          </ul>
        </li>
        <li>
          <h4>
            <a href="#legend">Legend</a>
          </h4>
          <ul class="second"></ul>
        </li>
      </ul>
    </div>        
        """
        )
        in de_space_html(fix_html)
    ), "ToC logo not generated correctly"
