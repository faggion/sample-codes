from setuptools import setup, find_packages

setup(
    #include_package_data = True,
    packages     = find_packages('src'),  # include all packages under src
    package_dir  = {'':'src'},   # tell distutils packages are under src
    package_data = {
        'eventregist': ['templates/*.html'],
    },
    name     ='eventregist',
    version  = '1.0',

    #install_requires = ['distribute'],
    #packages = find_packages(),
    #package_dir = {'':''},
    #package_data={'eventregist': ['templates/*.html']},
    #package_data={'': ['templates/*.html']},
    #test_suite = 'unit_test_eventregist.EventRegistTestCase',
    )
