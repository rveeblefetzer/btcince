#!/usr/bin/env python3.6

"""The point of this module is to compare an old value in Bitcoin to now.

Given a date and an amount in USD, it returns the difference in value between
that amount in bitcoin then and yesterday. Rates use volume-weighted average
price (VWAP), and values are rounded to two decimals in instances when a
human would expect it.

It uses Bitstamp data from the free Quandl API. To use it, add your API key
somewhere as:

authtoken = YOUR_API_KEY
"""

from config import authtoken
import quandl
import datetime
from decimal import Decimal as d
from decimal import ROUND_HALF_UP


class Transaction(object):
    """A class to govern Transaction objects and operations."""

    def __init__(self, user=None, orig_usd=None, orig_date=None, orig_btc=None):
        """Instantiate a Transaction object."""
        self.user = user
        self.orig_usd = orig_usd
        self.orig_date = orig_date
        self.orig_btc = orig_btc

    def get_orig_tx_amount(self):
        """Ask user for starting amount."""
        number_check = None
        while number_check is None:
            try:
                self.orig_usd = input('What was the original amount in USD?:\n$')
                number_check = float(self.orig_usd)
            except ValueError as e:
                print(f'Wait, no, I need a number, int or float:\n{e}')
            return self.orig_usd

    def get_orig_tx_date(self):
        """Ask user for starting date."""
        date_check = None
        while date_check is None:
            try:
                self.orig_date = input('What was the date? Format it "YYYY-MM-DD":\n>')
                check_setup = datetime.datetime.strptime(self.orig_date, '%Y-%m-%d')
                date_check = datetime.date.isoformat(check_setup)
            except ValueError:
                print('No, it must be formatted YYYY-MM-DD')
            return self.orig_date

    def convert_orig_usd_btc(self):
        """Convert original USD into BTC value on original date."""
        if self.orig_usd is None:
            orig_usd = self.get_orig_tx_amount()
        if self.orig_date is None:
            orig_date = self.get_orig_tx_date()
        orig_rates = quandl.get('BITSTAMP/USD', authtoken=authtoken,
                                start_date=self.orig_date, end_date=self.orig_date)
        orig_vwap = orig_rates['VWAP'][0]
        self.orig_btc = float(self.orig_usd) / orig_vwap
        return self.orig_btc

    def get_btc_yesterday(self):
        """Get yesterday's BTC/USD rate."""
        yesterday = (datetime.date.today() - datetime.timedelta(days=1))\
            .isoformat()
            if yesterday 
        yesterday_rates = quandl.get('BITSTAMP/USD', authtoken=authtoken,\
            start_date=yesterday, end_date=yesterday)
        yesterday_vwap = yesterday_rates['VWAP'][0]
        return yesterday_vwap

    def get_updated_btc_value(self, yesterday_vwap):
        """Get USD value of original btc amount at yesterday's rate."""
        if self.orig_btc is None:
            self.orig_btc = self.convert_orig_usd_btc()
        yesterday_usd_value = float(self.orig_btc) * yesterday_vwap
        return yesterday_usd_value

    def round_value_like_normal_money(self, fiat_value):
        """Round the value to max two decimal places."""
        fiat_value_nice = d(fiat_value).quantize(
            d('0.00'), rounding=ROUND_HALF_UP)
        return float(fiat_value_nice)

    def calculate_latest_value_difference(self, usd_value_now):
        """Show the difference in value from original transaction."""
        diff = usd_value_now - float(self.orig_usd)
        return diff

    def main():
        anon = Transaction()
        anon.orig_btc = anon.convert_orig_usd_btc()
        new_value = anon.get_updated_btc_value(anon.get_btc_yesterday())
        new_value_nice = anon.round_value_like_normal_money(new_value)
        diff = anon.calculate_latest_value_difference(new_value_nice)

        print(f'You started with USD {anon.orig_usd} on {anon.orig_date}, which equaled BTC {anon.orig_btc}')
        print(f'As of yesterday, that amount of bitcoin was valued at ${new_value_nice}.\n')
        print(f'The change in value is ${round(diff, 2)}.')

if __name__ == '__main__':
    Transaction.main()
