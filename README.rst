pypersonalassistant
===================

Easy, secure self notification via email and sms, using smtplib and twilio

Using pycrypto AES, personal credentials such as passwords and tokens are encrypted and persistently stored, to allow later automatic use without a user present. User authentication with a master password is required at object initialisation each time

Installation
------------

.. code-block:: python

    pip install pypersonalassistant

`PyCrypto`_ needs to be compiled during installation; if this is a problem,
install a prebuilt binary.

.. _PyCrypto: https://www.dlitz.net/software/pycrypto/

Usage
-----

Import to your project
^^^^^^^^^^^^^^^^^^^^^^

::

    import pypersonalassistant.secure
    
    ppa_secure = import pypersonalassistant.secure.secure()

On calling the ``secure()`` object, the user will be prompted for the master password.

If no password is found stored, the input will be hashed for future use and first-time setup will be performed.

By calling the ``secure()`` object at the beginning of the script, validation is already carried out, and secure can be called later at any time::

    results = some_long_task()
    ppa_secure.SMS_me('Task completed')
    ppa_secure.email_me('Subject: Task completed\n{0}'.format(results))

The email functions can also take an ```email.message.Message``` object and handle it correctly::

    import pypersonalassistant.secure
    import email.mime.text

    ppa_secure = import pypersonalassistant.secure.secure()
    MIMEemail = email.mime.text.MIMEText('This string will be converted to MIME format')
    ppa_secure.email('my.name@company.com', MIMEemail)
    ppa_secure.SMS('+44XXXXXXXXXX', 'The results are in your inbox')

More info can can be found in the reference on `readthedocs`_

.. _readthedocs: http://pypersonalassisstant.readthedocs.org/en/latest/reference/helpers.html)

Run from the command line
^^^^^^^^^^^^^^^^^^^^^^^^^

First time setup or editing of credentials can be done from the command-line with ``pypersonalassistant-credentials``. Raise the ``-h`` flag for arguments.
::

    pypersonalassistant-credentials
    >>> Password for pypersonalassistant module (hidden):
    >>> Starting new credentials file: credentials.json

The script will then prompt the user to input credentials. All credentials are optional, but leaving some blank may cause errors during execution.

All phone numbers should be entered complete with international dialling code (e.g. ``+44XXXXXXXXXX``).

Development
-----------

Additional development requirements can be installed using ``pip install -r requirements_dev.txt``

Documentation is built using sphinx::
    
    cd docs
    sphinx-build . ./_build