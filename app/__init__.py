"""
This module initializes and runs the application.
"""

import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand


class App:
    """
    Main application class responsible for initialization and running the application.
    """

    def __init__(self):
        """
        Initialize the application.
        """
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        """
        Configure logging settings.
        """
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """
        Load environment variables.
        """
        settings = dict(os.environ.items())
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """
        Get a specific environment variable.

        Args:
            env_var (str): The name of the environment variable.

        Returns:
            str: The value of the environment variable, or None if not found.
        """
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """
        Load and register plugins.
        """
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning("Plugins directory '%s' not found.", plugins_path)
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error("Error importing plugin %s: %s", plugin_name, e)

    def register_plugin_commands(self, plugin_module, plugin_name):
        """
        Register commands from a plugin module.

        Args:
            plugin_module: The module object representing the plugin.
            plugin_name: The name of the plugin.
        """
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            try:
                if issubclass(item, Command):  # Check if it's a subclass of Command
                    self.command_handler.register_command(plugin_name, item())
                    logging.info("Command '%s' from plugin '%s' registered.",
                                 item.__name__, plugin_name)
            except TypeError:
                continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        """
        Start the application.
        """
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip().lower()
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:  # Assuming execute_command raises KeyError for unknown commands
                    logging.error("Unknown command: %s", cmd_input)
                    sys.exit(1)  # Use a non-zero exit code to indicate failure or incorrect command
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")


if __name__ == "__main__":
    app = App()
    app.start()
