component = 'glance'
ports = ['9292']
configuration_files = ['glance-api.conf', 'glance-registry.conf']
debian_packages = ['glance', 'python-openstackclient', 'python-glanceclient']
rhel_packages = ['openstack-glance', 'openstack-utils', 'openstack-selinux', 'python-openstackclient']
debian_services = ['glance-api', 'glance-registry']
rhel_services = ['openstack-glance-api', 'openstack-glance-registry']

execfile('common.py')
