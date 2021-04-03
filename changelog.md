# Changelog for in-progress branch

## 04/03/2021 18:20
Fixed another fail, the fail regarding the extra data plot points. One test remains.

## 04/03/2021 18:18
Fixed one failure, the label typo.

## 04/03/2021 18:12
Three failures in the test. Details are below:

- Test Data Plot Points
    - Failure:
        - Expected different data points in scatter plot. 
        - First list contains 37 additional elements.
        - First extra element is 2014.
    - Possible fix:
        - May have to do with the way I added the years to the dataframe to be able to plot out to 2050. May try altering this depending on other errors.
        - May also be an error due to a second plotting of the chart. May also try just making the main plot from the df, then adding in the lines w/ the additional years without redrawing the plot.
- Test Plot Labels
    - Failure:
        - Expected 'inches' and not 'Inches'
    - Possible fix:
        - correct typo.
- Test Plot Lines:
     - Failure:
        - First list contains 1 additional element (at 170), 10.175455257136548
    - Possible fix:
        - Not sure at this point. Will need to see what element 170 is.

## 04/03/2021 18:08
I think I may have already completed this? Going to run it through the repl.it test to see if everything works the way it should, but the function ends by creating a chart that looks about right. Going to test and see.