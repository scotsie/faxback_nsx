#!/bin/bash

NAME=$(python3 -c 'print(eval(open("faxback_nsx.manifest").read())["name"])')
VERSION=$(python3 -c 'print(eval(open("faxback_nsx.manifest").read())["version"])')
rm /omd/sites/cmk/var/check_mk/packages/${NAME} \
   /omd/sites/cmk/var/check_mk/packages_local/${NAME}-*.mkp ||:

mkp -v package faxback_nsx.manifest 2>&1 | sed '/Installing$/Q' ||:

cp /omd/sites/cmk/var/check_mk/packages_local/$NAME-$VERSION.mkp .

mkp inspect $NAME-$VERSION.mkp
