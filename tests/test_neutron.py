import pytest

component = 'neutron'
ports = ['9696']
configuration_files = ['neutron.conf', 'plugin.ini']
debian_packages = ['neutron-server', 'neutron-plugin-openvswitch-agent', 'neutron-plugin-ml2', 'neutron-l3-agent', 'neutron-metadata-agent', 'python-openstackclient', 'python-neutronclient']
rhel_packages = ['openstack-neutron', 'openstack-neutron-openvswitch', 'openstack-neutron-ml2', 'openstack-utils', 'openstack-selinux', 'python-openstackclient', 'openvswitch']
debian_services = ['neutron-server', 'neutron-openvswitch-agent', 'neutron-dhcp-agent', 'neutron-l3-agent', 'neutron-metadata-agent', 'openvswitch-switch']
rhel_services = ['neutron-server', 'neutron-openvswitch-agent', 'neutron-dhcp-agent', 'neutron-l3-agent', 'neutron-metadata-agent', 'openvswitch']
configuration_files = ["/etc/%s/%s" % (component, configuration_file) for configuration_file in configuration_files]


@pytest.fixture()
def Variables(SystemInfo):
    def f(args):
        version = SystemInfo.distribution
        if args == 'packages':
            if version in ['debian', 'ubuntu']:
                return debian_packages
            else:
                return rhel_packages
        elif args == 'services':
            if version in ['debian', 'ubuntu']:
                return debian_services
            else:
                return rhel_services
        elif args == 'ports':
            return ports
    return f


def test_packages(Package, Variables):
    packages = Variables('packages')
    for package in packages:
        assert Package(package).is_installed


def test_services(Service, Variables):
    for service in Variables('services'):
        assert Service(service).is_running
        assert Service(service).is_enabled


def test_ports(Socket, Variables):
    for port in Variables('ports'):
        socket = Socket("tcp://0.0.0.0:%s" % port)
        assert socket.is_listening


@pytest.mark.parametrize("conf", configuration_files)
def test_configuration_files(File, conf):
    _file = File(conf)
    assert _file.exists
