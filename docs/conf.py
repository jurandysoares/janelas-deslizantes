# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Protocolos de Janela Deslizante'
copyright = '2026, Jurandy Soares'
author = 'Jurandy Soares'
release = '2026'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
]

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['index.md']

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = html_short_title = project

myst_fence_as_directive = ["mermaid"]

# Força o formato de saída para PNG
mermaid_output_format = 'png'

latex_documents = [
    (master_doc, 
     'Protocolos_de_Janela_Deslizante.tex', 
     'Protocolos de Janela Deslizante', 
     'Prof. Me. Jurandy Soares',
     'manual'),
]
latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
}
latex_show_urls = 'footnote'

