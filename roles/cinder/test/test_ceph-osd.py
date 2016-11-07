import pytest

@pytest.mark.parametrize("name", [
    ("ceph"),
    ("ceph-common"),
    ("ceph-osd"),
    ("ceph-radosgw"),
    ("ceph-mon"),
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("process,enabled", [
    ("ntpd", True),
    ("ceph", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("node_service", [
    ("ceph"),
])
def test_main_services_files(File, node_service):
    _file = File("/etc/" + node_service + "/" + node_service + ".conf")
    assert _file.exists
