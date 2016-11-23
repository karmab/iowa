component = 'heat'
ports = ['8004', '8000']
configuration_files = ['heat.conf']
debian_packages = ['heat-api', 'heat-api-cfn', 'heat-api-cloudwatch', 'heat-engine', 'python-heatclient', 'python-openstackclient']
rhel_packages = ['openstack-heat-api', 'openstack-heat-api-cfn', 'openstack-heat-common', 'openstack-heat-engine', 'openstack-heat-api-cloudwatch', 'heat-cfntools', 'python-heatclient', 'openstack-utils', 'python-openstackclient']
debian_services = ['heat-api', 'heat-api-cfn', 'heat-api-cloudwatch', 'heat-engine']
rhel_services = ['openstack-heat-api', 'openstack-heat-api-cfn', 'openstack-heat-api-cloudwatch', 'openstack-heat-engine']

execfile('common.py')
