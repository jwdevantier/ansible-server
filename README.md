# Ansible Server Management

## Initialization

You need to initialize a virtual-env into which ansible and its dependencies can be installed.

*Note:* the helper scripts in `bin/` assumes the virtual-env dir will be `.env` - which git is also configured to ignore.

```
# First time installation
$ python3 -m venv .env
$ source .env/bin/activate
(.env)$ pip install -r requirements.txt
```

To enter the environment in the future, simply read in the activation file:

```
$ source .env/bin/activate
```

## Usage
This directory provides roles, modules and module utilities to aid in server configuration. It is for you to populate the inventory file with hosts and write the playbook(s) affecting the desired changes to your hosts.

To execute a playbook (yml) file, enter python virtual environment (see above) and issue `ansible-playbook <path/to/playbook>.yml`.

For examples - consult the README.md file contained in each role's directory.

For a general introduction to Ansible, see Servers for Hacker's [Ansible 2 tutorial](https://serversforhackers.com/c/an-ansible2-tutorial).

## Configuration

This ansible project is written to be self-contained as opposed to relying on globablly accessible system directories.

To that end, this project expects you to invoke `ansible` or `ansible-playbook` from the root directory - which ensures that `ansible.cfg` is consulted.

The configuration files are:

  * `ansible.cfg` - central [configuration file](http://docs.ansible.com/ansible/latest/intro_configuration.html). Overrides various paths to make ansible look in the local directories here.
  * `inventory` - the [ansible inventory](http://docs.ansible.com/ansible/latest/intro_inventory.html) file. This is where hosts and their connection options are mentioned and collected into groups.

The expected directory structure:
  * `library/` - a misnomer, but this directory will be consulted for custom [modules](http://docs.ansible.com/ansible/latest/modules.html)
  * `module_utils/` - can provide [module utilities](http://docs.ansible.com/ansible/latest/dev_guide/developing_module_utilities.html) - essentially where code shared across ansible modules should be placed (as python modules).
  * `roles/` - where all roles will be placed. Note you can install additional roles using [ansible galaxy](https://galaxy.ansible.com/) (`ansible galaxy install <role-name>`)

The `fact_path` setting is not relative to the project structure. This is because the path is consulted _on the remote system_ whenever ansible collects facts on each host. In this case, '`.fact`' files in `/etc/ansible/facts` are used to enrich facts available for the particular host on which they reside.
Each `.fact` file can be json/ini or a script returning valid JSON, see [local facts](http://docs.ansible.com/ansible/latest/playbooks_variables.html#local-facts) for more details.

## Helper Scripts

The `bin/` directory contains small helper scripts.

  * `ping` - uses the ping module in ansible to test connection to all (or if provided) a specific host/group of hosts.
  E.g. `bin/ping servers` will ping each host in the `servers` entry of the ansible inventory file.

  * `role-init` - takes one argument, the name of the new role and creates the directory structure for a new role.

  * `facts` - queries each host in the ansible inventory file for its facts - these are normally collected automatically before the play is executed and made available as top-level variables within the play. If a path is given, the facts are all written out to a file - this can be very helpful to determine the facts available.