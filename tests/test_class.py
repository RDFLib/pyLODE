import pylode


def test_basic_class():
    m = pylode.MakeDocco(input_data_file="agrif.ttl")

    agrif_html = m.document()

    assert '<li><a href="#Series">Series</a></li>' in agrif_html
    assert '''    <div class="entity class" id="Series">
        <h3>
          Series<sup title="class" class="sup-c">c</sup>
          <span style="float:right; margin-right:10px; font-size:smaller;"><a href="#Series" title="fragment link to here">#</a> <a href="#classes" title="Classes Index">Classes</a></span>
        </h3>
        <table>
            <tr>
                <th>URI</th>
                <td><code>https://linked.data.gov.au/def/agrif#Series</code></td>
            </tr>
            <tr>
                <th>Description</th>
                <td>
                    <p>A Series is an identifier for an item, and when combined with a control symbol gives an item its intellectual context.</p>
                </td>
            </tr>
            <tr>
                <th>Super-classes</th>
                <td>
                    <a href="#IntellectualControlSystem">Intellectual Control System</a><sup class="sup-c" title="class">c</sup><br/>
                </td>
            </tr>
            <tr>
                <th>Restrictions</th>
                <td>
                    <a href="#associatedFunction">associated Function</a><sup class="sup-op" title="object property">op</sup> <span class="cardinality">only</span> <a href="#Function">Function</a><sup class="sup-c" title="class">c</sup><br/>
                </td>
            </tr>
        </table>
    </div>''' in agrif_html


if __name__ == "__main__":
    test_basic_class()
