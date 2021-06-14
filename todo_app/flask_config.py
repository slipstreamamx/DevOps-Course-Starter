import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')

    TRELLO_API_KEY=
    TRELLO_API_SECRET=
    TRELLO_BOARD_ID=

    TRELLO_BASE_URL = 'https://api.trello.com/1'

    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
