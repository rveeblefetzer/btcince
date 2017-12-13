[![Build Status](https://travis-ci.org/rveeblefetzer/btcince.svg?branch=master)](https://travis-ci.org/rveeblefetzer/btcince)
[![Coverage Status](https://coveralls.io/repos/github/rveeblefetzer/btcince/badge.svg)](https://coveralls.io/github/rveeblefetzer/btcince)

# btcince
Compare an old bitcoin transaction [(or one that didn't happen)](https://github.com/rveeblefetzer/btcince/blob/master/README.md#why) to the value of
that transaction now(ish).

It takes a USD amount and a date (formatted 'YYYY-MM-DD'), and it returns the
difference in value between that amount in bitcoin then and for the most recent
end-of-day trading in New York. Rates use volume-weighted average price (VWAP),
and values are rounded to two decimals in instances when a human would expect
it.

## Usage
`python btcince.py [<original_USD_amount> <original_date>]`

If you don't add the optional arguments, the program will prompt the user for
the values.

## Installation
All that's needed is the btcince.py module and to `pip install Quandl pytz
docopt`. 

The pytz library is for comparing current time and date with 7pm in New York,
when the API updates for the day.

The data is provided by Bitstamp, from the [Quandl
API](https://www.quandl.com/data/BITSTAMP-Bitstamp).  To use it, add your API
key somewhere as: `authtoken = YOUR_API_KEY`. This can be in a separate
config.py file, or at the top of your btcince.py.

## Why
The idea for this came up not actually to track a certain btc transacation, but
from the question 'What if?' In particular, sometime in January 2017, a friend
and I bought some hardware online, and we bundled our order and shipping. He paid,
and I half-jokingly asked him if I could pay him the $80 I owed him in bitcoin.
He didn't take me up on it. Plugging in that amount and date into this
program, it basically tells me that, as of the original final working commit,
he'd lost out on $609.82. Likewise, my $45 Micropython pyboard represented $388 in
bitcoin.

*EDIT:* As of this merge for adding sysargv input and incorporating docopt, that
original $80 in bitcoin would now be $1508.79, and I have an $848.70 pyboard. 

