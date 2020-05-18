# coding: utf-8
# Nuevo comentario

import webapp2
import time

from webapp2_extras import jinja2

from google.appengine.ext import ndb

from model.comentario import Comentario

from webapp2_extras.users import users

import model.usuario as usr_mgt



class NuevoComentarioHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
            "id_publicacion": self.request.GET["id"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_comentario.html",
                                  **valores_plantilla))

    def post(self):
        texto = self.request.get("edTexto", "")
        clave_publicacion= self.request.GET["id"]
        user = users.get_current_user()
        usuario = usr_mgt.retrieve(user)



        if (not (texto)):
            return self.redirect("/foro")
        else:
            comentario = Comentario(texto=texto, clave_publicacion=ndb.Key(urlsafe = clave_publicacion), email_creador = usuario.email)
            comentario.put()
            time.sleep(1)
            return self.redirect("/foro/publicaciones/comentarios?id=" +clave_publicacion)


app = webapp2.WSGIApplication([
    ('/foro/publicaciones/comentarios/nuevo', NuevoComentarioHandler)
], debug=True)