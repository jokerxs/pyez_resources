# 3rd-party modules
from lxml.builder import E

# module packages
from jnpr.junos.cfg import Resource
from jnpr.junos import jxml as JXML
from jnpr.junos.cfg.prefix_list_item import PrefixListItem


class PrefixList(Resource):

    """
    [edit policy-otions prefix-list <name>]

    Resource name: str
      <name> is the prefix-list name

    Manages resources:
      prefix_list_item, PrefixListItem
    """

    PROPERTIES = [
        '$prefix_list_items'      # read only names of prefix-list-items
    ]

    MANAGES = { 'prefix_list_item': PrefixListItem }

    # -----------------------------------------------------------------------
    # XML readers
    # -----------------------------------------------------------------------

    def _xml_at_top(self):
        return E('policy-options', E('prefix-list', E.name(self._name)))

    def _xml_at_res(self, xml):
        return xml.find('.//prefix-list')

    def _xml_to_py(self, has_xml, has_py):
        Resource._r_has_xml_status(has_xml, has_py)

        # prefix-list-item
        has_py['$prefix_list_items'] = [ item.text 
                    for item in has_xml.xpath('.//prefix-list-item/name') ]

    # -----------------------------------------------------------------------
    # Manager List, Catalog
    # -----------------------------------------------------------------------

    def _r_list(self):
        get = E('policy-options', E('prefix-list', JXML.NAMES_ONLY))
        got = self.R.get_config(get)
        self._rlist = [ name.text 
                    for name in got.xpath('.//prefix-list/name') ]
