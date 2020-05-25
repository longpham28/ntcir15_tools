import setuptools
package_data = {
    "": ["baselines/baselines.pbz2"]
}
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ntcir15_tools-longpham",
    version="0.0.1",
    author="longpham",
    author_email="huulongpham28@gmail.com",
    description="Tools package for ntcir15-datasearch",
    long_description=long_description,
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    install_requires=["pyNTCIREVAL", "numpy"],
    package_data=package_data
)
