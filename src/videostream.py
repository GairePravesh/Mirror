from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
vc = cv2.VideoCapture(0)

def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = vc.read()
        byteArray = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + byteArray + b'\r\n')


@app.route('/')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='192.168.43.41', debug=True, threaded=True)
