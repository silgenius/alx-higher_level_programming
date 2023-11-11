#include <Python.h>

void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	Py_ssize_t i, len;
	PyObject *item;
	const char *item_type_name;

	len = PyObject_Length(p);
	PyListObject *object_allocation = (PyListObject *) p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", object_allocation->allocated);

	for (i = 0; i < len; i++)
	{
		item = PySequence_GetItem(p, i);
		if (item != NULL)
		{
			item_type_name = item->ob_type->tp_name;
			printf("Element %ld: %s\n", i, item_type_name);
			if (strcmp(item_type_name, "bytes") == 0)
				print_python_bytes(item);
		}
	}
}


void print_python_bytes(PyObject *p)
{
	size_t i, len;
	char *str;
	Py_buffer data;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	len = PyObject_Length(p);
	printf("  size: %ld\n", len);

	len >= 10 ? len = 10: len * 1;

	if (PyObject_CheckBuffer(p))
	{
		if (PyObject_GetBuffer(p, &data, PyBUF_SIMPLE) == 0)
			str = (char *) data.buf;
	}

	printf("  trying string: %s\n", str ? str : "(no data)");

	printf("  first %ld bytes: ", len >= 10 ? len : len + 1);
	for (i = 0; i <= len && i < 10; i++)
	{
		printf("%02hhx", (unsigned char)str[i]);
		if (i < len)
			printf(" ");
	}
	putchar('\n');
}
