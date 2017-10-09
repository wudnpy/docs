#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging

import helpers as hlp
from .position import *


class Nakladnaya(object):
	
	def __init__(self):
		self.__created = datetime.now()
		self.__positions = []
		
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
	
	def append(self, *args, **kwargs):
		if isinstance(args[0], Position):
			P = args[0]
		else:
			P = Position(*args, **kwargs)
		self.__positions.append(P)