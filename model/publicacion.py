from google.appengine.ext import ndb

from usuario import Usuario


class Publicacion(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    fecha = ndb.DateProperty(indexed=True,auto_now_add=True)
    hora = ndb.TimeProperty(auto_now_add=True)
    foto = ndb.BlobProperty(default="null")
    email_creador = ndb.StringProperty(required=True)


    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except:
            id = ""

        return ndb.Key(urlsafe=id).get()


    @staticmethod
    def recuperar_user(req):
        try:
            email_user = req.GET["email"]
        except:
            email_user = ""

        if email_user:
            email_creador = ndb.Key(urlsafe=email_user)
            publicaciones = Publicacion.query(Publicacion.email_creador == email_creador)
            return (email_creador.get(), publicaciones)
        else:
            print("ERROR: creador no encontrado")