# pylint: disable=no-member
import sqlalchemy as db
from sqlalchemy.engine import Engine


def test_basic_reflection(test_engine: Engine):
    conn = test_engine.connect()
    metadata = db.MetaData(bind=test_engine, reflect=True, schema='system')
    table = db.Table('tables', metadata)
    query = db.select([table.columns.create_table_query])
    result = conn.execute(query)
    rows = result.fetchmany(100)
    assert rows


def test_full_table_reflection(test_engine: Engine):
    conn = test_engine.connect()
    conn.execute(
        'CREATE TABLE IF NOT EXISTS sqla_test.reflect_test (key UInt32, value FixedString(20))' +
        'ENGINE MergeTree ORDER BY key')
    metadata = db.MetaData(bind=test_engine, reflect=True, schema='sqla_test')
    table = db.Table('reflect_test', metadata)
    print(db.select([table.columns.key]))
