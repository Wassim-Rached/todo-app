import pytest

def test_change_password(user_1):
    assert user_1.username == 'user_1'
    assert user_1.username == 'user_1'
    assert user_1.is_staff == False


