#!/bin/sh

set -e

mkdir -p /srv/public/static
cat <<EOT > /srv/public/static/config.json
{
  "apiUrl": "$API_URL",
  "format": {
    "timeZone": "Europe/Warsaw",
    "dateTime": "YYYY-MM-DD HH:mm:ss",
    "pickerDateTime": "yyyy-MM-dd HH:mm"
  }
}
EOT

yarn install
# yarn build

exec npm run serve
