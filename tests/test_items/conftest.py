import pytest

from django.contrib.auth.models import User

@pytest.fixture
def new_user_factory(db):
	def create_app_user(
		username ,
		password ,
		email='test@email.com',
		first_name='firstname',
		is_staff=False,
		is_superuser=False,
		is_active=True,
		):
		user = User.objects.create_user(
			username=username,
			email=email,
			password=password,
			first_name=first_name,
			is_active=is_active,
			is_staff=is_staff,
			is_superuser=is_superuser,
			)
		return user
	return create_app_user

@pytest.fixture
def user_1(new_user_factory):
	return new_user_factory('user_1', 'password')