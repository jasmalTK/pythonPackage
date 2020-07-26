from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()


setup_args = dict(
    name='jasmal-test-pypi',
    version='0.0.2',
    description='Useful tools to work with test',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Sabeel K M',
    author_email='jasmaljaizz@gmail.com',
    keywords=['test', 'testpypi', 'testSearch'],
    url='https://github.com/jasmalTK/pythonPackage',
    download_url='https://pypi.org/project/jasmal-test-pypi/'
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
