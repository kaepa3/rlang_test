library(plyr)

A1.CVR <-0.09
B1.CVR <-0.09

n <- 10000
set.seed(2)

AB1 <-data.frame(Pattern=c(rep("A", n), rep("B",n)),
                 CV = c(rbinom(n,1,A1.CVR), rbinom(n,1,B1.CVR)))

ddply(AB1, .(Pattern), summarise, CVR=mean(CV))

A2.CVR <-0.095
B2.CVR <-0.097

AB2 <-data.frame(Pattern=c(rep("A", n), rep("B",n)),
                 CV = c(rbinom(n,1,A2.CVR), rbinom(n,1,B2.CVR)))

ddply(AB2, .(Pattern), summarise, CVR=mean(CV))
chisq.test(table(AB1))
chisq.test(table(AB2))

A3.CVR <-0.095
B3.CVR <-0.097
n <- 50000
set.seed(2)

AB3 <-data.frame(Pattern=c(rep("A", n), rep("B",n)),
                 CV = c(rbinom(n,1,A3.CVR), rbinom(n,1,B3.CVR)))
ddply(AB3, .(Pattern), summarise, CVR=mean(CV))

chisq.test(table(AB3))
