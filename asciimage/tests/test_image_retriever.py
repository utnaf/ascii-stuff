import unittest
import os
from ddt import ddt, data, unpack
from asciimage import image_retriever
from PIL import Image

class TestImageRetriever(unittest.TestCase):
    def test_it_returns_an_image_if_called_with_path(self):
        image = image_retriever.get_from_path(os.path.realpath("asciimage/tests/assets/test.jpg"))
        self.assertIs(type(image), Image.Image)

    def test_it_returns_an_image_if_called_with_url(self):
        image = image_retriever.get_from_url("https://placeimg.com/640/480/any")
        self.assertIs(type(image), Image.Image)

if __name__ == '__main__':
    unittest.main()
