Improving the usability of launchpadlib-using code
#parser reST

Normally when you write some code using launchpadlib you end up with Launchpad
showing your users something like this:

.. image:: /images/lplib-before.png

This isn't great, how is the user supposed to know which option to click? What
do you do if they don't choose the option you want?

Instead it's possible to limit the choices that the user has to make to only
those that your application can use, plus the option to deny all access, by
changing the way you create your Launchpad object.

::

  from launchpadlib.launchpad import Launchpad

  lp = Launchpad.get_token_and_login("testing", allow_access_levels=["WRITE_PUBLIC"])

This will present your users with something like this:

.. image:: /images/lplib-after.png

which is easier to understand. There could be further improvements, but they would
happen on the Launchpad side.

This approach works for both Launchpad.get_token_and_login and Launchpad.login_with.

The values that you can pass here aren't documented, and should probably be constants
in launchpadlib, rather than hardcoded in every application, but for now you can
use:

- READ_PUBLIC
- READ_PRIVATE
- WRITE_PUBLIC
- WRITE_PRIVATE

