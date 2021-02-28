# Happiness-Detection
It detects your happy and smily face through your webcam of your computer.

## Files Input
```python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
```

## Access to Webcam
```python
webcam = cv2.VideoCapture(0)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
