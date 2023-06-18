import setuptools

LONG_DESC = open("README.md").read()
VERSION = '0.1.0'
DOWNLOAD = "https://github.com/png261/meoww/archive/%s.tar.gz" % VERSION

setuptools.setup(
    name="meoww",
    version=VERSION,
    author="Phuong Nguyen",
    author_email="nhphuong.code@gmail.com",
    description="Meoww meoww meoww",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    keywords="meoww",
    license="MIT",
    url="https://github.com/png261/meoww",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["meoww"],
    entry_points={"console_scripts": ["meoww=meoww.__main__:main"]},
    python_requires=">=3.5",
    install_requires=[
        "pygame>=2.4.0",
    ],
    include_package_data=True,
    zip_safe=False,
)

