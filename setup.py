import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MyGTY",
    version="0.0.1",
    author="Luís Flávio Ferrante Marcos",
    author_email="luisflaviomarcos@outlook.com",
    description="My Greatest Tools Yet: a mighty package to deal with day to day tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luislffm/MyGTY",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)