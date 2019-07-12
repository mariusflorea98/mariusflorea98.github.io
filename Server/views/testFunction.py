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
    json_data_from_request = request.get_json()         #{'data': data}

    img=json_data_from_request['data']
    #print(img)
    base64result = img.split(',')[1]                    #remove data:image/png;base64 header
    #print(base64result)

    imgdata = base64.b64decode(str(base64result))       #Decode the Base64 encoded bytes-like object or ASCII string and return the decoded bytes.

    image = Image.open(io.BytesIO(imgdata))
    #plt.imshow(image)
    #plt.show()                                          #plot image

    imag={'data':img}                                    #attempt to send image from flask to web

    return imag