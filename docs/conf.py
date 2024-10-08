project = "mypackage"
author = "John T. Wodder II"
copyright = "2024 John T. Wodder II"  # noqa: A001

extensions = [
    "autoclasstoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

exclude_patterns = ["_build"]
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
version = "0.0.0"
release = "0.0.0"
today_fmt = "%Y %b %d"
default_role = "py:obj"
pygments_style = "sphinx"

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "prev_next_buttons_location": "both",
}
html_last_updated_fmt = "%Y %b %d"
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
