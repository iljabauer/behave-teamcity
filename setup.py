from setuptools import setup

setup(
    name='behave-teamcity',
    version="0.1.23",
    packages=['behave_teamcity', ],
    url='https://github.com/iljabauer/behave-teamcity',
    license='MIT',
    author='Ilja Bauer',
    author_email='i.bauer@cuescience.de',
    description='TeamCity test report formatter for behave',
    install_requires=["behave>=1.2.5,<=1.3", "teamcity-messages"]
)
