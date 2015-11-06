Commit access is no more
#parser reST

Many projects that I work on, or follow the development of, and granted there may
be a large selection bias here, are showing some of the same tendencies. Combined
these indicate to me that we need to change the way we look at becoming a trusted
member of the project.

The obvious change here is the move to distributed version control. I'm obviously
a fan of this change, and for many reasons. One of those is the democratisation of
the tools. There is no longer a special set of people that gets to use the best
tools, with everyone else having to make do. Now you get to use the same tools
whether you were the founder of the project, or someone working on your first
change. That's extremely beneficial as it means that we don't partition our efforts
to improve the tools we use. It also means that new contributors have an easier
time getting started, as they get to use better tools. These two influences combine
as well: a long time contributor can describe how they achieve something, and the
new contributor can directly apply it, as they use the same tools.

This change does mean that getting "commit access" isn't about getting the ability
to commit anymore; everyone can commit anytime to their own branch. Some projects,
e.g. Bazaar, don't even hand out "commit access" in the literal sense, the project
blessed code is handled by a robot, you just get the ability to have the robot merge
a branch.

While it is true that getting "commit access" was never really about the tools,
it was and is about being trusted to shepherd the shared code, a lot of projects
still don't treat it that way. Once a developer gets "commit access" they just
start committing every half-cooked patch they have to trunk. The full use of
distributed version control, with many branches, just emphasises the shared
code aspect. Anyone is free to create a branch with their half-baked idea and
see if anyone else likes it. The "blessed" branch is just that, one that the
project as a whole decides they will collaborate on.

This leads to my second change, code review. This is something that I also deeply
believe in; it is vital to quality, and a point at which open source software
becomes a massive advantage, so something we should exploit to the full. I see
it used increasingly in many projects, and many moving up jml's `code review
"ladder"`_ towards pre-merge review of every change. There seems to be increasing
acceptance that code review is valuable, or at least that it is something a good
project does.

.. _code review "ladder": http://mumak.net/stuff/your-code-sucks.html

Depending on the project the relationship of code review and "commit access" can
vary, but at the least, someone with "commit access" can make their code review
count. Some projects will not allow even those with "commit access" to act
unilaterally, requiring multiple reviews, and some may even relegate the concept,
working off votes from whoever is interested in the change.

At the very least, most projects will have code review when a new contributor
wishes to make a change. This typically means that when you are granted "commit
access" you are able or expected to review other people's code, even though
you may never have done so before. Some projects also require every contribution
to be reviewed, meaning that "commit access" doesn't grant you the ability to
do as you wish, it instead just puts the onus on you to review the code of others
as well as write your own.

As code review becomes more prevalent we need to re-examine what we see as
"commit access," and how people show that they are ready for it. It may be
that the concept becomes "trusted reviewer" or similar, but at the least
code review will be a large part of it. Therefore I feel that we shouldn't
just be looking at a person's code contributions, but also their code review
contributions. Code review is a skill, some people are very good at it, some
people are very very bad at it. You can improve with practice and teaching,
and you can set bad examples for others if you are not careful. We will
have to make sure that review runs through the blood of a project, everyone
reviews the code of everyone else, and the reviews are reviewed.

The final change that I see as related is that of empowering non-code
contributors. More and more projects are valuing these contributors, and
one important part of doing that is trusting them with responsibility. It
may be that sometimes trusting them means giving them "commit access",
if they are working on improving the inline help for instance. Yes, it may
be that distributed version control and code review mean that they do
not have to do this, but those arguments could be made for code contributors
too.

This leads me to another, and perhaps the most important, aspect of the
"commit access" idea: trust. The fundamental, though sometimes unspoken,
measure we use to gauge if someone should get "commit access" is whether
we believe them to be trustworthy. Do we trust them to introduce code without
review? Do we trust them to review other people's changes? Do we trust them
to change only those areas they are experts in, or to speak to someone
else if they are not? This is the rule we should be applying when making
this decision, and we should be sure to be aware that this is what we
are doing. There will often be other considerations as well, but this
decision will always factor.

These ideas are not new, and the influences described here did not create
them. However the confluence of them, and the changes that will likely
happen in our projects over the next few years, mean that we must be sure
to confront them. We must discard the "commit access" idea as many projects
have seen it, and come up with new responsibilities that better reflect
the tasks people are doing, the new ways projects operate, and that
reward the interactions that make our projects stronger.

