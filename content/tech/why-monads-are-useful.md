Title: Why Monads Are Useful
Date: 2017-1-17 20:13
Category: tech
Tags: programming, functional, monads
Slug: tech/why-monads-are-useful
Authors: James Westby
Summary: Why everyone is on about monads.

You may be hearing lots of people talking about monads,
particularly if they are in to Haskell, and wonder what
all of the fuss about. You may have read an article or two
that tried to explain what a monad is, but not really
understood what all the fuss is about.

I was in a similar situation, thinking that monads were
an advanced programming concept that I was missing out on.
I spent a lot of time reading a lot of articles about monads
to try and understand them, always unsure whether I wasn't
understanding what they were, or just missing what made them
so special. Most articles about monads just focus on the
mechanics, and don't explain why they are interesting
to working programmers.

There's a lot to say about monads, and as you have seen there
are thousands of attempts to explain them. I don't want to
try and do that though, I'd like instead to tell you why
they are useful, as I think that is far more important, and
may help you decide if you want to invest the time to
learn about how they work. I don't want to be another person
trying to explain to you what a monad is.

## What is a Monad?

However I can't really talk about why they are useful without
giving you some intuition about what a Monad actually is.

This isn't a monad tutorial. You aren't going to fully understand
what a monad is just from reading this. I just want to
use some familiar programming concepts to give you an idea
of what a monad is so that I can explain what it is.

