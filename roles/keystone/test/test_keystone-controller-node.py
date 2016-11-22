import pytest


@pytest.mark.parametrize("name", [
    ("openstack-selinux"),
    ("openstack-utils"),
    ("python-keystoneclient"),
    ("openstack-keystone"),
    ("python-keystonemiddleware"),
    ("python-keystone"),
    ("httpd"),
    ("mod_wsgi"),
])
def test_packages(Package, name):
    assert Package(name).is_installed


@pytest.mark.parametrize("name,port", [
    ("keystone_user", "5000"),
    ("keystone_admin", "35357"),
    ("httpd", "80"),
    ("httpd-ssl", "443"),
])
def test_listening_interfaces(Socket, name, port):
    socket = Socket("tcp://0.0.0.0:" + port)
    assert socket.is_listening


@pytest.mark.parametrize("process,enabled", [
    ("httpd", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled


@pytest.mark.parametrize("service,conf_file", [
    ("keystone", "keystone.conf"),
    ("keystone", "policy.json"),
    ("keystone", "keystone-paste.ini"),
    ("keystone", "logging.conf"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
