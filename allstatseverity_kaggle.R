### Configuration
################################################################
# File paths
#config_package_folder = '...'

source("C:/FractalWork/allstate-claims-severity/missingvaluesummary.R")
source("C:/FractalWork/allstate-claims-severity/correlationandplots.R")
source("C:/FractalWork/allstate-claims-severity/datawranglingandmanipulation.R")


# CRAN package imports
cran_pkgs = c('dplyr', 'testit', 'testthat','ggplot2','onehot','glmnet')
lapply(cran_pkgs, require, character.only = TRUE)

# Internal package imports
#setwd(config_package_folder)
#internal_pkgs = paste0(config_package_folder, list.files(config_package_folder,pattern="*.R"),sep = '')
#sapply(internal_pkgs, source, .GlobalEnv)


### dplyr Demonstration
################################################################
# good resource: https://rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf


##Read the data 
allstateseverity <- read.table("C:/FractalWork/allstate-claims-severity/train.csv", header=TRUE,
                                 sep=",")

missing_value_summary(allstateseverity)
traindf=data.frame(x = allstateseverity$id, y = allstateseverity$loss)

#(encoder <- onehot(allstateseverity,stringsAsFactors=TRUE))

#allstateseverityonehot <- predict(encoder,allstateseverity)


sapply(allstateseverity, typeof)
allstateseverityonehot <- onehotencode(allstateseverity)

# Density Plot
ggplot(traindf, aes(y)) +
  theme_bw() +
  geom_density(alpha = 0.2) +
  labs(x = "INDEX",
       y = "TARGET_AMT",
       title = "Target AMT_density plot") +
  theme(legend.position = "none")





numericseverity <- dplyr::select_if(allstateseverity, is.numeric)
(corr= tidy_corr_pvals(numericseverity))


#Now lets take the correlations inlcuding one hot encoded values 
(corrallincludingcategory= tidy_corr_pvals(allstateseverityonehot))

# P-value heat map
pvalueheatmap(corr)


# Correlation heat map
corrheatmap(corr)


#glm modelling 

severity <- glm(loss ~ . , family=Gamma(link=inverse), data=allstateseverity)
