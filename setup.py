from setuptools import setup, find_packages

setup(
    name="djv_cli",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points="""
        [console_scripts]
        djv=djv_cli_tool:cli
    """,
)
