#here all the password related functions are written

from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)


def check_password(stored_password,provided_password):
    return check_password_hash(stored_password, provided_password)