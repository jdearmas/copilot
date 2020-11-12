# setup.py: a build script for setuptools
import setuptools

with open("README.wiki", "r") as h:
    long_description = fh.read()

setuptools.setup(
        name="copilot-jdearmas",
        version="0.0.1",
        author="John De Armas",
        author_email="var.mail.john@gmail.com",
        description="copilot helps you understand and manage an Apache HTTP server.",
        url="https://github.com/jdearmas/copilot",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPL License",
            "Operating System :: OS Independent",
            ],
        python_requires='>=3.6',
        )
