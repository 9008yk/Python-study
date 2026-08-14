import main
# print(type(main.app))   # FastAPI 实例
# print(main.app.routes)
from fastapi import Route, APIRoute

main.app.routes=[
 Route(path='/openapi.json', name='openapi', methods=['GET', 'HEAD']),
 Route(path='/docs', name='swagger_ui_html', methods=['GET', 'HEAD']), 
 Route(path='/docs/oauth2-redirect', name='swagger_ui_redirect', methods=['GET', 'HEAD']), 
 Route(path='/redoc', name='redoc_html', methods=['GET', 'HEAD']), 
 APIRoute(path='/', name='read_root', methods=['GET']), 
 APIRoute(path='/todos', name='list_todos', methods=['GET']), 
 APIRoute(path='/todos', name='create_todo', methods=['POST']), 
 APIRoute(path='/todos/{todo_id}', name='get_todo', methods=['GET']), 
 APIRoute(path='/todos/{todo_id}', name='update_todo', methods=['PUT']), 
 APIRoute(path='/todos/{todo_id}', name='delete_todo', methods=['DELETE'])
 ]