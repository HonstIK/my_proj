import json

from flask import request

from . import create_app, database
from .models import Sharks

app = create_app()


@app.route('/', methods=['GET'])
def fetch():
    shark = database.get_all(Sharks)
    all_shark = []
    for shark in Sharks:
        new_shark = {
            "id": shark.id,
            "name": shark.name,
            "color": shark.color,
            "view": shark.view,
            "jaw": shark.jaw
        }

        all_sharks.append(new_shark)

    if (len(all_sharks) == 0):
        return json.dumps("No Sharks found"), 200
    else:
        return json.dumps(all_sharks), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    color = data['color']
    view = data['view']
    jaw = data['jaw']

    database.add_instance(Sharks, name=name, color=color, view=view, jaw=jaw)
    return json.dumps("Added"), 200


@app.route('/remove/<shark_id>', methods=['DELETE'])
def remove(shark_id):
    database.delete_instance(Sharks, id=shark_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<shark_id>', methods=['PATCH'])
def edit(shark_id):
    data = request.get_json()
    new_color = data['color']
    database.edit_instance(Sharks, id=shark_id, color=new_color, view=new_view)
    return json.dumps("Edited"), 200

@app.route('/bite',methods=['POST'])
def bite():
    view = data['view'] 
     jaw = data['jaw']
     name = data['name']

 database.add_instance(Sharks, name=name, view=view, jaw=jaw)
   return json.dumps("Bited"), 200