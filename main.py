"""
Usage:  hermes install [-dsvV] <pkg>...
        hermes -h | --help
        hermes --version

Options:
    -d, --depends           Require dependency installation
    -h, --help              Display usage and options
    -s, --check-sigs        Verify package GPG signatures
    -v, --verify            Verify package checksums
    -V, --verbose           Display debugging messages
    --version               Display version

"""

from configure import valid_hermes_config
from configure import valid_pkg_config

from docopt import docopt               # MIT License
import os                               # Standard Library
import requests                         # Apache License v2.0
import sh                               # MIT License
import tarfile                          # Standard Library


def dl_url(url):
    dl = requests.get(source_url)
    if not dl.status == 200:  # is this actually a meaningful test?
        return False
    with open(pkg_id, 'wb') as archive:  # pkg_id deoesn't include extension(s)
        for chunk in dl.iter_content(1024):
            archive.write(chunk)
    # where does it write it? how does it know?
    # what about errors?
    return True


def get_pkg(pkg_id):
    source_url = pkg_configs[pkg_id][source_url]
    if not dl_pkg(source_url):
        return False
    if not os.path.isfile(os.path.join(hermes_dir, 'archives', pkg_id)):
        return False
    if not valid_archive(pkg_id):
        return False
    # if runtime_config[verify_pkg]:
        # if not verified:
            # return False
    # if runtime_config[check_sigs]:
        # if not verified:
            # return False
    return True


def get_pkg_config(pkg_id):
    # This is a placeholder for repository-enabled functionality
    return True


def install_pkg(pkg_id):
    if runtime_config['install_dependencies']:
        for dependency in pkg_configs[pkg_id]['dependencies']:
            if not pkg_installed(dependency):
                install_pkg(dependency)
    # actual install code here


def main_installer(pkg_list):
    for pkg_id in pkg_list:
        if pkg_installed(pkg_id):
            print pkg_id, 'is already installed.'
        elif pkg_prepared(pkg_id):
            install_pkg(pkg_id)
        else:
            # Error message
            return False


def pkg_avail(pkg_id):
    if True:  # if archive is in hermes/archives and valid_archive(pkg_id)
        return True
    if get_pkg(pkg_id):
        return True
    # Error message
    return False


def pkg_config_avail(pkg_id):
    pkg_config_path = os.path.join(hermes_dir, 'configs', (pkg_id + '.hermes'))
    if pkg_id in pkg_configs:
        return True
    elif os.path.isfile(pkg_config_path):
        pkg_config = valid_pkg_config(pkg_config_path)
        if pkg_config:
            # populate pkg_configs[pkg_id] with contents of pkg_config
            return True
        else:
            # Error message
            return False
    elif get_pkg_config(pkg_id):
        return False  # temporary short-circuit (get_pkg_config() is a dummy)
        pkg_config = valid_pkg_config(pkg_config_path)
        if pkg_config:
            # populate pkg_configs[pkg_id] with contents of pkg_config
            return True
        else:
            # Error message
            return False


def pkg_installed(pkg_id):
    # if symlink in target_dir points at package in hermes/pkg
        # return True
    # if symlink in target_dir points elsewhere
        # deal with conflict
    # if binary already exists in target_dir
        # deal with conflict
    # Error message
    return False


def pkg_prepared(pkg_id):
    if pkg_installed(pkg_id):
        return True
    if not pkg_config_avail(pkg_id):
        # Error message
        return False
    if not pkg_avail(pkg_id):
        # Error message
        return False
    if runtime_config[install_dependencies]:
        for dependency in pkg_configs[pkg_id][dependencies]:
            if not pkg_prepared(dependency):
                # Error message
                return False
    return True


def populate_runtime_config():
    hermes_config = dict()
    system_config_path = os.path.join(hermes_dir, '.hermes.conf')
    user_config_path = os.path.expanduser(os.path.join('~', '.hermes.conf'))
    if os.path.isfile(user_config_path):
        hermes_config = valid_hermes_config(user_config_path)
    if not hermes_config and os.path.isfile(system_config_path):
        hermes_config = valid_hermes_config(system_config_path)
    if not hermes_config:
        hermes_config['check_sigs'] = True
        hermes_config['install_dependencies'] = False
        hermes_config['target_dir'] = '/usr/local'
        hermes_config['verify_pkgs'] = True
    if cli_args['--depends']:
        runtime_config['install_dependencies'] = True
    if cli_args['--check-sigs']:
        runtime_config['check_sigs'] = True
    if cli_args['--verify']:
        runtime_config['verify_pkgs'] = True
    return hermes_config


def valid_archive(pkg_id):
    tarball_name = pkg_id + pkg_configs[pkg_id]['tarball_ext']
    tarball_path = os.join.path(hermes_dir, 'archives', tarball_name)
    if not os.path.isfile(tarball_path):
        return False
    if not tarfile.is_tarfile(tarball_path):
        return False
    return True


def valid_pkg(pkg_id):
    # if not valid_archive(pkg_id):
        # Error message
        # return False
    # if cli_args[--verify'] and checksum is bad:
        # Error message
        # return False
    # if cli_args['--check-sigs'] and sig is bad:
        # Error message
        # return False
    return True


if __name__ == '__main__':
    cli_args = docopt(__doc__, version='hermes v0.0.1')
    print cli_args
    # hermes_dir = os.path.dirname(sh.which('hermes'))
    hermes_dir = 'hermes'
    runtime_config = populate_runtime_config()
    print runtime_config
    pkg_configs = dict()
    if cli_args['install']:
        print 'Installing ', str(cli_args['<pkg>'])
        main_installer(cli_args['<pkg>'])
