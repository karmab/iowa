
component = 'mysql'
ports = ['3306']
configuration_files = ['/etc/my.cnf']
debian_packages = ['mariadb-server', 'python-mysqldb']
rhel_packages = ['mariadb-galera-server', 'MySQL-python']
debian_services = ['mysql']
rhel_services = ['mariadb']

execfile('common.py')
