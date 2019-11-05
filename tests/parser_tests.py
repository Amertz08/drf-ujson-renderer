from io import BytesIO

import pytest
import ujson

from drf_ujson.parsers import UJSONParser


@pytest.fixture()
def uut():
    return UJSONParser()


@pytest.fixture()
def data():
    return {
        "a": [1, 2, 3],
        "b": True,
        "c": 1.23,
        "d": "test",
        "e": {"foo": "bar"},
    }


def test_basic_data_structure_parsed_correctly(uut, data):
    dumped = ujson.dumps(data)
    parsed = uut.parse(BytesIO(dumped.encode("utf-8")))

    assert parsed == data


def test_parser_works_correctly_when_media_type_and_context_provided(uut, data):
    dumped = ujson.dumps(data)

    parsed = uut.parse(
        BytesIO(dumped.encode("utf-8")),
        media_type="application/json",
        parser_context={},
    )

    assert parsed == data
