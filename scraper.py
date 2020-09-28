#!/usr/bin/env python3

import argparse
import json
import prettytable
from progress.bar import IncrementalBar
from providers import *
import config

# Just reduce the providers list in the config, -a will be only for the providers in the list ;)
providedrs_list = {}
for provider in config.credentials.keys():
	providedrs_list[provider] = None

message = 'Scraper za troskove sa web stranica javnih i privatnih preduzeca u Kantonu Sarajevo.'
parser = argparse.ArgumentParser(description=message)
parser.add_argument('-a','--fetch-all', action='store_true', help='Fetch data from all providers.')
parser.add_argument('-p','--providers',nargs='+', choices=providedrs_list, help='Fetch data from the providers from the list.')
parser.add_argument('-f','--format', nargs='+', choices=['json','table'], help='Return data on std in JSON or ASCII Table')
args = parser.parse_args()

result = '' # The final outcome will be in the result variable!
all_data = {}

def fetch_provider(provider):
	credentials = config.credentials[provider]
	data  = eval(provider +'.fetch(credentials)')
	return data

def get_table(data):
	asciitable = prettytable.PrettyTable(hrules=prettytable.ALL) 

	asciitable.field_names = ["Service", "Ugovor i Opis Stanja", "Stanje"] 
	asciitable.align["Service"] = "l"
	asciitable.align["Ugovor i Opis Stanja"] = "l"
	asciitable.align["Stanje"] = "r"

	for provider in data.keys():
		providersdata = data[provider]
		tabledata = eval(provider +'.get_table_row(providersdata)')
		asciitable.add_row(tabledata)
	return asciitable

if  args.providers:
	providedrs_list = args.providers

num = len(providedrs_list)
if args.format:
	if args.format[0] == 'table':
		bar = IncrementalBar('Fetching:', max=num)
		for provider in providedrs_list:
			all_data[provider] = fetch_provider(provider)
			bar.next()
		bar.finish()
		result = get_table(all_data)
	elif args.format[0] == 'json':
		for provider in providedrs_list:
			all_data[provider] = fetch_provider(provider)
		result = json.dumps(all_data, indent = 4)
else:
	for provider in providedrs_list:
		all_data[provider] = fetch_provider(provider)
	result = all_data

print(result)