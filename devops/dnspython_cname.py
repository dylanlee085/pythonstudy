#! /usr/bin/env python
# coding: utf-8

import dns.resolver

domain = raw_input('please input an domain:')
cname = dns.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()