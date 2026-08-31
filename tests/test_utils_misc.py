import json

from astropy import units as u
from astropy.time import Time

from astropy_extension.utils_misc import JsonCustomDecoder, JsonCustomEncoder


def test_encoder_serializes_quantity():
    encoded = json.dumps({"length": 5 * u.V}, cls=JsonCustomEncoder)
    assert json.loads(encoded) == {"length": {"value": 5.0, "unit": "V"}}


def test_decoder_restores_quantity():
    decoded = json.loads('{"length": {"value": 5.0, "unit": "V"}}', cls=JsonCustomDecoder)
    assert decoded == {"length": 5 * u.V}


def test_decoder_restores_datetime():
    decoded = json.loads('{"datetime": "2018-11-08 14:09:39.401948"}', cls=JsonCustomDecoder)
    assert decoded == {"datetime": Time("2018-11-08 14:09:39.401948", format="iso")}


def test_decoder_leaves_unrelated_objects_unchanged():
    decoded = json.loads('{"foo": 1, "bar": 2}', cls=JsonCustomDecoder)
    assert decoded == {"foo": 1, "bar": 2}


def test_roundtrip_encode_decode():
    sample = {"length": 5 * u.V, "datetime": Time.now()}
    decoded = json.loads(json.dumps(sample, cls=JsonCustomEncoder), cls=JsonCustomDecoder)

    assert decoded["length"] == sample["length"]
    assert decoded["datetime"].iso == sample["datetime"].iso
