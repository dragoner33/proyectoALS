from google.appengine.ext import ndb

from publicacion import Publicacion


class Comentario(ndb.Model):
    texto = ndb.StringProperty(required=True)
    fechaC = ndb.DateProperty(indexed=True, auto_now_add=True)
    horaC = ndb.TimeProperty(auto_now_add=True)
    clave_publicacion = ndb.KeyProperty(kind=Publicacion)
    email_creador = ndb.StringProperty(required=True)

    @staticmethod
    def recupera_para(req):
        try:
            id_publicacion = req.GET["id"]
        except:
            id_publicacion = ""
        if id_publicacion:
            clave_publicacion = ndb.Key(urlsafe=id_publicacion)
            comentarios = Comentario.query(Comentario.clave_publicacion == clave_publicacion).order(-Comentario.fechaC)
            return (clave_publicacion.get(), comentarios)
        else:
            print("ERROR: publicacion no encontrada")

    def recuperar_email_comentario(req):
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

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except:
            id = ""

        return ndb.Key(urlsafe=id).get()