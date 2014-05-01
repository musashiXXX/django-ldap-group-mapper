from setuptools import find_packages, setup

long_description = 'A simple LDAP group -> Django group mapper, for use with' \
                   + ' django-auth-ldap.'

setup(
  name = 'django-ldap-groups',
  version = '0.1.0',
  author = 'Charles Hamilton',
  author_email = 'musashi@nefaria.com',
  packages = find_packages(exclude = [
    '*.tests', '*.tests.*','tests.*','tests']),
  url = 'https://github.com/musashiXXX/django-ldap-groups',
  download_url = 'https://github.com/musashiXXX/django-ldap-groups/tarball/0.1.0',
  keywords = ['django-auth-ldap', 'django', 'ldap'],
  license = 'LICENSE.txt',
  description = 'Django LDAP Group Mapper',
  long_description = long_description,
  zip_safe = False,
  install_requires = [
    'django-auth-ldap >= 1.2.0',
    'python-ldap >= 2.0',
    'Django >= 1.3']
)
