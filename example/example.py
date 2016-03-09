#!/usr/bin/env python

import agate
from agate.data_types import *
import agatelookup

agatelookup.patch()

taxfields = agate.data_types.TypeTester(force={
    'kommunenr': agate.Text(),
    'has_propertytax': agate.Number(),
    'propertytax_120kvm': agate.Number()
})

propertytax_table = agate.Table.from_csv('data/ssb_eiendomsskatt_2015.csv', column_types=taxfields)

norway_lookup_source = agatelookup.source.Source(root='http://something.github.com')

joined = propertytax_table.lookup('kommunenr', 'has_propertytax', lookup_key='kommunenr',
	source=norway_lookup_source)

print join.print_table(max_rows=10)