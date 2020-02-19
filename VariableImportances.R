#This script includes all functions and their variable importances

VarImpCaret_meandecreaseGini =function(model,topN){
  #' Given a model create a data frame of variable importances using VarImp in Caret
  #' This function calculates the mean gini index : 
  #' https://www.r-bloggers.com/variable-importance-plot-and-variable-selection/ 
  #' @param model any model object 
  #' @param topN, number of topN features to pick 
  #' Dependency on  caret packages.
  #Example to call this function : varimp= VarImpCaret_meandecreaseGini(severity,10)
  
  library(caret)
  varimpcaret <- caret::varImp(severity)
  varimpcaret <- data.frame(variable   = rownames(varimpcaret),importance = varimpcaret$Overall
  )
  varimpcaretsorted<- arrange(varimpcaret, desc(importance)) #Soring in decreasing order of importance
  
  
  print(varimpcaretsorted %>% head())
  
  (varimptopN <- head(varimpcaretsorted,topN))# #Selecting only topN variable importances
  
  
  #Plotting the variable importance 
  plot.new
  varimpplot <- ggplot(varimptopN, aes(x=reorder(variable, importance),weight=importance,color=importance,fill=importance)) + 
    geom_bar() +
    labs(x="Variable name",y="Importance",title="Mean Decrease Gini Variable importances")+
    coord_flip()
  
  print(varimpplot)
  
  return(varimptopN)
  
  #
  
}