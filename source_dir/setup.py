from setuptools import setup


def readme():
	with open('README.md') as f:
		return f.read()


setup(name='myDemo',
	version='0.0.1',
	description='Demo Project',
	long_description=readme(),
	long_description_content_type='text/markdown',
	classifers=[
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent'
	],
	url='https://github.com/jasmalTK/pythonPackage.git',
	author='',
	author_email='',
	keywords='core package',
	license='MIT',
	packages=['myDemo'],
	install_requires=[],
	include_package_data=True,
	zip_safe=False)