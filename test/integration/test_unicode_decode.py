from ..helpers import get_honcho_output, assert_equal, assert_regexp_matches


def test_unicode_decode_error():
    ret, out, err = get_honcho_output(['-f',
                                       'Procfile.unicode_decode', 'start'])
    assert_equal(ret, 0)
    assert_regexp_matches(out, "normal output")
