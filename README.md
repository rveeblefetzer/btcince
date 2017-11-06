# btcince
A Python script to compare an old bitcoin transaction to the value of that transaction now(ish).

As a script, it takes user input for a date and an amount in USD, and returns
the difference in value between that amount in bitcoin then and yesterday.
Rates use volume-weighted average price (VWAP), and values are rounded to two
decimals in instances when a human would expect it.

It uses Bitstamp data from the free [Quandl API](https://www.quandl.com/data/BITSTAMP-Bitstamp).
