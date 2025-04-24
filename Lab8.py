class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = int(year)  

    def __str__(self):
        return f'UID: {self.uid}, Title: {self.title}, Year: {self.year}'

    def __eq__(self, a):
        return self.uid == a.uid
    
    def is_recent(self, n):  
        return 2025 - self.year <= n  
    
class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):  
        super().__init__(uid, title, year)  
        self.author = author
        self.pages = int(pages)  

    def __str__(self):
        return f'{super().__str__()}, Author: {self.author}, Pages: {self.pages}'

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f'{super().__str__()}, Journal: {self.journal}, DOI: {self.doi}'

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = int(duration) 

    def __str__(self):
        return f'{super().__str__()}, Host: {self.host}, Duration: {self.duration}'

def save_to_file(items, filename):
    with open(filename, 'w') as f:  
        for item in items:
            if item is not None:
                if isinstance(item, Book): 
                    f.write(f'Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n')
                elif isinstance(item, Article):
                    f.write(f'Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n')
                elif isinstance(item, Podcast):
                    f.write(f'Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n')

def load_from_file(filename):
    obj_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                instance = line.strip().split(',')
                if instance[0] == 'Book':
                    obj_list.append(Book(instance[1], instance[2], instance[3], instance[4], instance[5]))
                elif instance[0] == 'Article':  
                    obj_list.append(Article(instance[1], instance[2], instance[3], instance[4], instance[5]))
                elif instance[0] == 'Podcast':
                    obj_list.append(Podcast(instance[1], instance[2], instance[3], instance[4], instance[5]))
    except FileNotFoundError:
        print(f"Warning: File '{filename}' not found.")
    return obj_list


book1 = Book('B001', 'Deep Learning', 2018, 'Ian Goodfellow', 775)
book2 = Book('B002', 'Machine Learning', 2018, 'Dean Goodfellow', 700)

art1 = Article('A101', 'Quantum Computing', 2022, 'Nature', '10.1234/qc567')
art2 = Article('A102', 'Mathematical Computing', 2020, 'Nature', '10.5678/qc567')

podcast1 = Podcast('P301', 'TechTalk AI', 2023, 'Jane Doe', 45)
podcast2 = Podcast('P302', 'TechTalk Nature', 2022, 'John Doe', 40)

items = [book1, book2, art1, art2, podcast1, podcast2]

save_to_file(items, 'archive.txt')

items = load_from_file('archive.txt')  

print("Loaded items from file:")
for item in items:
    print(item) 

print("\nAll archive items that are published in the last 5 years:")
for item in items:
    if item.is_recent(5):
        print(item)

print("\nAll archive items that have DOI starting with '10.1234' :")
for item in items:
    if isinstance(item,Article) and item.doi.startswith('10.1234'):
        print(item)


