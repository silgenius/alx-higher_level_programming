#include "lists.h"

/**
 * insert_nodeint_at_index - Inserts a new node at a specified index.
 * @head: A pointer to a pointer to the head of the linked list.
 * @idx: The index at which to insert the new node.
 * @n: The integer value to be stored in the new node.
 *
 * Description: This function takes a pointer to the head of a linked list,
 *              an index, and an integer value. It creates a new node with
 *              the specified value and inserts it at the specified index.
 *
 * Return: A pointer to the newly created node, or NULL if the insertion fails.
 */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	unsigned int i;
	listint_t *temp;
	listint_t *new;

	i = 0;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	temp = *head;

	if (idx == 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (temp != NULL && i < idx - 1)
	{
		temp = temp->next;
		i++;
	}

	if (temp == NULL)
	{
		free(new);
		return (NULL);
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}
