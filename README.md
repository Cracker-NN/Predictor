<p align='center'>
<img src="https://user-images.githubusercontent.com/88227750/212111396-cca97611-cb3f-4475-89b7-1cd63825d9a6.png" align="center">
</p>

<br>

<p align='center'>
    <a href='#'><img src='https://img.shields.io/badge/License-MIT-brightgreen'></a>
    <a href='#'><img src='https://img.shields.io/badge/Platform-Linux%20Based-yellow'></a>
    <a href='#'><img src='https://img.shields.io/badge/Version-0.1-red'></a>
    <br>
    <a href='#'><img src='https://img.shields.io/badge/Author-Aman%20Raj-orange'></a>
    <a href='https://www.python.org/'><img src='https://img.shields.io/badge/Python-%3E%3D3.9-blue'></a>
    <a href='https://github.com/amanraj-bose'><img src='https://img.shields.io/badge/Author-Aman%20Raj-orange'></a>
    <br>
    <a href='https://twitter.com/amanraj_Phunish'><img src='https://img.shields.io/twitter/follow/amanraj_Phunish?style=social'></a>
    <a href='https://github.com/Cracker-NN'><img src='https://img.shields.io/github/followers/amanraj-bose?style=social'></a>
    <a href='https://en.wikipedia.org/wiki/India'><img src='https://img.shields.io/badge/Made%20In-India-orange'></a>
</p>

<h1 align='center'>The Predictor</h1>

**Predictor is a Amazing Deep Learning Library which Contain Pretained Model But this time, It's contain small number of pretrainde model.**

</br>

>## **Working Type**
- **GUI**
- **Code**
<!-- - **CLI** -->

>## **Installation**
- **Automate Installation**
```bash
$ chmod +x setup.sh
$ sudo ./setup.sh
```
- **Python Method**
```bash
$ python3 -m pip install -r requirements.txt
```
- **Linux Packages**
```bash
$ sudo apt install python3
$ sudo apt install python3-pip
```
- **Python Library**
```bash
$ python3 -m pip install -U joblib
$ python3 -m pip install -U numpy
$ python3 -m pip install -U keras
$ python3 -m pip install -U opencv-python
$ python3 -m pip install -U PyQt6
```
>## **GUI Preview**


<img src="https://user-images.githubusercontent.com/88227750/212110833-f117980f-ffdd-4ab0-8c97-e6d8727642a9.png" align="center">

<br>

>## **Code Preview**

```python
import local
import os


DIRECTORY = "<DIRECTORY PATH>"
MODEL_FILENAME = "<MODEL FILENAME>"
IMAGE_FILENAME = "<IMAGE FILENAME>"
CLASS_FILENAME = "<CLASS FILENAME>"

PREDICTION = local.img_decoder(
    model_path=os.path.join(DIRECTORY, MODEL_FILENAME),
    img_path=os.path.join(DIRECTORY, IMAGE_FILENAME),
    classes=os.path.join(DIRECTORY, CLASS_FILENAME)
    )

print("Prediction is :", PREDICTION)
```
*If You have any Confusion then only over write the Variables `DIRECTORY`*

<br>

<!-->## **CLI Preview**-->

<!-- ```bash

$ python3 predictor --help

Usage: predictor  [ -d Directory Path ] [ -m Model Filename ] [ -c Class Filename ] [ -i Image Filename ]

``` -->

<br>

---

<h2>Availabel Library</h2>


|      Library        | Class        | Model                    |   ClassList   |   Label |
|---------------------|--------------|--------------------------|---------------|---------|
| Shoe Classification | classes.pkl    |  shoe_classifier.h5      | ['Ballet Flat', 'Boat', 'Brogue', 'Clog', 'Sneaker']  |    ✔️      |
|Animal Classification| classes.pkl    |  animal_classifier.h5    | ['cane', 'cavallo', 'elefante', 'farfalla', 'gallina', 'gatto', 'mucca', 'pecora', 'ragno', 'scoiattolo'] |   ✔️  |
| Dumb Sign Classification  | classes.pkl     | dumb-sign.h5    |   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']   |   ✔️ |

>## **Author**
- [Aman  Raj](https://github.com/amanraj-bose)

>## **License**

- [**MIT**](https://opensource.org/licenses/MIT)

>## **Contact Us**

- [Github](https://github.com/amanraj-bose)
- [Twitter](https://twitter.com/amanraj_Phunish)
