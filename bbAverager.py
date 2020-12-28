#!/usr/bin/env python3

import requests
import argparse

# Parse command line arguments
def parseArgs():
	p = argparse.ArgumentParser(
		description="Calculate average prices on BestBuy.com for a given manufacturer")
	p.add_argument('apiKey', help="BestBuy API key")
	p.add_argument('manufacturer', help="Manufacturer name")
	p.add_argument('--baseUrl', default="https://api.bestbuy.com/v1/products")
	return p.parse_args()

# Return a dictionary of results from Best Buy products endpoint
def getProducts(baseUrl, apiKey, manufacturer, page = 1):
	try:
		params = {'format': 'json', 'apiKey': apiKey, 'pageSize': 100, 'page': page}
		request = requests.get(baseUrl + '(manufacturer="' + manufacturer + '")', params)
	except Exception as e:
		print(f"Exception: {e}")
		exit(1)
	else:
		if request.status_code != 200:
			print(f"Unexpected HTTP status code: {request.status_code}")
			exit(1)
		return request.json()

def main(args = parseArgs()):
	prices = {}
	totalProducts = 0
	page = 1
	totalPages = 1

	while page <= totalPages:
		results = getProducts(args.baseUrl, args.apiKey, args.manufacturer, page)
		if results['total'] == 0:
			print("The query returned zero results.")
			exit(1)
		totalPages = results['totalPages']
		for product in results['products']:
			totalProducts += 1
			subclass = product['subclass']
			price = product['regularPrice']
			if subclass not in prices:
				prices[subclass] = { 'count': 0, 'total': 0 }
			prices[subclass] = { 
				'count': prices[subclass]['count'] + 1, 
				'total': prices[subclass]['total'] + price
			}
		page += 1

	# Find the longest subclass name for formatting purposes
	col_width = max(len(key) for key in prices) + 2

	for subclass, prices in prices.items():
		avg = round(prices['total'] / prices['count'], 2)
		print(f"{subclass:<{col_width}} ${avg:>}")

	print(f"Total products: {totalProducts}")

if __name__ == "__main__":
	main()
