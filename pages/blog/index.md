$$$
title=Blog
$$$
# Blog Posts

$$$
posts=()
for post in pages/blog/posts/*.md; do
  post="${post#pages/}"
  post="${post%.md}"
  posts[${#posts[@]}]="[${post##*/}]($post)"
done
$$$
$> printf -- '- %s\n\n' "${posts[@]}"
