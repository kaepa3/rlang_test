hdist <- read.table("HokkaidoCitiesMDS.tsv", header = F)
hcities <- c("札幌","旭川","稚内", "釧路市","帯広市","室蘭市","函館","小樽")
names(hdist) <- hcities
rownames(hdist) <- hcities

hdist.cmd <- cmdscale(hdist)

hdist.cmd.df <- as.data.frame(hdist.cmd)
hdist.cmd.df$city <- rownames(hdist.cmd.df)
names(hdist.cmd.df) <- c("x","y","city")

ggplot(hdist.cmd.df, aes(x=-x,y=-y,label=city)) + geom_text(family="HiraKakuProN-W3") + theme_gray( base_family = "HiraKakuPro-W3")
