Running the demo
================

* You must have an LDAP server.
* It is recommended that you use OpenLDAP for the demo, unless you have a spare,
  non-production Active Directory server that you can use for testing purposes.
* It is recommended that you use (i.e., import) the included ``Example_LDIFs/openldap.ldif``.
  At this time, this package does not include an LDIF for Microsoft Active Directory (AD), but
  you may be able to modify and import the aforementioned LDIF. 
* *This* package does not have to be installed in order for the demo to run however,
  any requirements still need to be installed or available via ``PYTHONPATH``.
  See ``requirements.txt`` for more details.


Installing and configuring OpenLDAP is beyond the scope of this document, but the
basics are as follows:

1.  Make sure the following line appears in ``/etc/hosts``, change ``myhostname``
    to the hostname of the OpenLDAP server:

        127.0.1.1   myhostname.example.local myhostname

    You can change or remove this line after you've installed OpenLDAP.

2. Install OpenLDAP. On debian variants you'll run the following command:

        sudo apt-get install slapd slapd-utils

    You should be prompted to set an Administrator password.

3.  Either manually populate the database, or import the included LDIF. If you
    choose to do the latter, the command is as follows:

        ldapadd -x -D cn=admin,dc=example,dc=local -W -f Example_LDIFs/openldap.ldif

    You will be prompted for the password that you set in step #2.

4.  This step is optional, but before running the demo, attempt to connect to your 
    LDAP directory with an "LDAP explorer" such as [JXplorer](http://jxplorer.org/).
    The "connect" dialog in JXplorer will prompt you for the following settings:

    * Host: ``localhost``
    * Port: ``389``
    * Base DN: ``dc=example,dc=local``
    * Level: ``User + Password``
    * User DN: ``cn=admin,dc=example,dc=local``
    * Password: _the password you set in step #2_


That should be sufficient to get you started.

After you've imported the example ldif that is appropriate for your LDAP server
(again, at this time there is only one included in this package), you will have
three users in your LDAP directory -- appadmin, appuser, lbind -- each with the
password of ``password``. 

Next, take a look at ``settings.py``. You'll notice that it is a minimal config,
containing just the required options to run tests and/or the demo. If you look
at the last few lines, you'll see the option to import the LDAP config for either
OpenLDAP or AD. OpenLDAP is uncommented by default.

If you are using OpenLDAP, and you've imported ``Example_LDIFs/openldap.ldif``,
then you can probably just run the demo like so: `` ./rundemo.sh``. However, if
you intend to run the demo against an AD server, you might need to modify both
the common configuration: ``common_config.py`` and the Active Directory specific
configuration: ``msad_config.py``. Both of these files can be found in the
``tests/Example_LDAP_Configs`` directory. 

The reason the two configurations are separate is to highlight the differences
between them. In future releases, I intend to include more examples, along with
an LDIF that you can import into AD.

Once you are ready to run the demo, simply run the script ``rundemo.sh``. It will
automatically load the required fixtures, which include the mapping between the
LDAP groups: ``App Admins``, ``App Users`` to the Django groups: ``Admins``,
``Users``; respectively. On first run, Django will prompt you to create a superuser
account as well.

Verify that the demo is working by browsing to the admin url, by default this will
be: ``http://localhost:8000/admin``, and logging in with the username: ``appadmin``
and the password: ``password``. You should be redirected to the admin interface's
home page. Log out. Then, attempt to login with the username: ``appuser`` and the
password: ``password``. You should _not_ be able to login. Change the password to
the ``appadmin`` user from within your LDAP directory; then try to login to the
Django admin with the new password. You _should_ be able to login.


