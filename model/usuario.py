from google.appengine.ext import ndb

from google.appengine.api import users


class Usuario(ndb.Model):
    email = ndb.TextProperty(indexed=True)
    added = ndb.DateProperty(auto_now_add=True, indexed=True)

def create(usr):
    toret = Usuario()

    toret.email = usr.email()
    return toret


def create_empty_user():

    return Usuario(email="")


@ndb.transactional
def update(usr):
    return usr.put()


def retrieve(usr):
    toret = None

    if usr:
        usr_email = usr.email()
        found_users = Usuario.query(Usuario.email == usr_email).order(-Usuario.added)

        if found_users.count() == 0 and users.is_current_user_admin():
            toret = create(usr)
            update(toret)
        else:
            if found_users.count() == 0:
                toret = create(usr)
                update(toret)
            else:
                toret = found_users.iter().next()
                toret.usr = usr

    return toret