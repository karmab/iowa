component = 'nova'
ports = []
configuration_files = ['nova.conf']
debian_packages = ['nova-compute']
rhel_packages = ['openstack-nova-compute']
debian_services = ['nova-compute']
rhel_services = ['openstack-nova-compute']

execfile('common.py')
