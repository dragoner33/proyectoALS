#coding: utf-8
# Eliminar asinatura

import webapp2
import time


from model.publicacion import Publicacion

class EliminaPublicacionHandler(webapp2.RequestHandler):
    def get(self):
        publicacion = Publicacion.recupera(self.request)
        publicacion.key.delete()
        time.sleep(1)
        return self.redirect("/foro")



app = webapp2.WSGIApplication([
    ('/foro/publicaciones/elimina', EliminaPublicacionHandler)
], debug=True)