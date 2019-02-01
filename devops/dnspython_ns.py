#!/usr/bin/env python
# coding: utf-8


import dns.resolver

domain = raw_input('please input an domain:')
ns = dns.resolver.query(domain, 'NS')
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()