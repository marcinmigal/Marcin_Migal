from csv import reader
from flask import Flask
from flask_restful import Resource, Api


class CsvClass(Resource):
    def __init__(self, header, row) -> None:
        self.__dict__ = dict(zip(header, row))


def get_dicts_list(csv_file):
    with open(csv_file, encoding='utf-8') as read_obj:
        csv_list = list(reader(read_obj))
        return [CsvClass(csv_list[0], i).__dict__ for i in csv_list[1:]]


movies_list = get_dicts_list('movies.csv')
links_list = get_dicts_list('links.csv')
ratings_lists = get_dicts_list('ratings.csv')
tags_list = get_dicts_list('tags.csv')


class Movies(Resource):
    def get(self):
        return movies_list


class Links(Resource):
    def get(self):
        return links_list


class Ratings(Resource):
    def get(self):
        return ratings_lists


class Tags(Resource):
    def get(self):
        return tags_list


app = Flask(__name__)
api = Api(app)


api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Ratings, '/ratings')
api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
