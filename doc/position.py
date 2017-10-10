#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress
from decimal import Decimal


class Position(object):
	
	def __init__(self, title, quantity, **kwargs):
		self.__title = title
		self.__quantity = quantity
		self.__suspected = True
		with suppress(KeyError): # подавление исключения
			self.__unit = kwargs['unit']
		with suppress(KeyError):
			self.__price = Decimal(kwargs['price'])
		try:
			self.__sum = Decimal(kwargs['sum'])
		except KeyError:
			try:
				self.__sum = self.quantity * self.price
			except AttributeError as exc: # подмена исключения
				raise ValueError('Price or sum have to be specified') from exc
		try:
			self.check_pos()
		except:
			#print('ХУЕТА')
			self.__suspected = False
	title = property(lambda self: self.__title)
	quantity = property(lambda self: self.__quantity)
	unit = property(lambda self: self.__unit)
	price = property(lambda self: self.__price)
	sum = property(lambda self: self.__sum)
	suspected = property(lambda self: self.__suspected)
	
	__str_data = [
		('N','title'),
		('C','quantity'),
		('P','price'),
		('S','sum'),
		('S', 'suspected')
	]
	
	def check_pos(self):
		if self.__quantity * self.__price == self.__sum:
			self.__suspected = False


	
	def __str__(self):
		L = []
		for text, prop_name in type(self).__str_data:
			with suppress(AttributeError):
				L.append('{0}: {1}'.format(text, getattr(self, prop_name)))
		return ', '.join(L)