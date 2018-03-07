#!/bin/bash

IFS=\; read -r -a cookies <<<"$HTTP_COOKIE"

for c in "${cookies[@]}"; do
  if [[ "${c%%=*}" = dark ]]; then
    del=1
    break
  fi
done

echo "Set-Cookie: dark=chocolate; Path=/${del:+; Max-Age=-1}"
echo "Location: ${HTTP_REFERER:-/}"
echo
