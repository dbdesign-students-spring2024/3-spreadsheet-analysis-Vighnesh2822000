# Report

### Data origin
- The data I deal with in this assignment is Data from the MTA about the number of buses during peak hours, scheduled for a specific  route for each month starting from the January of 2015 till Decemeber of 2019. It also seperated the routes on the basis of which borough they start in. 
Here is the link to the webpage: [MTA Bus service Delivered: 2015-2019](https://data.ny.gov/Transportation/MTA-Bus-Service-Delivered-2015-2019/tw28-zvtk/about_data)

- The original file i downloaded was in CSV format, although you could choose a number of different ones.
- First twenty rows from the original file

|month  | borough| day_type|trip_type|route_id|period|actual_number_of_buses|scheduled_number_of_buses|service_delivered|
|-------|--------|---------|---------|--------|------|----------------------|-------------------------|-----------------|
|2015-01|Bronx|1|EXP|BXM1|Peak|486|532|0.913533835|
|2015-01|Bronx|1|EXP|BXM10|Peak|491|494|0.993927126|
|2015-01|Bronx|1|EXP|BXM11|Peak|454|456|0.995614035|
|2015-01|Bronx|1|EXP|BXM18|Peak|187|201|0.930348259|
|2015-01|Bronx|1|EXP|BXM2|Peak|283|283|1|
|2015-01|Bronx|1|EXP|BXM3|Peak|326|321|1.015576324|
|2015-01|Bronx|1|EXP|BXM4|Peak|168|171|0.98245614|
|2015-01|Bronx|1|EXP|BXM6|Peak|278|285|0.975438596|
|2015-01|Bronx|1|EXP|BXM7|Peak|842|855|0.984795322|
|2015-01|Bronx|1|EXP|BXM8|Peak|605|618|0.978964401|
|2015-01|Bronx|1|EXP|BXM9|Peak|636|650|0.978461538|
|2015-01|Bronx|2|EXP|BXM1|Peak|67|70|0.957142857|
|2015-01|Bronx|2|EXP|BXM10|Peak|75|76|0.986842105|
|2015-01|Bronx|2|EXP|BXM11|Peak|71|75|0.946666667|
|2015-01|Bronx|2|EXP|BXM18|Peak|11|10|1.1|
|2015-01|Bronx|2|EXP|BXM2|Peak|64|72|0.888888889|
|2015-01|Bronx|2|EXP|BXM3|Peak|43|42|1.023809524|
|2015-01|Bronx|2|EXP|BXM4|Peak|40|39|1.025641026|
|2015-01|Bronx|2|EXP|BXM6|Peak|45|45|1|
|2015-01|Bronx|2|EXP|BXM7|Peak|120|124|0.967741935|
|2015-01|Bronx|2|EXP|BXM8|Peak|70|72|0.972222222|


### Problems with the data set
- There wasn't problem as such to solve with this data. It was very well formatted and pretty consistent. But on top of data on a specific route for a given month, there were two additional entries at the end of each month which summed up the systemwide data for the month, differentiating for weekdays and weekends. The position of this was not ideal for my analyses, so I moved them towards the end of the table using python (I didnt want to delete these records either).
- The other scrubbing I did was to completely remove the period column, because every record had the same value, and on the systemwide record row it was not necessary either.

### Links to data files
- The raw data from the source - [MTA Bus service data](https://drive.google.com/file/d/17dgr2tyx6_93027JDnmxGm6Pza9B7OmT/view?usp=drive_link)
- The munged data- [Cleaned up data file](https://drive.google.com/file/d/134WxhqUF-Sgnx4FcFE7DYtOyVKD3FptM/view?usp=drive_link)
- Spreadsheet file- [Excel file with analysis](https://docs.google.com/spreadsheets/d/1W9dNrOOUAwffJOhX9_7CNFn7eUk6ioRu/edit?usp=drive_link&ouid=104316166021361528428&rtpof=true&sd=true)


## Analysis
_IT IS IMPORTANT TO NOTE THAT THE DATA IS FOR SERVICES DURING PEAK HOURS AND NOT A WHOLE DAY, SO ALL THE ANALYSIS ARE CATERED TO THIS PERIOD ONLY_
- First i calculated the total number of buses that actually ran from January 2015-December 2019
- Next i also wanted to know the total number of buses that were scheduled for the same period
- With the above two information i calculated the number of buses that were scheduled but didnt run
- then I found out the percentage of buses that didn't run- Less than half a percent, very impressive for a five year period! And also for the size of the city!
-I also wanted to know the maximum number of buses for specific route that were scheduled for a specific month(during peak hours) 
- Similarly I also calculated the minimum number for the above mentioned criteria.

- Next, I calculated the sum of buses scheduled during the weekdays and weekends seperately for a specific borough for the year 2015.
- Followed by the total number of express buses for the year 2015
- I wanted to compare that with the most recent year for which we have data (2019), so i did the same thing for 2019- I was surprised to find out that most buses were scheduled in Queens and as a whole the total number of buses scheduled had increase in the five year period.
- I read somehwere that the most busy route in NYC is the B46 route, so i wanted to find out the average number of buses scheduled in a month
- To compare that with something, i chose the M14A buses that i frequented in while living in palladium hall.
- I also found out the maximum and minimum number of B46 buses scheduled for a specific month (both weekends and weekdays)

## Pivot Table
        
|Row Labels|	Sum of scheduled_number_of_buses|	Sum of actual_number_of_buses|
|----------|------------------------------------|--------------------------------|
|2015-01   |	
|1		|
|Bronx	|35218|	33602|
|Brooklyn	|45889	|43799|
|Manhattan|	26837	|24709|
|Queens	|66883|	61821|
|Staten Island	|22683|	21898|
|Systemwide	|197510	|185829|
|2		|
|Bronx	|8933|	8208|
|Brooklyn	|11951|	11035|
|Manhattan	|7417	|6834|
|Queens	|13796	|12554|
|Staten Island|	2881|	2682|
|Systemwide	|44978	|41313|


- The results in the pivot table show the varying number of schedulede and actual number of buses that run for a given month seperated by weekends(1) and weekdays(2), similar to the analysis done ableve, but more visually pleasing. I assumed that the number of buses running on the weekends would be higher for the touristy months in NYC, but that is not the case and there is no correlation from year to year. It doesnt follow any pattern!

## EXTRA CREDIT
_This assignment deserves extra credit because of the very large size of the data _and also my effort to use requests library to pull the data from the webpage(although unsuccessful). If you go to the MTA data page you will see a Export button on top and i tried to extract the data using beautiful soup in this webpage , but failed to do it. I also tried to go to the data page from the webpage where the data is visible, but only 50 rows per page and i didnt know how to move to the next page using beautiful soup