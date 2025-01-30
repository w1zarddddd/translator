Транслятор из Python в JavaScript

# План тестирования проекта

## История изменений документа

| Дата       | Автор         | Внесённые изменения       |
|------------|---------------|---------------------------|
| 25.12.2022 | Ше С. В. | Исходная версия документа |

## Тесты для подсистемы «Пользовательский интерфейс»

Тест TEST_UI_001
Тестируемые требования: REQ_UI_001
Описание теста: Нажать на окно ввода, начать вводить любой текст с клавиатуры
Ожидаемый результат: Печатаемый текст отображается в окне ввода
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

Тест TEST_UI_002
Тестируемые требования: REQ_UI_001
Описание теста: Нажать на окно вывода, начать вводить любой текст с клавиатуры
Ожидаемый результат: Печатаемый текст не отображается в окне вывода
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

Тест TEST_UI_003  
Тестируемые требования: REQ_UI_001, REQ_UI_002, REQ_UI_003, REQ_UI_004,  REQ_UI_005
Описание теста: Нажать на окно ввода, ввести код на языке Python, например `print("hello")`, нажать на кнопку трансляции языка.
Ожидаемый результат: В окне вывода отобразился код на JavaScript `console.log("hello");`
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

Тест TEST_UI_004
Тестируемые требования: REQ_UI_001
Описание теста: Нажать на окно вывода, начать вводить любой текст с клавиатуры
Ожидаемый результат: Печатаемый текст не отображается в окне вывода
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

### **Тесты для тестирования подсистемы «Лексический анализатор»**

Тест TEST_LA_001  
Тестируемые требования: REQ_LA_001, REQ_UI_001, REQ_UI_002, REQ_UI_004, REQ_UI_005  
Описание теста:  
1. Нажать на окно ввода  
2. Ввести
```
{
a=5
```
3. Нажать на кнопку трансляции языка.  
 Ожидаемый результат: Окно вывода содержит сообщение о лексической ошибке вида `<class 'UnexpectedTokenError'>: unexpected '{' on line 1`
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

Тест TEST_LA_002  
Тестируемые требования: REQ_LA_001, REQ_SYNTA_001, REQ_SEMANTA_001, REQ_GEN_001, REQ_UI_001, REQ_UI_004, REQ_UI_005  
Описание теста:  
1. Нажать на окно ввода  
2. Ввести
```
print("hello, world")
```
3.Нажать на кнопку трансляции языка.  
Ожидаемый результат:  Окно вывода содержит код на языке JavaScript
```
console.log("hello, world")
```
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

