import glob
from pylode.makedocco import MakeDocco
# get all the Turtle files in this dir
ttl_files = glob.glob("*.ttl")

# for each file, make both an owlp html & md output
for f in sorted(ttl_files):
    print("making {}".format(f))
    h = MakeDocco(input_data_file=f)
    h.document(destination=f.replace(".ttl", ".html"))
    h = MakeDocco(input_data_file=f, outputformat="md")
    h.document(destination=f.replace(".ttl", ".md"))


# for these files, make a skosp html & md output
skosp_files = [
    'agrif.ttl',
    'asgs.ttl',
    'collection-item-format.ttl',
    'data-access-rights.ttl',
    'earth-science-data-category.ttl',
    'iso19115-1-RoleCodes.ttl'
]
for f in sorted(skosp_files):
    print("making skosp for {}".format(f))
    h = MakeDocco(input_data_file=f, profile="skosp")
    h.document(destination=f.replace(".ttl", ".skosp.html"))
    h = MakeDocco(input_data_file=f, profile="skosp", outputformat="md")
    h.document(destination=f.replace(".ttl", ".skosp.md"))
