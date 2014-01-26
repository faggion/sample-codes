from setuptools import setup, find_packages

setup(
    namespace_packages=['tanarky'],
    packages     = ['tanarky',
                    'tanarky.package'],
    package_dir  = {'':'src'},
    name         = 'tanarky.package',
    version      = '1.1.0',
    package_data = {
        'tanarky': [],
        },
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    tanarky_package = tanarky.package:Uploader.cli
    """
    )
