from setuptools import setup, find_packages


setup(
    name="dundie",
    version="0.1.0",
    description="Rewards Point System for Dunder Mifflin",
    author="Marcelo de Moura",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts":[
            "dundie = dundie.__main__:main"
        ],
    },

)
