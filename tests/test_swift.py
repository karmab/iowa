component = 'swift'
ports = ['8080']
configuration_files = ['proxy-server.conf', 'object.builder', 'container.builder', 'account.builder']
debian_packages = ['swift', 'swift-proxy', 'python-swiftclient', 'python-keystoneclient', 'python-keystonemiddleware', 'memcached', 'python-openstackclient']
rhel_packages = ['openstack-swift-proxy', 'openstack-swift-plugin-swift3', 'memcached', 'python-swiftclient']
debian_services = ['swift-proxy']
rhel_services = ['openstack-swift-proxy', 'memcached']

execfile('common.py')
