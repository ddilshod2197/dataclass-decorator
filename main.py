from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    age: int

user = User(1, "John Doe", 30)
print(user)
```

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Book:
    title: str
    author: str
    pages: int
    reviews: List[str] = field(default_factory=list)

book = Book("Python Programming", "John Smith", 300)
book.reviews.append("Good book!")
print(book)
