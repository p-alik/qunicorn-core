"""Module containing all API schemas for tasks in the Taskmanager API."""

import marshmallow as ma
from marshmallow import fields, ValidationError
from ..util import MaBaseSchema

__all__ = ["TaskIDSchema", "TaskRegisterSchema"]


class CircuitField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, str) or isinstance(value, list):
            return value
        else:
            raise ValidationError("Field should be str or list")


class TaskRegisterSchema(MaBaseSchema):
    circuit = CircuitField(required=True)
    provider = ma.fields.Str(required=True)
    qpu = ma.fields.Str(required=True)
    credentials = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Str(), required=True
    )
    shots = ma.fields.Int(required=False)
    noise_model = ma.fields.Str(required=False)
    only_measurement_errors = ma.fields.Boolean(required=False)
    circuit_format = ma.fields.Str(required=False)
    parameters = ma.fields.List(ma.fields.Float(), required=False)


class TaskIDSchema(MaBaseSchema):
    uid = ma.fields.Url(required=True, allow_none=False, dump_only=True)
    description = ma.fields.String(required=True, allow_none=False, dump_only=True)
    taskmode = ma.fields.Int(required=True, allow_none=False, dump_only=True)