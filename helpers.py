#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

def value_not_none(method):
	def checked_method(self, value):
		if value is None:
			raise ValueError('\'None\' is not allowed for property value')
			return method(self, value)
	checked_method.__name__ = method.__name__
	return checked_method
	
def trace_value(loglevel = logging.DEBUG):
	def tracing_value(method):
		def traced_method(self, value):
			p_name = method.__name__
			old = getattr(self, p_name)
			msg = ('Property \'{p_name}\' will be change' +
			'from  \'{old}\' to \'{value}\'').format(**locals())  
			logging.log(loglevel, msg)
			return method(self, value)
		traced_method.__name = method.__name__
		return traced_method
	return tracing_value
	
debug_value = trace_value(logging.DEBUG)
info_value = trace_value(logging.INFO)
warning_value = trace_value(logging.WARNING)
		