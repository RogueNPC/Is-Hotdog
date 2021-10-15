import cv2
import numpy as np
import tensorflow as tf


def read_from_file(file_object):
    """
    Produces a 3D array representing a color image.

    NumPy creates a new 1D array from the file object,
    and then using OpenCV we convert it to the proper 3D array
    that the model can run inference on.

    Args:
        file_object(fastapi.UploadFile): the uploaded image

    Returns:
        img_np: array-like object
    """
    arr = np.fromstring(file_object.read(), np.uint8)
    img_np = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    resized_arr = tf.image.resize_with_crop_or_pad(img_np, 256, 256)

    return resized_arr
