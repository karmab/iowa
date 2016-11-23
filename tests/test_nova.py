component = 'nova'
ports = ['8774']
configuration_files = ['nova.conf']
debian_packages = ['nova-api', 'nova-cert', 'nova-conductor', 'nova-consoleauth', 'nova-novncproxy', 'nova-scheduler', 'python-novaclient', 'python-openstackclient']
rhel_packages = ['openstack-nova-api', 'openstack-nova-conductor', 'openstack-nova-scheduler', 'openstack-nova-novncproxy', 'openstack-nova-console', 'openstack-utils', 'python-cinderclient', 'openstack-selinux', 'python-openstackclient']
debian_services = ['nova-api', 'nova-scheduler', 'nova-conductor', 'nova-novncproxy', 'nova-consoleauth']
rhel_services = ['openstack-nova-api', 'openstack-nova-scheduler', 'openstack-nova-conductor', 'openstack-nova-novncproxy', 'openstack-nova-consoleauth', 'openstack-nova-console']

execfile('common.py')
