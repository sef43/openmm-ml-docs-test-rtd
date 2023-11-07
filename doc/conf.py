# -*- coding: utf-8 -*-

import os
import sys

import openmmml

sys.path.append(os.path.abspath('../'))

import pkg_resources
version = pkg_resources.require("openmmml")[0].version
release = version


if os.getenv("PAGES_DEPLOY_PATH"):
    on_gh_actions=True
    print(on_gh_actions)
else:
    on_gh_actions=False

if on_gh_actions:
    version_match = os.getenv("PAGES_DEPLOY_PATH","dev").lstrip("refs/tags/")

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # "process-docstring",
    'm2r2'
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "member-order": "bysource",
}

source_suffix = ".rst"
master_doc = "index"

project = u"OpenMM ML"
copyright = u"2023, Stanford University and the Authors"


exclude_patterns = ["_build", "_templates"]
html_static_path = ["_static"]
templates_path = ["_templates"]

pygments_style = "sphinx"

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "logo": {
        "text": "OpenMM-ML docs",
        "image_light": "_static/logo.png",
        "image_dark": "_static/logo.png",
    },

    "external_links": [
      {"name": "OpenMM.org", "url": "https://openmm.org/"},
      {"name": "OpenMM docs", "url": "https://openmm.org/documentation"},
      {"name": "GitHub", "url": "https://github.com/openmm"}
    ],

    "github_url": "https://github.com/openmm/openmm-ml"
}

if on_gh_actions:
    # settings for version switcher and warning
    html_theme_options["navbar_start"]=["navbar-logo", "version-switcher"]
    html_theme_options["switcher"]= {
            "json_url": "https://sef43.github.io/openmm-ml/versions.json",
            "version_match": version_match,
        }
    html_theme_options["show_version_warning_banner"]=True
    html_theme_options["check_switcher"]=True


# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
