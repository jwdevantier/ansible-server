Bind9 DNS Server
================

Configure the Bind9 DNS Server to operate local domains and cache & forward requests for remote domains.

Inspired by: http://mixeduperic.com/ubuntu/seven-easy-steps-to-setting-up-an-interal-dns-server-on-ubuntu.html

Requirements
------------

Debian Linux 9+, Ubuntu 18.04+

Role Variables
--------------

The bind9 DNS will handle requests pertaining to its own domain(s). Other requests will be forwarded to an upstream DNS server and the results will be cached locally for future requests.
The net effect is a speed-up in DNS queries from the perspective of LAN users.

To configure the upstream DNS servers to consult, define `bind9_forwarders` as a list of IP addresses:
```
bind9_forwarders:
  - 8.8.8.8
```

The bind9 server can administer multiple domains by defining a pair of zones - one for domain to IP lookups (forward lookup) and one for IP to domain lookups (reverse lookups).

This role allows defining multiple roles as a list of entries in `bind9_zones`:
```
bind9_zones:
- domain: home
  # addr of bind host - e.g. '1' => {{network}}.1
  #gw_addr: 1
  network: 10.7.5
  adm_email: contact@pseudonymous.me
  a_records:
  - subdomain: gw
    addr: 1
  c_records:
  - alias: fw
    dest: gw
```

In this configuration, bind9 will administrate the TLD `.home` and install a single A-record (in addition to a record for the server itself) for `gw.home` which will point to `10.7.5.1` because `addr` is set to `1` and the zone network is `10.7.5` (corresponding to CIDR `10.7.5.0/24`).

Additionally, a single CNAME record is installed which creates an alias from `fw.home` to `gw.home`.

Dependencies
------------

No role dependencies.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: my_dns_server
      roles:
         - role: bind9
           domain: lan
           gw_addr: 254
           network: 192.168.1
           adm_email: john@example.com
           a_records:
           - subdomain: files
             addr: 10
           - subdomain: mail
             addr: 20
           c_records:
           - alias: files01
             dest: files

In this case, the `bind9` DNS server is configured to operate the `lan` domain (that is, a TLD) on the network `192.168.1.X` (`network`). It is expected that the Bind9 server resides on a machine whose address on the network is `192.168.1.254` (`gw_addr`).
The network has two A-records, `files.lan` points to `192.168.1.10` and `mail.lan` to `192.168.1.20`. Also the alias `files01.lan` points to `files.lan`.

Note
-------
* `network` should only be the 3 major octests - the fourth is omitted
* `domain` can be a TLD (as in the example of `lan` or `home`), but can also be a domain, e.g. `linux.home`. In this case, A-records would create entries like `<subdomain>.linux.home`.

Example: use on Debian Linux
----------------------------
Edit `/etc/resolv.conf`:

```
nameserver <ip of bind9 dns server machine>
domain <zone.domain>
search <zone.domain>
```

For example, given the bind9 host is `192.168.1.254` and is configured to administrate `lan.home`:
```
nameserver 192.168.1.254
domain lan.home
search lan.home
```

License
-------

BSD
