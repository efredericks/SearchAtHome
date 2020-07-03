library(ggplot2)
library(reshape2)

setwd("C:/Users/erik/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/erik/research/SSBSE20/SSBSE20-LoadBalancer/HomeLab")
#baseline = read.csv("baseline-pi2.csv", h=T)
#baseline_front = read.csv("baseline-front.csv", h=T)

# Plot String Search results
string_search <- read.csv("string-search-results.csv", h=T)
categories <- c("Generations", "Time")
d = data.frame()

#boxplot(string_search$Laptop.Generations, string_search$Pi.Generations)
wilcox.test(string_search$Laptop.Generations, string_search$Pi.Generations)
df1 = data.frame(string_search$Laptop.Generations, string_search$Pi.Generations, string_search$Pi4.Generations)
colnames(df1) = c("Laptop", "Raspberry Pi 3B", "Raspberry Pi 4")
gens = melt(df1)
ggplot(gens, aes(x=variable,y=value))+geom_boxplot()+xlab("")+ylab("Number of Generations")+theme(text=element_text(size=20))

wilcox.test(string_search$Laptop.Time, string_search$Pi.Time)
wilcox.test(string_search$Laptop.Time, string_search$Pi4.Time)
wilcox.test(string_search$Pi4.Time, string_search$Pi.Time)
df2 <- data.frame(string_search$Laptop.Time, string_search$Pi.Time, string_search$Pi4.Time)
colnames(df2) <- c("Laptop", "Raspberry Pi 3B", "Raspberry Pi 4")
times <- melt(df2)
ggplot(times, aes(x=variable,y=value))+geom_boxplot()+xlab("")+ylab("Execution Time (s)")+theme(text=element_text(size=20))

# Plot haproxy search results
haproxy_search <- read.csv("../../fromPi/haproxy-search-results.csv", h=T)
categories <- c("Fitness", "Time")
d = data.frame()

#boxplot(string_search$Laptop.Generations, string_search$Pi.Generations)
wilcox.test(haproxy_search$GA.Fitness, haproxy_search$Random.Fitness)
wilcox.test(haproxy_search$OnePlusOne.Fitness, haproxy_search$Random.Fitness)
wilcox.test(haproxy_search$OnePlusOne.Fitness, haproxy_search$GA.Fitness)

df1 = data.frame(haproxy_search$GA.Fitness, haproxy_search$Random.Fitness)
colnames(df1) = c("GA", "Random")

df1 = data.frame(haproxy_search$OnePlusOne.Fitness, haproxy_search$GA.Fitness, haproxy_search$Random.Fitness)
colnames(df1) = c("OnePlusOne","GA", "Random")

df1 = data.frame(haproxy_search$OnePlusOne.Fitness, haproxy_search$Random.Fitness)
colnames(df1) = c("OnePlusOne", "Random")



fits = melt(df1)
ggplot(fits, aes(x=variable,y=value))+geom_boxplot()+xlab("")+ylab("Fitness")+theme(text=element_text(size=20))



wilcox.test(haproxy_search$OnePlusOne.Time, haproxy_search$Random.Time)
df2 <- data.frame(haproxy_search$OnePlusOne.Time,haproxy_search$GA.Time, haproxy_search$Random.Time)
colnames(df2) <- c("OnePlusOne", "GA", "Random")

df2 <- data.frame(haproxy_search$OnePlusOne.Time,haproxy_search$Random.Time)
colnames(df2) <- c("OnePlusOne", "Random")



times <- melt(df2)
ggplot(times, aes(x=variable,y=value))+geom_boxplot()+xlab("")+ylab("Execution Time (s)")+theme(text=element_text(size=20))

# ---





category <- c("raspberrypi01", "raspberrypi02")
d = data.frame(category=category, hrsp_1xx=baseline$hrsp_1xx, hrsp_2xx=baseline$hrsp_2xx, 
               hrsp_4xx=baseline$hrsp_4xx, hrsp_5xx=baseline$hrsp_5xx, 
               hrsp_other=baseline$hrsp_other,
               status=baseline$status,
               downtime=baseline$downtime,
               econ=baseline$econ,
               eresp=baseline$eresp,
               chkfail=baseline$chkfail,
               check_status=baseline$check_status,
               qtime=baseline$qtime,
               ctime=baseline$ctime,
               rtime=baseline$rtime,
               ttime=baseline$ttime,
               check_duration=baseline$check_duration,
               device=baseline$Device)

df = data.frame(category=category, hrsp_1xx=baseline_front$hrsp_1xx, hrsp_2xx=baseline_front$hrsp_2xx, 
               hrsp_4xx=baseline_front$hrsp_4xx, hrsp_5xx=baseline_front$hrsp_5xx, 
               hrsp_other=baseline_front$hrsp_other,
               status=baseline_front$status,
               downtime=baseline_front$downtime,
               econ=baseline_front$econ,
               eresp=baseline_front$eresp,
               chkfail=baseline_front$chkfail,
               check_status=baseline_front$check_status,
               qtime=baseline_front$qtime,
               ctime=baseline_front$ctime,
               rtime=baseline_front$rtime,
               ttime=baseline_front$ttime,
               device=baseline_front$Device)
               #check_duration=baseline_front$check_duration)
               



ggplot(d, aes(x=category,y=hrsp_1xx))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=hrsp_2xx))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=hrsp_4xx))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=hrsp_5xx))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=hrsp_other))+geom_bar(stat="identity")

ggplot(d, aes(x=category,y=status))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=downtime))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=econ))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=eresp))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=chkfail))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=check_status))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=qtime))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=ctime))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=ttime))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=rtime))+geom_bar(stat="identity")
ggplot(d, aes(x=category,y=check_duration))+geom_bar(stat="identity")



ggplot(df, aes(x=category,y=hrsp_1xx))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=hrsp_2xx))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=hrsp_4xx))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=hrsp_5xx))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=hrsp_other))+geom_bar(stat="identity")

ggplot(df, aes(x=category,y=status))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=downtime))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=econ))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=eresp))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=chkfail))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=check_status))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=qtime))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=ctime))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=ttime))+geom_bar(stat="identity")
ggplot(df, aes(x=category,y=rtime))+geom_bar(stat="identity")

# 14 - status (DOWN/UP)
# 21 - downtime (int)
# - ereq
# 10 - econ
# 11 - eresp
# 18 - chkfail
# 29 - check_status
# 31 - hrsp_1xx
# 32 - hrsp_2xx
# 33 - hrsp_3xx
# 34 - hrsp_4xx
# 35 - hrsp_5xx
# 36 - hrsp_other ???
# 41 - qtime
# 42 - ctime
# 43 - rtime