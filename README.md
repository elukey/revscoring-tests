=== Why ===

Running Wikimedia's revscoring on Debian Bullseye+ requires some tweaking, and having it in a Dockerfile helps while debugging issues.

=== Prerequisites ===

The revscoring model binary can be fetched from [https://analytics.wikimedia.org/published/wmf-ml-models/|this link].

=== How ===

```
docker-build .
docker run --volume /local/path/to/revscoring-tests:/revscoring-tests -it --rm --entrypoint /bin/bash revscoring-test
python3 test.py model.bin xxxxx en
