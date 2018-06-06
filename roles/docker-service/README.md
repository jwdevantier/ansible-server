Role Name
=========

Configures & installs a systemd service for managing a docker container as a service.

Requirements
------------

No dependencies on external python libraries.

Role Variables
--------------

The role is configured entirely by variables - see the example playbook below for an example service.

Dependencies
------------

No dependencies on other roles.

Example Playbook
----------------


```
- hosts: server

  roles :
    - role: docker-service
      name: gogs
      image: gogs/gogs
      volumes:
        - gogs_data:/data
      ports:
        - 10022:22
        - 10080:3000
```

**TODO  SHOULD ALLOW BEFORE & AFTER HOOKS HERE TOO**

License
-------

BSD

Author Information
------------------

Jesper Wendel Devantier (github.com/jwdevantier)