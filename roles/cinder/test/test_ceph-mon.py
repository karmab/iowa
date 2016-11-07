import pytest

@pytest.mark.parametrize("name,version", [
    ("ceph"),
    ("ceph-common"),
    ("ceph-osd"),
    ("ceph-mon"),
])
def test_packages(Package, name, version):
    assert Package(name).is_installed

@pytest.mark.parametrize("name,port", [
    ("ceph-mon","6789"),
])
def test_listening_interfaces(Socket, Interface, name, port):
    socket = Socket("tcp://0.0.0.0:" + port)
    assert socket.is_listening

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
