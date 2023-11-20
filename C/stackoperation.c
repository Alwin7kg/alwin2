#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 5

//Structure to represent the stack

struct Stack
{

int items[MAX_SIZE];
int top;
};
//Initialize the stack
void initialize(struct Stack*stack)
{
stack->top= -1;
}
//Check if the stack is empty

int isEmpty(struct Stack*stack)
{
return(stack->top==-1);
}
//Check if the stack is full
int isFull(struct Stack*stack)
{
return (stack->top==MAX_SIZE - 1);
}
//Push an item into the stack
void push(struct Stack*stack,int item)
{
if(isFull(stack))
{
printf("OVERFLOW %d\n",item);
}
else{
stack->items[++stack->top]=item;
printf("%d pushed into the stack.\n",item);
}
}

//Pop an item from the stack
void pop(struct Stack*stack)
{
if (isEmpty(stack))
{
printf("UNDERFLOW\n");
}
else
{
printf("%d popped from the stack.\n",stack->items[stack->top--]); 
}
}
//Peek at the top item of the stack
void peek(struct Stack*stack)
{
if(isEmpty(stack))
{
printf("Stack is empty.Cannot peek.\n");
}
else
{
printf("top item: %d\n",stack->items[stack->top]);
}
}
//Display the elements of the stack
void display(struct Stack*stack)
{
if(isEmpty(stack))
{
printf("Stack is empty.\n");
}
else
{
printf("Stack elements: ");
for(int i=0;i<= stack->top;i++)
{
printf("%d\t",stack->items[i]);
}
printf(" \n ");
}
}
int main()
{
struct Stack stack;
initialize(&stack);
int choice, item;
do
{
printf("\nStack Operations: \n");
printf("1.PUSH\n");
printf("2.POP\n");
printf("3.PEEK\n");
printf("4.DISPLAY\n");
printf("5.QUIT\n");

printf("Enter your choice: \n");
scanf("%d",&choice);

switch(choice)
{
case 1:
   printf("enter an item to push into the stack: ");
   scanf("%d",&item);
   push(&stack,item);
   break;
case 2:
   pop(&stack);
   break;
case 3:
   peek(&stack);
   break;
case 4:
   display(&stack);
   break;
case 5:
   printf("Exiting the program.\n");
   exit(0);
default:
   printf("Invalid choice. Please try again.\n");  
}
}
while(1);
return 0;
}             
