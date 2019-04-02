from setuptools import setup, find_packages

setup(
    name='vklabs.tika-python',
    version='0.0.1',
    python_requires='>=3.6',
    packages=find_packages(),
    package_data={},
    install_requires=[
        "setuptools"
        "requests"
        "python-coveralls"
        "pytest-cov==2.5"
    ],
    entry_points='''
    ''',
)
