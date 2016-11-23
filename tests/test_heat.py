import pytest

component = 'heat'
ports = ['8004', '8000']
configuration_files = ['heat.conf']
debian_packages = ['heat-api', 'heat-api-cfn', 'heat-api-cloudwatch', 'heat-engine', 'python-heatclient', 'python-openstackclient']
rhel_packages = ['openstack-heat-api', 'openstack-heat-api-cfn', 'openstack-heat-common', 'openstack-heat-engine', 'openstack-heat-api-cloudwatch', 'heat-cfntools', 'python-heatclient', 'openstack-utils', 'python-openstackclient']
debian_services = ['heat-api', 'heat-api-cfn', 'heat-api-cloudwatch', 'heat-engine']
rhel_services = ['openstack-heat-api', 'openstack-heat-api-cfn', 'openstack-heat-api-cloudwatch', 'openstack-heat-engine']
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
