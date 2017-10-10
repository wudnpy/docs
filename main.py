#!/usr/bin/python3
# -*- coding: utf-8 -*-
#19:19
import doc

N = doc.Nakladnaya()

N.append('Рога', 25, unit='шт', price=100.02)
N.append(doc.Position('Копыта', 100, sum=1000.45))

print(N)
