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

df = pandas.read_csv('scripts/selangor.csv')
politicians_df = df[['person_name_en', 'on_behalf_of_name_ms', 'area_name_ms']]

#assign seats
for index, row in politicians_df.iterrows():

    name = row['person_name_en']
    seat = row['area_name_ms']


    state_seat = portal_catalog.unrestrictedSearchResults(
            Title=seat, portal_type='State Seat')
    
    rep = portal_catalog.unrestrictedSearchResults(
            Title=name, portal_type='representative')

    if rep:
        rep_obj = rep[0].getObject()

        if state_seat:
            seat_obj = state_seat[0].getObject()
        
            rep_intid = intids.getId(rep_obj)
    
            seat_obj.representative.append(RelationValue(rep_intid))
    
            seat_obj.representative = seat_obj.representative

            print name
            print "Assigned Seat"
            print rep_intid
            print seat_obj.representative
        
transaction.commit()
app._p_jar.sync()
