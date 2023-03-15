from app.api import bp 
from app import db
from flask import request
from flask_login import current_user, login_required
from app.models import List, Task
from flask_restful import Resource
class Lists(Resource):
    @login_required
    def post(self):
        if List.query.filter_by(author=current_user).count() > 21:
            return {'error': "You have reached lists limit!"}
        list_name = request.json['list_name']
        if not list_name:
            return {"error": "List name can't be empty!"}
        if len(list_name) > 32:
            return {'error': "This name is too long."}
        the_same_list = List.query.filter_by(author=current_user, name=list_name).first()
        if the_same_list:
            return {'error': "Lists can't have the same names!"}
        new_list = List(name=list_name, author=current_user)
        db.session.add(new_list)
        db.session.commit()
        return {}, 201
    @login_required
    def put(self):
        old_name = request.json['old_name']
        new_name = request.json['new_name']
        if not new_name:
            return {'error': "List name can't be empty!"}
        if len(new_name) > 32:
            return {'error': "This name is too long."}
        if new_name == old_name:
            return {}, 304
            return {}, 200
        the_same_list = List.query.filter_by(name=new_name, author=current_user).first()
        if the_same_list:
            return{'error': "Lists can't have the same names!"}
# -94,7 +94,7 @@ def put(self):
        if len(new_name) > 64:
            return {'error': "This task is too long."}
        if new_name == old_name:
            return {}, 304
            return {}, 200
        active_list = List.query.filter_by(name=active_list_name, author=current_user).first_or_404()
        task_to_edit = Task.query.filter_by(name=old_name, parent_list=active_list).first_or_404()
        task_to_edit.name = new_name
# -115,7 +115,6 @@ def delete(self):
class Display_list(Resource):
    @login_required
    def post(self):
        print('proba')
        list_name = request.json['list_name']
        active_list = List.query.filter_by(author=current_user, name=list_name).first_or_404()
        tasks = [[task.name, task.is_done] for task in active_list.tasks]