=if(a1<0.000000,"N/A",if(a1<0.001452,0.000000+196968.223480*(a1-0.000000),if(a1<0.002697,286.012512+44449.661524*(a1-0.001452),if(a1<0.004142,341.336121+4334.512698*(a1-0.002697),if(a1<=0.005215,347.599152+3891.458381*(a1-0.004142),"N/A")))))
=+(a1-0.001452)/(-0.001452)*(a1-0.002697)/(-0.002697)*(a1-0.004142)/(-0.004142)*(a1-0.005215)/(-0.005215)*0.000000+(a1-0.000000)/(0.001452)*(a1-0.002697)/(-0.001245)*(a1-0.004142)/(-0.002690)*(a1-0.005215)/(-0.003763)*286.012512+(a1-0.000000)/(0.002697)*(a1-0.001452)/(0.001245)*(a1-0.004142)/(-0.001445)*(a1-0.005215)/(-0.002518)*341.336121+(a1-0.000000)/(0.004142)*(a1-0.001452)/(0.002690)*(a1-0.002697)/(0.001445)*(a1-0.005215)/(-0.001073)*347.599152+(a1-0.000000)/(0.005215)*(a1-0.001452)/(0.003763)*(a1-0.002697)/(0.002518)*(a1-0.004142)/(0.001073)*351.774536