#include<stdio.h>

int first=0;
int second=1;
int fib(int a)
{
  if(a<3)
  {
  	return 0;
  }

 
  int third=first+second;
  first=second;
  second=third;
  printf(",%d",third);
  return fib(a-1);
}
int main()
{
	int n;
	printf("Enter the number of terms:");
	scanf("%d",&n);
	if(n<=0)
	{
		printf("invalid input");
	}
	else if(n==1)
	{
	printf("%d",0);
    }
	else if(n==2)
	{
		printf("%d,%d",0,1);
	}
	else
	{
		printf("%d,%d",0,1);
		fib(n);
	}
	
}


