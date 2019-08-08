from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    readme = f.read()

about = {}
with open(path.join(here, "papi", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

packages = ["papi"]
requirements = ["webob>=1.8", "parse>=1.12", "unicorn>=19.9"]
test_requirements = ["pytest>=5.0"]

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=packages,
    python_requires=">=3.5",
    install_requires=requirements,
    license=about["__license__"],
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=about["__keywords"],
    project_urls={
        "Bug Reports": "https://github.com/joshfinnie/papi/issues",
        "Source": "https://github.com/joshfinnie/papi/",
    },
)
