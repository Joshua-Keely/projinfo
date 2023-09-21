# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Declaration of source root directories ----------------------------------
import os, sys
# List of directories to be added
sys.path.insert(0, os.path.abspath('../src/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'R5.04-ProjInf'
copyright = '2023, Keely'
author = 'Keely'
release = 'v0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'renku'
html_static_path = ['_static']

# -- Autodoc config -----------------------------------------------------------
autodoc_default_options = {
    "members": True, # Inclut toutes les entrées (fonctions, classes, méthodes) de la documentation
    "undoc-members": True, # même celle non documentées
    "special-members": True, # même les méthodes spéciales (__init__)
    "private-members": True, # même les entrées privées
    "member-order": "bysource", # par ordre de déclaration dans le code
}
# -- External Links --------------------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}