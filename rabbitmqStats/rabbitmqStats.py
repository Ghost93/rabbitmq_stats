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

	timestamp = 0

	def __init__(self, host, port, url, user, pwd):
		# Get epoch. can be formatted later
		self.timestamp = int(time.time())
		self.host = host
		self.port = port
		self.base_url = url
		self.username = user
		self.password = pwd

	def get_queues(self):
		body = self._request('/queues')
		return body

	def _request(self, path):
		try:
			r = requests.get('http://{0}:{1}{2}{3}'.format(self.host, self.port, self.base_url, path), auth = (self.username, self.password))
		except Excpetion as e:
			print('_request: {0}'.format(e))
			return {}
		return r.json()

def queue_names(queues):
	return [str(queue['name']) for queue in queues.values()]

def clean_msg_stats(node):
	stat_data = {}
	for key, item in node.items():
		if isinstance(item, dict):
			if 'rate' in item:
				stat_data[str(key)] = int(item['rate'])
			else:
				self.__walk_json(item)
		else:
			stat_data[str(key)] = int(item)

	return stat_data

def queue_msg_stats(queues, name):
	names = queue_names(queues)
	num = names.index(name)
	queue = queues[num]

	if('message_stats' in queue):
		msg_stats = queue['message_stats']
		cleaned_msg_stats = clean_msg_stats(msg_stats)
		cleaned_msg_stats['name'] = name
		return cleaned_msg_stats
	else:
		return 'Queue \'{}\' doe snot have any \'message_stats\' available'.format(name)

