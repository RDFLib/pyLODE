import pylode


def basic():
    m = pylode.MakeDocco(
        input_data_file="agrif.ttl",
        # profile="ontdoc",
        # outputformat="html",
    )

    f = "agrif.html"
    print(m.document(destination=f))


if __name__ == "__main__":
    basic()
