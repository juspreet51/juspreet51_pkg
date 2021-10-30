import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="juspreet51",
    version="0.0.8001",
    author="Jaspreet Singh",
    author_email="contact@juspreet51.in",
    description="An EDA & modellling assist library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juspreet51/juspreet51_pkg",
    project_urls={
        "Bug Tracker": "https://github.com/juspreet51/juspreet51_pkg",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires = ["numpy","matplotlib","pandas", "seaborn", "plotly"],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)