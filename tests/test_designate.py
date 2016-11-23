component = 'designate'
ports = ['9001']
configuration_files = ['designate.conf']
debian_packages = ['designate', 'designate-central', 'designate-sink', 'designate-pool-manager', 'designate-mdns', 'python-openstackclient']
rhel_packages = ['openstack-designate-api', 'openstack-designate-central', 'openstack-designate-sink', 'openstack-designate-pool-manager', 'openstack-designate-mdns', 'openstack-designate-common', 'python-designate', 'python-designateclient', 'openstack-designate-agent', 'python-openstackclient']
debian_services = ['designate-api', 'designate-central', 'designate-mdsn', 'designate-pool-manager']
rhel_services = ['openstack-designate-api', 'openstack-designate-central', 'openstack-designate-mdsn', 'openstack-designate-pool-manager']

execfile('common.py')
