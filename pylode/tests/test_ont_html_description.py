from pylode import MakeDocco
from os.path import join, dirname, abspath
TESTS_DIR = dirname(abspath(__file__))


h = MakeDocco(input_data_file=join(TESTS_DIR, "test_ont_html_description.ttl"))
# generate the HTML doc
h.document(destination="test_ont_html_description.html")

