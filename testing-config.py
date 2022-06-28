import config

# get properties from the config file
my_api_key = getattr(config, 'api_key', 'no_key_found')
my_username = getattr(config, 'username', 'no_username_found')
my_password = getattr(config, 'password', 'no_password_found')

# get an invalid property from the config file
invalid_prop = getattr(config, 'test_bad_prop', 'no_property_found')

# print the properties retrieved from config.py
print(f'my_api_key = {my_api_key}')
print(f'my_username = {my_username}')
print(f'my_password = {my_password}')
print(f'invalid_prop = {invalid_prop}')
