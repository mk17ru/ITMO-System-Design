# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys


# it's required to support imports in Sphinx generated .rst files
sys.path.append(os.path.abspath('../../'))
cli_path = os.path.abspath('../../cli')
sys.path.append(cli_path)

for root, dirs, files in os.walk(cli_path):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        sys.path.append(os.path.abspath(dir_path))

# Теперь все поддиректории внутри cli добавлены в sys.path

project = 'itmo-software-design'
copyright = '2024, Nikita Stepanov && Michael Frolov && Arseny Brothers [Arseny Vityazev && Arseny Schevchenko]'
author = 'Nikita Stepanov && Michael Frolov && Arseny Brothers [Arseny Vityazev && Arseny Schevchenko]'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'autodocsumm',
    'sphinx.ext.coverage',
    'sphinx_markdown_builder',
]
auto_doc_default_options = {'autosummary': True}

templates_path = ['_templates']
exclude_patterns = ['build/*']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
