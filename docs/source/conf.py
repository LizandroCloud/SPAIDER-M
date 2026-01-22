# Configuration file for the Sphinx documentation builder.

# -- Project information
copyright = '2026, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output


html_theme = 'sphinx_rtd_theme'

html_logo = 'static/logo_v5.png'
html_static_path = ['static']
html_title = "SPAIDER"

def setup(app):
    app.add_css_file('custom.css')

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css",
]


# -- Options for EPUB output
epub_show_urls = 'footnote'
