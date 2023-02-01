import chardet

a = "\u3010\u7f51\u7ad9\u54c1\u8d28\u3011"
print(a)
filename = "w3school.html"
open(filename, 'w', encoding="utf-8").write(a)

