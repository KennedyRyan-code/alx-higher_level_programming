#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list contains a cycle
 * @list: a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);  /* Cycle detected */
	}

	return (0);  /* No cycle found */
}

