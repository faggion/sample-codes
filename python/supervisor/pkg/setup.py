from setuptools import setup, find_packages

setup(
    namespace_packages=['tanarky'],
    packages     = ['tanarky',
                    'tanarky.examples'],
    package_dir  = {'':'src'},
    name         = 'tanarky.examples',
    version      = '2.0',
    package_data = {
        'tanarky': ['examples/settings.ini']
        }
    )
