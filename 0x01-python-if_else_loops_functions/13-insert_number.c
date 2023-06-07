#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	current = *head;
	previous = NULL;

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	if (previous == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		previous->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
