import wikipedia

title = input("Title of article: ")
saved_page = wikipedia.page(title, autosuggest=False)
print(saved_page.title)
print(saved_page.summary)
print(saved_page.url)
