from setuptools import setup

version = '0.1.2'

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pypersonalassistant',
      version=version,
      description='Easy, secure self notification via email and sms, using smtplib and twilio',
      long_description=readme(),
      url='https://github.com/tommilligan/pypersonalassisstant',
      author='Tom Milligan',
      author_email='code@tommilligan.net',
      license='GPL',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
      ],
      keywords='personal automation automatic notification email sms text secure',
      packages=['pypersonalassistant'],
      install_requires=[
          'pycrypto',
          'twilio',
      ],
      entry_points={
        'console_scripts': [
            'pypersonalassistant-credentials = pypersonalassistant.ppa_secure:main'
        ]
      }
)