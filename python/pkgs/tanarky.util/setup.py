from setuptools import setup, find_packages

setup(
    namespace_packages=['tanarky'],
    packages     = ['tanarky',
                    'tanarky.util'],
    package_dir  = {'':'src'},
    name         = 'tanarky.util',
    version      = '1.0.0',
    package_data = {
        'tanarky': ['models/default.ini'],
        },
    )
