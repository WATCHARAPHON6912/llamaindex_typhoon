from setuptools import setup, find_packages

setup(
    name="llamaindex_typhoon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "llama_index",
    ],
    entry_points={
        "console_scripts": [
            "typhoon=llamaindex_typhoon.typhoon:main",
        ],
    },
)
