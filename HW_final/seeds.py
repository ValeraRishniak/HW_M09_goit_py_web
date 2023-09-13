import json
from models import Author, Qoute
import connect



def load_json(file):
    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def post_authors(file):
    authors = load_json(file)

    for i in authors:
        post_author = Author(
            fullname=i["fullname"],
            born_date=i["born_date"],
            born_location=i["born_location"],
            bio=i["bio"],
        )
        post_author.save()


def post_qoutes(file):
    qoutes = load_json(file)

    for qoute in qoutes:
        # print(qoute)
        post_qoute = Qoute(
            author=[
                author.id
                for author in Author.objects()
                if author.fullname == qoute["author"]
            ],
            qoute=qoute["quote"],
            tags=qoute["tags"],
        )
        post_qoute.save()


if __name__ == "__main__":
    post_authors("authors.json")
    post_qoutes("quotes.json")
