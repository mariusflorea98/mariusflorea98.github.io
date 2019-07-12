from flask import Blueprint
from flask import request

test_function = Blueprint('test_function', __name__)

from PIL import Image
import base64
import io
import cv2
import matplotlib.pyplot as plt
import np
@test_function.route('/test',methods=["POST", "GET"])
def test():
    json_data_from_request = request.get_json()

    img=json_data_from_request['data']

    base64result = img.split(',')[1]
    #print(base64result)

    imgdata = base64.b64decode(str(base64result))
    image = Image.open(io.BytesIO(imgdata))
    plt.imshow(image)
    plt.show()
    return imgdata