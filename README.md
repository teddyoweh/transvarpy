# Pointers in Python
This module is a different way of assigning variables in python.

The most popular languages that have pointers are C and C++, pointers allow a variable to be change by altering the memory address of the variable.

## C Pointers 
```C
#include <stdio.h>

int main(void) {
	int num = 10;
	//declaring and initializing the pointer
	int *ptr = &num;

	printf("value of num: %d\n", num);
	printf("value of num: (using pointer): %d\n", *ptr);

	//updating the value
	*ptr = 20;

	printf("value of num: %d\n", num);
	printf("value of num (using pointer): %d\n", *ptr);

	return 0;
}


 

```

# Overview
In python, once a variable is assigned, there's is now other way to change that variable

```Python
name = 'teddy'
temp = '{}_'.format(name) # Adds _ at the end of the name variable ( teddy )
name = temp 
```



## Implementation

Than creating 10 different variables, create a dictionay object, insert the variable name as the key and the content as what you want the variable name to be equals to.

```Python
mydict = {
	'name':'teddy',
	'major':'cs',
	'language': 'English',
	'laptop':'Mac',
	'phone': 'Iphone',
	'class':'calc 1',
	'address':'est drive',
	'age':'5',
	'food':'burger',
	'car':'ford'
	}
for key,content in mydict.items():
	TransIndv(key,content)
```
### 10 different variables have been created ( name,major,language,laptop,phone,class,address,age,food and car.

### Using it

First, import Omark from Omark

```Python
from Omark import Omark 
```

 
## Initialize Omark
First, let's create a new Omark object. For this , just provide the students in a text file and a folder of all the students image with the names saved as the same name stored in the text file.

```Python
 
om = Omark(students='file.txt',data='folder')

```
## View all details
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.register())


```
## View all students
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.students)


```
## View all absent students
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.absent)


```

 ## View all present students
 

```Python
 
om = Omark(students='file.txt',data='folder')
print(om.present)


```



License
----

MIT License

Copyright (c) 2021 Teddy Oweh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Hire me: `teddyoweh`