Тест TEST_LA_003
Тестируемые требования: REQ_LA_001, REQ_LA_001, REQ_SYNTA_001, REQ_SEMANTA_001, REQ_GEN_001, REQ_UI_001, REQ_UI_004, REQ_UI_005  
Описание теста:  
1. Перейти в файл code/test.py
2. Ввести
```
while 4 + 4:  
    if True:
	    a = 0
	else:        
		while True:
			a = 0
```
3. Запустить тестовый файл.  
Ожидаемый результат:  Вывод токенов в консоли.
```
Token(type='NEWLINE', value='\n', line=2, column=0)
Token(type='BLOCK', value='while', line=2, column=0)
Token(type='NUMBER', value='4', line=2, column=6)
Token(type='OPERATOR', value='+', line=2, column=8)
Token(type='NUMBER', value='4', line=2, column=10)
Token(type='COLON', value=':', line=2, column=11)
Token(type='NEWLINE', value='\n', line=3, column=12)
Token(type='TAB', value='    ', line=3, column=0)
Token(type='BLOCK', value='if', line=3, column=4)
Token(type='BOOL', value='True', line=3, column=7)
Token(type='COLON', value=':', line=3, column=11)
Token(type='NEWLINE', value='\n', line=4, column=12)
Token(type='TAB', value='    ', line=4, column=0)
Token(type='TAB', value='    ', line=4, column=4)
Token(type='VARIABLE', value='a', line=4, column=8)
Token(type='ASSIGN', value='=', line=4, column=10)
Token(type='NUMBER', value='0', line=4, column=12)
Token(type='NEWLINE', value='\n', line=5, column=13)
Token(type='TAB', value='    ', line=5, column=0)
Token(type='BLOCK', value='else', line=5, column=4)
Token(type='COLON', value=':', line=5, column=8)
Token(type='NEWLINE', value='\n', line=6, column=9)
Token(type='TAB', value='    ', line=6, column=0)
Token(type='TAB', value='    ', line=6, column=4)
Token(type='BLOCK', value='while', line=6, column=8)
Token(type='BOOL', value='True', line=6, column=14)
Token(type='COLON', value=':', line=6, column=18)
Token(type='NEWLINE', value='\n', line=7, column=19)
Token(type='TAB', value='    ', line=7, column=0)
Token(type='TAB', value='    ', line=7, column=4)
Token(type='TAB', value='    ', line=7, column=8)
Token(type='VARIABLE', value='a', line=7, column=12)
Token(type='ASSIGN', value='=', line=7, column=14)
Token(type='NUMBER', value='0', line=7, column=16)
Token(type='NEWLINE', value='\n', line=8, column=17)
Token(type='NEWLINE', value='\n', line=9, column=0)
```
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден
### **Тесты для тестирования подсистемы «Синтаксический анализатор»**

Тест TEST_SYNTA_001  
Тестируемые требования: REQ_LA_001, REQ_SYNTA_001, REQ_UI_001, REQ_UI_002, REQ_UI_004, REQ_UI_005  
Описание теста:  
1. Нажать на окно ввода  
2. Ввести
```
priшnt(4)
```
3. Нажать на кнопку трансляции языка  
Ожидаемый результат:  
1. Окно вывода содержит сообщение о синтаксической ошибке вида `<class 'SyntaxError'>: unexpected 'ш' on line 1`  
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

Тест TEST_SYNTA_002  
Тестируемые требования: REQ_LA_001, REQ_SYNTA_001, REQ_UI_001, REQ_UI_002, REQ_UI_004, REQ_UI_005  
Описание теста:  
1. Нажать на окно ввода  
2. Ввести
```
if True:
print("yes")  
```
3. Нажать на кнопку трансляции языка  
Ожидаемый результат: Окно вывода содержит сообщение о синтаксической ошибке вида `IndentationError: expected an indented block (<unknown>, line 2)`
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

Тест TEST_SYNTA_003  
Тестируемые требования: REQ_LA_001, REQ_SYNTA_001, REQ_SEMANTA_001, REQ_GEN_001, REQ_UI_001, REQ_UI_004, REQ_UI_005  
Описание теста:  
1. Нажать на окно ввода  
2. Ввести
```
a=5
b=5
if a==b and b==5:
  print("Yes")
```
3. Нажать на кнопку трансляции языка 
Ожидаемый результат: Окно вывода содержит код на языке JavaScript
```
var a, b;
a = 5;
b = 5;
if (a === b && b === 5) {
  console.log("Yes");
}
```
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден

### **Тесты для тестирования подсистемы «Генератор кода»**
Тест TEST_GEN_001  
Тестируемые требования: REQ_LA_001, REQ_SYNTA_001, REQ_SEMANTA_001, REQ_GEN_001, REQ_UI_001, REQ_UI_004, REQ_UI_005  
Описание теста:  
1. Нажать на окно ввода  
2. Ввести
```
a=5
b=6
c=a+b
print(c)
```
3. Нажать на кнопку трансляции языка  
Ожидаемый результат: Окно вывода содержит код на языке JavaScript
```
var a, b, c;
a = 5;
b = 6;
c = a + b;
console.log(c);
```
Видимый результат: Полностью совпадает с ожидаемым  
Резюме: Тест пройден