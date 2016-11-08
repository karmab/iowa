import pytest

@pytest.mark.parametrize("name", [
    ("openstack-cinder"),
    ("python-cinderclient"),
    ("openstack-selinux"),
    ("openstack-utils")
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("process,enabled", [
    ("ntpd", True),
    ("openstack-cinder-volume", True),
    ("openstack-cinder-backup", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("cinder", "cinder.conf"),
    ("cinder", "api-paste.ini"),
    ("cinder", "rootwrap.conf"),
    ("cinder", "policy.json"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
