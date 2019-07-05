from setuptools import setup

setup(
      name='pyex',
      version='0.1',
      description='Example python program',
      url='https://github.com/ashwinmr/py_example',
      author='Ashwin Rao',
      author_email='iashwinrao@gmail.com',
      license='MIT',
      packages=['pyex'],
      include_package_data=True,
      entry_points = {
            'console_scripts': ['pyex = pyex.pyex:main']
      },
      zip_safe=False
)
