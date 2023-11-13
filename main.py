import time
from python_module.python_module import function_time


@function_time
def abcd():
    time.sleep(1)


abcd()
