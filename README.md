# Lina Tanslate

A private Google Translate frontend.

Lina does not use any Google framework libraries or APIs. It only parses the website in order to gain the information it needs.

This project is a fork of https://git.sr.ht/~metalune/simplytranslate_web.

## How to install/use
### Clone repository and install it
```sh
git clone https://github.com/Lacerte/lina.git
cd lina
sudo python3 setup.py install
cd ..
```

### Install dependencies
```sh
pip install -r requirements.txt
```

### Run main.py
```sh
# Directly
python3 main.py
# Using uvicorn
uvicorn main:app --port 5000
```

### Run in browser
```sh
http://localhost:5000
```
