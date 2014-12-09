# 3rd-party modules
from lxml.builder import E

# local module
from jnpr.junos.cfg import Resource
from jnpr.junos import jxml as JXML


class PrefixListItem(Resource):

    """
    [edit policy-options prefix-list <name> prefix-list-item <item> ]

    Resource name: str
      <name> is the prefix-list name
    """

    # there are no properties, since the name is the actual data

    PROPERTIES = []

    # -----------------------------------------------------------------------
    # XML readers
    # -----------------------------------------------------------------------

    def _xml_at_top(self):
        return E('policy-options', E('prefix-list', 
                E.name(self.P.name),
                E('prefix-list-item', E.name(self._name))
            ))

    def _xml_at_res(self, xml):
        return xml.find('.//prefix-list-item')

    def _xml_to_py(self, has_xml, has_py):
        Resource._r_has_xml_status(has_xml, has_py)

    # -----------------------------------------------------------------------
    # Manager List, Catalog
    # -----------------------------------------------------------------------

    def _r_list(self):
        # the key list comes from the parent object.
        self._rlist = self.P['$prefix_list_items']

    def _r_catalog(self):
        # no catalog but the keys
        self._rcatalog = dict((k, None) for k in self.list)

