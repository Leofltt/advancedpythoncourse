import os
import sqlite3
from pathlib import Path

import pytest

from datapipeline import DataPipeline, create_hardcoded_data_pipeline
from loading.loader import LoaderIterator
from loading.serializer import JSON_Serializer
from transforming.batchtransformer import BatchTransformer
from transforming.currencyconverter import CurrencyConverter, latest_exchange_rates
from transforming.pricemultiplier import PriceMultiplier
from storing.sqlitebatchproductstorer import SQLiteBatchProductStorer
from storing.sqlitecontextmanager import SQLiteContextManager
from storing.createdb import create_db



@pytest.fixture
def product_data():
    return 


@pytest.fixture
def expected_db_product_output():
    return [
        ("product_1", "euro", 220.),
        ("product_2", "euro", 22.),
        ("product_3", "euro", 22.),
        ("product_4", "euro", 22.),
        ("product_5", "euro", 20.)
    ]


@pytest.fixture
def data_pipeline():
    loader_iterator = LoaderIterator(JSON_Serializer(), 2)
    batch_transformer = BatchTransformer([CurrencyConverter(latest_exchange_rates, "euro"),
                                          PriceMultiplier(2.)])
    product_storer = SQLiteBatchProductStorer()
    sqlite_context_manager = SQLiteContextManager("dummy.db")
    return DataPipeline(loader_iterator,
                        batch_transformer,
                        product_storer,
                        sqlite_context_manager)


def test_data_pipeline_init():
    data_pipeline = DataPipeline("load_iterator", "transformer", "storer", "context")
    assert type(data_pipeline) == DataPipeline
    assert data_pipeline.loader_iterator == "load_iterator"
    assert data_pipeline.batch_transformer == "transformer"
    assert data_pipeline.storer == "storer"


def test_process_files(data_pipeline, expected_db_product_output):
    files = [Path("files/1.json"), Path("files/2.json"), Path("files/3.json"),
             Path("non-existing"), Path("files/4.json"), Path("files/5.json")]

    try:
        create_db("dummy.db")
        connection = sqlite3.connect("dummy.db")
        cursor = connection.cursor()

        data_pipeline.process(files)

        cursor.execute("SELECT NAME, CURRENCY, PRICE FROM PRODUCT")
        products = cursor.fetchall()

        for i in range(len(products)):
            assert products[i][0] == expected_db_product_output[i][0]
            assert products[i][1] == expected_db_product_output[i][1]
            assert products[i][2] == pytest.approx(expected_db_product_output[i][2])
    finally:
        os.remove("dummy.db")


def test_process_product_batch(data_pipeline, expected_db_product_output):
    product_data = [
        {
            "name": "product_1",
            "price": 100,
            "currency": "dollar"
        },
        {
            "name": "product_2",
            "price": 10,
            "currency": "dollar"
        },
        {
            "name": "product_3",
            "price": 10,
            "currency": "dollar"
        },
        {
            "name": "product_4",
            "price": 10,
            "currency": "dollar"
        },
        {
            "name": "product_5",
            "price": 10,
            "currency": "euro"
        }
    ]
    try:
        create_db("dummy.db")
        connection = sqlite3.connect("dummy.db")
        cursor = connection.cursor()

        data_pipeline._process_product_batch(cursor, product_data)

        cursor.execute("SELECT NAME, CURRENCY, PRICE FROM PRODUCT")
        products = cursor.fetchall()

        for i in range(len(products)):
            assert products[i][0] == expected_db_product_output[i][0]
            assert products[i][1] == expected_db_product_output[i][1]
            assert products[i][2] == pytest.approx(expected_db_product_output[i][2])
    finally:
        os.remove("dummy.db")


def test_hardcoded_data_pipeline_is_instantiated():
    data_pipeline = create_hardcoded_data_pipeline()
    assert type(data_pipeline) == DataPipeline
