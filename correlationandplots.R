#This R file has 3 functions with functions as below : 
# 1) tidy_corr_pvals -> This function takes in the numeric data frame and then returns
#Correlation matrix of all numeric features
#2)  corrheatmap -> This function plots the heatmap of correlation values taking the 
#output of tidy_coor_pvals as the input 
#3)  pvalueheatmap -> This function returns the pvalue heatmap taking the 
#output of tidy_coor_pvals as the input 



# Correlation matrix with p-values

tidy_corr_pvals = function(numeric_data_frame, corr_type = 'pearson'){
  #' Given a dataframe of numeric values, generate a
  #' flattened correlation matrix with p-values
  #' Dependency on Hmisc and dplyr packages.
  #' @param numeric_data_frame data.frame object with only numeric values
  #' @param corr_type type of correlation to calculate ('pearson' or 'spearman')
  #' @return data.frame object with fields 'row', 'column', 'cor', and 'p_value'
  
  cor_pval_matrix = numeric_data_frame %>%
    as.matrix() %>%
    Hmisc::rcorr(type = c(corr_type))
  
  corr_coefficients = cor_pval_matrix$r
  corr_pvalues = cor_pval_matrix$P
  
  positions = corr_coefficients %>% upper.tri()
  
  output_df = data.frame(
    row = rownames(corr_coefficients)[row(corr_coefficients)[positions]],
    column = rownames(corr_coefficients)[col(corr_coefficients)[positions]],
    cor  =(corr_coefficients)[positions],
    p_value = corr_pvalues[positions]
  )
  return(output_df)
}


# Correlation coefficient heat map

corrheatmap=function(corr) {
  #Given a correlation matrix,plot the heat map
  #' @param corr data.frame object with correlation values of numerical features
  #' You can get this using tidy_corr_pvals function , its the return value
  (corrggplot <- ggplot(corr, aes(row, column, fill = cor)) + 
     theme_bw() +
     geom_tile() +
     scale_fill_gradient2(low = "forestgreen",
                          mid = "white",
                          high = "red",
                          midpoint = 0.5) +
     labs(fill = 'Correlation',
          x = 'Variable',
          y = 'Variable',
          title = 'Correlation Coefficients',
          subtitle = 'Pearson correlation used') +
     theme(plot.title = element_text(hjust = 0.5),
           plot.subtitle = element_text(hjust = 0.5)))
  return(corrggplot)
}



# P-value heat map
pvalueheatmap=function(corr) {
  (pvalueggplot=ggplot(corr, aes(row, column, fill = p_value)) + 
  theme_bw() +
  geom_tile() +
  scale_fill_gradient2(low = "red",
                       mid = "white",
                       high = "forestgreen",
                       midpoint = 0.15) +
  labs(fill = 'P-Value',
       x = 'Variable',
       y = 'Variable',
       title = 'Correlation Coefficient P-Values',
       subtitle = 'Pearson correlation used') +
  theme(plot.title = element_text(hjust = 0.5),
        plot.subtitle = element_text(hjust = 0.5)))
  return(pvalueggplot)
  
}
