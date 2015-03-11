import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.esdstandards.model import setup as model_setup


class ESDStandardsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurable)
#    plugins.implements(plugins.IActions)

    # IConfigurable

    def configure(self, config):
        model_setup()



