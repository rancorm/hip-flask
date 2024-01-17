from setuptools import setup

setup(
    name="hip_flask",
    version="0.1",
    packages=["hip_flask"],
    install_requires=[
        "Flask",
        # Add other dependencies here
    ],
    author="Jonathan Cormier",
    description="Lightweight Flask extension to simplify the integration of CSS and JavaScript files into your applications",
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python :: 3",
    ],
)
