# Day 04 - Python Bootcamp

### Exercise 00

You need to write an `energy.py` script with a function called `fix_wiring()` which should accept three iterables (you can test the functionality with just lists) called `cables`, `sockets` and `plugs`. This function shouldn't make any assumptions about the length of these iterables, which can be different. It should return a different iterable over strings with commands like:

`plug cable1 into socket1 using plug1`
`weld cable2 to socket2 without plug`

You can see that the only iterator whose length doesn't matter is `plugs`, because in the worst case you can weld cables to sockets. If there are not enough cables or sockets, there is nothing you can do, so they shouldn't be present in a resulting iterator.

This means that for code like this:

```
plugs = ['plug1', 'plug2', 'plug3']
sockets = ['socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable1', 'cable2', 'cable3', 'cable4']

for c in fix_wiring(cables, sockets, plugs):
    print(c)
```

The output should be:

```
plug cable1 into socket1 using plug1
plug cable2 into socket2 using plug2
plug cable3 into socket3 using plug3
weld cable4 to socket4 without plug
```

Also, input iterators can contain other non-string datatypes, which should be filtered out. So, for an input like:

```
plugs = ['plugZ', None, 'plugY', 'plugX']
sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable2', 'cable1', False]
```

it should be just:

```
plug cable2 into socket1 using plugZ
plug cable1 into socket2 using plugY
```

Just for fun, you can get extra points if the body of your function could be written on a single line (starting with `return`), i.e. no block-starting colons (like in `if` conditions or `try/except`) are used.


### Exercise 01


First, you need to create a file `pressure.py` with a generator function `emit_gel()` that should simulate the measured pressure of a liquid. It should generate an infinite stream of numbers from 0 to 100 (values > 100 are considered an error) with a random step sampled from the range `[0, step]`, where `step` is an argument to a generator `emit_gel()`.

Second, you must follow the pressure control guidelines. The operating pressure should be between 20 and 80, i.e. if a generator emits a value below 20 or above 80, the action that reverses the sign of the step should be applied. To implement this kind of valve, you will need to write another function called `valve()`, which will loop over the values of `emit_gel()` and use the `.send()` method to reverse the sign of the current step.

Third, you should implement an emergency break. If a pressure is above 90 or below 10, the `emit_gel()` generator should gracefully close and the script should exit.

Feel free to experiment and choose a `step` so that your script runs for a few seconds before exiting. You can add a delay between `pressure measurements` to avoid using too much CPU to generate and process the sequence.



