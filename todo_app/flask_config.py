import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')

    TRELLO_API_KEY='0e8c5313a51ec05165d5846ccdb0b984'
    TRELLO_API_SECRET='02436356bfd15cc68db990ef94cc1f07ac2eca4526a7c3bc672201a588ea7879'
    TRELLO_BOARD_ID='60a21e48ae8d9a3a66965e3e'

    TRELLO_BASE_URL = 'https://api.trello.com/1'

    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
