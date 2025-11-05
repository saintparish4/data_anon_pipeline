from setuptools import setup, find_packages

setup(
    name="data_anon_pipeline",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "spacy",
    ],
    python_requires=">=3.8",
)

