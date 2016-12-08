MBSpricing

Final Project of Credit Risk Modeling

Group Member: Sunaina Nair, Yating Shen

Topic: Mortgate Backed Securities Pricing

###Description:
    Mortgage-backed securities are like coupon bonds but with prepayment risk. We simply treat the prepaymet rate as a threshold function of interest rates. And then we would get different prepayment schedules. Pricing an Angency MBS. Since Agency MBSs are backed up by GSE like Freddie Mac, Fannie Mae, and Geanna Mae, we would put less effort in default rate modeling because the probability of default will be low. Even there is an default, the agency will replace the defaulted loan with another new loan in the pools. 
    In reality, prepayment depends on various factors like refinancing rates and costs, weighted average lify of the loans in the pool, the seasoning factors etc. But the research on the prepayment would be a huge topic, so we decide to simplify our project by solely deciding the prepayment on the movement of interets rates and refianncing cost.

###Methodology:
    The general structure of our project is :
1.	Simulate the evolution of short term interest rates using Vasicek model 
2.	Using interest rates term structure to model prepayment due to refinancing and adjust cash flows on each path
3.  Embedded default risk into the discouting process of cash flows 
4.	Value Mortgage Backed Securities.
