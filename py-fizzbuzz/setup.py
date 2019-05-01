from setuptools import setup, find_packages


setup(
    name='py-fizzbuzz',
    version='0.0.1',
    url='https://github.com/erwagasore/rust-for-pysta',
    description='Fizz Buzz Game',
    license='Simplified BSD',
    package=find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={
        'dev': [
            'pytest==4.4.1',
            'pytest-cov==2.6.1',
            'pytest-flake8==1.0.4'
        ]
    },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Command-line Application',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
