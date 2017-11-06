#!/usr/bin/env python3.6

"""The point of this script is to compare an old value in Bitcoin to now.

It takes user input for a date and an amount in USD, and returns the
difference in value between that amount in bitcoin then and yesterday.
Rates use the volume-weighted average price (VWAP). It uses Bitstamp data
from the free Quandl API.

This runs as a script from the command line, but the transactions.py module
has the functions broken up. That was made primarily because with this file,
I got frustrated trying to assert exceptions in the try-except blocks.
"""

from config import authtoken
import quandl
import datetime
from decimal import Decimal as d
from decimal import ROUND_HALF_UP


def btc_diff_checker():
    """Take an old bitcoin transaction and calculate value change now."""
    number_check = False
    date_check = None

    while number_check is False:
        try:
            orig_usd = input('What was the original amount in USD?:\n$')
            number_check = float(orig_usd)
        except ValueError as e:
            print(f'Wait, no, I need a number, int or float:\n{e}')

    while date_check is None:
        try:
            orig_date = input('What was the date? Format it "YYYY-MM-DD":\n>')
            check_setup = datetime.datetime.strptime(orig_date, '%Y-%m-%d')
            date_check = datetime.date.isoformat(check_setup)
        except ValueError:
            print('No, it must be formatted YYYY-MM-DD')

    # Convert original USD into BTC value then
    orig_rates = quandl.get('BITSTAMP/USD', authtoken=authtoken,
                            start_date=orig_date, end_date=orig_date)
    orig_vwap = orig_rates['VWAP'][0]
    orig_btc = float(orig_usd) / orig_vwap

    # Get yesterday's BTC/USD rate
    yesterday = (datetime.date.today() - datetime.timedelta(days=1))\
        .isoformat()
    yesterday_rates = quandl.get('BITSTAMP/USD', authtoken=authtoken,
                                 start_date=yesterday, end_date=yesterday)
    yesterday_vwap = yesterday_rates['VWAP'][0]

    # Calculate difference
    yesterday_usd_value = float(orig_btc) * yesterday_vwap
    yesterday_usdval_rounded = d(yesterday_usd_value).quantize(
        d('0.00'), rounding=ROUND_HALF_UP)

    diff = yesterday_usd_value - float(orig_usd)


    print(f'You started with USD {orig_usd} on {orig_date}, which equaled BTC {orig_btc}')
    print(f'As of yesterday, that amount of bitcoin was valued at ${yesterday_usdval_rounded}.\n')
    print(f'The change in value is ${round(diff, 2)}.')

if __name__ == '__main__':
    btc_diff_checker()
