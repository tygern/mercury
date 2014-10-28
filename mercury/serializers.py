from flask import jsonify


def serialize(entity):
    return jsonify(entity.serialize)


def serialize_list(key, entity_list):
    return jsonify({
        key: [entity.serialize for entity in entity_list]
    })
