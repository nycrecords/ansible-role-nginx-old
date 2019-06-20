import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_nginx_installed(host):
    nginx = host.package("rh-nginx18")

    assert nginx.is_installed


def test_nginx_config_exists(host):
    nginx_config = host.file("/etc/opt/rh/rh-nginx18/nginx/nginx.conf")

    assert nginx_config.exists
    assert nginx_config.is_file
    assert nginx_config.user == "root"
    assert nginx_config.group == "root"


def test_nginx_vhost_example_exists(host):
    nginx_vhost = host.file("/etc/opt/rh/rh-nginx18/nginx/nginx.conf")

    assert nginx_vhost.exists
    assert nginx_vhost.is_file
    assert nginx_vhost.user == "root"
    assert nginx_vhost.group == "root"


def test_nginx_listening_http(host):
    socket = host.socket("tcp://0.0.0.0:80")

    assert socket.is_listening
