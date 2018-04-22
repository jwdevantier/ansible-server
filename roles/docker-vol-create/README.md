docker-vol-create
=================

Role for creating docker volumes.

The `docker_volume` module fails on some systems if the system itself has
no volumes yet. This role is designed as a work-around for this issue, it
allows new volumes to be created regardless of whether the volume(s) are
the first to be made.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------
`volumes` should be a list of strings, each string will be the name of a volume.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Use
----------------

This role is not really intended to be used as part of a playbook because it does not accomplish anything meaningful on its own.

However, many roles would use docker, e.g. install a docker container as a system service, and these roles would often require modules.

Hence, the expected use is to include this module as a dependency of another, but to pass parameters along which determine the volume(s) to make.

```
dependencies:
- role: docker
- role: docker-vol-create
  volumes:
  - myvol1
  - {{ variable_from_role }}
```

License
-------

MIT
