"""
blog views definitions
"""
# from pyramid.response import Response
from pyramid.view import view_config

# from sqlalchemy.exc import DBAPIError


@view_config(
    route_name='entry',
    request_method="GET",
    renderer='../templates/entries/show.jinja2'
)
def entry_view(request):
    ''' Shows the full content of the entry
    '''

    return {}


@view_config(
    route_name='tag',
    request_method="GET",
    renderer='../templates/tag_results.jinja2'
)
def tag_view(request):
    """
    Shows the entries related to a single tag
    """
    return {}
