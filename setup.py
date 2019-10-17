import setuptools

setuptools.setup(
   name='radforest_pd',        # package name on PyPI
   version='0.1.0',
   description='A library to interact with forests... ',
   url='https://github.com/pabloderen/radforest',
   author='Pablo Derendinger',
   author_email='pderendinger@gmail.com',
   license='MIT',
   packages= setuptools.find_packages(exclude=['tests'])   # use find_packages instead
)