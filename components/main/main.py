from reactpy import component, html
from ..todo_list.todo_list import todo_list_component

@component
def main():
  return html.div(
    todo_list_component()
  )