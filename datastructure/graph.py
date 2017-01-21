# encoding: utf-8

"""
图算法
"""


class Vertex(object):
    """顶点"""
    def __init__(self, id):
        self._id = id
        self._connect_to = {}

    def add_neighbor(self, nbr, weight=0):
        self._connect_to[nbr] = weight

    def __unicode__(self):
        return u"%s connected to %s" (self._id, ''.join([x.id for x in self._connect_to]))

    @property
    def id(self):
        return str(self._id)

    def get_connections(self):
        return self._connect_to.keys()

    def get_weight(self, nbr):
        return self._connect_to.get(nbr, 0)


class Graph(object):
    """图"""
    def __init__(self):
        self._vert_list = {}
        self._vert_num = 0

    def add_vertext(self, key):
        self._vert_num += 1
        vertex = Vertex(key)
        self._vert_list[key] = vertex
        return vertex

    def get_vertex(self, key):
        return self._vert_list.get(key, None)

    def __contains__(self, key):
        return key in self._vert_list

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self._vert_list:
            self.add_vertext(from_vertex)

        if to_vertex not in self._vert_list:
            self.add_vertext(to_vertex)

        self._vert_list[from_vertex].add_neighbor(self._vert_list[to_vertex], cost)

    @property
    def vertices(self):
        return self._vert_list.keys()

    def __iter__(self):
        print "call iter"
        return iter(self._vert_list.values())


def test_graph():
    graph = Graph()
    for n in range(6):
        graph.add_vertext(n)

    print graph.vertices

    graph.add_edge(0,1,5)
    graph.add_edge(0,5,2)
    graph.add_edge(1,2,4)
    graph.add_edge(2,3,9)
    graph.add_edge(3,4,7)
    graph.add_edge(3,5,3)
    graph.add_edge(4,0,1)
    graph.add_edge(5,4,8)
    graph.add_edge(5,2,1)

    for v in graph:
        for w in v.get_connections():
            print "(%s->%s)" % (v.id, w.id)
