#!/usr/bin/python3
# -*- coding: utf-8 -*-

def mixin(module):
	def mix(cls):
		for name in module.__all__:
			setattr(cls, name, getattr(module, name))
		return cls
	return mix