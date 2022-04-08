import logging

import clickhouse_connect.datatypes.container
import clickhouse_connect.datatypes.network
import clickhouse_connect.datatypes.numeric
import clickhouse_connect.datatypes.registry
import clickhouse_connect.datatypes.special
import clickhouse_connect.datatypes.string as dt_string
import clickhouse_connect.datatypes.temporal

# pylint: disable=protected-access
try:
    from clickhouse_connect.driverc import creaders
    dt_string.String._from_native_impl = creaders.read_string_column
    dt_string.FixedString._from_native_str = creaders.read_fixed_string_str
    dt_string.FixedString._from_native_bytes = creaders.read_fixed_string_bytes
except ImportError:
    logging.warning('Unable to connect optimized C driver functions, falling back to pure Python', exc_info=True)


def fixed_string_format(fmt: str, encoding: str = 'utf8'):
    clickhouse_connect.datatypes.string.FixedString.format(fmt, encoding)


def big_int_format(fmt: str):
    clickhouse_connect.datatypes.numeric.BigInt.format(fmt)


def uint64_format(fmt: str):
    clickhouse_connect.datatypes.numeric.UInt64.format(fmt)


def uuid_format(fmt: str):
    clickhouse_connect.datatypes.special.UUID.format(fmt)


def ip_format(fmt: str):
    clickhouse_connect.datatypes.network.IPv4.format(fmt)
    clickhouse_connect.datatypes.network.IPv6.format(fmt)
