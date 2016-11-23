
component = 'redis'
ports = ['6379']
configuration_files = ['/etc/redis.conf']
debian_packages = ['redis']
rhel_packages = ['redis']
debian_services = ['redis']
rhel_services = ['redis']

execfile('common.py')
