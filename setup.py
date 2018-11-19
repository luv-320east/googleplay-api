from setuptools import setup

setup(name='gpapi',
      version='0.5.1',
      description='Unofficial Google Play API in Python',
      url='https://github.com/luv-320east/googleplay-api',
      author='LUV',
      author_email='luv@abox42',
      license='MIT',
      packages=['gpapi'],
      package_data={'gpapi': ['device.properties']},
      install_requires=['cryptography>=2.4.1',
                        'protobuf>=3.6.1',
                        'requests'])