I am going to do my best to not fall prey to the
["Burrito Falacy"](https://byorgey.wordpress.com/2009/01/12/abstraction-intuition-and-the-monad-tutorial-fallacy/)
and try and convince you that you can understand Monads through
one simple analogy. A monad is a monad. If you want to understand
them then study them.

However, to get some idea about what they are, consider these
four more-or-less familiar programming concepts:

  * Operations that perform nullable/optional values
  * Operations that return a value or an error
  * Operations that peform a List/Array
  * Operations that peform a Promise

What links these four concepts? In this case it's the effect
that they can have on the rest of the computation.

In each case the code can make a decision about how to
execute the rest of the code, for instance those decisions
could be:

  * Execute the rest of the code only if the value isn't null
  * Execute the rest of the code only if there was no error
  * Execute the rest of the code once for each value in the list
  * Execute the rest of the code once the promise fires

In each case there is something that is making a decision about
how to execute the rest of the code. We could represent these as
functions:

    function notNull(f, rest) {
        const value = f();
        if (value !== null) {
            return rest(value);
        } else {
            return null;
        }
    }

    function noError(f, rest) {
        let value;
        try {
            value = f();
        } catch (e) {
            // Yeah, you wouldn't actually write this, but bear with me
            throw e;
        }
        rest(value);
    }

    function eachResult(f, rest) {
        const l = f();
        for (item in l) {
            rest(item);
        }
    }

    function whenFires(f, rest) {
        const p = f();
        p.then(rest);
    }

Each has a different way of passing the value from the first operation on
to the rest of the code.

The key to understanding this is to see that a line of code can be seen
as performing an operation, and then deciding what value to pass to the
rest of the code that will come afterwards. How would we model the normal
control flow of just running the next operation in this way? Easy:

    function sequence(f, rest) {
        return rest(f());
    }

Now, this isn't a precise definition of a monad, but each of these is
a monad: a different way of linking the result of an operation with the
rest of the code that follows it.

You can probably think of lots more examples along these lines now that
you have seen some, and that's the point, monads appear all over the place.
Monads aren't an invention, they are an observation. There's a lot of code
that we write all the time that has a similar form. So that sort of answers
the original question of this article: why are monads useful? We prove
them to be useful by using them all the time, even if we don't write
functions like the ones I wrote above.

That's not very satisfying though. Why do people go on about monads if
they are just simple things like this? It's a good question, and you
can be perfectly happy continuing as you have, and just knowing that monads
are a common programming pattern. However, what do we do when we spot a
repeated pattern in programming? We try and formalise it and do something
useful with it.

Therefore I want to look at a slightly different question.

## Why is it useful for my programming language to have special monad constructs?

Usually when people are talking about monads, they are talking about
having special support in a programming language for them. As we
saw above monads are very common, and every language supports them,
but not many have special constructs for handling them. Why would we want such a thing?

The first reason is that most languages don't have great support for
dealing with "the rest of the code". There are usually two ways to do
this:

  1. Return statements
  2. If blocks

Return statements are very useful, but can become pretty repetitive. Consider
Go's error handling:

    value, err := someOperation()
    if err != nil {
        return nil, err
    }
    value2, err := otherOperation(value)
    if err != nil {
        return nil, err
    }
    return value2

If blocks are great to reduce the duplication if there is a common exit
pattern, but can become very deeply nested quickly.

    value, err := someOperation()
    if err == nil {
        value2, err := otherOperation(value)
        if err == nil {
            return value2
        }
    }
    return nil, err

There are better ways to write this, but let's just say for a minute
that a better way of doing this might be useful. What might that
way be? We have a common pattern that we want to repeat lots of times.
We know what we want that pattern to be for error handling, it's the
familiar

    if err != nil {
        return nil, err
    }

(there are variations on this, like adding extra information to the error,
we would have to support those, but let's ignore it for now.)

We want to put this after every operation that can return an error, so
let's invent a new bit of syntax that does that, and let's use `<<==`, so
we can write

    value <<== someOperation()

This means, run `someOperation`, then if there is an error return it, otherwise
assign the result to the variable and execute the rest of the code. We
can then chain these operations easily:

    value <<== someOperation()
    value2 <<== otherOperation(value)

This would have the same behaviour as before, but it hides all the error handling
away behind those arrows.

So far you may not be that impressed though, we've invented a new bit of syntax
to do something specific (and ignored things like wrapping the errors). That's not
very impressive.

Remember though that we had several different examples that I said were similar.
Can we re-use this for another of those cases? What about if `someOperation` doesn't
return an error, but returns a nullable type instead?

In that case we want the code that we put in the middle to not do the error
checking, but instead do a nil check.

    if value == nil {
       return value
    }

Now we can re-use `<<==` from above.

    value <<== someOperationMaybeReturningNil()
    value2 <<== someOperationThatCantReceiveNil(value)

The second operation can't receive nil, but we have inserted the nil
check code using the `<<==` so it won't.

I realise I have completely glossed over how we change what the arrow
does in the two cases. Obviously we need a way to do that, but I won't
cover how to do that in this article, but it clearly requires
language support.

If we figured out all of the details, then this would work for anything
that is a monad, meaning that we would have a single consistent interface
for describing how to thread the operations together whenever there
was a monad involved.

To show that let's look at something that seems different, the list
case.

I lied a little before with what the `<<==` was doing, implying that
it just inserted a block of code, but remember from before that we
need to be able to control how the rest of the code is executed.
In the case of the list we need to execute it several times, so in
fact the arrow is doing something more like our original functions.
In this list case this was

    function eachResult(f, rest) {
        const l = f();
        for (item in l) {
            rest(item);
        }
    }

If we make that the `<<==` and thread it in to

    value <<== someOperationReturningAList()
    value2 <<== someOperationOnEachItem(value)

The second operation wouldn't receive the list as a whole, but
would be called once for each item in the list.

Maybe I still haven't convinced you that this is useful yet, so
let's look at one more example. Consider a HTTP API client
that needs to sequence several API calls, each of which may
fail:

    articleID <<== getLatestArticle()
    content <<== getArticleContent(articleID)

This time we are using the `<<==` that handles errors again.

What if we decided that we wanted to change this code so that
it was asynchronous using Promises instead? If we don't have
`<<==` then our code would start out like:

    articleID, err := getLatestArticle()
    if err != nil {
        return nil, err
    }
    content, err := getArticleContent(articleID)
    if err != nil {
        return nil, err
    }

and would need to change to

    promise := getLatestArticle()
    promise.then(getArticleContent)

However, if we instead are able to use `<<==` and change its
meaning to chain the functions using the promise, then our
code is

    articleID <<== getLatestArticle()
    content <<== getArticleContent(articleID)

This is exactly the same as before. That means we changed
from synchronous to asynchronous without changing this code.
That's pretty amazing, as when we started out defining
`<<==` we weren't thinking about synchronicity at all.

All we have to do is redefine `<<==` for that block of code
and we change the way in which it executes.

`<<==` seems pretty magical then, but hopefully you can see
how the language might handle it, and how you might
be able to redefine its behaviour when you need to. If
you want to know how it really works and how languages
make it all work in practice then go read up on Monads
some more.

## Why are monads useful?

Monads are useful as they appear everywhere. We've seen
a few examples, but hopefully you can think of many similar
ones.

Just because they are everywhere doesn't mean that
we need to do anything special with them. You can continue
using them, either noticing them when you spot them, or
completely ignoring them and you will be fine.

Monads provide us with a single way of describing many
different types of computation that seem very different
at first (errrors, lists and promises for example). This
can be really powerful if your language provides support
for talking about monads directly.

We can use one bit of syntax to hide many different bits
of boilerplate. This then also allows for code to operate
on any monad, without caring about which one it is. We
saw how you can write one bit of code that doesn't care
whether it runs synchronously or asynchronously.

That provides us with very powerful high-level tools for
describing our code. We can describe the operations we
want to happen, while hiding the boilerplate, both to
keep the code cleaner, but also to allow us to swap
out that boilerplate if we want.

That's why I'm interested in monads: they are a possibility
to provide powerful abstractions that work in many different
areas. Exactly what programming languages should be doing.
