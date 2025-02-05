#!/bin/bash

curl -s -H "Content-Type: application/x-ndjson" -XPOST 127.0.0.1:9200/receipe/_bulk --data-binary "@receipe.json" &&\
printf "\n✅ Insertion receipe index to elastic node OK ✅\n"

curl -s -H "Content-Type: application/x-ndjson" -XPOST 127.0.0.1:9200/accounts/_bulk --data-binary "@accounts.json" &&\
printf "\n✅ Insertion accounts index to elastic node OK ✅\n"

curl -s -H "Content-Type: application/x-ndjson" -XPOST 127.0.0.1:9200/movies/_bulk --data-binary "@movies.json" &&\
printf "\n✅ Insertion movies index to elastic node OK ✅\n"

curl -s -H "Content-Type: application/x-ndjson" -XPOST 127.0.0.1:9200/products/_bulk --data-binary "@products.json" &&\
printf "\n✅ Insertion products index to elastic node OK ✅\n"
