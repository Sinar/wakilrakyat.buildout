import pandas
from z3c.relationfield import Relation
from plone import api
from zope import component
from zope.intid.interfaces import IIntIds
from z3c.relationfield import RelationValue
from plone import api
from plone.dexterity.utils import createContentInContainer
import transaction

portal_catalog = api.portal.get_tool('portal_catalog')
intids = component.getUtility(IIntIds)

logos = {'bn': 'Barisan Nasional',
         'bjis': 'Barisan Jemaah Islamiah Se-Malaysia',
         'dap': 'Parti Tindakan Demokratik',
         'par': 'Parti Alternative Rakyat',
         'pbds': 'Parti Bansa Dayak Sarawak',
         'pbk': 'Parti Bumi Kenyalang',
         'pbsm': 'Parti Bersama Malaysia',
         'pcm': 'Parti Cinta Malaysia',
         'pcs': 'Parti Cinta Sabah',
         'phrs': 'Parti Harapan Rakyat Sabah',
         'pas': 'Parti Islam Se-Malaysia',
         'pkr': 'Parti Keadilan Rakyat',
         'pkan': 'Parti Kerjasama Anak Negeri',
         'pms': 'Parti Maju Sabah',
         'pnp': 'Penang Front Party',
         'pprs': 'Parti Perpaduan Rakyat Sabah',
         'prgjp': 'Parti Rakyat Gabungan Jaksa Pendamai',
         'prn': 'Parti Reformasi Negeri',
         'prm': 'Parti Rakyat Malpaysia',
         'ppsta': 'Parti Solidariti Tanah Airku',
         'pprks': 'Pertubuhan Perpaduan Rakyat Kebangsaan Sabah',
         'psm': 'Parti Sosialis Malaysia',
         'warisan': 'Parti Warisan Sabah'
         }

df = pandas.read_csv('scripts/selangor.csv')

politicians_df = df[['person_name_en', 'on_behalf_of_name_ms', 'area_name_ms']]

#create candidates
for index, row in politicians_df.iterrows():

    name = row['person_name_en']
    party = row['on_behalf_of_name_ms']
    seat = row['area_name_ms']

    print name, party, seat

    folder = app.unrestrictedTraverse("Plone5/calon-calon")
    item = createContentInContainer(folder,
                                    'representative',
                                    title=name)

    for key, value in logos.iteritems():

        if party == value:
            item.logo = key
            print "Assigned Logo"

transaction.commit()
app._p_jar.sync()
