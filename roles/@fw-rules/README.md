Role Name
=========

Installs a list of firewall rules provided the firewall is enabled.

This is really a convenience wrapper around the `ufw` module, providing some sensible defaults for standard rules.

Requirements
------------

* No prerequisites - for the role to have any effect though, use the `ufw` role of this repo.

Role Variables
--------------

Variables should be set as parameters *directly* to the role as this role is supposed to be used multiple times. The role 

* `rules` (required)
  * a list of rules to install into the firewall
* `default_*` (optional)
  * a series of variables which provide a default/fallback value for various attributes of a rule.
  * See the 'Rule defaults' section below.

The role takes a list of rules to install into the firewall, each rule is specified as a key->map/object where only the `port` is strictly required. Thus, a minimal rule would be `{ port: 80 }`.

### Rule defaults
The firewall rule accepts many parameters. To cut down on typing, most parameters are optional and their value will be sourced from a default value variable.
Defaults are specified in variables to allow the role to remain flexible. This means you can invoke the role multiple times with different defaults to limit typing. 

In all cases, these variables are the attribute in question prefixed by `default_`. Please refer to the section describing the rule format for an explanation of what they do.

* `default_policy`
  * **default**: `allow`
* `default_proto`
  * **default**: `tcp`
* `default_src`
  * **default**: `any`
* `default_dest`
  * **default**: `any`
* `default_comment`
  * **default**: 'installed by ansible'

### Rule format




The *required* rule parameters are:
* `port`
  * which port or port range to cover
  * example: `80` for a single port or `5500:5600` to specify a range

The *optional* rule parameters are:
* `policy`
  * what to do with a packet matching the rule
  * **examples**: `reject`, `limit`
  * **allowed values**: See [ufw module](https://docs.ansible.com/ansible/2.4/ufw_module.html), `rule` argument
  * **default**: `allow`
* `proto`
  * the protocol to which this rule applies
  * **allowed**: See [ufw module](https://docs.ansible.com/ansible/2.4/ufw_module.html), `proto` argument.
  * **default**: `tcp`
* `src`
  * limits rule to packets whose origin matches the specified. Supports single IP and CIDR notation.
  * **allowed**:
    * `any` - equivalent to ignoring the source
    * `lan` - only apply to packets originating from inside the LAN (unique to this role)
    * Anything from [ufw module](https://docs.ansible.com/ansible/2.4/ufw_module.html), `from_ip` argument.
  * **default**: `any`
  * **examples**:
    * `192.168.0.0/16`
    * `192.168.1.254`
* `dest`
  * limits rule to packets whose destination matches the specified. Supports single IP and CIDR notation
  * **allowed**:
    * `any` - equivalent to ignoring this setting.
    * `lan` - apply rule iff. packet's destination/target is a machine on the local LAN.
    * Anything else from [ufw module](https://docs.ansible.com/ansible/2.4/ufw_module.html), `to_ip` argument
* `comment`
  * A free-form string which is printed alongside the rule in UFW's configuration files

Dependencies
------------

No dependencies on outside roles. Although if the `ufw` role is not used, the entire role here is skipped as rules are only installed into the firewall if the `ufw` role has run for this host.

Example Playbook
----------------

It is generally *not* recommended to use directly in a playbook, but if you did:

```
- hosts: servers
  roles:
  - role: @fw-rules
    default_proto: tcp
    rules:
    - { port: 80 }
    - { port: 22, src: lan }
```

Again, ***it is not recommended to use directly in a playbook!***

Using in a role
---------------

```
- name: install firewall rules for HTTP server
  import_role:
    name: @fw-rules
  vars:
    default_src: lan
    default_direction: in
    rules:
    - { port: 80 }
    - { port: 443 }
  when: myrole_open_ports|default(false)
```

License
-------

BSD
