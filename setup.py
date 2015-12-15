from setuptools import setup


setup(name='Alfe',
      version='0.1.0',
      py_modules=['index'],
      description='extract comment tags from source files',
      author='cyluun',
      url='https://github.com/cyluun/code-butler',
      license='MIT',
      install_requires=[
          'Click'
          ],
      entry_points='''
        [console_scripts]
        alfe=index:cli
      ''',
      )
