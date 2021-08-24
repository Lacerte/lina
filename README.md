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