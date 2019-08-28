import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compose-to-manifest",
    version="0.0.8",
    author="typeli",
    author_email="juncli@outlook.com",
    description="Convert Docker Compose project to Azure IoT Edge deployment manifest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VSChina/compose-to-manifest",
    packages=setuptools.find_packages(),
    python_requires='>=3.6.0',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": ["compose-to-manifest=convertor.convertor:main"],
    },
    install_requires=[
        "docker-compose==1.24.0",
    ],
)
