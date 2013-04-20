from distutils.core import setup

setup(
    name='WikiRep',
    version='0.4.0',
    author='Roei Bar Aviv',
    author_email='rbaraviv@gmail.com',
    packages=['wikirep', 'wikirep.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/WikiRep/',
    license='LICENSE.txt',
    description='Python implementation of Semantic Intepreter',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy >= 1.6.0", "mwparserfromhell"
    ],
)


