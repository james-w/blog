Command support in bzr-builder
#parser reST

I've just implemented the most requested feature in bzr-builder
(Hi `Ted`_), command support.

.. _Ted: http://gould.cx/ted/blog

Sometimes you need to run a particular command to prepare a branch
of your project for packaging (e.g. autoreconf). I think this should
generally go in your build target, but not everyone agrees, and
sometimes there is just no other way.

Therefore I added a new instruction to bzr-builder recipes, "run".
If you put

..

  run some command here

in your recipe then it will run "some command here" at that point
when assembling.

Note that running commands that require arbitrary network access
is still to be discouraged, as you don't know in what environment
someone may assemble the recipe. I'd also advise against using
commands unless you really need them, but that's obviously your
call.
