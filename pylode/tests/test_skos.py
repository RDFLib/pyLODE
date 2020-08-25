from pylode import MakeDocco
from os.path import join, dirname, abspath
TESTS_DIR = dirname(abspath(__file__))

h = MakeDocco(input_data_file=join(TESTS_DIR, "test_skos_cif.ttl"), profile='skos')
# generate the HTML doc
h.document(destination=join(TESTS_DIR, "test_skos_cif.html"))
