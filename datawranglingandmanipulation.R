
#This code is mainly for data wrangling or manipulation methods

#r constants
n.values <- c(500, 1000, 2000)
iterations <- 3
WeightRow <- 0.25
WeightTime <- 0.25
WeightError <- 0.5


find_mode = function(in_vector) {
  #' Return most frequently occuring element in vector
  unique_values = unique(in_vector)
  mode_value = unique_values[which.max(tabulate(match(in_vector, unique_values)))]
  return(mode_value)
}


#function to one hot encode :

onehotencode=function(data) {
  #' Given a dataframe of , generate a
  #' new dataframe trsf which returns dummy values
  #' #' Dependency on  caret packages.
  #' @param data data.frame object with both numeric and categorical values
library(caret) 
dmy <- caret::dummyVars(" ~ .", data = data )
trsf_data <- data.frame(predict(dmy, newdata = data))
return(trsf_data)

}

# dat_n_k: training set at sample size n with kth sample

samplefromdata=function(data){
sampledata.names <- data()
for (n in n.values) {
  for (k in (1:iterations)){
    index <- sample(1:nrow(data),n)
    dat_name <- paste('dat',n,k,sep = '_')
    assign(dat_name,train[index,])
    sampledata.names <- c(sampledata.names,dat_name)
  }
}

}