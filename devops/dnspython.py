#/usr/bin/env python
# coding: utf-8


import dns.resolver

domain = raw_input('please input an domain:')
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        print j.address


