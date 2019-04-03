from setuptools import setup, find_packages

setup(
    name='vklabs.tika',
    version='0.0.4',
    python_requires='>=3.6',
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'requests'
    ],
    entry_points='''
    ''',
)
