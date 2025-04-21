from setuptools import setup, find_packages

setup(
    name="excel_comparator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'streamlit>=1.22.0',
        'pandas>=1.5.0',
        'openpyxl>=3.0.0',
        'xlsxwriter>=3.0.0'
    ],
    entry_points={
        'console_scripts': [
            'excel-compare=excel_comparator.cli:main',
        ],
    },
    python_requires='>=3.8',
)