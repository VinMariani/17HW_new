from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import GenreSchema

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        read_json = request.json
        genre_service.create(read_json)

        return "", 201


@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    def delete(self, gid: int):
        genre_service.delete(gid)
        return '', 204

    def put(self, gid: int):  # замена данных
        read_json = request.json
        read_json['id'] = gid
        genre_service.update(read_json)

        return '', 204

    def patch(self, gid: int):
        read_json = request.json
        read_json['id'] = gid

        genre_service.update_partial(read_json)

        return '', 204
