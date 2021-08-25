# SimpleTranslate

A private Google Translate frontend.

SimpleTranslate does not use any Google framework libraries or APIs. It only parses the website in order to gain the information it needs.

This project is a fork of https://git.sr.ht/~metalune/simplytranslate_web.

## How to install/use
### Clone the repository and install it
```sh
git clone https://github.com/PrestoSole/SimpleTranslate.git
cd SimpleTranslate
sudo python3 setup.py install
cd ..
```

### Install the dependencies
```sh
pip install -r requirements.txt
```

### Run the main.py
```sh
# Directly
python3 main.py
# Using uvicorn
uvicorn main:app --port 5000
```
