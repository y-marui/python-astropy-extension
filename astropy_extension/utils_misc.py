# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""astropy の既存クラスの一部を拡張して、便利な関数を定義する."""

import json
from typing import Any

from astropy import units as u
from astropy.time import Time
from astropy.utils.misc import JsonCustomEncoder as JsonEncoder


class JsonCustomEncoder(JsonEncoder):  # type: ignore[misc]
    """astropy の JsonCustomEncoder に Time のシリアライズ対応を追加する.

    JsonCustomDecoder は "datetime" キーの値を Time に復元するが、対になる
    エンコード側（Time -> 文字列）は astropy 本体の JsonCustomEncoder には
    実装されていないため、ここで補う.
    """

    # astropy ships no inline type stubs for `JsonCustomEncoder`, so mypy
    # sees it as `Any` and flags the subclass; see issue #34.

    def default(self, o: Any) -> Any:
        if isinstance(o, Time):
            return o.iso
        return super().default(o)


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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """初期化する."""
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj: dict[str, Any]) -> Any:
        """オブジェクトの内指定のものを変換."""
        if ["unit", "value"] == sorted(obj):
            return u.Quantity(**obj)
        if "datetime" in obj.keys():
            obj["datetime"] = Time(obj["datetime"], format="iso")

        return obj
