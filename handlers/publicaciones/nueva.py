#coding: utf-8
# Nueva publicación

import webapp2
import time

from webapp2_extras import jinja2

from google.appengine.ext import ndb

from model.publicacion import Publicacion

from webapp2_extras.users import users

import model.usuario as usr_mgt

class NuevaPublicacionHandler(webapp2.RequestHandler):
    def get(self):
        url_usr = users.create_logout_url("/")
        valores_plantilla = {
            "email_creador": self.request.GET["email"],
            "url_usr": url_usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nueva_publicacion.html",
            **valores_plantilla))

    def post(self):
        titulo = self.request.get("edTitulo", "")
        str_foto = self.request.get("edFoto", "")
        email_creador = self.request.GET["email"]

        try:
            foto = int(str_foto)
        except ValueError:
            foto = "null"

        if (not(titulo)):
            return self.redirect("/")
        else:
            publicacion = Publicacion(titulo = titulo, foto = foto, email_creador=email_creador)
            publicacion.put()
            time.sleep(1)
            return self.redirect("/foro?email=" +email_creador)



app = webapp2.WSGIApplication([
    ('/foro/publicaciones/nueva', NuevaPublicacionHandler)
], debug=True)