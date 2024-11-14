def introspection_info(obj):
    """
    Функция для получения информации об объекте в Python.

    Args:
        obj: объект, информацию о котором нужно получить.

    Returns:
        Словарь с информацией об объекте.
    """

    # Тип объекта
    obj_type = type(obj).__name__

    # Атрибуты объекта
    attributes = dir(obj)

    # Методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Модуль, к которому принадлежит объект
    module = obj.__module__

    return {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": module,
    }

number_info = introspection_info(42)
print(number_info)