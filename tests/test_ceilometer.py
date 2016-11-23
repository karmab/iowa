component = 'ceilometer'
ports = ['8777']
configuration_files = ['ceilometer.conf']
debian_packages = ['ceilometer-api', 'ceilometer-collector', 'ceilometer-agent-central', 'ceilometer-agent-notification', 'python-ceilometerclient', 'python-openstackclient']
rhel_packages = ['openstack-ceilometer-api', 'openstack-ceilometer-central', 'openstack-ceilometer-collector', 'openstack-ceilometer-common', 'openstack-ceilometer-compute', 'openstack-ceilometer-alarm', 'openstack-ceilometer-notification', 'openstack-utils', 'python-ceilometer', 'python-ceilometerclient', 'openstack-selinux', 'python-openstackclient']
debian_services = ['ceilometer-api', 'ceilometer-collector', 'ceilometer-agent-central', 'ceilometer-agent-notification', 'ceilometer-alarm-evaluator', 'ceilometer-alarm-notifier', 'ceilometer-notification']
rhel_services = ['openstack-ceilometer-api', 'openstack-ceilometer-collector', 'openstack-ceilometer-central', 'openstack-ceilometer-alarm-evaluator', 'openstack-ceilometer-alarm-notifier', 'openstack-ceilometer-notification']

execfile('common.py')
