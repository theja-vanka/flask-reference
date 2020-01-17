from cassandra.cqlengine.management import sync_table
from models.person import Person
from cassandra.cqlengine import connection
from cassandra.auth import PlainTextAuthProvider
from cassandradb import CassandraSession

cassObj = CassandraSession()

auth_provider = PlainTextAuthProvider(username='cassandra', password='N4udsKzcujSx')
connection.set_session(cassObj.session)

sync_table(Person)