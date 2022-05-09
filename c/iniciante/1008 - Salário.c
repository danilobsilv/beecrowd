#include <stdio.h>

int main(){
    int idf, workHours;
    float hourIncome;

    scanf("%d",&idf);
    scanf("%d",&workHours);
    scanf("%f",&hourIncome);

    printf("NUMBER = %d\n",idf);
    printf("SALARY = U$ %.2f\n",workHours*hourIncome);
    return 0;
}
