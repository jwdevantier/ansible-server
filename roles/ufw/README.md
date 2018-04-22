Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Input Variables:

* `ssh_port` - the port which SSH is running on. This port will be opened before the firewall is first activated.
* `ufw_policies` - holds the default policies for incoming/outgoing packets which are not otherwise affected by an installed rule. See the example playbook below to see its shape.

Output Variables:

* `ufw_enabled` - a fact set to `true`. Can be used to conditionally install UFW rules. See 'Dependencies' for information.

Dependencies
------------

This role will expose a fact, `ufw_enabled` which other roles should use to
conditionally install firewall entries, e.g.:

```
- name: allow external access to ganache
  ufw:
    rule: allow
    port: 8545
    proto: tcp
  notify:
    - restart ufw
  when: ufw_enabled
```

To ensure no role fail due to `ufw_enable` being undefined, I recommend setting
`ufw_enabled: false` in `group_vars/all.yml`.

**NOTE** if SSH runs on a non-standard port then you need to provide a better
supply the `ssh_port` variable when running the role.

Example Playbook
----------------

```
- hosts: servers
	roles:
  - role: ufw
    ssh_port: 22
    ufw_policies:
    - direction: incoming
      policy: deny
    - direction: outgoing
      policy: allow
```
This is equivalent to running the role without any parameters. By default, the firewall will allow outgoing traffic, but deny any incoming requests.

License
-------

MIT
