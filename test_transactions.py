"""Testing module for transactions.py."""

import pytest
from unittest import mock
from unittest.mock import MagicMock
from transactions import Transaction


@pytest.fixture(scope='function')
def full_tester():
    tester = Transaction('test', '100', '2017-01-01')
    yield tester

@pytest.fixture(scope='function')
def blank_tester():
    tester = Transaction()
    yield tester

def test_transcation_created(full_tester):
    assert full_tester.orig_usd == '100'

def test_blank_transaction_initialized(blank_tester):
    assert blank_tester.orig_usd is None

@mock.patch('builtins.input', lambda _:  '500')
def test_good_usd_input(blank_tester):
    blank_tester.get_orig_tx_amount()
    assert blank_tester.orig_usd == '500'

# @mock.patch('builtins.input', lambda _: 'a')
# def test_bad_usd_input(blank_tester):
#         blank_tester.get_orig_tx_amount()
#         with pytest.raises(ValueError):
#             assert excinfo.value.message == 'Wait, no, I need a number, int or float'

@mock.patch('builtins.input', lambda _: '2017-01-01')
def test_good_date_input(blank_tester):
    blank_tester.get_orig_tx_date()
    assert blank_tester.orig_date == '2017-01-01'

# @mock.patch('builtins.input', lambda _: 'charlie')
# def test_good_date_input(blank_tester):
#     with pytest.raises(TypeError):
#         blank_tester.get_orig_tx_date()
#     # assert blank_tester.orig_date == '2017-01-01'
