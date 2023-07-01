from marshmallow import Schema, fields, validate


class SignupInputSchema(Schema):
    """
    Defines the input schema for the CreateSignup mutation. It requires a name, email,
    and password. The name must be at least 4 characters long, and the password must be at least 6
    characters long.
    """

    name = fields.Str(required=True, validate=validate.Length(min=4))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


class LoginInputSchema(Schema):
    """
    Validates a dictionary with keys 'email' and 'password' where 'email'
    is a valid email address and 'password' is a string with a minimum
    length of 6 characters.
    """

    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
