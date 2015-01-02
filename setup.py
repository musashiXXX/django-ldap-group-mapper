from setuptools import find_packages, setup

version = '0.1.2'
github_url = 'https://github.com/musashiXXX/django-ldap-group-mapper'
long_description = 'A simple LDAP group -> Django group mapper, for use with' \
                   + ' django-auth-ldap.'

setup(
  name = 'django-ldap-group-mapper',
  version = version,
  author = 'Charles Hamilton',
  author_email = 'musashi@nefaria.com',
  packages = find_packages(exclude = [
    '*.tests', '*.tests.*','tests.*','tests', 'ldap_groups_test_db']),
  url = github_url,
  download_url = '%s/tarball/%s' % (github_url, version),
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
