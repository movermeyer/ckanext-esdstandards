import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.esdstandards.model import setup as model_setup
from ckanext.esdstandards.logic import (esd_function_autocomplete,
                                        esd_service_autocomplete,
                                        esd_auth,
                                        )


class ESDStandardsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IAuthFunctions)

    # IConfigurable

    def configure(self, config):
        model_setup()

    # IActions
    def get_actions(self):
        return {
            'esd_function_autocomplete': esd_function_autocomplete,
            'esd_service_autocomplete': esd_service_autocomplete,
        }

    # IAuthFunctions
    def get_auth_functions(self):
        return {
            'esd_function_autocomplete': esd_auth,
            'esd_service_autocomplete': esd_auth,
        }
