#!/bin/bash
. /usr/share/install-libraries/il-lib.sh

pushd /opt/fmc_repository/Process || exit;
mk_meta_link "php_sdk" "Reference"
popd || exit;
