from google.appengine.ext import ndb

from publicacion import Publicacion


class Like(ndb.Model):
    id_publicacion = ndb.KeyProperty(kind=Publicacion)
    email = ndb.StringProperty(required=True)

    @staticmethod
    def recupera_likes(req):
        try:
            id_publicacion = req.GET["id"]
        except:
            id_publicacion = ""
        if id_publicacion:
            clave_publicacion = ndb.Key(urlsafe=id_publicacion)
            likes = Like.query(Like.id_publicacion == clave_publicacion)
            return (clave_publicacion.get(), likes)
        else:
            print("ERROR: publicacion no encontrada")
