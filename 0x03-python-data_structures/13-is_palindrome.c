#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *next;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n)
        {
            is_palindrome = 0;
            break;
        }
        prev = prev->next;
        slow = slow->next;
    }

    prev = NULL;
    while (slow != NULL)
    {
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }
    *head = prev;

    return is_palindrome;
}
