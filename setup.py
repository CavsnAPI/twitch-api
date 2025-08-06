from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="twitch-api-client",
    version="1.0.0",
    author="cavsn api",
    author_email="contactcavsn@gmail.com",
    description="A Python client library for the Twitch API available on RapidAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cavsn/twitch-api-client",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",   
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    keywords="twitch api client rapidapi streaming gaming",
    project_urls={
        "Bug Reports": "https://github.com/cavsn/twitch-api-client/issues",
        "Source": "https://github.com/cavsn/twitch-api-client",
        "RapidAPI": "https://rapidapi.com/cavsn/api/twitch-api8",
    },
) 