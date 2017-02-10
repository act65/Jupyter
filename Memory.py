"""
Each memory type should be optimised for its function.


"""
# TODO; would like a few different ways to look up content.
# - location, content, availability, ?
# storage.
# - high level. substitute width for depth (and abs to approx). associative, ...
# - low level. array, graph, ...?
# would like to abstract away from data structures?!?

"""
A base memory class. They all need to;
FORM new memories
STORE formed memories
RECALL stored memories
RETRIEVE stored memories
CONSOLIDATE stored memories
"""
class Memory():
    def __init__(self, size):
        """
        Args:
            size (int): The size (in number of bytes) of the memory
        """
        self.size = size

    def form(self, value, key=None):
        """
        Form a new memory.
        May need to generate a key. I.e. next available index (however that is chosen).
        """
        raise NotImplemented

    def flush(self):
        """
        Clear entire memory.
        """
        raise NotImplemented

    def __call__(self, x):
        raise NotImplemented


class Associative(Memory):
    """
    Associative memory is
    """
    def __init__(self, size):
        super.__init__(self, size)

    def form(self, value, key):
        # treats value and key equally.
        pass

    def flush(self):
        pass

    def __call__(self, x, c=None):
        """
        Args:
            x (trace): The ??? (needs a name)
            c (trace): the context.

        Returns:
            (trace): A closely related memory
        """
        pass
        # there are a couple of ways to do this?
        # - hhr?
        # - content indexing (linear search with similarity metric)
        # - ?


class External(Memory):
    """
    Traditional storage. Everything is stored, nothing is lost. Lossless.
    Could do some fancy stuff?
    Heirarcical? Optimise for parallel? Differentiable?
    """
    def __init__(self, size):
        super.__init__(self, size)

    def form(self, value):
        key = self._nextkey()
        pass

    def flush(self):
        pass


class Procedural(Memory):
    def __init__(self, size):
        super.__init__(self, size)

    def form(self, value):
        key = self._nextkey()
        pass

    def flush(self):
        pass


class Episodic(Memory):
    """
    Similar to a linked list?
    Each recalled memory is associated closely with the next in the sequnce?
    """
    def __init__(self, size):
        super.__init__(self, size)

    def form(self, value):
        key = self._nextkey()
        pass

    def flush(self):
        pass


class Working(Memory):
    """
    Needs the ability to chunk!!!
    Save past working memory states into memory in a meaningful way.
    """
    def __init__(self, size):
        super.__init__(self, size)

    def form(self, value, key):
        pass

    def flush(self):
        pass

    def __call__(self, x, c=None):
        """
        Args:
            x (trace): The ??? (needs a name)

        Returns:
            ??? Not a memory? but an action?
        """
        pass
        # there are a couple of ways to do this?
        # - hhr?
        # - content indexing (linear search with similarity metric)
        # - ?
