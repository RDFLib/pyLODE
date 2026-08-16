import re
import sys
from pathlib import Path

from pylode.cli import main


def toc_order(html, identifiers):
    toc = html[html.index('<div id="toc">') :]
    links = re.findall(r'href="#([^"]+)"', toc)
    return [link for link in links if link in identifiers]


def test_props(monkeypatch, tmp_path):
    source = Path(__file__).parent / "data" / "symmetric.ttl"

    sorted_output = tmp_path / "symmetric-sorted.html"
    monkeypatch.setattr(
        sys,
        "argv",
        ["pylode", str(source), "--outputfile", str(sorted_output)],
    )
    main()
    sorted_html = sorted_output.read_text()
    sorted_properties = re.findall(
        r'<div class="property entity" id="([^"]+)">',
        sorted_html,
    )
    assert sorted_properties == ["adjacentTo", "regularProp", "touches"]
    assert toc_order(sorted_html, sorted_properties) == sorted_properties

    unsorted_output = tmp_path / "symmetric-unsorted.html"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "pylode",
            str(source),
            "--sort",
            "false",
            "--outputfile",
            str(unsorted_output),
        ],
    )
    main()
    unsorted_html = unsorted_output.read_text()
    unsorted_properties = re.findall(
        r'<div class="property entity" id="([^"]+)">',
        unsorted_html,
    )
    assert unsorted_properties == ["adjacentTo", "touches", "regularProp"]
    assert toc_order(unsorted_html, unsorted_properties) == unsorted_properties


def test_classes(monkeypatch, tmp_path):
    source = Path(__file__).parent / "data" / "fruits.ttl"
    class_ids = {
        "Berry",
        "Blueberry",
        "Cherry",
        "CitrusFruit",
        "Fruit",
        "Lemon",
        "Orange",
        "Peach",
        "StoneFruit",
        "Strawberry",
    }

    sorted_output = tmp_path / "fruits-sorted.html"
    monkeypatch.setattr(
        sys,
        "argv",
        ["pylode", str(source), "--outputfile", str(sorted_output)],
    )
    main()
    sorted_html = sorted_output.read_text()
    sorted_classes = re.findall(
        r'<div class="property entity" id="([^"]+)">', sorted_html
    )
    assert sorted_classes == sorted(class_ids)
    assert toc_order(sorted_html, class_ids) == sorted(class_ids)

    unsorted_output = tmp_path / "fruits-unsorted.html"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "pylode",
            str(source),
            "--sort",
            "false",
            "--outputfile",
            str(unsorted_output),
        ],
    )
    main()
    unsorted_html = unsorted_output.read_text()
    source_order = [
        "Peach",
        "Fruit",
        "Lemon",
        "Berry",
        "Cherry",
        "CitrusFruit",
        "Strawberry",
        "StoneFruit",
        "Orange",
        "Blueberry",
    ]
    unsorted_classes = re.findall(
        r'<div class="property entity" id="([^"]+)">', unsorted_html
    )
    assert unsorted_classes == source_order
    assert toc_order(unsorted_html, class_ids) == source_order
