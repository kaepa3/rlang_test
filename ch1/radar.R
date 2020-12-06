library(fmsb)
df <- as.data.frame(scale(state.km$centers))
dfmax <- apply(df,2,max) +1
dfmin <- apply(df,2,min) -1
df <-rbind(dfmax, dfmin, df)

radarchart(df,seg=5,plty=1,pcol=rainbow(3))
legend("topright", legend = 1:3, col=rainbow(3), lty=1)
