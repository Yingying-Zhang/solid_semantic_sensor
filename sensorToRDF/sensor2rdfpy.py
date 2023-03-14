
#from http.client import _DataType
import string
import pandas as pd 
from rdflib import Graph, Literal, RDF, URIRef, Namespace, BNode
from rdflib.namespace import XSD, SOSA, RDFS 
import urllib.parse 
from iribaker import to_iri
#import rdflib

filen = "C:/Users/Zhang/sciebo/Bo3/语义传感器数据/sensor/RawData.csv"
file=pd.read_csv(filen,sep=",",quotechar='"')

g = Graph()
#g.parse ('geo.owl', format='xml')
OBS = Namespace('http://mysensor.rwth-aachen.de/citysensor/')
LOC = Namespace('http://mysensor.rwth-aachen.de/location/')
SCHEMA = Namespace('http://mysensor.rwth-aachen.de/')
#GEO = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#location")
GEO = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')

g.bind('obs',OBS)
g.bind('loc',LOC)
g.bind('geo', GEO)

for index, row in file.iterrows():
    #observation as primary key
    observation = URIRef(to_iri(OBS + row['Observation']))
    observation_name = Literal(row['Observation'],datatype=XSD.string)

    sensor = BNode()
    #sensor = URIRef(to_iri(OBS + row['Sensor']))
    #sensor_name = Literal(row['Result'],datatype=XSD.string)

    result_info = Literal(row['Result'],datatype=XSD.integer)
    resulttime = Literal(row['ResultTime'],datatype=XSD.dateTime)

    platform = Literal(row['Platform'],datatype=XSD.string)

    location = BNode()

    lat = Literal(row['Latitude'],datatype=XSD.decimal)
    long = Literal(row['Longtitude'],datatype=XSD.decimal)


    g.add((observation,RDF.type, SOSA.Observation))
    g.add((observation,SOSA.hasResult,result_info))
    g.add((observation,SOSA.resultTime,resulttime))
    g.add((observation,SOSA.madeBySensor,sensor))

    g.add((sensor,GEO.haslocation,location))
    g.add((location,GEO.lat, lat))
    g.add((location,GEO.long, long))
    g.add((sensor,SOSA.isHostedBy,platform))



print(g.serialize(format='turtle'))
g.serialize(destination='C:/Users/Zhang/sciebo/Bo3/语义传感器数据/sensor/sensor2rdf.ttl',format='turtle')
