import os
from setuptools import setup, find_packages

version = '1.1.1'
if "GITHUB_REF" in os.environ:
    version = os.environ("GITHUB_REF").split("/")[-1]

setup(
  name = 'metadata_service',
  version = 'version',
  license='Apache License 2.0',
  description = 'Metadata Service: backend service for Metaflow',
  author = 'Machine Learning Infrastructure Team at Netflix',
  author_email = 'help@metaflow.org',
  url = 'https://github.com/Netflix/metaflow-service',
  keywords = ['metaflow', 'machinelearning', 'ml'],
  py_modules=['metadata_service'],
  packages=find_packages(),
  entry_points='''
        [console_scripts]
        metadata_service=metadata_service.server:main
   ''',
  install_requires=[
          'aiohttp',
          'aiohttp_swagger',
          'psycopg2',
          'aiopg',
          'boto3',

      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.7',
  ],
)
