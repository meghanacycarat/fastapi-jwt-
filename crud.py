from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
  {
    "id": 1,
    "title": "The Whispering Grove",
    "author": "Elena Hart",
    "pages": 324,
    "publish_date": "2018-06-12"
  },
  {
    "id": 2,
    "title": "Chronicles of the Silver Sea",
    "author": "Marcus Flint",
    "pages": 289,
    "publish_date": "2020-11-03"
  },
  {
    "id": 3,
    "title": "Shadows of the Forgotten City",
    "author": "Priya Nandesh",
    "pages": 412,
    "publish_date": "2016-09-27"
  },
  {
    "id": 4,
    "title": "Beyond the Iron Gate",
    "author": "Liam Cross",
    "pages": 350,
    "publish_date": "2019-02-14"
  },
  {
    "id": 5,
    "title": "The Last Ember",
    "author": "Sofia Greer",
    "pages": 276,
    "publish_date": "2021-05-18"
  },
  {
    "id": 6,
    "title": "Nebula Rising",
    "author": "Arjun Mehta",
    "pages": 398,
    "publish_date": "2017-08-09"
  },
  {
    "id": 7,
    "title": "The Painted Horizon",
    "author": "Clara Wilde",
    "pages": 231,
    "publish_date": "2015-03-22"
  },
  {
    "id": 8,
    "title": "Fragments of Eternity",
    "author": "Jonas Reed",
    "pages": 487,
    "publish_date": "2022-10-07"
  },
  {
    "id": 9,
    "title": "The Storm Weaver",
    "author": "Nidhi Rangan",
    "pages": 362,
    "publish_date": "2014-12-30"
  },
  {
    "id": 10,
    "title": "Valley of Echoes",
    "author": "Darren Cole",
    "pages": 305,
    "publish_date": "2023-04-11"
  }
]
app = FastAPI()

@app.get("/book")
def get_book():
    return books

class Book(BaseModel):
    id : int
    title : str
    author : str
    pages : int
    publish_date: str
    

@app.post("/add_book")
def create(book : Book):
    new_book =book.model_dump()
    books.append(new_book)
    return {"append successfull",200}
    
@app.get("/book/{id}")
def get_book_byid(id : int):
    for book in books:
        if book['id'] == id:
            return book  
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found") 


class BookUpdate(BaseModel):
    title: str
    author: str
    publish_date : str
    pages : int

@app.put("/book/update/{id}")
def book_update(id : int , bookupdate : BookUpdate):
    for book in books:
        print("book")
        if book["id"] == id:
            book["title"] = bookupdate.title
            book["author"] = bookupdate.author
            book["pages"] = bookupdate.pages
            book["publish_date" ] = bookupdate.publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")      

@app.delete("/book/{id}")
def delete_book(id:int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
        return {"message :":"book deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "book not foind")
    
  