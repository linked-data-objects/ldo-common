"""
ldo.py
Implementation of Linked Data Object interfaces
A Linked Data Object is a self-contained data object which contains the following elements:
- Index - set of triples pointing to object elements and other objects, the well-known entry point of a LDO
- Data - RDF data and metadata according to some application schema or shape, also embedded links to external data
- Views - bindings to HTML with CSS templates and client side JS handlers
- Interfaces - bindings to APIs
- Controls - bindings to server side handlers, conditionally invoked by data and metadata operations
- Certificates - signed attestations to be used to mutually authenticate interactions with clients,
- Permissions - bindings of certificates to Views, Interfaces, or Controls
- ldo triples - triples to organize the LDO itself
- ldo ID - a LDO URI of the form ldo://<uuid>

Index => Data 
Bindings reference data e.g. WoT TD

"""

from rdflib import Graph, URIRef
from ldocommon import Ldoid, LdoTemplate

class Ldo():
    def __init__(self, rdf=None):
        # Could there be a case where an RDF constructor for a new LDO is supplied, without a ldoid?
        # there could be a graph constructor that may or may not have a ldoid
        if (None == rdf):
           # Make a new LDO with a fresh ID
           self._ldoid = Ldoid()
            self._ldoGraph = Graph(URIRef(self._ldoid))
            self._mergetriples(LdoTemplate) # merge in the ldo triples from the base template
        else:
            # Parse the RDF pointed to and create a LDO with the ID from the serialized LDO
            self._ldoGraph = Graph()
            self._ldoGraph.parse(rdf) # figure out content format, parse, and set graph identifier 
            self._ldoid = self._ldoGraph.__identifier
            

