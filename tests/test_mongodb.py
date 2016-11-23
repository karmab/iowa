
component = 'mongodb'
ports = ['27017']
configuration_files = ['/etc/mongod.conf']
debian_packages = ['mongodb-server', 'mongodb-clients', 'python-pymongo']
rhel_packages = ['mongodb-server', 'python-pymongo', 'mongodb']
debian_services = ['mongodb']
rhel_services = ['mongod']

execfile('common.py')
