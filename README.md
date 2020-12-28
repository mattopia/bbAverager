# bbAverager.py - Calculate average prices on BestBuy.com for a given manufacturer

This script will query the BestBuy.com API for all products by a given manufacturer. For each unique product category, an average price of all return products is calculated. The API returns paginated results -- the script will handle pagination, ensuring all results are calculated in the average.

## Requirements
 - Python 3.x
 - Requests library
 - A BestBuy API key

## Usage
The script requires two arguments - API key and manufacturer.  

```
./bbAverager.py <myApiKey> canon
```

An optional `--baseUrl` can be specified, however, the built-in default should suffice in most instances.  For detailed help, run the script with the `-h` flag:

```
./bbAverager.py -h
usage: bbAverager.py [-h] [--baseUrl BASEURL] apiKey manufacturer

Calculate average prices on BestBuy.com for a given manufacturer

positional arguments:
  apiKey             BestBuy API key
  manufacturer       Manufacturer name

optional arguments:
  -h, --help         show this help message and exit
  --baseUrl BASEURL
```

## Example Output

```
./bbAverager.py <myApiKey> canon
INK- ER                $22.66
INK- NON ER            $27.26
SO SCANNERS            $286.99
...
Total products: 416
```
