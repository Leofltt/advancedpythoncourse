from pathlib import Path

import pytest

from loading.loader import LoaderIterator
from loading.serializer import JSON_Serializer


@pytest.fixture
def loader_iterator():
    paths = [Path("files/1.json"), Path("files/2.json"), Path("non-existing-path"),
             Path("files/3.json"), Path("files/4.json"), Path("files/5.json")]
    return LoaderIterator(JSON_Serializer(), 2, paths)


def test_loader_iterator_init():
    loader_iterator = LoaderIterator(JSON_Serializer(), 2, "dummy_paths")
    assert type(loader_iterator) == LoaderIterator
    assert type(loader_iterator.serializer) == JSON_Serializer
    assert loader_iterator.load_paths == "dummy_paths"
    assert loader_iterator.num_files_per_iteration == 2


def test_loop_through_loaded_data(loader_iterator):
    expected_data = [
        [
            {
                "name": "product_1",
                "price": 100,
                "currency": "dollar",
            },
            {
                "name": "product_2",
                "price": 10,
                "currency": "dollar"
            }
        ],
        [
            {
                "name": "product_3",
                "price": 10,
                "currency": "dollar"
            }
        ],
        [
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
    ]

    for i, data in enumerate(loader_iterator):
        for j, d in enumerate(data):
            assert d == expected_data[i][j]


def test_iter(loader_iterator):
    assert loader_iterator._current_iteration == None
    iterator = iter(loader_iterator)
    assert loader_iterator._current_iteration == 0
    assert type(iterator) == LoaderIterator


def test_next(loader_iterator):
    iterator = iter(loader_iterator)

    data_iteration_0 = next(iterator)
    expected_data_iteration_0 = [
        {
            "name": "product_1",
            "price": 100,
            "currency": "dollar"
        },
        {
            "name": "product_2",
            "price": 10,
            "currency": "dollar"
        }
    ]
    for i,d in enumerate(data_iteration_0):
        assert d == expected_data_iteration_0[i]

    data_iteration_1 = next(iterator)
    expected_data_iteration_1 = [ {
            "name": "product_3",
            "price": 10,
            "currency": "dollar"
        } ]
    for i,d in enumerate(data_iteration_1):
        assert d == expected_data_iteration_1[i]

    data_iteration_2 = next(iterator)
    expected_data_iteration_2 = [
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
    for i,d in enumerate(data_iteration_2):
        assert d == expected_data_iteration_2[i]

    with pytest.raises(StopIteration):
        next(iterator)


def test_load_data_batch(loader_iterator):
    loader_iterator._current_iteration = 0
    expected_data = [
        {
            "currency": "dollar",
            "name": "product_1",
            "price": 100
        },
        {
            "currency": "dollar",
            "name": "product_2",
            "price": 10
        }
    ]
    loaded_data = loader_iterator._load_data_batch()
    for i,d in enumerate(loaded_data):
        assert d == expected_data[i]


def test_load_data_batch_with_non_existing_file(loader_iterator):
    loader_iterator._current_iteration = 1
    expected_data = [
        {
            "name": "product_3",
            "currency": "dollar",
            "price": 10
        }
    ]
    loaded_data = loader_iterator._load_data_batch()
    for i,d in enumerate(loaded_data):
        assert d == expected_data[i]


def test_did_load_all_batches(loader_iterator):
    loader_iterator._current_iteration = 0
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 1
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 2
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 3
    assert loader_iterator._did_load_all_batches() == True

    loader_iterator.load_paths = [1, 2, 3, 4, 5, 6, 7]
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 4
    assert loader_iterator._did_load_all_batches() == True

    loader_iterator.load_paths = [1, 2, 3, 4, 5, 6, 7, 8]
    assert loader_iterator._did_load_all_batches() == True

    loader_iterator.num_files_per_iteration = 3
    loader_iterator.load_paths = [1, 2, 3, 4, 5]
    loader_iterator._current_iteration = 0
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 1
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 2
    assert loader_iterator._did_load_all_batches() == True

