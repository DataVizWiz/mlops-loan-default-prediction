from setuptools import setup, find_packages

setup(
    name="mlops-loan-default-predictions",
    version="0.1.0",
    author="Metin Alisho",
    author_email="",
    description="The deployment and productionization of predicting loan defaults",
    packages=find_packages(),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
