# Janelas deslizantes

<https://jurandysoares.github.io/janelas-deslizantes/>


## Geração da documentação

Antes de gerar a documentação em qualquer formato, instale o uv (Google: [uv install](https://www.google.com/search?q=uv+install)).

Com o comando `uv` instalado, e o projeto clonado, entre no diretório do projeto e execute o comando de acordo com o formato desejado.

1. HTML: `uv run make html`
2. PDF: `uv run make latexpdf`
3. DOCX: 
   1. `uv run make singlehtml`
   2. `cd build/singlehtml`
   3. `pandoc -f html -t docx -s ./index.html -o ./protocolos-janela-deslizante.docx`

