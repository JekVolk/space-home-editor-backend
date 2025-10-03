from drf_spectacular.utils import extend_schema, OpenApiParameter


def path_params(*params):
    return extend_schema(
        parameters=[OpenApiParameter(p, int, OpenApiParameter.PATH) for p in params]
    )