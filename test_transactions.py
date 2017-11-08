"""Testing module for transactions.py."""

import pytest
from unittest import mock
import transactions


class TestClass(object):

    @pytest.fixture
    def basic_setup():
        from transactions import Transaction
        anon = Transaction()

    @pytest.fixture()
    def before():
        print('\nbefore each test')


    def test_invalid_usd(before):
        print('why you no print fixture print?!?')
        assert 1 == 1
