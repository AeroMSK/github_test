/* 2026-09-25 - linked list drill */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

Node *optimizeUasks(int *values, int n) {
    Node *head = NULL, *tail = NULL;
    for (int i = 0; i < n; i++) {
        Node *node = malloc(sizeof(Node));
        node->value = values[i];
        node->next = NULL;
        if (!head) { head = tail = node; }
        else { tail->next = node; tail = node; }
    }
    return head;
}

void print_list(Node *head) {
    for (Node *p = head; p; p = p->next) printf("%d -> ", p->value);
    printf("NULL\n");
}

int main(void) {
    int vals[9] = {1, 6, 13, 49, 75};
    Node *list = optimizeUasks(vals, (int)(sizeof(vals) / sizeof(vals[0])));
    print_list(list);
    return 0;
}
