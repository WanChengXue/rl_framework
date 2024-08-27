"""Python setup.py for rl_framework package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("rl_framework", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="rl_framework",
    version=read("rl_framework", "VERSION"),
    description="Awesome rl_framework created by WanChengXue",
    url="https://github.com/WanChengXue/rl_framework/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="WanChengXue",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["rl_framework = rl_framework.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
