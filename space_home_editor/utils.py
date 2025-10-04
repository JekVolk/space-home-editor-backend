from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

def path_params(*params):
    """
    Декоратор для ViewSet, який додає path-параметри:
    - для list / create → тільки передані params
    - для detail-ендпоінтів → params + 'id'

    Використання:
        @path_params()  # list: [], detail: ['id']
        @path_params("project_pk")  # list: ['project_pk'], detail: ['project_pk', 'id']
        @path_params("project_pk", "module_pk")  # list: ['project_pk','module_pk'], detail: [..., 'id']
    """
    list_parameters = [OpenApiParameter(p, int, OpenApiParameter.PATH) for p in params]

    # для detail-ендпоінтів додаємо 'id'
    detail_parameters = [OpenApiParameter(p, int, OpenApiParameter.PATH) for p in list(params) + ["id"]]

    return extend_schema_view(
        list=extend_schema(parameters=list_parameters),
        create=extend_schema(parameters=list_parameters),
        retrieve=extend_schema(parameters=detail_parameters),
        update=extend_schema(parameters=detail_parameters),
        partial_update=extend_schema(parameters=detail_parameters),
        destroy=extend_schema(parameters=detail_parameters),
    )
