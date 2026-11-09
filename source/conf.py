# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MY Research Documentation'
copyright = '2026, Meng YIN'
author = 'Meng YIN'
release = '20261106_v0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # This allows you to write documentation in Markdown format (.md) rather than only reStructuredText (.rst).   
]

templates_path = ['_templates']
exclude_patterns = []
root_doc = 'index'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
