import pytest

@pytest.mark.parametrize("name", [
    ("openstack-selinux"),
    ("openstack-utils"),
    ("python-glance-store"),
    ("python-glanceclient"),
    ("openstack-glance"),
    ("python-glance"),
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("name,port", [
    ("heat-api","8004"),
    ("heat-cfn","8000"),
    ("heat-watch","8003"),
])
def test_listening_interfaces(Socket, name, port):
    socket = Socket("tcp://0.0.0.0:" + port)
    assert socket.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("ntpd", True),
    ("openstack-heat-api-cfn", True),
    ("openstack-heat-api-cloudwatch", True),
    ("openstack-heat-api", True),
    ("openstack-heat-engine", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("heat", "heat.conf"),
    ("heat", "policy.json"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
