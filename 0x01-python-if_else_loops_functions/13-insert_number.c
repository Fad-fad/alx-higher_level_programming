#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current = *head;
listint_t *precedent = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (current->n < number)
{
precedent = current;
current = current->next;
}
else
{
new->next = current;
precedent->next = new;
}
return (new);
}
