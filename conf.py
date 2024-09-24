# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Blue Brain Open Platform - Documents'
copyright = 'Blue Brain Open Platform'
author = 'Blue Brain Open Platform'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
# source_suffix = ['.md']
templates_path = ['_templates']
exclude_patterns = ['.vscode', '_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "resources/obp_logo.drawio.svg"
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "BlueBrain", # Username
    "github_repo": "platform-docs", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/", # Path in the checkout to the docs root
}