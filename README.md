# from Python to JS translator

Transpiler from Python to JavaScript. Includes transpiler module which performs
all logic and a simple web interface to interact with.

## <a>Go checkout http://mrsemyon12.pythonanywhere.com

To run the project locally use following commands `python3.9 required`:

```bash
git clone https://github.com/MrSemyon12/py-to-js-translator.git
cd py-to-js-translator
python -m venv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
python .\code\webapp\app.py
```

After that you can check [localhost:5000](http://localhost:5000)


## Available constructions
* Binary operators `= / + * - and or == != < > <= >=`
```python
example = -5 * 1.44 + 7 / -0.62
example = True and -5 or 0 and 8.42 > 9
```
* Math functions `sin cos tan sqrt abs`
```python
example = math.sin(-0.005 + abs(0.1 / -66))
```
* Strings
```python
example = "hello" + 'world'
```
* Loops `while`
```python
example = 10
while example >= 4 and math.sin(example) != math.cos(4):
    example = example - 1
    while True:
        example = 5
```
* Console output
```python
print(4 + math.sqrt(2))
```
* Conditional orerator `if else`
```python
if 5 < 0:
    print('hello')
    if True:
        print(8)
    else:
        age = 9
```
