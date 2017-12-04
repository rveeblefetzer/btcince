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
    """Test that Transaction object initialized with data."""
    assert full_tester.orig_usd == '100'

def test_blank_transaction_initialized(blank_tester):
    """Test that empty Transaction object initialized."""
    assert blank_tester.orig_usd is None

@mock.patch('builtins.input', lambda _:  '500')
def test_good_usd_input(blank_tester):
    """Test valid user input for USD amount."""
    blank_tester.get_orig_tx_amount()
    assert blank_tester.orig_usd == '500'

# @mock.patch('builtins.input', lambda _: 'a')
# def test_bad_usd_input(blank_tester):
#         blank_tester.get_orig_tx_amount()
#         with pytest.raises(ValueError):
#             assert excinfo.value.message == 'Wait, no, I need a number, int or float'

@mock.patch('builtins.input', lambda _: '2017-01-01')
def test_good_date_input(blank_tester):
    """Test valid user input for date."""
    blank_tester.get_orig_tx_date()
    assert blank_tester.orig_date == '2017-01-01'

# @mock.patch('builtins.input', lambda _: 'charlie')
# def test_good_date_input(blank_tester):
#     with pytest.raises(TypeError):
#         blank_tester.get_orig_tx_date()
#     # assert blank_tester.orig_date == '2017-01-01'

def test_orig_btc_conversion(full_tester):
    assert full_tester.convert_orig_usd_btc() == 0.10463206135624077

def test_rounding(blank_tester):
    assert blank_tester.round_value_like_normal_money(13.372600) == 13.37

@mock.patch('transactions.Transaction.get_now', lambda _:  '2017-01-01')
def test_getting_btc_api_updated(blank_tester):
    assert blank_tester.get_btc_current() == 955.73000000000002

