def solution(module):
    def test_solution(func):
        def wrapper(*args, **kwargs):
            _globals = func.__globals__
            sentinel = object

            oldvalue = _globals.get('solution', sentinel)
            _globals['solution'] = module.Solution()

            try:
                result = func(*args, **kwargs)
            finally:
                if oldvalue is sentinel:
                    del _globals['solution']
                else:
                    _globals['solution'] = oldvalue

            return result
        return wrapper
    return test_solution
