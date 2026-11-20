import json
all_books = [
    {"title": "Python Basics", "price": "£25", "availability": "In stock"},
    {"title": "Machine Learning", "price": "£40", "availability": "In stock"},
    {"title": "Data Science", "price": "£30", "availability": "In stock"}
]
with open("books.json","w",encoding="utf-8") as file:
    json.dump(all_books,file,indent=4,ensure_ascii=False)
with open("books.json","r",encoding="utf-8") as file:
    records = json.load(file)
    print(f"Records loaded: {len(records)}")
    if all_books == records:
        print("JSON verificaiton successful.")
    else:
        print("JSON verification failed.")

