<p align='center'>
<img src="https://user-images.githubusercontent.com/88227750/212111396-cca97611-cb3f-4475-89b7-1cd63825d9a6.png" align="center">
</p>

<br>

<p align='center'>
    <a href='#'><img src='https://img.shields.io/badge/License-MIT-brightgreen'></a>
    <a href='#'><img src='https://img.shields.io/badge/Platform-Linux%20&%20Windows%20Based-yellow'></a>
    <a href='#'><img src='https://img.shields.io/badge/Version-0.1-red'></a>
    <br>
    <a href='#'><img src='https://img.shields.io/badge/Author-Aman%20Raj-orange'></a>
    <a href='https://www.python.org/'><img src='https://img.shields.io/badge/Python-%3E%3D3.9-blue'></a>
    <img src='https://img.shields.io/badge/Maintained%3F-yes-green.svg'>
    <br>
    <a href='https://twitter.com/amanraj_Phunish'><img src='https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white'></a>
    <a href='https://github.com/Cracker-NN'><img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'></a>
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
>> # **Windows**
```
If you're Windows User then You wil need to install some packages from the Browser.
```
**Python Installation**

- [Python](https://www.python.org/downloads/)

**Run The Following Commands on Your `CMD/Powershell` :**

```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\USERNAME> cd Predictor
PS C:\Users\USERNAME> pip install -r requirements.txt
PS C:\Users\USERNAME> python setup.py
```

*If any TroubleShoot Happened Then*

```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\USERNAME> pip install joblib
PS C:\Users\USERNAME> pip install opencv-python
PS C:\Users\USERNAME> pip install numpy
PS C:\Users\USERNAME> pip install PyQt6
PS C:\Users\USERNAME> pip install beautifulsoup4
PS C:\Users\USERNAME> pip install requests
PS C:\Users\USERNAME> pip install tensorflow
```

**Now Starting it :**
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\USERNAME> python launcher.py
```
> ## **Linux**

**Run Following Commands :**
```bash
$ git clone https://github.com/Cracker-NN/Predictor.git
$ cd Predictor
$ chmod +x setup.py
$ sudo apt install -y python3
$ python3 setup.py
```
*If you have getting any error then you will install manually some packages :*
```bash
$ sudo apt install -y python3
$ sudo apt install -y python3-pip
$ sudo apt install -y gcc
$ cd Predictor
$ pip3 install -r requirements.txt
```
*If Module Error Then*
```bash
$ pip3 install joblib
$ pip3 install opencv-python
$ pip3 install numpy
$ pip3 install PyQt6
$ pip3 install beautifulsoup4
$ pip3 install requests
$ pip3 install tensorflow
```
**Now Starting It :**

```bash
$ python3 launcher.py
```

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
<h2>Availabel Library</h2>


|      Library        | Class        | Model                    |   ClassList   |   Label |
|---------------------|--------------|--------------------------|---------------|---------|
| Shoe Classification | classes.pkl    |  shoe_classifier.h5      | ['Ballet Flat', 'Boat', 'Brogue', 'Clog', 'Sneaker']  |    ❌      |
|Animal Classification| classes.pkl    |  animal_classifier.h5    | ['cane', 'cavallo', 'elefante', 'farfalla', 'gallina', 'gatto', 'mucca', 'pecora', 'ragno', 'scoiattolo'] |   ✔️  |
| Dumb Sign Classification  | classes.pkl     | dumb-sign.h5    |   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']   |   ✔️ |

<br>

>## **Author**
- [Aman  Raj](https://github.com/amanraj-bose)

>## **License**

- [**MIT**](https://opensource.org/licenses/MIT)

>## **Contact Us**

- [Github](https://github.com/amanraj-bose)
- [Twitter](https://twitter.com/amanraj_Phunish)


