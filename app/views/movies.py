from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        read_json = request.json
        movie_service.create(read_json)

        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):  # получение одного объекта
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def delete(self, mid: int):
        movie_service.delete(mid)
        return '', 204

    def put(self, mid: int):  # замена данных
        read_json = request.json
        read_json['id'] = mid
        movie_service.update(read_json)

        return '', 204

    def patch(self, mid: int):  # частичная замена данных
        read_json = request.json
        read_json['id'] = mid

        movie_service.update_partial(read_json)

        return '', 204
