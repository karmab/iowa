import pytest

service = 'cinder'
ports = ['8776']
configuration_files = ['cinder.conf']
debian_packages = ['cinder-api', 'python-openstackclient', 'python-cinderclient', 'cinder-volume', 'python-mysqldb']
rhel_packages = ['openstack-cinder', 'openstack-utils', 'openstack-selinux', 'python-openstackclient', 'device-mapper-multipath', 'python-oslo-log']
debian_services = ['cinder-api', 'cinder-scheduler']
rhel_services = ['openstack-cinder-api', 'openstack-cinder-scheduler']
configuration_files = ["/etc/%s/%s" % (service, configuration_file) for configuration_file in configuration_files]


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
