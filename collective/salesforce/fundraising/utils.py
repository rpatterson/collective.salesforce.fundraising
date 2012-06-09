from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.salesforce.fundraising.controlpanel.interfaces import IFundraisingSettings


def get_settings():
    registry = getUtility(IRegistry)
    return registry.forInterface(IFundraisingSettings, False)

def sanitize_soql(s):
    """ Sanitizes a string that will be interpolated into single quotes
        in a SOQL expression.
    """
    return s.replace("'", "\\'")
