from configobj import ConfigObj         # BSD License
from validate import Validator          # BSD License

hermes_configspec = """
check_sigs = boolean(default = True)                # check GPG signature?
install_dependencies = boolean(default = False)     # resolve dependencies?
target_dir = string(default = '/usr/local')         # where to install packages?
verify_pkgs = boolean(default = True)               # check hash?
"""

pkg_configspec = """
pkg_id = string                             # Package identifier
home_url = string                           # homepage for the project
source_url = string                         # URL for the source download
hash_type = option('md5', 'sha5')           # hashing algorithm
hash = string                               # hash for the source download
signature = string(default=None)            # GPG signature for the source download
dependencies = string_list(default=None)    # list of dependencies, if any
"""

def valid_hermes_config(file_path):
    spec = hermes_configspec.split('\n')
    hermes_config = ConfigObj(file_path, configspec=spec)
    validator = Validator
    valid = hermes_config.validate(validator)
    if valid:
        return hermes_config
    return False

def valid_pkg_config(file_path):
    spec = pkg_configspec.split('\n')
    pkg_config = ConfigObj(file_path, configspec=spec)
    validator = Validator
    valid = pkg_config.validate(validator)
    if valid:
        return pkg_config
    return False
