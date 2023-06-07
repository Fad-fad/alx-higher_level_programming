#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - gd
 * @head: A pointer the head
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current = *head;
listint_t *previous = NULL;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (*head == NULL || number < current->n)
{
new->next = *head;
*head = new;
return (new);
}
while (current != NULL && number >= current->n)
{
previous = current;
current = current->next;
}
previous->next = new;
new->next = current;
return (new);
}
