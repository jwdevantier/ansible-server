RevProxy
=========

Configure nginx to act as a SSL-terminating reverse proxy server.

Requirements
------------

No external requirements

Role Variables
--------------

The role is configured by the following variables:

* `certs_root` - The directory which will store all the Let's Encrypt configuration files and the SSL certificates themselves. Default is `/etc/letsencrypt`.

* `cert_email` - Email which will receive notifications from Let's Encrypt with regards to the requested SSL certificates. In particular - this email receives warnings when a cert is about to expire.

* `vhosts` - the list of entries for the domains to act as a reverse proxy for.

Each entry in `vhosts` has the following format:

```
- server_name: blog.example.com
  label: example-blog
  addr: localhost
  port: 81
```

In this example, traffic on `http://blog.example.com` and `https://blog.example.com` will be forwarded to the server bound to `localhost` port `81`.

Dependencies
------------

The `docker` role also included in this repository.

Example Playbook
----------------

The following shows a simple setup where variable configuration is inlined into the playbook itself.

In this example, requests on the domains `example.com` and `www.example.com` are both handled by a process listening on `localhost:8080`.

```
---
- hosts: server
  vars:
    certs_root: /etc/letsencrypt
    cert_email: cert-admin@example.com
    vhosts:
      - server_name: example.com
        label: oi4p
        addr: localhost
        port: 8080
      - server_name: www.example.com
        label: test
        addr: localhost
        port: 8080
  roles:
    - revproxy
```

Keep in mind, it's also possible to simply refer to a separate variables file like so:

```
---
- hosts: server
  vars:
    certs_root: /etc/letsencrypt
    cert_email: cert-admin@example.com
  vars_file: ./vhosts.yml
  roles:
    - revproxy
```

```
---
# inside 'vhosts.yml'
vhosts:
  - server_name: example.com
    label: oi4p
    addr: localhost
    port: 8080
  - server_name: www.example.com
    label: test
    addr: localhost
    port: 8080
```

License
-------

BSD

Author Information
------------------

Jesper Wendel Devantier (github.com/jwdevantier)
