#!/bin/bash
. /usr/share/install-libraries/il-lib.sh

pushd /opt/fmc_repository/Process || exit;
mk_meta_link "php-sdk" "Reference"
popd || exit;
