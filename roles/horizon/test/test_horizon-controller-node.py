import pytest

@pytest.mark.parametrize("name", [
    ("openstack-selinux"),
    ("openstack-utils"),
    ("openstack-dashboard"),
    ("python-keystonemiddleware"),
    ("httpd"),
    ("mod_wsgi"),
    ("memcached"),
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("name,port", [
    ("httpd","80"),
    ("httpd-ssl","443"),
    ("memcached","11211"),
])
def test_listening_interfaces(Socket, name, port):
    socket = Socket("tcp://0.0.0.0:" + port)
    assert socket.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("ntpd", True),
    ("httpd", True),
    ("memcached", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("openstack-dashboard", "local_settings"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
