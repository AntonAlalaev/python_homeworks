def test_function():
    def inner_function():
        print('Я в области видимости test_function')
    inner_function()

test_function()
# inner_function() - ошибка т.к. она находится только в области видимости test_function

