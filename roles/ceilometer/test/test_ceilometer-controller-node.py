import pytest

@pytest.mark.parametrize("name", [
    ("openstack-ceilometer-alarm"),
    ("openstack-ceilometer-api"),
    ("openstack-ceilometer-central"),
    ("openstack-ceilometer-collector"),
    ("openstack-ceilometer-common"),
    ("openstack-ceilometer-notification"),
    ("openstack-utils"),
    ("openstack-selinux"),
    ("ntpd"),
])
def test_packages(Package, name, version):
    assert Package(name).is_installed

def test_listening_interfaces(Socket):
    socket = Socket("tcp://0.0.0.0:8777")
    assert socket.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("ntpd", True),
    ("openstack-ceilometer-api", True),
    ("openstack-ceilometer-notification", True),
    ("openstack-ceilometer-central", True),
    ("openstack-ceilometer-collector", True),
    ("openstack-ceilometer-alarm-evaluator", True),
    ("openstack-ceilometer-alarm-notifier", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("ceilometer", "ceilometer.conf"),
    ("ceilometer", "pipeline.yaml"),
    ("ceilometer", "event_pipeline.yaml"),
    ("ceilometer", "policy.json"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
