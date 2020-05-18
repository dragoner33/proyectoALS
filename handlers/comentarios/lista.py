import webapp2

from model.comentario import Comentario

from webapp2_extras import jinja2

from webapp2_extras.users import users

import model.usuario as usr_mgt



class ListaComentariosHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        usuario = usr_mgt.retrieve(usr)
        url_usr = users.create_logout_url("/")

        publicacion, comentarios = Comentario.recupera_para(self.request)

        valores_plantilla = {
            "url_usr": url_usr,
            "comentarios": comentarios,
            "publicacion": publicacion,
            "usuario": usuario
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_comentarios.html", **valores_plantilla))




app = webapp2.WSGIApplication([
    ('/foro/publicaciones/comentarios', ListaComentariosHandler)
], debug=True)