import unittest
from Traingles import sides_triangles, angle_triangles

class TestTriangles(unittest.TestCase):
    def test_sides_triangle1(self):
        self.assertEqual(sides_triangles(1,1,1), 'The triangle type = equilateral triangle')
    def test_sides_triangle2(self):
        self.assertEqual(sides_triangles(5,7,3), 'The triangle type = scalene triangle')
    def test_sides_triangle3(self):
        self.assertEqual(sides_triangles(10,10,19), 'The triangle type = isosceles triangle')
    def test_sides_triangle4(self):
        self.assertEqual(sides_triangles(16, 30, 34), 'The triangle type = right-angle triangle')
    def test_sides_triangle5(self):
        with self.assertRaises(ValueError):
            sides_triangles(-1, 4,2)
    def test_sides_triangle6(self):
        with self.assertRaises(ValueError):
            sides_triangles(16, -30, 35)
    def test_sides_triangle7(self):
        with self.assertRaises(ValueError):
            sides_triangles(16, 30,-34)
    def test_sides_triangle8(self):
        with self.assertRaises(ValueError):
            sides_triangles(5, 1, 3)
    def test_sides_triangle9(self):
        with self.assertRaises(ValueError):
            sides_triangles(5, 10, 1)
    def test_sides_triangle10(self):
        with self.assertRaises(ValueError):
            sides_triangles(15, 10, 1)
    def test_sides_triangle11(self):
        with self.assertRaises(ValueError):
            sides_triangles(0, 7, 1)
    def test_sides_triangle12(self):
        with self.assertRaises(ValueError):
            sides_triangles(15, 0, 1)
    def test_sides_triangle13(self):
        with self.assertRaises(ValueError):
            sides_triangles(15, 12, 0)
    def test_sides_triangle14(self):
        with self.assertRaises(ValueError):
            sides_triangles(0, 0, 0)

if __name__ == '__main__':
    unittest.main()