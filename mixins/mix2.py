#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ('func1', 'z',)

def func1(self, m):
	print('func1', 2*m)

z = property(lambda self: self.var)

@z.setter
def z(self, value):
	self.var = value

	
	