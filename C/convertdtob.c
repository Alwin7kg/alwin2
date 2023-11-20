#include <stdio.h>
#include <string.h>


void setUnion(char set1[][50], int size1, char set2[][50], int size2)
{
int i,j;
printf("Union of the sets: {");
for (i = 0; i< size1; i++)
{
printf("%s", set1[i]);
}
for (i=0;i<size2;i++)
{
int isDuplicate = 0;
for(j=0;j<size1;j++)
{
if (strcmp(set2[i],set1[j])==0)
{
isDuplicate=1;
break;
}
}
if (!isDuplicate)
{
printf("%s",set2[i]);
}
}
printf("}\n");
}

void setIntersection(char set1[][50],int size1, char set2[][50], int size2)
{
int i,j;
printf("Intersection of the sets:{ ");
for(i=0;i<size1;i++)
{
for(j=0;j<size2;j++)
{
if (strcmp(set1[i],set2[j])==0)
{
printf("%s",set1[i]);
break;
}
}
}
printf("}\n");
}
void setDifference(char set1[][50],int size1, char set2[][50], int size2)
{
int i,j;
printf("Difference of the sets {Set1-Set2:{ ");
for(i=0;i<size1;i++)
{
int isInSet2=0;
for(j=0;j<size2;j++)
{
if(strcmp(set1[i],set2[j])==0)
{
isInSet2=1;
break;
}
}
if(!isInSet2)
{
printf("%s",set1[i]);
}
}
printf("}\n");
}
int main(){
char set1[][50]={"apple","mango","banana","fruit"};
int size1 = 4;

char set2[][50]={"apple","fruit","banana","mango"};
int size2=4;
setUnion(set1,size1,set2,size2);
setIntersection(set1,size1,set2,size2);
setDifference(set1,size1,set2,size2);

return 0;
}

