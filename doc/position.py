#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress

class Position(object):
	
	def __init__(self, title, quantity, **kwargs):
		self.__title = title
		self.__quantity = quantity
		with suppress(KeyError): # подавление исключения
			self.__unit = kwargs['unit']
		with suppress(KeyError):
			self.__price = kwargs['price']
		try:
			self.__sum = kwargs['sum')
		except KeyError:
			try:
				self.__sum = self.quantity * self.price
			except AttributeError as exc: # подмена исключения
				raise ValueError('Price or sum have to be specified') from exc
				
	title = property(lambda self: self.__title)
	quantity = property(lambda self: self.__quantity)
	unit = property(lambda self: self.__unit)
	price = property(lambda self: self.__price)
	sum = property(lambda self: self.__sum)