import setuptools

with open("README.md","r",encoding="utf-8") as file:
    long_description = file.read()

__version__ = "0.0.0"
Repo_name = "Kidney-disease_classificationMLOpsCICD"
Author_user_name = "rushit2608"
src_repo = "kidneyDiseaseClassfier"
author_email = "rushisa123@gmail.com"

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=Author_user_name,
    author_email=author_email,
    description="A small python package for cnn app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_user_name}/{Repo_name}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")  

)