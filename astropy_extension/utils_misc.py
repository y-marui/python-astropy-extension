# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""astropy の既存クラスの一部を拡張して、便利な関数を定義する."""

import json

from astropy import units as u
from astropy.time import Time
from astropy.utils.misc import JsonCustomEncoder as JsonEncoder


class JsonCustomEncoder(JsonEncoder):
    pass


class JsonCustomDecoder(json.JSONDecoder):
    """
    json で astropy からエンコードしたファイルをロードするときに使う.

    * key が unit と value のみのオブジェクトは Quantity に変換.
    * key が datetime の場合は Time に変換.

    Example
    -------
    >>> import json
    >>> from astropy import units
    >>> from astropy.time import Time
    >>> from moke_meas2.core.astropy import JsonCustomEncoder, JsonC
    ustomDecoder
    >>> sample = {"length": 5 * units.V, "datetime": Time.now()}
    >>> print(sample)
    {'length': <Quantity 5. V>, 'datetime': <Time object: scale='utc' format='
    datetime' value=2018-11-08 14:09:39.401948>}
    >>> sample_enc = json.dumps(sample, cls=JsonCustomEncoder)
    >>> print(sample_enc)
    {"length": {"value": 5.0, "unit": "V"}, "datetime": "2018-11-08 14:09:39.4
    01948"}
    >>> json.loads(sample_enc, cls=JsonCustomDecoder)
    {'length': <Quantity 5. V>, 'datetime': <Time object: scale='utc' format='
    iso' value=2018-11-08 14:09:39.402>}

    """

    def __init__(self, *args, **kwargs):
        """初期化する."""
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        """オブジェクトの内指定のものを変換."""
        if ["unit", "value"] == sorted(obj):
            return u.Quantity(**obj)
        if "datetime" in obj.keys():
            obj["datetime"] = Time(obj["datetime"], format="iso")

        return obj
