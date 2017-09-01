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

	def get_nodes(self, memory = False, binary = False, health = False):
		nodes = self._request('/nodes')
		body = []
		for node in nodes:
			if(memory or binary):
				node = self.get_node_details(node['name'], memory, binary)
			if(health):
				node['health'] = self.get_node_health(node['name'])
			body.append(node)
		return body

	def get_node_details(self, node_name, memory = True, binary = False):
		body = self._request('/nodes/%s?memory=%s&binary=%s' % (node_name, str(memory).lower(), str(binary).lower()))
		return body

	def get_node_health(self, node_name):
		body = self._request('/healthchecks/node/%s' % (node_name))
		return body

	def get_queues(self):
		body = self._request('/queues')
		return body

	def get_listeners(self):
		overview = self.get_overview()
		listeners_by_node = {}
		for listener in overview['listeners']:
			if(listener['node'] not in listeners_by_node):
				listeners_by_node[listener['node']] = []
			listeners_by_node[listener['node']].append(listener)
		return listeners_by_node

	def get_partitions(self):
		nodes = self.get_nodes()
		partitions = []
		for node in nodes:
			partitions.extend(node['partitions'])
		return partitions

	def get_applications(self):
		nodes = self.get_nodes()
		applications = {}
		for node in nodes:
			for application in node['applications']:
				applications[application['name']] = application
		return applications

	def _request(self, path):
		try:
			r = requests.get('http://{0}:{1}{2}{3}'.format(self.host, self.port, self.base_url, path), auth = (self.username, self.password))
		except Exception as e:
			print('_request: {0}'.format(e))
			return {}
		return r.json()

