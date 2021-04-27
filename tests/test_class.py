import pylode


def test_basic_class():
    m = pylode.MakeDocco(
        input_data_file="agrif.ttl",
        # profile="ontdoc",
        # outputformat="html",
    )

    agrif_html = m.document(destination="agrif.html")
    agrif_html = m.document()

    assert '<h3>Series<sup title="class" class="sup-c">c</sup></h3>' in agrif_html
    assert '''    <div class="entity class" id="Series">
        <h3>Series<sup title="class" class="sup-c">c</sup></h3>
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
                    <a href="https://linked.data.gov.au/def/agrif#IntellectualControlSystem">https://linked.data.gov.au/def/agrif#IntellectualControlSystem</a><sup class="sup-c" title="class">c</sup><br/>
                </td>''' in agrif_html


if __name__ == "__main__":
    test_basic_class()
