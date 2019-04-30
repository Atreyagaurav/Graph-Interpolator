#include<stdio.h>
#include<conio.h>
#include<windows.h>
#include<math.h>
#include<strings.h>
void main(int argc,char *argv[])
{
    float x[2][40],p;
    char c;
    int i,k,n;
    char xep[20];
    FILE *fp,*ffo;
    fp=fopen(argv[2],"r");
    ffo=fopen("data\\formula.lin","w");
    strcpy(xep,argv[1]);
    for(n=0;n<40;n++)
    {
        fscanf(fp,"%f,%f",&x[0][n],&x[1][n]);
        c=fgetc(fp);
        if(c=='\0')
        {
            break;
        }
    }
    n=strtod(argv[3],&c)-1;
    fprintf(ffo,"=if\(");
    fprintf(ffo,xep);
    fprintf(ffo,"<%f,\"N/A\",",x[0][0]);
    for(i=0;i<n-1;i++)
    {
        fprintf(ffo,"if\(");
        fprintf(ffo,xep);
        fprintf(ffo,"<%f,%f+%f*\(",x[0][i+1],x[1][i],(x[1][i+1]-x[1][i])/(x[0][i+1]-x[0][i]));
        fprintf(ffo,xep);
        fprintf(ffo,"-%f\),",x[0][i]);
    }
    fprintf(ffo,"if\(");
    fprintf(ffo,xep);
    fprintf(ffo,"<=%f,%f+%f*\(",x[0][n],x[1][n-1],(x[1][n]-x[1][n-1])/(x[0][n]-x[0][n-1]));
    fprintf(ffo,xep);
    fprintf(ffo,"-%f\),\"N/A\"\)",x[0][i]);
    for(i=0;i<n;i++)
    {
        fprintf(ffo,"\)");
    }
    fclose(ffo);
    ffo=fopen("data\\formula.lan","w");
    fprintf(ffo,"=");
    for(i=0;i<=n;i++)
    {
        if(x[1][i]==0)
        {
            continue;
        }
        fprintf(ffo,"+");
        for(k=0,p=1.0;k<=n;k++)
        {
            if(k!=i)
            {
                fprintf(ffo,"\(%s-%f\)/\(%f\)*",xep,x[0][k],x[0][i]-x[0][k]);
            }
        }
        fprintf(ffo,"%f",x[1][i]);
    }
    fclose(fp);
    fclose(ffo);
}
