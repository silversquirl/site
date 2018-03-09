#!/bin/bash
cd ../../

render() {
  echo "Content-type: text/html; charset=utf-8"
  echo
  ./vs3/vs3 "$1"
}

notfound() {
  echo "Status: 404"
  render 404.md
  exit 1
}

IFS=\; read -r -a cookies <<<"$HTTP_COOKIE"
for c in "${cookies[@]}"; do
  if [[ "${c%%=*}" = dark ]]; then
    echo "Set-Cookie: $c; Path=/; Max-Age=$((60*60*24*7*2))"
    dark="${c#*=}"
    break
  fi
done

[[ -n "$REDIRECT_URI" ]] && export PATH_INFO="$REQUEST_URI"
[[ -z "$PATH_INFO" ]] && notfound

# Don't allow relative paths. Prevents directory traversal
[[ "$PATH_INFO" = *../* ]] && notfound
[[ "$PATH_INFO" = */..* ]] && notfound

[[ -d "pages/$PATH_INFO" ]] && export PATH_INFO="$PATH_INFO/index"

src="pages/$PATH_INFO.md"
[[ -f "$src" ]] || notfound
render "$src"
