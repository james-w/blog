Sandwiches


`Mr LeSage`_, I just happened to run ``bzr plugins`` today, and noticed this::

  .
  .
  sandwich 
      (no description)
  .
  .

Curious as to what the hell that was, I ran the command again with ``-v`` and
saw that it was installed in my ``~/.bazaar/plugins/`` directory. I opened the
file and found this that I wrote a few months ago::

  from bzrlib.commands import Command, register_command

  class cmd_make_me_a_sandwich(Command):

      def run(self):
          self.outf.write("What? Make it yourself.\n")

  class cmd_sudo_make_me_a_sandwich(Command):

      def run(self):
          self.outf.write("Okay.\n")

  register_command(cmd_make_me_a_sandwich)
  register_command(cmd_sudo_make_me_a_sandwich)

Not quite what you were after though. That would be this plugin::

  class SandwichCommand(Command):

      def run(self, **kwargs):
          for name, arg in kwargs.items():
              if arg != name:
                  self.outf.write(self.fail_message + "\n")
                  return 1
          self.outf.write(self.success_message + "\n")
          return 1

  class cmd_make(SandwichCommand):

      takes_args = ["me", "a", "sandwich"]
      fail_message = "Make you a what?"
      success_message = "What? Make it yourself."

  class cmd_sudo(SandwichCommand):

      takes_args = ["make", "me", "a", "sandwich"]
      fail_message = "Of course, but what do you want me to do?"
      success_message = "Okay."

  register_command(cmd_make)
  register_command(cmd_sudo)

I'm still none the wiser as to why I wrote that plugin in the first place
though.

.. _Mr LeSage: http://rickroll.it/9d6422
