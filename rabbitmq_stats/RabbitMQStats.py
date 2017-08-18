#!/usr/bin/python

import requests
import time
import json
import sys

class RabbitMQStats():
	"""This is the class docstring"""
	host = None
	port = None
	base_url = None
	username = None
	password = None

	def __init__(self, host, port, url, user, pwd):
		self.host = host
		self.port = port
		self.base_url = url
		self.username = user
		self.password = pwd

	def get_overview(self):
		body = self._request('/overview')
		return body

	def get_nodes(self):
		body = self._request('/nodes')
		return body

	def get_queues(self):
		body = self._request('/queues')
		return body

	def get_partitions(self):
		queues = self.get_queues()
		partitions = []
		for queue in queues:
			partitions.extend(queue['partitions'])
		return partitions

	def get_applications(self):
		queues = self.get_queues()
		applications = {}
		for queue in queues:
			for application in queue['applications']
				applications[application['name']] = application
		return applications

	def _request(self, path):
		try:
			r = requests.get('http://{0}:{1}{2}{3}'.format(self.host, self.port, self.base_url, path), auth = (self.username, self.password))
		except Excpetion as e:
			print('_request: {0}'.format(e))
			return {}
		return r.json()

