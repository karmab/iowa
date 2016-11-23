component = 'swift'
ports = ['6200', '6201', '6202']
configuration_files = ['swift.conf', 'proxy-server.conf', 'object.builder', 'container.builder', 'account.builder']
debian_packages = ['rsync', 'xinetd', 'swift', 'swift-account', 'swift-container', 'swift-object']
rhel_packages = ['rsync', 'xinetd', 'openstack-swift-object', 'openstack-swift-container', 'openstack-swift-account', 'python-swiftclient']
debian_services = ['swift-object', 'swift-container', 'swift-account', 'xinetd']
rhel_services = ['openstack-swift-object', 'openstack-swift-container', 'openstack-swift-account', 'xinetd']

execfile('common.py')
