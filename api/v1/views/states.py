#!/usr/bin/python3
"""States module"""

from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """Retrieve the list of all State objects"""
    states_list = []
    for state in storage.all(State).values():
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieve a State object"""
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Delete a State object"""
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Create a new State"""
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    data = request.get_json()
    new_state = State(**data)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update a State object"""
    state = storage.get(State, state_id)
    if state:
        if not request.get_json():
            abort(400, "Not a JSON")
        data = request.get_json()
        for key, value in data.items():
            if key != "id" and key != "created_at" and key != "updated_at":
                setattr(state, key, value)
        storage.save()
        return jsonify(state.to_dict()), 200
    abort(404)
