import pylode


def test_make_fragment_id():
    doc = pylode.HtmlDocument
    doc.fragment_ids = ['x']

    uri = 'http://example.com/aaa/bbb/ccc'
    print('testing {}'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) == 'ccc'

    uri = 'http://example.com/aaa/bbb/'
    print('testing {}'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) is None

    uri = 'http://example.com/aaa/bbb#ccc'
    print('testing {}'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) == 'ccc'

    uri = 'http://example.com/aaa/bbb#'
    print('testing {}'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) is None

    uri = 'http://example.com'
    print('testing {}'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) is None

    uri = 'http://example.'
    print('testing {}'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) is None

    uri = ''
    print('testing {} <- empty URI'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) is None

    uri = 'http://example.com/aaa/bbb/Mikołaj'
    print('testing {} <- non-Latin char'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) == 'Mikołaj'

    uri = 'http://example.com/aaa/bbb/£'
    print('testing {} <- non-Latin char'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) == '£'

    uri = 'http://example.com/aaa/bbb/\xa3'
    print('testing {} <- non-Latin char, encoded as \\xa3'.format(uri))
    assert pylode.make_fragment_id(uri, 'x', doc) == '\xa3'


if __name__ == '__main__':
    test_make_fragment_id()
