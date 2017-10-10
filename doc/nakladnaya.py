#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging
from contextlib import suppress

import helpers as hlp
from .position import *


class Nakladnaya(object):
	
	def __init__(self):
		self.__created = datetime.now()
		self.__positions = []
		self.__suspected = True
	created = property(lambda self: self.__created)	
	suspected = property(lambda self: self.__suspected)
	
	@property
	def number(self):
		return self.__number
	
	@number.setter
	@hlp.info_value
	@hlp.value_not_none
	def number(self, value):
		self.__number = value
		
	@number.deleter
	def number(self):
		logging.info('Number {0} deleted'.format(self.number))
		del self.__number
		
	@property # это свойство можно также создать следующей командой: address = property(lambda self: self.__address)
	def address(self):
		return self.__address
		
	@address.setter
	@hlp.warning_value
	@hlp.value_not_none
	def address(self, value):
		self.__address = value
		
	@property
	def responser(self):
		return self.__responser
		
	@responser.setter
	@hlp.trace_value(logging.ERROR - 1)
	@hlp.value_not_none
	def responser(self, value):
		logging.warning('Нежелательно менять ответственного сотрудника!')
		self.__responser = value
		
	@responser.deleter
	def responser(self):
		logging.error('Всему пиздец!')
		del self.__responser
	
	
	subscribed = property(lambda self: False)
	
	@property
	def itogo(self):
		if self.subscribed:
			return self.__itogo
		else:
			return sum(P.sum for P in self.__positions)
	
	def append(self, *args, **kwargs):
		if isinstance(args[0], Position):
			P = args[0]
		else:
			P = Position(*args, **kwargs)
		self.__positions.append(P)
		self.check_nakl()

	__str_data = [
		('Number', 'number'),
		('Creation date', 'created'),
		('Address', 'address'),
		('Responible persone', 'responser'),
		('Is subscribed', 'subscribed'),
		('Result', 'itogo'),
		('Suspected', 'suspected') 
	]
	
	def check_nakl(self):
		if len(self.__positions) > 0:
								#print('LEN ITEMS: '+str(len(self.__positions)))
								for item in self.__positions:
									#print('ITEM SUSPECTED {0}: {1}'.format(item.title, item.suspected))
									if item.suspected:
										self.__suspected = True
										break
									else:
										self.__suspected = False
				
	
	def __len__(self):
		return len(self.__positions)
	
	def __str__(self):
		L = []
		for text, prop_name in type(self).__str_data:
			with suppress(AttributeError):
				L.append('{0}: {1}'.format(text, getattr(self, prop_name)))
		L.extend(map(str, self.__positions))
		return '\n'.join(L)
	
	def __getitem__(self, key):
		if not isinstance(key, int):
			raise ValueError('Slices or keys not supported')
		return self.__positions[key]
		
	def __setitem__(self, key, value):
		if not isinstance(key, int):
			raise ValueError('Slices or keys not supported')
		self.__positions[key] = value
		
	def __delitem__(self, key):
		if not isinstance(key, int):
			raise ValueError('Slices or keys not supported')
		del self.__positions[key]
		
	def __iter__(self):
		yield from self.positions
		
		
	
		