from ast import Not
# এখানে যে পরে আসবে সে আগে যাবে 

books = []

books.append("Learne c")
books.append("Learne c++")
books.append("Learne java")
books.append("Learne python")

print(books)

books.pop()
print(books[-1])

books.pop()
print(books[-1])

books.pop()
print(books[-1])

books.pop()
if not books:
    print("Not books left")
