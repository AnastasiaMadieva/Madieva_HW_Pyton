from smartphone import Smartphone

Catalog = [
    Smartphone ("Nokia", "15", "+79179994555"),
    Smartphone ("Siemens", "X16", "+79869867555"),
    Smartphone ("Tecno Spark", "10 Pro", "+79624561212"),
    Smartphone ("Redmi", "9 Pro", "+79194564545"),
    Smartphone ("Apple iPhone", "14 Pro", "+79870617201")
]

for Smartphone in Catalog:
    print (f"телефон: {Smartphone.stamp} {Smartphone.model}, номер: {Smartphone.num}")