import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaiby",
    version="0.1.0",
    author="Neopad",
    author_email="neopad.azienda@gmail.com",
    description="Create your own AI algorithm for processing files and post data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neopadAI/kaiby",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
