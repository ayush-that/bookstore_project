from setuptools import setup, find_packages

setup(
    name="bookstore_project",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # Add your project's dependencies here
        # Example: 'requests>=2.23.0',
    ],
    entry_points={
        "console_scripts": [
            "bookstore=main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A bookstore management application",
    long_description=open("docs/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bookstore_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
