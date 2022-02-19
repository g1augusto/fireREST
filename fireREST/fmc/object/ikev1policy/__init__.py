from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource


class Ikev1Policy(Resource):
    PATH = '/object/ikev1policies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
