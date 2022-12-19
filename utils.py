import inspect
import os
import datetime
def logger(path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            datetime.datetime.now()
            nonlocal path
            cash = []
            cash.append(datetime.datetime.now())
            for i in list(args):
                cash.append(i)
            for i in list(kwargs.values()):
                cash.append(i)

            cash.append(old_function.__name__)
            result = old_function(*args, **kwargs)
            cash.append(result)
            with open(path, 'a+') as file:
                file.write(str(cash) + '\n')
            return result
            cash.append(result)
        return new_function
    return _logger