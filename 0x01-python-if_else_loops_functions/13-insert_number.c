#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slow, *ptr, *new_node;

	ptr = *head;
	slow = ptr;

	while (ptr != NULL)
	{
		if (ptr->n > number)
		{
			break;
		}
		slow = ptr;
		ptr = ptr->next;
	}

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (ptr == slow)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	if (ptr == NULL)
	{
		slow->next = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	new_node->next = slow->next;
	slow->next = new_node;

	return (new_node);
}
