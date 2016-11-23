component = 'neutron'
ports = ['9696']
configuration_files = ['neutron.conf', 'plugin.ini']
debian_packages = ['neutron-server', 'neutron-plugin-openvswitch-agent', 'neutron-plugin-ml2', 'neutron-l3-agent', 'neutron-metadata-agent', 'python-openstackclient', 'python-neutronclient']
rhel_packages = ['openstack-neutron', 'openstack-neutron-openvswitch', 'openstack-neutron-ml2', 'openstack-utils', 'openstack-selinux', 'python-openstackclient', 'openvswitch']
debian_services = ['neutron-server', 'neutron-openvswitch-agent', 'neutron-dhcp-agent', 'neutron-l3-agent', 'neutron-metadata-agent', 'openvswitch-switch']
rhel_services = ['neutron-server', 'neutron-openvswitch-agent', 'neutron-dhcp-agent', 'neutron-l3-agent', 'neutron-metadata-agent', 'openvswitch']

execfile('common.py')
