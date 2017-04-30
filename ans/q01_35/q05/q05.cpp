// author kbb
#include <iostream>
using namespace std;

int main()
{
    int sum_coins;//枚数
    int max_coins;//値段
    int count = 0;
        for(int coin500 = 0; coin500 <= 2; coin500++){
            for(int coin100 = 0; coin100 <= 10; coin100++){
                for(int coin50 = 0; coin50 <= 15; coin50++){
                    for(int coin10 = 0; coin10 <= 15; coin10++){
                        sum_coins = coin500 + coin100 + coin50 + coin10;
                        max_coins = coin500*500 + coin100*100 + coin50*50 + coin10*10;
                        if(sum_coins <= 15 && max_coins == 1000){
                            count++;
                        }
                    }
                }
            }
        }
        cout<<count<<endl;
}
