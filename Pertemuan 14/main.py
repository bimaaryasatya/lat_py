from module import EBook

ebook1 = EBook("Mein Kampf", "Adolf Hitler", "1942", "12.4 MB")
print(ebook1.get_information().replace(",","\n"))
print()
# print(ebook1.get_book().get_information().replace(",","\n"))
