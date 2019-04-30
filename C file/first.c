#include<stdio.h>
#include<conio.h>
#include<windows.h>
#include<math.h>
main()
{
    float x[2][40];
    int i,n;
    char xep[20];
    printf("Enter independent variable:");
    scanf("%s",xep);
    printf("Enter number of points:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("Enter x[%d],y[%d]:",i+1,i+1);
        scanf("%f,%f",&x[0][i],&x[1][i]);
    }
    printf("The required expression is:\n");
    printf("\n\tLinear interpolation:\n");
    printf("=if\(");
    printf(xep);
    printf("<%f,\"N/A\",",x[0][0]);
    for(i=0;i<n-1;i++)
    {
        printf("if\(");
        printf(xep);
        printf("<%f,%f+%f*\(",x[0][i+1],x[1][i],(x[1][i+1]-x[1][i])/(x[0][i+1]-x[0][i]));
        printf(xep);
        printf("-%f\),",x[0][i]);
    }
    printf("if\(");
    printf(xep);
    printf("<=%f,%f+%f*\(",x[0][n],x[1][n-1],(x[1][n]-x[1][n-1])/(x[0][n]-x[0][n-1]));
    printf(xep);
    printf("-%f\),\"N/A\"\)",x[0][i]);
    for(i=0;i<n;i++)
    {
        printf("\)");
    }

    printf("\n\n\tLagranze's Interpolation:\n");
    getch();
}
