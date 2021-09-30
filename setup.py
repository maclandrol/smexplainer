from setuptools import setup
from setuptools import find_packages

# Sync the env.yml file here
install_requires = ["datamol", "requests-toolbelt"]

setup(
    name="smexplainer",
    version="0.0.1",
    author="Emmanuel Noutahi",
    description="A python library to work with molecules. Built on top of RDKit.",
    python_requires=">=3.7",
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
)
