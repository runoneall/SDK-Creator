# import module
import os
import sys
import yaml
from termcolor import colored

# set work dir
script_path = os.path.abspath(__file__)
creator_folder = os.path.dirname(script_path)

# load config tool
def load_config(file_path:str) -> dict:
    with open(file_path, "r") as config:
        return yaml.safe_load(config)

# get sdk file path
def sdk_file(file_name:str) -> str:
    return f'{creator_folder}/{file_name}'

# echo color log tool
def echo_log(level:str, msg:str):
    if level == 'info':
        print(colored('INF', 'black', 'on_cyan'), end=' : ')
        print(colored(msg, 'cyan'))
    if level == 'warning':
        print(colored('WAR', 'black', 'on_yellow'), end=' : ')
        print(colored(msg, 'yellow'))
    if level == 'error':
        print(colored('ERR', 'black', 'on_red'), end=' : ')
        print(colored(msg, 'red'))

# get installed packages
def installed_pkgs() -> list:
    pkg_root_folder = f'{creator_folder}/packages'
    return os.listdir(pkg_root_folder)

def add_import_path(folder_path:str):
    if folder_path not in sys.path:
        sys.path.append(folder_path)

# init module
class SDK:
    pass
    
# load sdk config
sdk_config = load_config(sdk_file('sdk_config.yml'))

# load packages
need_pkgs = sdk_config['Load']
for pkg_name in need_pkgs:
    echo_log('info', f'Loading {pkg_name}...')

    # package dir
    pkg_folder = f'{creator_folder}/packages/{pkg_name}'

    # add import path
    add_import_path(pkg_folder)

    # check package exists
    if os.path.exists(pkg_folder):

        # create package class
        class PackageClass:
            pass

        # read package config
        pkg_config = load_config(f'{pkg_folder}/install.yml')

        # load steps
        steps = pkg_config['step']

        # check require
        require = steps['require']
        if require != None:
            for pkg_name_tmp in require:
                if pkg_name_tmp not in installed_pkgs():
                    echo_log('error', f'  Package `{pkg_name}` require `{pkg_name_tmp}`')
                    echo_log('error', f'  But `{pkg_name_tmp}` not installed')
                    exit()

        # load install steps
        install_steps = steps['install']

        # check install steps
        if install_steps == None:
            echo_log('warning', f'  Module `{pkg_name}` not have any install steps')
            echo_log('warning', '  skip...')
            continue

        # run install
        Package_Name = str()
        for step in install_steps:
            step_name = list(step.keys())[0]
            echo_log('info', f'  Run Step `{step_name}`')

            # set package name
            if step_name == 'Set_Package_Name':
                Package_Name = step[step_name]
                echo_log('info', f'    Set Package Name `{Package_Name}`')

            # add function
            if step_name == 'Add_Function':
                source = step[step_name][0]
                source = source.split('/')
                source_file = f'{pkg_folder}/{source[0]}'
                source_name = source[1]
                link_to = step[step_name][1]
                print(source_name, source_file, link_to)

    # if not, warning
    else:
        echo_log('warning', '  Got an error in `Load` from `sdk_config.yml`')
        echo_log('warning', f'   -{pkg_name}: Package Not Found')
        echo_log('warning', '  skip...')