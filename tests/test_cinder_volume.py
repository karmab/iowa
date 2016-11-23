component = 'cinder'
ports = []
configuration_files = ['cinder.conf']
debian_packages = ['cinder-api', 'python-openstackclient', 'python-cinderclient', 'cinder-volume', 'python-mysqldb']
rhel_packages = ['openstack-cinder', 'openstack-utils', 'openstack-selinux', 'python-openstackclient', 'device-mapper-multipath', 'python-oslo-log']
debian_services = ['cinder-volume']
rhel_services = ['openstack-cinder-volume']

execfile('common.py')
