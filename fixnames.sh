for pg in pagina-*.md; do
    titulo="$(head -1 $pg | sed 's/^# //')"
    slug=$(slugify "$titulo")
    echo "- [${titulo}](${slug}.md)"
    git mv "$pg" "${slug}.md"
done