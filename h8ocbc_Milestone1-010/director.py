"""
This is the directors module and supports all the REST actions for the
directors data
"""

from flask import make_response, abort
from config import db
from models import Director, DirectorSchema, Movie


def read_all():
    """
    This function responds to a request for /api/directors
    with the complete lists of director
    :return:        json string of list of director
    """
    # Create the list of director from our data
    director = Director.query.order_by(Director.id).limit(10)

    # Serialize the data for the response
    director_schema = DirectorSchema(many=True)
    data = director_schema.dump(director)
    return data


def read_one(id):
    """
    This function responds to a request for /api/director/{id}
    with one matching director from director
    :param id:   Id of director to find
    :return:            director matching id
    """
    # Build the initial query
    director = (
        Director.query.filter(Director.id == id)
        .outerjoin(Movie)
        .one_or_none()
    )

    # Did we find a director?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for Id: {id}")


def create(director):
    """
    This function creates a new director in the director structure
    based on the passed in director data
    :param director:  director to create in director structure
    :return:        201 on success, 406 on director exists
    """
    name = director.get("name")
    gender = director.get("gender")
    uid = director.get("uid")
    department = director.get("department")

    existing_director = (
        Director.query.filter(Director.name == name)
        .one_or_none()
    )

    # Can we insert this director?
    if existing_director is None:

        # Create a director instance using the schema and the passed in director
        schema = DirectorSchema()
        new_director = schema.load(director, session=db.session)

        # Add the director to the database
        db.session.add(new_director)
        db.session.commit()

        # Serialize and return the newly created director in the response
        data = schema.dump(new_director)

        return data, 201

    # Otherwise, nope, director exists already
    else:
        abort(409, f"Director {name} exists already")


def update(id, director):
    """
    This function updates an existing director in the director structure
    :param director_id:   Id of the director to update in the director structure
    :param director:      director to update
    :return:            updated director structure
    """
    # Get the director requested from the db into session
    update_director = Director.query.filter(
        Director.id == id
    ).one_or_none()

    # Did we find an existing director?
    if update_director is not None:

        # turn the passed in director into a db object
        schema = DirectorSchema()
        update = schema.load(director, session=db.session)

        # Set the id to the director we want to update
        update.id = update_director.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated director in the response
        data = schema.dump(update_director)

        return data, 200

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for Id: {id}")


def delete(id):
    """
    This function deletes a director from the director structure
    :param director_id:   Id of the director to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the director requested
    director = Director.query.filter(Director.id == id).one_or_none()

    # Did we find a director?
    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director {id} deleted", 200)

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"director not found for Id: {id}")