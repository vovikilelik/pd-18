from flask import Flask

from .utils import is_callable, get_key


class FlaskApp:

    def __init__(self, import_name, **args):
        self._application = Flask(import_name, **args)
        self._modules = {}

    def set_config(self, **args):
        for key, value in args.items():
            self._application.config[key] = value

        return self

    def _register_module(self, key, module):
        if key in self._modules:
            raise RuntimeError(f'Module {key} has already defined')

        self._modules[key] = module

    def add_module(self, context, name: str = None):
        key = name if name else type(context).__name__
        self._register_module(
            key,
            context.init(self, **self._modules)
        )

        return self

    def add_callable(self, executable, name: str):
        if is_callable(executable):
            self._register_module(
                name,
                executable(self, **self._modules)
            )
        else:
            raise TypeError(f'{type(executable)} has no executable context')

        return self

    def get_module(self, name_or_type):
        return self._modules[get_key(name_or_type)]

    @property
    def current(self) -> Flask:
        return self._application
