#!/usr/bin/env sh

tee .env <<EOF!
PUID=`id -u $USER`
PGID=`getent group docker | cut -d: -f3`
TZ=`cat /etc/timezone`

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

SWAG_EMAIL=
SWAG_SUBDOMAINS=
SWAG_URL=

MAXMINDDB_LICENSE_KEY=

EOF!

