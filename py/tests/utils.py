import inspect


def test(func):
    def test_decorator(test_func):
        def wrapper(self, *args, **kwargs):
            solution_class = getattr(inspect.getmodule(func), func.__qualname__.rsplit('.', 1)[0])
            solution = solution_class()

            def _test(*params, result=None, **states):
                with self.subTest(params=params, result=result, states=states):
                    self.assertEqual(func(solution, *params), result)

                    for key, state in states.items():
                        if key[0] == '_':
                            try:
                                idx = int(key[1:])
                            except ValueError:
                                continue

                            self.assertEqual(params[idx-1], state)

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

# TODO: Need some util to set func for wrapping params/result/state: e.g. non-order sensitive result comparing
