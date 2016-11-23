
component = ''
ports = ['6379']
configuration_files = ['redis.conf']
debian_packages = ['redis']
rhel_packages = ['redis']
debian_services = ['redis']
rhel_services = ['redis']

execfile('common.py')
