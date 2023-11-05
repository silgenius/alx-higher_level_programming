#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
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
