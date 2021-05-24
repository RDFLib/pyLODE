# this file runs pyLODe against the ontology, vocabulary and profile files in this dir
from pylode.common import MakeDocco


def main():
    # OntDoc
    ontdoc_file = [
        "agrif-notitle.ttl",
        "agrif.ttl",
        "alternates.ttl",
        "asgs.ttl",
        "bfo.ttl",
        "brick.ttl",
        "crs.ttl",
        "datatype.ttl",
        "decprov.ttl",
        "doap.ttl",
        "ebg.ttl",
        "foaf.ttl",
        "geo.ttl",
        "geoadminfeatures.ttl",
        "geofabric.ttl",
        "geox.ttl",
        "gnaf.ttl",
        "iso19160-1-nz-profile.ttl",
        "iso21972.ttl",
        "loci.ttl",
        "om.ttl",
        "owl.ttl",
        "placenames.ttl",
        "plot.ttl",
        "project.ttl",
        "ra.ttl",
        "rdf.ttl",
        "rdfs.ttl",
        "reg.ttl",
        "sosa.ttl",
        "ssn.ttl"
    ]
    for f in sorted(ontdoc_file):
        print("making ontdoc for {}".format(f))
        h = MakeDocco(input_data_file=f)
        h.document(destination=f.replace(".ttl", ".html"))
        h = MakeDocco(input_data_file=f, outputformat="md")
        h.document(destination=f.replace(".ttl", ".md"))


    # for these files, make a vocpub html & md output
    vocpub_files = [
        'agrif.ttl',
        "agift.ttl",
        'asgs.ttl',
        'collection-item-format.ttl',
        'data-access-rights.ttl',
        'earth-science-data-category.ttl',
        'iso19115-1-RoleCodes.ttl'
    ]
    for f in sorted(vocpub_files):
        print("making vocpub for {}".format(f))
        h = MakeDocco(input_data_file=f, profile="vocpub")
        h.document(destination=f.replace(".ttl", ".vocpub.html"))
        h = MakeDocco(input_data_file=f, profile="vocpub", outputformat="md")
        h.document(destination=f.replace(".ttl", ".vocpub.md"))


    prof_files = [
        "ga-skos.ttl",
        "geo.profile.ttl",
    ]
    for f in sorted(prof_files):
        print("making prof for {}".format(f))
        h = MakeDocco(input_data_file=f, profile="prof")
        h.document(destination=f.replace(".ttl", ".prof.html"))
        h = MakeDocco(input_data_file=f, profile="prof", outputformat="md")
        h.document(destination=f.replace(".ttl", ".prof.md"))


if __name__ == "__main__":
    main()
