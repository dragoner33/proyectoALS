#coding: utf-8
# Eliminar comentario

import webapp2
import time


from model.comentario import Comentario

class EliminaComentarioHandler(webapp2.RequestHandler):
    def get(self):
        comentario = Comentario.recupera(self.request)
        comentario.key.delete()
        time.sleep(1)
        return self.redirect("/foro")



app = webapp2.WSGIApplication([
    ('/foro/publicaciones/comentarios/elimina', EliminaComentarioHandler)
], debug=True)