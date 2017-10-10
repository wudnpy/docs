#!/usr/bin/python3
# -*- coding: utf-8 -*-

#from mymix import mymix
import mix2
from mixin import mixin
#@mymix

@mixin(mix2)
class MyClass(object):
	
	def method1(self):
		print('method1')
	
	def method2(self):
		print('method2')
		
	x = property(lambda self: self.__x)

	@x.setter
	def x(self.value):
		self.__x = value
	
Z = MyClass()
Z.method1()
Z.method2()
print(Z.x)