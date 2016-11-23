import pytest

component = 'ceilometer'
ports = ['8777']
configuration_files = ['ceilometer.conf']
debian_packages = ['ceilometer-api', 'ceilometer-collector', 'ceilometer-agent-central', 'ceilometer-agent-notification', 'python-ceilometerclient', 'python-openstackclient']
rhel_packages = ['openstack-ceilometer-api', 'openstack-ceilometer-central', 'openstack-ceilometer-collector', 'openstack-ceilometer-common', 'openstack-ceilometer-compute', 'openstack-ceilometer-alarm', 'openstack-ceilometer-notification', 'openstack-utils', 'python-ceilometer', 'python-ceilometerclient', 'openstack-selinux', 'python-openstackclient']
debian_services = ['ceilometer-api', 'ceilometer-collector', 'ceilometer-agent-central', 'ceilometer-agent-notification', 'ceilometer-alarm-evaluator', 'ceilometer-alarm-notifier', 'ceilometer-notification']
rhel_services = ['openstack-ceilometer-api', 'openstack-ceilometer-collector', 'openstack-ceilometer-central', 'openstack-ceilometer-alarm-evaluator', 'openstack-ceilometer-alarm-notifier', 'openstack-ceilometer-notification']
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
