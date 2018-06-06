#!/usr/bin/env bash

container_running () {
    local container="${1}"
    if [[ `docker ps -a|perl -nle 'print "$1" if /.*\s([^\s]+)$/g' | perl -ne "print "\$\&" if /${container}/g"` == "${container}" ]]; then
        return 0
    else
        return 1
    fi
}

container_stop () {
    local container="${1}"
    # stop the container - if the container wasn't found, that's also a success
    2>&1 \docker stop "${1}" | perl -wnE 'exit 0 if /no such container/i'
    return $?
}

container_destroy () {
    local container="${1}"
    # destroy container - if it doesn't exist, that's also OK
    2>&1 \docker rm "${1}" | perl -wnE 'exit 0 if /no such container/i'
    return $?
}

err () {
    >&2 echo "$*"
}

case_create () {
    local container="${1}"
    HOST_IP=`ip addr show dev docker0 | perl -nle 'print "$1" if /^.*inet\s+([^\/]*).*/g'`
    \docker create \
        --restart=always \
        --name "${container}" \
        --add-host docker-host:"${HOST_IP}" \
        {{ container_docker_args | replace('\n', '') }} \
        {{ container_image }} \
        {{ container_program_args }}
    if [[ $? -ne 0 ]]; then
        err "failed to create container ${container}"
        exit 1
    fi
}

case_stop () {
    local container="${1}"
    container_stop "${container}"
}

case_destroy () {
    local container="${1}"
    if container_running "${container}"; then
        container_stop "${container}"
    fi
    if ! container_destroy "${container}"; then
        err "failed to destroy container '${container}'\!"
        exit 1
    fi
}

case_start () {
    local container="${1}"
    if ! \docker start "${container}"; then
        err "failed to start ${container}"
        exit 1
    fi
}

case "$1" in
    start)
        case_start "{{ container_service_name }}"
        ;;
    stop)
        case_stop "{{ container_service_name }}"
        ;;
    create)
        case_create "{{ container_service_name }}"
        ;;
    destroy)
        case_destroy "{{ container_service_name }}"
        ;;
    *)
        err "Usage $0 {create|destroy|start|stop}"
        exit 1
esac