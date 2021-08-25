from setuptools import setup

setup(
    name = "SimpleTranslate",
    version = "1.0.0",
    url = "https://github.com/PrestoSole/SimpleTranslate",

    license = "AGPLv3",
    keywords = "translation",
    packages = ["SimpleTranslate"],
    install_requires = [
        "lxml",
        "requests"
    ]
)
