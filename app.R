#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggfortify)
library(survival)

data = read.csv('ODG_Sample_Raw.csv')
data = data[,c('X3_Age','X4_Gender','X12_Total.Disability.Duration')]
data['censor'] = 1
colnames(data) = c('Age','Gender','Disability_Duration','Censor')


# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("KM Curve"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
        selectInput(inputId = "age", 
                    label = "Age: ",
                    choices = c("Young"   = "young", 
                                "Middle Age" = "old"), 
                    selected = "young")
                    
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
         plotOutput("distPlot")
      )
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  fit <- reactive({
    if (input$age=='young'){
      subdata = subset(data, Age <38)
    }
    else{
      subdata = subset(data, Age >=38)
    }
    fit <- survfit(Surv(Disability_Duration, Censor) ~ Gender, data = subdata)
  })
   output$distPlot <- renderPlot({
      # generate bins based on input$bins from ui.R
      autoplot(fit())
   })
}

# Run the application 
shinyApp(ui = ui, server = server)

