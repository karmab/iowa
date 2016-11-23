
component = 'rabbitmq'
ports = ['25672']
configuration_files = ['rabbitmq.config']
debian_packages = ['rabbitmq-server']
rhel_packages = ['rabbitmq-server']
debian_services = ['rabbitmq-server']
rhel_services = ['rabbitmq-server']

execfile('common.py')
