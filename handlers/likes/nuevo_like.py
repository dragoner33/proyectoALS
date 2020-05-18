# coding: utf-8
# Nuevo comentario

import webapp2
import time

from webapp2_extras import jinja2

from google.appengine.ext import ndb

from model.comentario import Comentario

from webapp2_extras.users import users

import model.usuario as usr_mgt

from model.likes import Like



class NuevoLikeHandler(webapp2.RequestHandler):

    def get(self):
        id_publicacion= self.request.GET["id"]
        user = users.get_current_user()
        usuario = usr_mgt.retrieve(user)



        like = Like( id_publicacion=ndb.Key(urlsafe = id_publicacion), email = usuario.email)
        like.put()
        time.sleep(1)
        return self.redirect("/foro")


app = webapp2.WSGIApplication([
    ('/foro/publicaciones/likes', NuevoLikeHandler)
], debug=True)