import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='so',
    version='1.0',
    scripts=['so'],
    author="Ajeet Khan",
    author_email="i.ajeetkhan@gmail.com",
    description="A package to check system related metrics and values for simpler blackbox monitoring",
    long_description="A package that can help to do blackbox monitoring by providing metrics related to system-overview,IOPS,Disks,Memory,CPU etc using a single command.",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Linux Based",
    ],
    )