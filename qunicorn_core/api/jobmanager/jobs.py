"""Module containing the routes of the Taskmanager API."""

from ..models.jobs import JobIDSchema
from ..models.jobs import JobRegisterSchema
from typing import Dict
from flask.helpers import url_for
from flask.views import MethodView
from dataclasses import dataclass
from http import HTTPStatus

from .root import JOBMANAGER_API


@dataclass
class JobID:
    id: str
    description: str
    taskmode: int


@dataclass
class JobRegister:
    circuit: str
    provider: str
    qpu: str
    credentials: dict
    shots: int
    circuit_format: str


@JOBMANAGER_API.route("/")
class JobIDView(MethodView):
    """Tasks endpoint for collection of all tasks."""

    @JOBMANAGER_API.response(HTTPStatus.OK, JobIDSchema())
    def get(self):
        """Get registered task list."""
        return [
            JobID(
                id=url_for("jobmanager-api.JobIDView", _external=True),
                description="Placeholder for Tasks",
                taskmode=0,
            )
        ]

    @JOBMANAGER_API.arguments(JobRegisterSchema(), location="json")
    @JOBMANAGER_API.response(HTTPStatus.OK, JobIDSchema())
    def post(self, new_task_data: dict):
        """Create/Register new job."""
        
        pass


@JOBMANAGER_API.route("/<string:job_id>/")
class JobDetailView(MethodView):
    """Tasks endpoint for a single task."""

    @JOBMANAGER_API.response(HTTPStatus.OK, JobIDSchema())
    def get(self, job_id: str):
        """Get the urls for the taskmanager api for tasks control."""
        
        pass

    @JOBMANAGER_API.arguments(JobRegisterSchema(), location="json")
    @JOBMANAGER_API.response(HTTPStatus.OK, JobIDSchema())
    def post(self, job_id: str):
        """Cancel a job execution via id."""
       
        pass
