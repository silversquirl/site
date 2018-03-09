#!/bin/bash

IFS=\; read -r -a cookies <<<"$HTTP_COOKIE"

for c in "${cookies[@]}"; do
  if [[ "${c%%=*}" = dark ]]; then
    age=-1
    break
  fi
done

age="${age:-$((60*60*24*7*2))}" # Default to 2 weeks until expiry

echo "Set-Cookie: dark=chocolate; Path=/; Max-Age=$age"
echo "Location: ${HTTP_REFERER:-/}"
echo
