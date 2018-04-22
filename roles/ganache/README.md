Ganache
=======

A role which runs a (dockerized) copy of the `ganache-cli` service for powering a private ethereum-based blockchain.

[Ganache](http://truffleframework.com/ganache/) comes as a complete package for local development, and a [cli-only](https://github.com/trufflesuite/ganache-cli) variant to host in server (cli only) or low-RAM environments.
The Truffle project also maintains an official [docker image](https://hub.docker.com/r/trufflesuite/ganache-cli/) which this role uses.

Requirements
------------

A functioning docker install. This role will include the `docker` role.

Role Variables
--------------

The variables generally have reasonable defaults, so configuration should not be necessary for typical use. However:

* `container_image` - Governs which docker image to use (default: `trufflesuite/ganache-cli`)
* `container:_name` - the name assigned the container which will be running `ganache`. Re-assign if running multiple instances of this service.
* `container_tag` - docker-specific. Run a specific (tag) version of the image or just the newest one?

* `service_name` - The service name. This variable determines the name of the systemd service which will operate the docker image (default: `ganache`).
* `eth_rpc` - The port to use for pointing to the ethereum RPC port (default: `8545`)
* `eth_nw_id` - Equivalent to `-i` in Ganache
* `eth_initial_accounts` - Equivalent to `-a` in Ganache
* `eth_default_balance_ether` - Equivalent to `-e` in Ganache
* `eth_chain_db_volname` - the name of the volume used to host the ethereum blockchain data.

Dependencies
------------

The `docker` role.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
  - hosts: someserver
    roles:
      - role: ganache
        eth_rpc: 9999
```

License
-------

MIT
