#!/bin/bash

set -e

SOURCE=../index.html

echo "Replace url with ${URL_FULL_BACKEND}"

sed -i -E "s#ws://localhost:8019#'wss://${URL_FULL_BACKEND}'#g" ${SOURCE}
sed -i -E "s#http://localhost:8019#'https://${URL_FULL_BACKEND}'#g" ${SOURCE}

echo "Modified html file:"
cat ${SOURCE}
