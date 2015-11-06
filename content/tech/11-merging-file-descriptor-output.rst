Merging file descriptor output
#parser reST

I have a problem that I believe will be easy for someone with a bit of
UNIX coding knowledge to solve, so I appeal to those that can to help.

I'm trying to write a DBus service that will spawn a command, and provide
the output to the user. The service runs on the system bus as root, and
so it is a form of privilege escalation. However, the command may be long
running, and produce a lot of output as it works, so I want to allow the
calling process to get this output before the command completes.

My current approach uses `gobject.spawn_async` and so gets file descriptors
back, one for stdout and one for stderr. I currently have a thread that
uses `select` to wait for output, and then uses DBus signals to allow the
client to access it. This works great, except that stdout and stderr can
become interleaved in the middle of lines.

I believe that I can't just wait for full lines before signalling, as
a command might do something like print "Username: " and then wait for
input. I could normally do full lines, and then if the child blocks on
stdin send whatever it has written so far, but that doesn't seem ideal.
(I haven't implemented anything about proving input on stdin so far,
but I don't want a solution that makes it difficult to do so).

It seems to me that this is something that will be implemented somewhere,
for instance my shell can run commands and then interleave the output
in a desirable manner, but I haven't found how yet. Any suggestions
are welcome, but this is from python, so system calls that I can't make
directly from python would be a pain, though I'm not that bothered about
portability.
