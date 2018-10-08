======
TOMLer
======

A simple reader for configuration file with TOML syntax.

Usage
-----
At first, import the module as follows

.. code-block::

    from tomler import Config

After that, you can call for the first time the configuration file as follows

.. code-block::

    config = Config('<path to the configuration file>', [True | False])

The second parameter is optional. It activates (or deactivates) the hot
reloading of the configuration file each time a value is accessed.

The Config class implements the singleton pattern.