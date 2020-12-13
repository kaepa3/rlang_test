library(ggplot2)
library(scales)

grp.data <- read.csv("grp.csv", header = T)

head(grp.data)

#ggplot(grp.data, aes(x=grp, y=amount)) +
#  geom_point() + 
#  ylab("売上") + 
#  xlab("GRP") + 
#  theme_bw(16)

ggplot(grp.data, aes(x=grp, y=amount)) +
  geom_point() + 
  scale_y_continuous(labels = comma, limits = c(0,360000) ) + 
  theme_bw(16)

#fit <-lm(amount ~ grp, data=grp.data)
#summary(fit)

fit <- lm(log(amount) ~ log(grp), data = grp.data)
summary(fit)

fit.data <- data.frame(grp = grp.data$grp, amount=exp(fit$fitted.values))

ggplot(grp.data,aes(x=grp, y=amount)) +
  geom_point() +
  geom_line(data = fit.data, aes(x=grp, y = amount)) +
  scale_y_continuous(labels = comma, limits = c(0,360000)) + 
  theme_bw(16)
