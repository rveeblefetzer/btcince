# btcince
A Python script to compare an old bitcoin transaction to the value of that transaction now(ish).

As a script, it takes user input for a date and an amount in USD, and returns
the difference in value between that amount in bitcoin then and yesterday.
Rates use volume-weighted average price (VWAP), and values are rounded to two
decimals in instances when a human would expect it.

My first stab at this was with the [btcince.py](btcince/btcince.py) script, which is one big quick sketch of a function. The
[transactions.py](btcince/transactions.py) module breaks that all up into a class and methods. The latter was made primarily
because the former frustrated the hell out of me trying to assert exceptions in the try-except blocks. But, this should make
it way easier to port to Django too.

It uses Bitstamp data from the free [Quandl API](https://www.quandl.com/data/BITSTAMP-Bitstamp).
