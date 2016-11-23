import pytest

component = 'designate'
ports = ['9001']
configuration_files = ['designate.conf']
debian_packages = ['designate', 'designate-central', 'designate-sink', 'designate-pool-manager', 'designate-mdns', 'python-openstackclient']
rhel_packages = ['openstack-designate-api', 'openstack-designate-central', 'openstack-designate-sink', 'openstack-designate-pool-manager', 'openstack-designate-mdns', 'openstack-designate-common', 'python-designate', 'python-designateclient', 'openstack-designate-agent', 'python-openstackclient']
debian_services = ['designate-api', 'designate-central', 'designate-mdsn', 'designate-pool-manager']
rhel_services = ['openstack-designate-api', 'openstack-designate-central', 'openstack-designate-mdsn', 'openstack-designate-pool-manager']
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
