#!/usr/bin/python3
# -*- coding: utf-8 -*-
#19:19
import doc

N = doc.Nakladnaya()

N.append('Рога', 25, unit='шт', price=100.02)
N.append(doc.Position('Копыта', 100, sum=1000.45))
N.append('Левый сапог', 2, price=4, sum = 10)
N.append('Правый сапог', 2, price=4, sum = 8)

print(N[1])

print('-------------------')
N[2] = doc.Position('Бублики', 21, price=100, sum=1000)
print(N)
print('-------------------')
del N[1]
print(N)
