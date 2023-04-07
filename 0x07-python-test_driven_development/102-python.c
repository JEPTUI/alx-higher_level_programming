#include <Python.h>
/**
 * print_python_string - prints python string
 * @p: string
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t size;
	const char* str;
	
	if (!PyUnicode_Check(p))
	{
		printf("Error: Invalid String Object.\n");
		return;
	}
	
	str = PyUnicode_AsUTF8AndSize(p, &size);
	if (str == NULL)
	{
		printf("Error: unable to decode string.\n");
		return;
	}
	
	printf("%.*s\n", (int)size, str);
}
