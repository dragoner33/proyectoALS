
import webapp2
from webapp2_extras import jinja2

from webapp2_extras.users import users

import model.usuario as usr_mgt

from model.publicacion import Publicacion

class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        usuario = usr_mgt.retrieve(usr)

        publicaciones = Publicacion.query().order(-Publicacion.fecha)

        if usr and usuario:
            url_usr = users.create_logout_url("/")

            jinja = jinja2.get_jinja2(app=self.app)
            valores_plantilla = {
                "url_usr": url_usr,
                "publicaciones": publicaciones,
                "usuario": usuario
            }
            print (usuario)
            self.response.write(jinja.render_template("index.html", **valores_plantilla))

        else:
            self.redirect("/")
            return

app = webapp2.WSGIApplication([
    ('/foro', MainHandler)
], debug=True)