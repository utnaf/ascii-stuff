import unittest
from ddt import ddt, data, unpack
from asciimage import image_processor

@ddt
class TestDecideDimensions(unittest.TestCase):
    @unpack
    @data({
        'image_dims': (100,50),
        'max_dims': (40,30),
        'expected_new_dims': (40,20)
    },{
        'image_dims': (40,20),
        'max_dims': (40,30),
        'expected_new_dims': (40,20)
    },{
        'image_dims': (1000,2000),
        'max_dims': (40,30),
        'expected_new_dims': (15,30)
    },{
        'image_dims': (10,3),
        'max_dims': (40,30),
        'expected_new_dims': (10,3)
    },{
        'image_dims': (100,100),
        'max_dims': (40,30),
        'expected_new_dims': (30,30)
    },{
        'image_dims': (100,99),
        'max_dims': (40,30),
        'expected_new_dims': (30,30)
    },{
        'image_dims': (99,100),
        'max_dims': (40,30),
        'expected_new_dims': (29,30)
    })
    def test_it_keeps_ratio(self, image_dims, max_dims, expected_new_dims):
        new_image_dims = image_processor.decide_dimensions(image_dims, max_dims, 1)

        self.assertEqual(new_image_dims, expected_new_dims)

if __name__ == '__main__':
    unittest.main()
