# Standard
import os

# Vendor
import toml
from singleton_decorator import singleton


@singleton
class Config:

    def __init__(self, path: str, activate_hot_reload_of_the_configuration_file: bool = False):
        """
        Class constructor.
        :param str path: The path of the configuration file
        :param boolean activate_hot_reload_of_the_configuration_file: Indicates whether the hot reloading of
            the configuration file is active or not.
        """
        assert isinstance(path, str), "The variable 'path' must be a string value."
        assert isinstance(activate_hot_reload_of_the_configuration_file, bool), \
            "The variable 'activate_hot_reload_of_the_configuration_file' must be a boolean value."

        if os.path.exists(path):
            self._path = path
            self._configuration_file_instance = toml.load(path)
            self._hot_reload_of_the_configuration_file = activate_hot_reload_of_the_configuration_file
        else:
            raise FileNotFoundError("The configuration file does not exist.")

    def __getitem__(self, value_path: str) -> any:
        """
        Get a value that belongs to the configuration file.
        :param str value_path: The path of the value inside the configuration file.
        :return any: If the value_path exists returns the
        """
        assert isinstance(value_path, str), "The variable 'value_path' must be a string."

        if self._is_hot_reload_active():
            self._reload_configuration_file()

        keys_in_path = value_path.split('/')

        return self._find_value(keys_in_path, self._configuration_file_instance)

    def _find_value(self, keys_in_path: list, starting_value: dict) -> any:
        """
        Find the searched value, represented by the list of the keys, inside
        the configuration.
        :param keys_in_path: The list of the keys to use to access the value.
        :param starting_value: The starting level of the configuration file.
        :return: The value associated to the list of the keys, None if the list
        of the keys leads to nothing or contains keys that not exist.
        """
        current_value = starting_value
        for key_in_path in keys_in_path:
            if self._key_exists(key_in_path, current_value):
                current_value = current_value[key_in_path]
            else:
                return None
        return current_value

    def _is_hot_reload_active(self) -> bool:
        return self._hot_reload_of_the_configuration_file

    def _key_exists(self, key: str, current_accessed_configuration: dict) -> bool:
        """
        Check if the current key exists inside the current accessed level
        of the configuration file.
        :param key: The key to check.
        :param dict current_accessed_configuration: The current level of the configuration file.
        :return: True if the key exists, False otherwise
        """
        return key in current_accessed_configuration.keys()

    def _reload_configuration_file(self) -> None:
        self._configuration_file_instance = toml.load(self._path)
