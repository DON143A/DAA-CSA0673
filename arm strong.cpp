#include<stdio.h>

int sum=0;

int arm(int a)
{
	if(a>0)
	{
    int r=a%10;
	sum=sum+(r*r*r);
	return arm(a/10);
    }
	else{
		return sum;
	}
    
	
}
int main()
{
	int n;
	printf("Enter the number :");
	scanf("%d",&n);
	if(arm(n)==n)
	{
		printf("Armstrong ");
	}
	else
	{
		printf("Not An Armstrong");
	}
}
