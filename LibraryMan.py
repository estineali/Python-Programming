class Book(object):
        """docstring for Book"""
        def __init__(self, title, author, form):
                self.BookTitle = title
                self.Author = author
                self.Form = form

        def details(self):
                return "(" + self.BookTitle + ", " + self.Author + ", " + self.Form + ")"  


class Bookshelf(object):
	def __init__(self):
		self.container = []
		file = open("BookShelf.txt", 'a')
		file.close()
		self.LoadBooks()

	def LoadBooks(self):
		file = open("BookShelf.txt", 'r')
		for i in file:
			i = i.strip()[1:-1].split(", ")
			self.container.append(Book(i[0], i[1], i[2]))
		file.close()

	def __len__(self):
		return len(self.container)
	
	def BooksInShelf(self):
		return len(self.container)

	def AddBook(self):
		bookName = input("Book name: ").strip().capitalize()
		bookAuthor = input("Author's name: ").strip().capitalize()
		bookForm = input("Ebook, Hardcopy, or Both: ").strip().capitalize()

		self.NewBook(Book(bookName, bookAuthor, bookForm))


	def NewBook(self, book):
		if self.findBook(book.BookTitle) == False:
			self.container.append(book)
			self._writeToFile(book)
		else:
			return False

	def findBook(self, bookName):
		for i in self.container:
			if i.BookTitle == bookName.strip().capitalize():
				return i
		return False
	def removeBook(self, bookName):
		for i in self.container:
			if i.BookTitle == bookName.strip().capitalize():
				container.remove(i)
				return True
		return False
	def _writeToFile(self, book):
		bookshelf = open("BookShelf.txt", 'a')
		bookshelf.write(book.details() + "\n")
		bookshelf.close()

	def ShowShelf(self):
		if not len(self.container):
			print("Book shelf is empty. Add some books.")
		for i in self.container:
			print(i.details())

	def ClearShelf(self):
		bookshelf = open("BookShelf.txt", 'w')
		self.container.clear()
		bookshelf.close()

	def ExportShelf(self):
		warning = input("Any previously exported shelves will be overwritten. Press enter to continue...")
		Exporting = open("TheBookShelf.txt", 'w')
		for book in self.container:
			Exporting.write(book.details() + ", \n")
		Exporting.close()

	def EditABook(self):
		for i in range(len(self.container)):
			print(str(i+1) + ".", self.container[i].details()[1:-1])

		selectedBook = int(input("Enter book serial number to change details of: ")) - 1
		selectedBook = self.container[selectedBook]

		bookName = input("Book name(leave empty if no change required): ").strip().capitalize()
		selectedBook.BookTitle = bookName if bookName != '' else selectedBook.BookTitle

		bookAuthor = input("Author's name: ").strip().capitalize()
		selectedBook.Author = bookAuthor if bookAuthor != '' else selectedBook.Author

		bookForm = input("Ebook, Hardcopy, or Both: ").strip().capitalize()
		selectedBook.Form = bookForm if bookForm != '' else selectedBook.Form

		bookshelf = open("BookShelf.txt", 'w')

		for i in self.container:
			self._writeToFile(i)

		bookshelf.close()


def main():
	print("Hello World!")

	BShelf = Bookshelf()
	BShelf.ShowShelf()


	BShelf.AddBook()
	BShelf.ShowShelf()
	BShelf.AddBook()
	BShelf.ShowShelf()
	BShelf.AddBook()
	BShelf.ShowShelf()
	BShelf.AddBook()
	BShelf.ShowShelf()

	BShelf.EditABook()
	BShelf.ShowShelf()

	# BShelf.ExportShelf()
	


main()