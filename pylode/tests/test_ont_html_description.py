from makedocco import MakeDocco


h = MakeDocco(input_data_file="test_ont_html_description.ttl")
# generate the HTML doc
h.document(destination="test_ont_html_description.html")

