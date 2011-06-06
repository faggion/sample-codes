#!/bin/sh

HOST=test.server
if test $1 = "prod"
then
    HOST=api.server
fi

echo $HOST
