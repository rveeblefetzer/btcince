[![Build Status](https://travis-ci.org/rveeblefetzer/btcince.svg?branch=master)](https://travis-ci.org/rveeblefetzer/btcince)

# btcince
A Python script to compare an old bitcoin transaction to the value of that transaction now(ish).

## why
The idea for this came up not actually to track a certain btc transacation, but from the question 'What if?'
In particular, sometime in January 2017, a friend and I bought some parts online, and we bundled our order and shipping. 
He paid, and I half-jokingly asked him if I could pay him the $80 I owed him in bitcoin. He didn't take me up on it.
And if I plug in that amount and date into this program, it basically tells me that, as of this commit, he's lost out on
$609.82. Or that my $45 Micropython pyboard is now worth $388.

## how
The program takes user input for a date and an amount in USD, and returns the difference in value between that amount in
bitcoin then and yesterday. Rates use volume-weighted average price (VWAP), and values are rounded to two decimals in
instances when a human would expect it.

It uses Bitstamp data from the free [Quandl API](https://www.quandl.com/data/BITSTAMP-Bitstamp). To use it, add your API key
somewhere as: `authtoken = YOUR_API_KEY`

This can be in a separate config.py file, or at the top of btcince.py or transactions.py.

## errata
My first stab at this was with the [btcince.py](btcince/btcince.py) script, which is one big quick sketch of a function. The
[transactions.py](btcince/transactions.py) module breaks that all up into a class and methods. The latter was made primarily
because the former frustrated the hell out of me trying to assert exceptions in the try-except blocks. But, this should make
it way easier to port to Django too.
