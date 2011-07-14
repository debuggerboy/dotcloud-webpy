This code shows how to run a minimalistic `web.py <http://webpy.org/>`_
application on `DotCloud <http://www.dotcloud.com/>`_.

To run this code on DotCloud, you need to `get a DotCloud account
<https://www.dotcloud.com/accounts/register/>`_. DotCloud has a free tier,
so you won't even need to draw your wallet!

Then clone this repository::

  $ git clone git://github.com/stackomatic/webpy.git

And push it to DotCloud::

  $ cd webpy
  $ dotcloud push webpy

Happy hacking! Remember: each time you modify something, you need to
git add + git commit your changes before doing "dotcloud push".

Would You Like To Know More? Have a look at the `DotCloud documentations 
<http://docs.dotcloud.com/>`_, especially the one for the `Python service
<http://docs.dotcloud.com/services/python/>`_ which is used by this app.
