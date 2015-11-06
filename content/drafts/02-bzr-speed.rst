Bazaar's speed of operation
#parser reST

There are many articles comparing the current crop of distributed version
control systems. This doesn't usually deal with actually working with the
systems for a period of time, and usually deals with the speed of operation.

I personally use Bazaar for most of my stuff, and this doesn't do to well 
in most of the speed comparisons. There are a few reasons for this, the main
being that the testers normally are not familiar with Bazaar, and so use
te naive methods of doing things, and those are the most inefficient. This
is partly Bazaar's fault for making that non-obvious. The aim of this post
is to show what you can do if you use the more sophisticated ways of doing
things. You will need the 0.14 release to use some of these things.

I am going to use the post at <http://weblogs.mozillazine.org/jst/archives/2007/02/more_on_distributed_vcs_perfor.html>
for my subject. It uses the Mozilla tree, that is one of the largest
open-source trees there is, so it really tests the system. I don't know hg,
so I will assume that the methods used there are good (and anyway the
speed is impressive, so it probably can't be improved on massively).

So I checked out the entire mozilla tree from CVS (just over 3 minutes 29 
seconds for reference), and blew away the CVS dirs. I then did ``init`` to
create a branch (0.42 seconds), and ``add` to add all the files (I used
``--quiet``), which took 44.24 seconds. This is slow, but that number of files
are going to be added very rarely. Also in a version soon (it might make 0.15)
is dirstate, which is a new working tree format that will enable commands that
manipulate the working tree, like add, to go a lot quicker. That will also
speed up branching, as that normally has to create a working tree. However
that's the future, and we are dealing with the current. 

The next thing was commit, which took 6 minutes 43 seconds. Again this is slow,
and commit is an important operation to have run quickly. Again it was a very
large commit, and I guess most projects wont ever make a commit that large.
Let alone regularly.

This was all done server side. Lets move to the client side. We are going to
grab the code from the server, but as we know we are going to be creating local
branches let's create a repository first. A repository is a shared storage
area for branches. If you create a branch in a repository it will place
all of it's revisions in this shared storage. Then if you branch inside the
repository the revisions will be reused, so that the only thing to do is
create the working tree. As we are going to be working on these branches we
use the command::

  bzr init-repo --trees mozilla

where the --trees tells Bazaar to create working trees inside it. If you want
to use a repository on a shared server with several branches pass --no-trees
instead, so that you get the extra saving of not having to create a working
tree. This operation takes 0.35 seconds.

Now ``cd`` to the ``mozilla`` directory that command created. You are
now "inside" the repository, so any branches you create here will use it. So
now were going to do the branch from the server, however there's another
improvement we can make to the original. He branched using ``sftp://`` which
is over SSH. This method is a "dumb" protocol, i.e. everything is done from
the local side. This allows you to use Bazaar with a server that doesn't have
Bazaar installed. However if we do install Bazaar (0.14) on the server it
provides a "smart-server". This allows Bazaar to optimise it's remote
operations, speeding things up. So now if we use the command::

  bzr branch bzr+ssh://...

the ``bzr+ssh`` part tells it to use the smart-server. This command now takes
. This is . The smart-server is young, and it doesn't optimise all the
operations yet, but it can only get quicker now. 

Now for the local branch. This is going to be quicker than in the other post,
due to the repository. ``branch`` locally now takes .

As for the merge, it's not stated what the merge was, so I made 10 commits,
all adding 10 lines to 100 files. I then merged them back to the original
branch. This then took . Again the repository sped this up.

So yes, Bazaar is still slower, but used correctly it can remove a lot of the
long delays people talk about. This is just another post making observations
about the inital commands that are going to take a long time, and not a study
of what using the systems is actually like, I apologise for that. Perhaps I
will write one of those one day.

