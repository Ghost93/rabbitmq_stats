import setuptools

setuptools.setup(
	name = "rabbitmq_stats",
	version = '0.1.0',
	description = "Gather RabbitMQ Stats for external logging",
	author = "Mike Cronce",
	author_email = "mike@quadra-tec.net",
	license = 'MIT',
	url = "https://github.com/mcronce/rabbitmq_stats",
	packages = ['rabbitmq_stats'],
	install_requires = ['requests'],
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
	]
)

