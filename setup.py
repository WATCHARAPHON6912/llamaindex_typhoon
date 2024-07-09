from setuptools import setup, find_packages

setup(
    name="llamaindex_typhoon",
    version="0.0.2",
    # description="A Modbus communication module for Film69 devices",
    py_modules=["typhoon"],  # ต้องตรงกับชื่อไฟล์ Modbus_Film69.py
    install_requires=[
        "llama-index",
    ],
    entry_points={
        'console_scripts': [
            'llamaindex_typhoon=llamaindex_typhoon:typhoon',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
