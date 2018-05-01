import inspect


def test(func):
    def test_decorator(test_func):
        def wrapper(self, *args, **kwargs):
            solution_class = getattr(inspect.getmodule(func), func.__qualname__.rsplit('.', 1)[0])
            solution = solution_class()

            def _test(*params, result):
                with self.subTest(params=params, result=result):
                    self.assertEqual(func(solution, *params), result)

            _globals = test_func.__globals__
            sentinel = object

            oldvalue = _globals.get('test', sentinel)
            _globals['test'] = _test

            try:
                result = test_func(self, *args, **kwargs)
            finally:
                if oldvalue is sentinel:
                    del _globals['test']
                else:
                    _globals['test'] = oldvalue

            return result
        return wrapper
    return test_decorator
