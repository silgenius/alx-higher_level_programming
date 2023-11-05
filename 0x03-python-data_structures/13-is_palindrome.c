#include "lists.h"

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	int length, i, j, len;
	listint_t *ptr, *last;

	i = 0, j = 0, length = 0;
	ptr = *head;

	while (ptr != NULL)
	{
		length++;
		ptr = ptr->next;
	}

	len = length / 2;
	ptr = *head;

	while (i < len)
	{
		last = *head;
		while (j < length - 1)
		{
			last = last->next;
			j++;
		}

		if (!(ptr->n == last->n))
			return (0);
		i++;
		ptr = ptr->next;
		length--;
		j = 0;
	}

	return (1);
}
