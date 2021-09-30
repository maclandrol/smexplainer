from setuptools import setup
from setuptools import find_packages

# Sync the env.yml file here
install_requires = ["datamol", "requests-toolbelt"]

setup(
    name="smexplainer",
    version="0.0.2",
    author="Emmanuel Noutahi",
    author_email="emmanuel.noutahi@gmail.com",
    description="A python library to explains molecular patterns (SMARTS)",
    url="https://github.com/maclandrol/smexplainer",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
