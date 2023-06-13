from reactpy import component, html, hooks


@component
def list_item_component(id, inner_text, on_click):
    def click_action(event):
        on_click(inner_text)
    return html.li({"key": id, "on_click": click_action, "style": {
        "cursor": "pointer", "border": "1px solid #07C", 'padding': '1rem',
        'display': "block", "border-radius": "5px", 'max-width': "850px", "margin": "1.5rem 0.5rem"
    }}, inner_text)

@component
def data_list_component(items, filter_by_priority=None, sort_by_priority=False, handle_click=None):
    if filter_by_priority is not None:
        items = [i for i in items if i["priority"] <= filter_by_priority]
    if sort_by_priority:
        items = sorted(items, key=lambda i: i["priority"])
    list_item_elements = [list_item_component(i["id"], i["text"], handle_click) for i in items]
    return html.ul({
        'style': {
            'list-style': 'none'
        }
    }, list_item_elements)


@component
def todo_list_component():
    clicked_todo, set_clicked_todo = hooks.use_state('Select any task')
    tasks = [
        {"id": 0, "text": "Make breakfast", "priority": 0},
        {"id": 1, "text": "Feed the dog", "priority": 0},
        {"id": 2, "text": "Do laundry", "priority": 2},
        {"id": 3, "text": "Go on a run", "priority": 1},
        {"id": 4, "text": "Clean the house", "priority": 2},
        {"id": 5, "text": "Go to the grocery store", "priority": 2},
        {"id": 6, "text": "Do some coding", "priority": 1},
        {"id": 7, "text": "Read a book", "priority": 1},
    ]
    def handle_click(todo_name):
        set_clicked_todo(todo_name)
    return html.section(
        html.h1("My Todo List"),
        html.p(clicked_todo),
        data_list_component(tasks, filter_by_priority=1, sort_by_priority=True, handle_click=handle_click),
    )
