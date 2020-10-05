#########################################
# Decorator
#########################################

def train():

    start_time = time()

    model.train()

    print("Finished training in {} secs".format(time() - start_time ))


@timer
def train():
    model.train()


def timer(func):

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time()
        value = func(*args, **kwargs)
        print("Finished {} in {} secs"
                .format(func.__name__, time() - start_time))
        return value

    return wrapper_timer
