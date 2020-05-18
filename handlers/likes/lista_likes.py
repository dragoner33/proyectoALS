import webapp2

from model.likes import Like

from webapp2_extras import jinja2

from webapp2_extras.users import users

import model.usuario as usr_mgt



class ListaLikesHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        usuario = usr_mgt.retrieve(usr)
        url_usr = users.create_logout_url("/")

        publicacion, likes = Like.recupera_likes(self.request)


        valores_plantilla = {
            "url_usr": url_usr,
            "likes": likes,
            "usuario": usuario,
            "publicacion": publicacion
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_likes.html", **valores_plantilla))




app = webapp2.WSGIApplication([
    ('/foro/publicaciones/likes/lista', ListaLikesHandler)
], debug=True)