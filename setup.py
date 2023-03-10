from setuptools import find_packages, setup

setup(
    name="loadero-py-testui-commands",
    author="Loadero",
    author_email="support@loadero.com",
    version="1.0.0",
    url="https://loadero.com",
    packages=find_packages(),
    install_requires=[
        "python_testui",
    ],
    python_requires=">=3.6",
)
