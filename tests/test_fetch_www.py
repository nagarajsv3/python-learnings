from unittest.mock import patch
from app.fetch_www import parse

@patch("app.fetch_www.bob_net")
@patch("app.fetch_www.fetch_net")
def test_parse(fetch_net_mock, bob_net_mock):
    fetch_net_mock.return_value = "def"
    bob_net_mock.return_value = "ppp"
    assert parse() == "def ----ppp"

     