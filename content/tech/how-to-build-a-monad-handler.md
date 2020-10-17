Title: How To Build A Monad Handler
Date: 2017-1-17 20:13
Category: tech
Tags: programming, functional, monads
Slug: tech/how-to-build-a-monad-handler
Authors: James Westby
Summary: How a language could add special handling for monads.

Hopefully in my [last post](why-monads-are-useful.html) I
convinced that you monads could be a useful common pattern for
programming languages to support.

While doing that though I was very vague about how it would
actually be implemented, to the point where my code examples
were pretty vague, and wouldn't actually work if you thought
about it.

I'd like to try and clear that up a bit by showing you
how a language could add features to support this common
pattern that we have identified. To do that we'll just
use our design skills to build something that works, and
not deal with any of the type theory that can be used
to derive these ideas.

## Injecting control flow

My illustration of how the feature could work hinged on
the magic `<<==` operator. We said that it would change
what value the rest of the code would see. It also needed
to change behaviour depending on which of our categories
of behaviour we wanted.

Remember that our four categories were:

  * Optional/nullable values
  * Errors/exceptions
  * Lists/arrays
  * Promises

If we need to run different code depending on the type
of the value, then let's try adding a method to the
value that has the behaviour that we want.

Let's start with promises. We want the behaviour to
be that the rest of the code receives the value when
it is ready. This is the `then` method that promises
already expose:

     p.then(rest);

will call the rest of the code with the value when it
is available.

How can we apply this to the other categories. For
lists we said that we wanted to run the rest of the
code for each of the values in the list. This is the
`map` method in those languages that have it.

    l.map(rest)

How about the other categories. In each case it's hard
to define the method, because we either have the value,
or we have something else, namely null, or an exception
bubbling up the stack.

Let's proceed by just defining an interface for this, and
then worry about making it work with the rest of the
language later. For a nullable value, so let's define
a new class that holds the value or null, and we can
define the behaviour there.

    class Nullable {
        constructor(value) {
            this.value = value;
        }

        bind(rest) {
            if (this.value === null) {
                return null;
            }
            return rest(this.value);
        }
    }

We called the method `bind` as that is the convention
for monads, but it could be any name really.

Now let's do the same thing for errors, but this time
we need a couple of different implementations.

    class MaybeError {
    }

    class IsError extends MaybeError {
        constructor(message) {
           this.message = message;
        }

        bind(rest) {
            // There was an error, so propogate it,
            // don't peform the rest of the computations.
            return this;
        }
    }

    class NotError extends MaybeError {
        constructor(value) {
            this.value = value;
        }

        bind(rest) {
            return rest(this.value);
        }
    }

(Again this is very weird code and you likely wouldn't write
it this way naturally, especially with those names, but hopefully
you can see that it is valid code.)

Now for each of our types we can call a method on the value
passing the rest of the code, and it will call it in the right
way for that type. We can alias the `then` method from promises
and the `map` method from lists to `bind` so that we have one
method that we can call regardless of the type.

We can now start chaining the operations using our `bind` function,
for example:

    getArticleID().bind(function(articleID) { 
        return getArticleContent(articleID);
    });

If `getArticleID()` returns something with a bind method then it will
be called with the rest of the code that we want to execute. The value
can then decide how to execute that code, whether `getArticleID` returns
a nullable value, an error, a list, or a promise, what you get out
as the result depends on the particular types that are used.

This code may look pretty familiar, particularly if you have worked
with promises. There's good reason to structure code like this, even
if you don't have any language features that support monads. In fact
you can implement all of this in pretty much every language, so again,
why all the fuss about monads?

## Removing the magic from `<<==`

Again it comes back to the magic `<<==` operator. Now that we
have defined everything above we can finally define how it would work,
and remove all the magic.

We want to take the code from above

    getArticleID().bind(function(articleID) { 
        return getArticleContent(articleID);
    });

and rewrite it to be more compact and less nested.

    articleID <<== getArticleID();
    return getArticleContent(articleID);

Our language then takes this and transforms it in to the function
calls from before. `<<==` is just "sugar" that makes the code nicer
to write, but underneath it is just tranformed in to function calls
using our `bind` method.

So now we see how `<<==` works we can see that it is pretty powerful.
We can define a simple `bind` method, and then our languages special
`<<==` syntax allows us to use that method to change how the code
flow happens, but without resorting to lots of nested functions.
The great thing is that it's one bit of syntax that doesn't care about
any of the specifics, it can work for anything: lists, promises, errors,
or anyting the user defines that we haven't thought of yet.

## Filling in some gaps

Again I've glossed over some details which might be confusing.

The first is that in order to get a fully working system the `bind`
method isn't quite sufficient. You need a second method for each
type, but it's even easier than `bind`. This method takes a plain
value and turns it in to one of the special ones. This is
usually called `return` but that's confusing in most languages,
as it doesn't mean "return this value from this function", so
let's call it `wrap`.

To define wrap you just have to take a plain value and turn it in
to one of your type in the most "plain" way possible. There is an
exact mathematical definition for that, but it usually just means
the easy, obvious way to do it. For promises we again have the
method already defined: `resolve`. This takes the value and
fires the callbacks with it straightaway. It allows you to
take a value you have now, and pretend that it's a value that
you don't know yet.

(In JS the `resolve` method doesn't follow the mathematical
definition required for a monad because of the behaviour
when you give it another promise. However we would fix that
if we were actually using a language with this special support)

For a list, it's pretty obvious how to turn a plain value in to
a list. We wrap it in square brackets: `[value]`.

For the other two we need to use those special classes that
we defined before. For a `Nullable` we would just use the
constructor: `new Nullable(value)`. For a `MaybeError` we would
use the `NotError` constructor: `new NotError(value)`.

The other gap to fill in is how weird the `Nullable` and `MaybeError`
classes are. They aren't things that you would usually write, because
there other ways of handling them in most languages.

You have three options if you are building a language with special
monad handling:

  * Have nulls and exceptions, and `<<==` doesn't support them.
  * Have nulls and exceptions, and have the language make them work with
    `<<==` with some special handling (e.g. null defines `bind`)
  * Don't have traditional nulls and exceptions, and have `Nullable` and
    `MaybeError` instead. This is what e.g. Haskell does. There are
    some advantages of this as well as natural `<<==` support, such as
    great synergy with static type checking.

## Summary

We define `bind` and `wrap` methods for each monad type, and that
provides a consistent interface to chain operations that allow the
value to dictate how the operations link together. We can then
define an operator like `<<==` that the language translates
to callbacks using `bind`.

Hopefully this has cleared up any confusion that the vague code samples
in my last article caused. I hope that it might also have deepened your
understanding of monads, and maybe helped you see how they can be useful.
