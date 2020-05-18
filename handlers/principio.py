
import webapp2
from webapp2_extras import jinja2

from webapp2_extras.users import users
import model.usuario as usr_mgt


class PrincipioHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        user = usr_mgt.retrieve(usr)

        if usr and user:
            self.redirect("/foro")
            return
        else:
            url_usr = users.create_login_url("/foro")

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "usr": usr,
            "url_usr": url_usr,
        }

        self.response.write(jinja.render_template("principio.html", **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/', PrincipioHandler)
], debug=True)