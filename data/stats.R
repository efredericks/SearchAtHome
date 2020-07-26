# Erik Fredericks
# This file plots out the data for SSBSE20 NIER paper for string search.  
# It requires that string-ga-parser.py be run first, and the output files be moved to an appropriate location.

library(ggplot2)
library(reshape2)

setwd(".") # Change as needed

# Plot String Search results
string_search <- read.csv("string-search-results.csv", h=T)
categories <- c("Generations", "Time")
d = data.frame()

# Wilcoxon test and plots (generation convergence)
wilcox.test(string_search$Laptop.Generations, string_search$Pi.Generations)
df1 = data.frame(string_search$Laptop.Generations, string_search$Pi.Generations, string_search$Pi4.Generations)
colnames(df1) = c("Laptop", "Raspberry Pi 3B", "Raspberry Pi 4")
gens = melt(df1)
ggplot(gens, aes(x=variable,y=value))+geom_boxplot()+xlab("")+ylab("Number of Generations")+theme(text=element_text(size=20))

# Wilcoxon tests and plots (run time)
wilcox.test(string_search$Laptop.Time, string_search$Pi.Time)
wilcox.test(string_search$Laptop.Time, string_search$Pi4.Time)
wilcox.test(string_search$Pi4.Time, string_search$Pi.Time)
df2 <- data.frame(string_search$Laptop.Time, string_search$Pi.Time, string_search$Pi4.Time)
colnames(df2) <- c("Laptop", "Raspberry Pi 3B", "Raspberry Pi 4")
times <- melt(df2)
ggplot(times, aes(x=variable,y=value))+geom_boxplot()+xlab("")+ylab("Execution Time (s)")+theme(text=element_text(size=20))