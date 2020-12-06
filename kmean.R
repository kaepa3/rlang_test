state.km <- kmeans(scale(state.x77[,1:6]),3)

state.pca.df <- data.frame(state.pca$x)
state.pca.df$name <- rownames(state.pca.df)
state.pca.df$cluster <- as.factor(state.km$cluster)

ggplot(state.pca.df, aes(x=PC1,y=PC2,label=name,col=cluster)) + geom_text(family="HiraKakuProN-W3") + theme_bw(16)
