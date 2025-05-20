#!/bin/bash

PKGNAME=$(python3 -c 'print(eval(open("package").read())["name"])')
ln -sv $WORKSPACE $OMD_ROOT/local/lib/python3/cmk_addons/plugins/$PKGNAME

# ORIGINAL SCRIPT
#PKGNAME=$(python3 -c 'print(eval(open("package").read())["name"])')
#ln -sv $WORKSPACE $OMD_ROOT/local/lib/python3/cmk_addons/plugins/$PKGNAME

#for DIR in 'agents' 'checkman' 'checks' 'doc' 'inventory' 'notifications' 'pnp-templates' 'web'; do
#    rm -rfv $OMD_ROOT/local/share/check_mk/$DIR
#    ln -sv $WORKSPACE/$DIR $OMD_ROOT/local/share/check_mk/$DIR
#done;