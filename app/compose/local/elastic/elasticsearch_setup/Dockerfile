FROM elasticsearch:8.5.3

USER root

COPY ./compose/local/elastic/elasticsearch_setup/entrypoint /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]

USER elasticsearch
