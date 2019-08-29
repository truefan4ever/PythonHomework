class A():
    """
    This class have read-only instance attribute 'x'."""

    def __init__(self):
        self._x = 'value'

    @property
    def foo(self):
        return self._x


a = A()
print(a.foo)
