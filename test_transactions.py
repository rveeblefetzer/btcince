"""Testing module for transactions.py."""

import pytest
from unittest import mock
from unittest.mock import patch, MagicMock


from transactions import Transaction

@pytest.fixture
def full_tester():
    tester = Transaction('test', '100', '2017-01-01')
    return tester

@pytest.fixture
def blank_tester():
    tester = Transaction()
    return tester

def test_transcation_created(full_tester):
    assert full_tester.orig_usd == '100'

@mock.patch('builtins.input', MagicMock(side_effect=['500']))
def test_good_usd_input(blank_tester):
    blank_tester.get_orig_tx_amount()
    assert blank_tester.orig_usd == '500'
