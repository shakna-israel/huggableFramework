import hug
from bottle import template

@hug.get('/happy_birthday', output=hug.output_format.html, versions=1)
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return template('<b>Happy {{age}} Birthday, {{name}}</b>', age=age, name=name).format('HTML')

@hug.get('/happy_birthday', output=hug.output_format.html, versions=range(2, 5))
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return template('<b>Happy Birthday, {{name}}, on your {{age}}nd birthday!</b>', age=age, name=name).format('HTML')
