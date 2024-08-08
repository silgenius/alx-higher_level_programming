#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, length = PyList_Size(p);
	PyListObject *listobject = (PyListObject *)p;
	Py_ssize_t allocated = listobject->allocated;
	PyObject *element;

	i = 0;
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", allocated);
	while (i < length)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		i++;
	}
}
