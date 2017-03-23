library(foreign)
library(Matching)
data <- read.dta('nsw_dw.dta')
#(1)
#Point estimate of the treatment effect
observed.diffmeans <- mean(data$re78[data$treat==1]) - mean(data$re78[data$treat==0])
observed.diffmeans 
#univariate linear regression
ulr = lm(formula = re78 ~ treat, data = data)
summary(ulr)
confint(ulr, 'treat', level=0.95)
#(2)
cpscontrols <- read.dta('cps_controls.dta')
nswtreat <- data[which(data$treat == 1),]
data2 <- rbind(nswtreat, cpscontrols)
observed.diffmeans2 <- mean(data2$re78[data$treat==1]) - mean(data2$re78[data$treat==0])
observed.diffmeans2
ulr2 <- lm(formula = re78 ~ treat, data = data2)
summary(ulr2)
confint(ulr2, 'treat', level=0.95)

#(3)
#use propensity score matching to produce an estimated treatment effect and confidence interval.
pscore.glm<-glm(treat ~ age+education+black+hispanic+married+nodegree+re74+re75,
                family=binomial(logit), data=data2)
y1 <- data2$re78
x1 <- fitted(pscore.glm)
tr1 <- data2$treat
r1 <- Match(Y=y1, Tr=tr1, X=x1, M=1)
summary(r1)
mb1 <- MatchBalance(treat ~ age+education+black+hispanic+married+nodegree+re74+re75, data=data2, match.out=r1, nboots=10)
lower_bound1 <- 1440.4 - 1.96*819.78
upper_bound1 <- 1440.4 + 1.96*819.78
ci1 <- c(lower_bound1,upper_bound1)
ci1
#(4)
#Use the Match() function to run a multivariate matching procedure 
#that uses all the covariates and also includes the estimated propensity scores. 
x2 <- data2[,c(3,4,5,6,7,8,9,10)]
x3 <- cbind(pscore.glm$fitted,x2)
r2 <- Match(Y=y1, Tr=tr1, X=x3, distance.tolerance=0.1, exact=c(F,T,F,F,F,F,F,F,F))
r4 <- Match(Y=y1, Tr=tr1, X=x3, distance.tolerance=0.1, exact='True')
summary(r4)
mb4 <- MatchBalance(tr1~pscore.glm$fitted+data2$age+data2$education+data2$black+data2$hispanic
                  +data2$married+data2$nodegree+data2$re74+data2$re75,match.out=r4, nboots=500)
r22 <- Match(Y=y1, Tr=tr1, X=x3)
mb2 <- MatchBalance(tr1~pscore.glm$fitted+data2$age+data2$education+data2$black+data2$hispanic
                    +data2$married+data2$nodegree+data2$re74+data2$re75,match.out=r2, nboots=500)
mb22 <- MatchBalance(tr1~pscore.glm$fitted+data2$age+data2$education+data2$black+data2$hispanic
                    +data2$married+data2$nodegree+data2$re74+data2$re75,match.out=r22, nboots=500)
summary(r2)
summary(r22)
lower_bound2 <- 1863.4 - 1.96*891.83
upper_bound2 <- 1863.4 + 1.96*891.83
ci2 <- c(lower_bound2,upper_bound2)
ci2
#(5) 
#Repeat #3 and #4 with genetic matching
genout2 <- GenMatch(Tr=tr1, X=x2, estimand="ATT", pop.size=50, max.generations=10, replace=TRUE)
genout1 <- GenMatch(Tr=tr1, X=x1, estimand="ATT", pop.size=50, max.generations=10, replace=TRUE)
mout2 <- Match(Y=y1, Tr=tr1, X=x2, estimand="ATT", Weight.matrix=genout2, replace=TRUE)
mout1 <- Match(Y=y1, Tr=tr1, X=x1, estimand="ATT", Weight.matrix=genout1)
summary(mout2)
summary(mout1)
mb2 <- MatchBalance(tr1~data2$age+data2$education+data2$black+data2$hispanic+data2$married+data2$nodegree+data2$re74+data2$re75, match.out=mout2, nboots=500)
