def first_decorator(age):
    def inner_function(func_to_decorate):
        def wrapper(name):
            print(f"BEFORE__FIRST {age}")
            func_to_decorate(name)
            print("AFTER__FIRST")

        return wrapper
    return inner_function


def second_decorator(func_to_decorate):
    def wrapper(name):
        print("BEFORE__SECOND")
        func_to_decorate(name)
        print("AFTER__SECOND")

    return wrapper


@second_decorator
@first_decorator(18)
def test_function(name):
    print(f"{name} call me")

# first_decorator(18)(test_function)
test_function("John")



