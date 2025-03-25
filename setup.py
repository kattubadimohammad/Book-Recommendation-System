from setuptools import setup, find_packages

## Readme File Handling:
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "K Mohammad"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy', 'pandas', 'scikit-learn']

## Setup Function:

setup(
    name=REPO_NAME,  # Changed to REPO_NAME for consistency
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",  # Corrected description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="miraclemohammad786@gmail.com",
    packages=find_packages(),  # Use find_packages()
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="book recommendation system machine learning streamlit",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
)
