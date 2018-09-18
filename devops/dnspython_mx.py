#!/usr/bin/env python
# coding:utf-8

import dns.resolver

domain = raw_input('please input an domain:')
MX = dns.resolver.query(domain, 'MX')
for i in MX:
    print 'MX preference =', i.preference, 'mail exchager =', i.exchange
