from setuptools import setup, find_packages

with open("requirements/req.txt") as f:
 required = f.read().splitlines()

setup(
    version = "0.0.1",
    packages=find_packages(where='src', exclude=["tests*"]),
    install_requires=required,
    name="myPkg",
    author="I am",
    author_email="",
    description="library for static functions",
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.7",
    package_dir={"": "src"},
    include_package_data = True
)