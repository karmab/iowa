component = 'cinder'
ports = ['8776']
configuration_files = ['cinder.conf']
debian_packages = ['cinder-api', 'python-openstackclient', 'python-cinderclient', 'cinder-volume', 'python-mysqldb']
rhel_packages = ['openstack-cinder', 'openstack-utils', 'openstack-selinux', 'python-openstackclient', 'device-mapper-multipath', 'python-oslo-log']
debian_services = ['cinder-api', 'cinder-scheduler']
rhel_services = ['openstack-cinder-api', 'openstack-cinder-scheduler']

execfile('common.py')
