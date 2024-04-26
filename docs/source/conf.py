# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '常夜国骑士谭RPG'
copyright = '2016, 神谷涼／インコグ・ラボ'
author = '常夜国真祖信仰正统華语社团'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
    'recommonmark',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

html_static_path = ["_drac"]
html_css_files = ["drac-style.css"]
html_js_files = ["drac-script.js"]

# -- Options for HTMLHelp output
htmlhelp_basename = '常夜国骑士谭RPG 资源整合'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for PDF output
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']