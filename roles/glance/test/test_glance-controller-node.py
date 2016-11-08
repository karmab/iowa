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

def test_listening_interfaces(Socket):
    socket = Socket("tcp://0.0.0.0:9292")
    assert socket.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("ntpd", True),
    ("openstack-glance-api", True),
    ("openstack-glance-registry", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("glance", "glance-api.conf"),
    ("glance", "glance-cache.conf"),
    ("glance", "glance-registry.conf"),
    ("glance", "glance-scrubber.conf"),
    ("glance", "schema-image.json"),
    ("glance", "policy.json"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
