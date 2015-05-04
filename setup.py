from setuptools import setup

setup(
    name='behave-teamcity',
    version="0.1.23",
    packages=['behave_teamcity', ],
    url='https://github.com/iljabauer/behave-teamcity',
    download_url='https://github.com/iljabauer/behave-teamcity/releases/tag/0.1.23',
    license='MIT',
    author='Ilja Bauer',
    author_email='i.bauer@cuescience.de',
    description='TeamCity test report formatter for behave',
    install_requires=["behave>=1.2.5,<=1.3", "teamcity-messages"],
    keywords=['testing', 'behave', 'teamcity', 'formatter', 'report'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities"
    ],
)
