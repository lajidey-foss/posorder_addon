from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in posorder_addon/__init__.py
from posorder_addon import __version__ as version

setup(
	name="posorder_addon",
	version=version,
	description="Creating Sales Invoice Order helper",
	author="Jide Olayinka",
	author_email="olajamesjide@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
