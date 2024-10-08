This is an MVCE for a bug in
[autoclasstoc](https://github.com/kalekundert/autoclasstoc/issues).  When using
the extension with Sphinx 7.4.0 or higher (including Sphinx 8.0.2, the current
version at time of writing), warnings of the following form are emitted despite
the documented code not referring to the current module:

```
WARNING: Summarised items should not include the current module. Replace 'mypackage.Foo.__init__' with '__init__'. [autosummary.import_cycle]
```

To run this MVCE, install [tox](http://tox.readthedocs.org) and run `tox -e
docs`.
