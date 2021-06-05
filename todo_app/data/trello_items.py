from flask import config, current_app as app
from todo_app.data.todo_items import Item
from flask.globals import request
from flask.wrappers import Request, Response
import requests


def get_auth_params():
    return {'key': app.config['TRELLO_API_KEY'], 'token': app.config['TRELLO_API_SECRET']}


def build_url(endpoint):
    return app.config['TRELLO_BASE_URL'] + endpoint


def build_params(params={}):
    full_params = get_auth_params()
    full_params.update(params)
    return full_params


def get_boards():
    params = build_params()
    url = build_url('/members/me/boards')

    response = requests.get(url, params = params)
    boards = response.json()

    return boards


def get_board(name):
    boards = get_boards()
    return next((board for board in boards if board['name'] == name), None)


def get_lists():
    params = build_params({'cards': 'open'})
    url = build_url('/boards/%s/lists' % app.config['TRELLO_BOARD_ID'])

    response = requests.get(url, params = params)
    print(response)
    lists = response.json()

    return lists


def get_list(name):
    lists = get_lists()
    return next((list for list in lists if list['name'] == name), None)


def get_items():
    lists = get_lists()
    items = []
    for card_list in lists:
        for card in card_list['cards']:
            items.append(Item.fromTrelloCard(card, card_list))
    return items


def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(name, desc, due):
    todo_list = get_list('To Do')

    url= build_url('/cards')
    params = build_params({'name': name,'desc': desc, 'due':due, 'idList':todo_list['id']})

    response = requests.post(url, params = params)
    card = response.json()

    return Item.fromTrelloCard(card, todo_list)


def move_card_to_list(card_id, list):
    url = build_url('/cards/%s' % card_id)
    params = build_params({'idList': list['id']})
    response = requests.put(url, params = params)
    card = response.json()

    return card


def start_item(id):
    doing_list = get_list('Doing')
    card = move_card_to_list(id, doing_list)

    return Item.fromTrelloCard(card, doing_list)


def complete_item(id):
    done_list = get_list('Done')
    card = move_card_to_list(id, done_list)

    return Item.fromTrelloCard(card, done_list)


def uncomplete_item(id):
    todo_list = get_list('To Do')
    card = move_card_to_list(id, todo_list)

    return Item.fromTrelloCard(card, todo_list)