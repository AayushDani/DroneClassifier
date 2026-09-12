# DroneClassifier · Face-position experiment

An early **OpenCV webcam experiment** that detects faces and displays their position relative to the center of the camera frame.

**Historical personal project · 2019 · Python / OpenCV / Haar cascades**

## What the code does

`CascadeClassifier.py` opens a webcam, applies a Haar-cascade face detector, draws bounding boxes, and displays horizontal/vertical offsets. It also compares the detected face-box height with a target height as a simple apparent-size signal.

The project explored a visual input for a possible drone-following idea. The repository contains no flight controller, autonomous navigation system, or trained custom model. The apparent-size difference is not a calibrated depth measurement.

## Reproduction status

The detector points to a machine-specific Windows path for its cascade XML file. Running it on another machine requires an available cascade file, a corrected path, compatible OpenCV, and an accessible webcam. Camera and detection behavior have not been revalidated.

The repository name is preserved for continuity; this README describes the implemented experiment rather than the original future-project ambition.
