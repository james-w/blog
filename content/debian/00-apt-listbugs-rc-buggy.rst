apt-listbugs RC bug problems

<p>
Recently apt-listbugs was 
<a href="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=374104">orphaned</a>, 
and it was in a 
<a href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=apt-listbugs">
bad shape</a>, including an 
<a href="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=323626">RC bug</a> 
that makes it virtually useless at the moment, not showing some bugs, and
showing ones that were closed long ago.
</p>

<p>
I then started work on the package, fixing all of the easy bugs while I got
used to coding in Ruby. I put my patches in to the BTS, mainly so that I could
tag the bug +patch, and it would be displayed differently, so that I could see
which bugs still need working on. I kept the package locally in svn, and by
the end had a <a href="http://jameswestby.net/debian/">package that fixed 
around 25 open bugs in the BTS.</a>. My plan was to seek a QA upload of the 
package, as I didn't want to become the maintainer.
</p>

<p>
Unfortuantely the package that I had didn't tackle the RC bug. This is because
the index files that apt-listbugs uses to get the status of bugs appeared to
be wrong or out of date. These files live on a non-Debian server, so the DDs
who had looked at the bug could not instantly see what was going on. There
were proposals to move the files to a Debian machine, but this had not
happened. Without access to the generation of these index files it was 
impossible to debug where the problem was coming from. 
</p>

<p>
Then another person stepped up to adopt apt-listbugs. This was good as it
seemed that he was in contact with a DD that could work out where the problem
was, and was apparently rewriting the scripts to be more reliable. I was
hopeful that the problem would be fixed soon.
</p>

<p>
However one problem was that the prospective maintainer said that he did not
want to use my packages as a base for his work, he would pull my patches out
of the BTS. In a way this is fine, and it is his choice, but at the same time
it is annoying as some of my work might go to waste. Not only did I make the
patches that ended up in the BTS, I did several more things that didn't have
an associated bug report. 
</p>

<p>
The other problem appears to be that there has been no further activity in the
BTS for apt-listbugs since the O became ITA. I'm not sure how the prospective
maintainer works, but I would have thought he would triage the new bugs, and
send some thoughts or questions to old bugs as he is working on them. There
has also been no activity on the RC bug, giving the process for interested
parties, or those that are looking to squash RC bugs in preparation for etch.
I understand that the DD doing this part is probably very busy though.
</p>

<p>
There is no way in which apt-listbugs can enter a stable release in its
current state, as it is worse that useless, continually giving false
positives. Hopefully all of this can be sorted out soon.
</p>

