

class ArchiveItem:

    def __init__(self, uid: str, title: str, year: int):
        self.uid = uid
        self.title = title
        self.year = year

    def is_recent(self, n: int) -> bool:
        current_year = 2025
        return (current_year - self.year) <= n

    def __str__(self) -> str:
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other: 'ArchiveItem') -> bool:
        if isinstance(other, ArchiveItem):
            return self.uid == other.uid
        return False


class Book(ArchiveItem):

    def __init__(self, uid: str, title: str, year: int, author: str, pages: int):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Book - {super().__str__()}, Author: {self.author}, Pages: {self.pages}"


class Article(ArchiveItem):

    def __init__(self, uid: str, title: str, year: int, journal: str, doi: str):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self) -> str:
        return f"Article - {super().__str__()}, Journal: {self.journal}, DOI: {self.doi}"


class Podcast(ArchiveItem):

    def __init__(self, uid: str, title: str, year: int, host: str, duration: int):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self) -> str:
        return f"Podcast - {super().__str__()}, Host: {self.host}, Duration: {self.duration} minutes"


def save_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            if isinstance(item, Book):
                file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")


def load_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            item_type = data[0]
            uid = data[1]
            title = data[2]
            year = int(data[3])

            if item_type == "Book":
                author = data[4]
                pages = int(data[5])
                items.append(Book(uid, title, year, author, pages))
            elif item_type == "Article":
                journal = data[4]
                doi = data[5]
                items.append(Article(uid, title, year, journal, doi))
            elif item_type == "Podcast":
                host = data[4]
                duration = int(data[5])
                items.append(Podcast(uid, title, year, host, duration))

    return items


def main():
    archive_items = [
        Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
        Book("B002", "Python Programming", 2021, "John Smith", 450),
        Article("A101", "Quantum Computing", 2022, "Nature", "10.1235/qc567"),
        Article("A102", "Machine Learning Advances", 2020, "Science", "10.1234/ml789"),
        Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
        Podcast("P302", "Programming 101", 2024, "Bob Johnson", 60)
    ]

    save_to_file(archive_items, "archive.txt")

    loaded_items = load_from_file("archive.txt")

    print("All Archive Items:")
    for item in loaded_items:
        print(item)

    print("\nRecent Items (last 5 years):")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)

    print("\nArticles with DOI starting '10.1234':")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)


if __name__ == '__main__':
    main()