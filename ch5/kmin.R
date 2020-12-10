library("ggplot2")
sp.user.data <- read.csv("sp_user_research_data.csv")
sp.user.pca <- prcomp(sp.user.data[,-1], scale = T)

biplot(sp.user.pca)

sp.user.km <- kmeans(sp.user.data[,-1],4)

print(sp.user.km)
sp.user.pca.df <- data.frame(sp.user.pca$x)
sp.user.pca.df$id <- sp.user.data$id
sp.user.pca.df$cluster <- as.factor( sp.user.km$cluster)

ggplot(sp.user.pca.df, aes(x=PC1,y=PC2, label = id, col= cluster)) + 
  geom_text() + theme_bw(16)

library(fmsb)
df <- data.frame(scale(sp.user.km$centers))
dfmax <- apply(df,2,max) + 1
dfmin <- apply(df,2,min) - 1
df <- rbind(dfmax, dfmin, df)

radarchart(df, seg=5, plty=1, pcol=rainbow(4))
legend("topright", legend=1:4, col = rainbow(4), lty = 1)
