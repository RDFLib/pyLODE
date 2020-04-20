from makedocco import MakeDocco


h = MakeDocco(profile='skos')
source_info = ("test_skos_cif.ttl", "turtle")
# generate the HTML doc
with open("test_skos_cif.html", "w") as f:
    f.write(h.document(source_info))
