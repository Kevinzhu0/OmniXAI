import os
import unittest
import tensorflow as tf
from PIL import Image as PilImage

from omnixai.data.image import Image
from omnixai.explainers.vision.specific.feature_visualization.tf.preprocess import \
    RandomBlur, RandomCrop, RandomResize, RandomFlip


class TestPreprocess(unittest.TestCase):

    def setUp(self) -> None:
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../datasets")
        img = Image(PilImage.open(os.path.join(directory, "images/dog_cat.png")).convert("RGB"))
        self.img = tf.expand_dims(tf.keras.preprocessing.image.img_to_array(img.to_pil()), axis=0)

    @staticmethod
    def _tensor_to_numpy(x):
        return x.numpy()

    def test_blur(self):
        transform = RandomBlur(kernel_size=9)
        y = transform.transform(self.img)
        self.assertEqual(y.shape, (1, 450, 450, 3))

    def test_crop(self):
        transform = RandomCrop(shift=100)
        y = transform.transform(self.img)
        self.assertEqual(y.shape, (1, 350, 350, 3))

    def test_resize(self):
        transform = RandomResize(scale=(0.5, 0.5))
        y = transform.transform(self.img)
        self.assertEqual(y.shape, (1, 225, 225, 3))

    def test_flip(self):
        transform = RandomFlip(horizontal=True, vertical=True)
        y = transform.transform(self.img)
        self.assertEqual(y.shape, (1, 450, 450, 3))


if __name__ == "__main__":
    unittest.main()
