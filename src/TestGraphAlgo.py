import unittest

from src.DiGraph import DiGraph
from src.MyNode import MyNode
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_save_to_json(self):
        v1 = MyNode(1, None)
        v2 = MyNode(2, None)
        v3 = MyNode(3, None)
        graph = DiGraph()
        graph.add_node(v1.id, v1.location)
        graph.add_node(v2.id, v2.location)
        graph.add_node(v3.id, v3.location)
        graph.add_edge(1, 2, 4)
        graph.add_edge(1, 3, 5)
        g = GraphAlgo(graph)
        g.save_to_json("jsonTest")

    def test_load_from_json(self):
        v1 = MyNode(1, None)
        v2 = MyNode(2, None)
        v3 = MyNode(3, None)
        graph = DiGraph()
        graph.add_node(v1.id, v1.location)
        graph.add_node(v2.id, v2.location)
        graph.add_node(v3.id, v3.location)
        graph.add_edge(1, 2, 4)
        graph.add_edge(1, 3, 5)
        alg = GraphAlgo(graph)

        alg.load_from_json("/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/src/jsonTest")
        self.assertEqual(2, alg.get_graph().e_size())
        self.assertEqual(3, alg.get_graph().v_size())

    def test_shortest_path(self):
        graph = DiGraph()
        a = MyNode(1, None)
        b = MyNode(2, None)
        c = MyNode(3, None)
        d = MyNode(4, None)
        e = MyNode(5, None)
        f = MyNode(6, None)
        g = MyNode(7, None)
        graph.add_node(a.id,a.location)
        graph.add_node(b.id, b.location)
        graph.add_node(c.id, c.location)
        graph.add_node(d.id, d.location)
        graph.add_node(e.id, e.location)
        graph.add_node(f.id, f.location)
        graph.add_node(g.id, g.location)
        graph.add_edge(a.id,c.id,3)
        graph.add_edge(a.id,f.id,2)
        graph.add_edge(f.id,c.id,2)
        graph.add_edge(c.id,d.id,4)
        graph.add_edge(c.id,e.id,1)
        graph.add_edge(f.id,e.id,3)
        graph.add_edge(e.id,b.id,2)
        graph.add_edge(f.id,b.id,6)
        graph.add_edge(f.id,g.id,5)
        graph.add_edge(g.id,b.id,2)
        graph.add_edge(d.id,b.id,1)
        alg = GraphAlgo(graph)
        self.assertEqual((6,[1,3,5,2]),alg.shortest_path(a.id,b.id))



if __name__ == '__main__':
    unittest.main()
