from setuptools import setup, find_packages

setup(
    name="sonic-harm-registry",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.3",
        "pandas>=2.0",
        "PyYAML>=6.0",
        "jsonschema>=4.19",
    ],
    entry_points={
        "console_scripts": [
            "shr-server=src.app:main",
        ],
    },
    author="Sonic Harm Registry Team",
    description="Open taxonomy and reference system for sound-based rights violations",
    license="CC BY-NC 4.0",
)
