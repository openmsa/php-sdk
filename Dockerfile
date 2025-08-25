FROM docker.io/ubiqube/msa2-linuxdev:latest AS builder
USER 1000
WORKDIR /home/ncuser

RUN install_default_dirs.sh

COPY . .
# Build tarball {{{
RUN cp -R . /opt/fmc_repository/php_sdk && \
    install_repo_deps.sh /opt/fmc_repository/php-sdk && \
    echo "⏳ Creating php-sdk-reference.tar.xz" && \
    chmod a+w -R /opt/fmc_repository/ && \
    tar cf php-sdk-reference.tar.xz --exclude-vcs /opt/fmc_repository/ -I 'xz -T0' --checkpoint=1000 --checkpoint-action=echo='%{%Y-%m-%d %H:%M:%S}t ⏳ \033[1;37m(%d sec)\033[0m: \033[1;32m#%u\033[0m, \033[0;33m%{}T\033[0m'
# }}}

FROM docker.io/ubiqube/ubi-almalinux10:latest
# Copy all resources to the final image {{{
RUN mkdir -p /opt/fmc_repository && chown -R 1000:1000 /opt/fmc_repository
USER 1000
COPY --from=builder /home/ncuser/*.xz /home/ncuser/
COPY --from=builder /usr/share/install-libraries/il-lib.sh /usr/share/install-libraries/il-lib.sh
COPY docker-entrypoint.sh /
COPY install.sh /home/ncuser/
ENTRYPOINT ["/docker-entrypoint.sh"]
# }}}


