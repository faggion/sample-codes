#!/bin/bash

echo "%root ALL=(ALL) NOPASSWD: ALL" > /tmp/root_group_nopass && chmod 0400 /tmp/root_group_nopass && mv /tmp/root_group_nopass /etc/sudoers.d/
