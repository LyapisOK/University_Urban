def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


#inner_function() - работать не будет так как вызывается внутри функции test_function()
test_function()