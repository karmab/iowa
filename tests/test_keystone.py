
component = 'keystone'
ports = ['5000', '35357']
configuration_files = ['keystone.conf']
debian_packages = ['keystone', 'python-openstackclient', 'apache2', 'libapache2-mod-wsgi', 'memcached', 'python-memcache']
rhel_packages = ['openstack-keystone', 'openstack-utils', 'openstack-selinux', 'python-openstackclient', 'python-keystonemiddleware', 'httpd', 'mod_wsgi', 'memcached', 'python-memcached']
debian_services = ['apache2']
rhel_services = ['httpd']

execfile('common.py')
