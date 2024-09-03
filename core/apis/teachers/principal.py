from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Teacher
from .schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of All teachers"""
    teachers_list = Teacher.list_all_teachers()
    teachers_list_dump = TeacherSchema().dump(teachers_list, many=True)
    return APIResponse.respond(data=teachers_list_dump)