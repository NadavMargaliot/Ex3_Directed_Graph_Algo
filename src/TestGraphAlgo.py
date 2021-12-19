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
        self.assertEqual(2 , alg.get_graph().e_size())
        self.assertEqual(3 , alg.get_graph().v_size())









if __name__ == '__main__':
    unittest.main()

