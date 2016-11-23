component = 'openstack-dashboard'
ports = []
configuration_files = ['local_settings']
debian_packages = ['apache2', 'libapache2-mod-wsgi', 'memcached', 'python-memcache', 'openstack-dashboard']
rhel_packages = ['httpd', 'mod_wsgi', 'mod_ssl', 'memcached', 'openstack-dashboard']
debian_services = ['apache2']
rhel_services = ['httpd']

execfile('common.py')
