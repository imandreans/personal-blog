import time

#decorater function, to get how long a function is executed
def get_duration(funct):
    #wrapper function will be returned 
    def wrapper():
        start = time.time()
        funct()
        end = time.time()
        return f'Fungsi {funct.__name__} berjalan selama {round(end - start, 2)}'
    return wrapper

@get_duration
def test():
    time.sleep(2)

print(test())