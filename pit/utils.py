#!/usr/bin/env python3

# deep_flatten a nested list
# flatten([1,[2,[3]],4]) = generator<[1,2,3,4]>
def deep_flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in deep_flatten(i):
                yield j
        else:
            yield i
