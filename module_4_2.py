def test_function():
    print("Z")
    def inner_function():
        print("Я в области видимости функции - inner_function")
    inner_function()
test_function()

# def test_function():
#     print("Z")
#     def inner_function():
#         print("Я в области видимости функции - inner_function")
#         return
# inner_function()  # Выдает ошибку
# test_function()