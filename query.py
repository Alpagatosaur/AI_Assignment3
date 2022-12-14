from rdflib import Graph

g = Graph()
# read ttl
g.parse("pressure.ttl", format='ttl')

q = """

    SELECT *
    WHERE {
        ?p sosa:hasSimpleResult ?reading .

        ?p sosa:resultTime ?dt .
    }
    ORDER BY ?dt
"""

for r in g.query(q):
    print(r["dt"], "|", r["reading"])

"""
2022-12-03T20:36:12+00:00 | 1199.12
2022-12-03T20:36:13+00:00 | 1201.64
2022-12-03T20:36:14+00:00 | 1198.06
2022-12-03T20:36:15+00:00 | 1199.01
2022-12-03T20:36:16+00:00 | 1199.31
2022-12-03T20:36:17+00:00 | 1198.74
2022-12-03T20:36:18+00:00 | 1201.20
2022-12-03T20:36:19+00:00 | 1200.13
2022-12-03T20:36:20+00:00 | 1200.50
2022-12-03T20:36:21+00:00 | 1199.99
"""