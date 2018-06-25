# -*- coding: utf-8 -*-
from rest_framework_jwt.utils import jwt_payload_handler as jwt_payload_handler_v0


def jwt_payload_handler(user):
	payload = jwt_payload_handler_v0(user)
	payload["permissions"] = list(user.get_all_permissions())
	return payload