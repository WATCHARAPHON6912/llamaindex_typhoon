from setuptools import setup, find_packages

setup(
    name="llamaindex_typhoon",
    version="0.0.3",
    description="A Modbus communication module for Film69 devices",
    py_modules=["typhoon"],  # Must match the filename 'typhoon.py'
    install_requires=[
        "llama-index",
    ],
    entry_points={
        'console_scripts': [
            'llamaindex_typhoon=typhoon:main',  # Ensure it calls the 'main' function from typhoon.py
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
