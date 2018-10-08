======
TOMLer
======

A simple reader for configuration file with TOML syntax.

Usage
-----
This modules implements the Singleton pattern. Hence, after the first call of the class,
the the module can be accessed simply recalling it.

At first, import the module as follows

.. code-block::

    from tomler import Config

After that, you can call for the first time the configuration file as follows

.. code-block::

    config = Config('<path to the configuration file>', [True | False])

The second parameter is optional. It activates (or deactivates) the hot
reloading of the configuration file each time a value is accessed.