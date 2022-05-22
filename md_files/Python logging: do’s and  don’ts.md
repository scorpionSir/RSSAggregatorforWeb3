# Python logging: do’s and don’ts¶

Logging is important. Python has a nice logging framework. I very rarely see
it used properly, even by experienced programmers.

This is an opinionated list of advices for basic usage of Python logging.

Just go through this list, and read each section if you don’t get it:

>   * `logger.info(f"You are {username}")` is bad! Use a format string with
> arguments.
>
>   * Never log through the `logging` module directly. Use a logger.
>
>   * Only setup logging / configure verbosity in your main program!
>
>   * Tip: use `logger.exception()` or `exc_info=True`.
>
>

## Use a format string with arguments¶

If you ever see code like:

>   * `logger.info(f"You are {username}")`
>
>   * `logger.debug("The object is: %s" % complex_object)`
>
>

It will work fine. But it’s bad. Don’t do it.

Instead, all the logging methods accept a string and arbitrary number of
parameters. It will then combine them together using `%` formatting. So you
should do:

    
    
    logger.info("You are %s", username)
    

### Why?¶

Under the hood, when you log something,
[LogRecord](https://docs.python.org/3/library/logging.html#logging.LogRecord)
objects are created. These contain your message (`msg`) and an arbitrary
number of arguments (`args`, these are the supplemental parameters).

This doesn’t make a big difference for basic usage. But imagine that later you
decide to send your logs to some systems for analyzing/aggregating them. In
the bad case, the system will see log records like this:

>   * `{level=INFO, msg="You are John Doe", args=[]}`
>
>   * `{level=WARN, msg="User John Doe unknown", args=[]}`
>
>   * `{level=INFO, msg="You are palkeo", args=[]}`
>
>

We see the messages. We don’t know that “You are John Doe” and “You are
palkeo” are actually the same log, nor that “John Doe” was involved in two log
records.

If we do it with arguments:

>   * `{level=INFO, msg="You are %s", args=["John Doe"]}`
>
>   * `{level=WARN, msg="User %s unknown", args=["John Doe"]}`
>
>   * `{level=INFO, msg="You are %s", args=["palkeo"]}`
>
>

Now we can still trivially generate a printable message, but we have the
template strings that will stay unchanged, and we can inspect the arguments
separately. Doing aggregation on grouping becomes trivial. Now we could
imagine surfacing the log message that was the most frequent, and then the
arguments that were the most frequent for that log, for example.

_For performance_ it’s also better, because if the log is immediately
discarded you don’t need to format the string at all. Imagine we are passing
some complex object that are doing non-trivial work to render themselves as a
string, then passing as an argument will cause that string rendering to be
avoided if the log is not printed anywhere.

### But I don’t like % formatting¶

There needed to be a default, and it’s hard to change while keeping backwards
compatibility, but if you really don’t like it there are ways to do it
properly while using arbitrary formattings. See the [logging
cookbok](https://docs.python.org/3/howto/logging-cookbook.html#using-
particular-formatting-styles-throughout-your-application) that explains it in
details.

## Never log through the logging module directly. Use a logger.¶

Code like this:

    
    
    import logging
    logging.info("some log")
    

Is bad. Why? Because it uses the root logger implicitly, it means there is no
way to silence what you log to it.

Instead, each python module (each file), should have this:

    
    
    import logging
    logger = logging.getLogger(__name__)
    

And then you can log everything through that logger. That’s the [recommended
way](https://docs.python.org/3/library/logging.html#logger-objects) of doing
it.

Using `__name__` as the name of the logger makes sure that the logger
hierarchy reflects the python module hierarchy, which is a great starting
point. I recommend you don’t use `__name__` only if you know exactly what you
are doing.

You can imagine explicitly passing loggers around, or storing them in class
instances for examples, but that’s only for advanced use. And is not needed in
most cases.

## Only setup logging / configure verbosity in your main program!¶

Calls to:

>   * `logger.setLevel()`
>
>   * `logging.basicConfig()`
>
>

Or similar methods should only be used in your main program.

If you use these, you can ask yourself the following question: in that same
code, would you consider using `print()` or `input()`, or maybe reading
program arguments from `sys.argv`? If the answer is yes, you are in the main
program, so it is fine to setup logging.

Otherwise, you are probably in library code, and you don’t want to mess up
with that! This would make the main program that want to do the setup behave
in unexpected ways.

## How to setup logging properly¶

In your main program (and in the main only!), you can do that:

    
    
    logging.basicConfig(level=logging.DEBUG)
    

To globally setup logging to the `DEBUG` level.

You may see stuff logged from some random libraries that you are using, and
that you don’t know about: this is good! You can see a lot about what your
program is doing.

But if some libraries you don’t care about are too noisy, you can easily
silence them:

    
    
    logging.getLogger("some_library").setLevel(logging.WARNING)
    

Here, we are setting the logger for `some_library` (and any logger under it)
to `WARNING`, so any log lower than that will not be propagated and not
printed.

## Tip: use logger.exception() or exc_info=True¶

In some code, you’ll catch an exception, and want to handle it properly. But
often you would also like to log that (say, as a `WARNING`) so that it’s
easier for a developer to know that it happens, and it’s potentially bad but
the program was able to recover.

In that case, you can do something like this:

    
    
    try:
        dangerous_code()
    except Exception:
        logger.exception("Something bad happened.")
    

Here, if `dangerous_code()` raises an exception, we’ll use
`logger.exception()` to log it as an error. But this method also append a full
backtrace of where the exception happened and will display it. This way it’s
much easier to see what happened.

If you don’t want to log it at the `ERROR` level with `logger.exception()`,
you can do something like that instead:

    
    
    logger.info("Something slightly bad happened.", exc_info=True)
    

This has the same effect, but allow you to use the level you want.

Previous: [ The bZx attacks explained ](../projets/ethereum/bzx.html)   Next:
[ Critical analysis of Flashbots ](../projets/ethereum/flashbots.html)

### [palkeo](../index.html)

  * [Projects](../projets/index.html)
  * [Blog articles](index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../about.html)

##  02 May 2020

  * Language: [English](language/english.html)
  * Tag: [python](tag/python.html)

(C)2020, palkeo.

