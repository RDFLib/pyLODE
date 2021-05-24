from pylode.common import MakeDocco


def test_issue_110():
    output_html_file = "test_issue_110_output.html"
    m = MakeDocco(input_data_file="test_issue_110_input.ttl")
    m.document(destination=output_html_file)
    assert "balance between £1,000 and £1,000,000 GBP" in open(output_html_file).read()


if __name__ == '__main__':
    test_issue_110()

    print("ok")
    # this test works running on BASH command line with with
    # `pylode -i test_issue_110_input.ttl -c true -o test_issue_110_output.html`
