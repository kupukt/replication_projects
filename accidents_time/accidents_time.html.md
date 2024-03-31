---
title: "Accidents in New York"
format: html
editor: visual
date: "`r format(Sys.time(), '%B %d, %Y')`"
execute:
  keep-md: true
warning: false
html:
  code-fold: true
  code_tools: true
---


::: {#f7505583 .cell execution_count=1}
``` {.python .cell-code}
import polars as pl
import pins
from lets_plot import *
LetsPlot.setup_html()

dat = pl.read_parquet("ny_crashes.parquet")

boroughdat = dat.fill_null("Unknown")

rates = boroughdat\
.with_columns(
    pl.col("date_time").dt.truncate("1h").alias("hour_floor"))\
    .group_by("hour_floor", "BOROUGH")\
    .agg(
        pl.sum("NUMBER OF PERSONS INJURED").alias("injured_total"),
        pl.col("BOROUGH").count().alias("accident_count")
    )\
    


rates_day = boroughdat\
.with_columns(
    pl.col("date_time").dt.truncate("1d").alias("day_floor"))\
    .group_by("day_floor", "BOROUGH")\
    .agg(
        pl.sum("NUMBER OF PERSONS INJURED").alias("injured_total"),
        pl.col("BOROUGH").count().alias("accident_count")
    )\
    .with_columns(pl.col("day_floor").dt.weekday().alias("weekday"))
```

::: {.cell-output .cell-output-display}

```{=html}

            <div id="n71VMI"></div>
            <script type="text/javascript" data-lets-plot-script="library">
                if(!window.letsPlotCallQueue) {
                    window.letsPlotCallQueue = [];
                }; 
                window.letsPlotCall = function(f) {
                    window.letsPlotCallQueue.push(f);
                };
                (function() {
                    var script = document.createElement("script");
                    script.type = "text/javascript";
                    script.src = "https://cdn.jsdelivr.net/gh/JetBrains/lets-plot@v4.2.0/js-package/distr/lets-plot.min.js";
                    script.onload = function() {
                        window.letsPlotCall = function(f) {f();};
                        window.letsPlotCallQueue.forEach(function(f) {f();});
                        window.letsPlotCallQueue = [];
                        
                    };
                    script.onerror = function(event) {
                        window.letsPlotCall = function(f) {};    // noop
                        window.letsPlotCallQueue = [];
                        var div = document.createElement("div");
                        div.style.color = 'darkred';
                        div.textContent = 'Error loading Lets-Plot JS';
                        document.getElementById("n71VMI").appendChild(div);
                    };
                    var e = document.getElementById("n71VMI");
                    e.appendChild(script);
                })()
            </script>
            
```

:::
:::


::: {#5b31dafb .cell execution_count=2}
``` {.python .cell-code}
ggplot(rates_day.sort("weekday"), aes(x= "weekday", y = "accident_count")) + geom_boxplot() + facet_wrap(facets= "BOROUGH") + scale_x_discrete()
```

::: {.cell-output .cell-output-display execution_count=2}

```{=html}
   <div id="IdaRJd"></div>
   <script type="text/javascript" data-lets-plot-script="plot">
       (function() {
           var plotSpec={
"data":{
},
"mapping":{
"x":"weekday",
"y":"accident_count"
},
"data_meta":{
},
"facet":{
"name":"wrap",
"facets":"BOROUGH",
"order":1.0,
"dir":"h"
},
"kind":"plot",
"scales":[{
"aesthetic":"x",
"discrete":true,
"reverse":false
}],
"layers":[{
"geom":"boxplot",
"mapping":{
},
"data_meta":{
"series_annotations":[{
"column":"weekday",
"factor_levels":[1.0,2.0,3.0,4.0,5.0,6.0,7.0]
}]
},
"data":{
"..middle..":[52.0,52.0,51.0,52.0,57.0,50.0,42.0,119.0,120.0,118.0,120.0,127.0,103.0,95.0,76.0,85.0,86.0,90.0,92.0,75.0,63.0,100.0,101.0,101.0,100.0,107.0,96.0,83.0,13.0,14.0,14.0,14.0,15.0,13.0,10.0,136.0,139.0,139.0,143.0,152.0,129.0,119.0],
"..lower..":[36.0,37.0,37.0,37.5,42.0,38.0,33.0,73.0,71.0,73.5,74.0,79.0,68.0,66.0,33.0,36.0,36.0,40.0,39.5,36.0,31.0,56.0,55.0,56.0,55.0,62.0,60.0,56.0,7.5,8.0,8.0,8.0,8.0,8.0,7.0,101.0,104.0,103.0,105.0,112.0,100.5,93.0],
"..upper..":[62.0,63.0,61.0,63.0,70.0,58.0,50.0,142.0,141.0,137.0,142.0,148.0,119.0,111.0,102.0,111.5,112.0,117.5,124.0,100.0,83.0,121.0,116.0,117.0,117.0,126.0,110.0,96.5,19.0,20.0,21.0,20.5,22.0,18.0,14.0,194.5,209.5,207.0,215.5,227.5,185.0,166.0],
"..ymin..":[12.0,11.0,10.0,13.0,12.0,14.0,8.0,24.0,30.0,15.0,21.0,31.0,26.0,17.0,5.0,6.0,7.0,5.0,5.0,4.0,3.0,16.0,17.0,18.0,11.0,16.0,18.0,14.0,1.0,2.0,1.0,1.0,2.0,1.0,1.0,47.0,35.0,37.0,31.0,35.0,37.0,32.0],
"..ymax..":[94.0,93.0,86.0,97.0,112.0,81.0,70.0,230.0,192.0,202.0,214.0,200.0,184.0,171.0,170.0,204.0,169.0,171.0,209.0,157.0,128.0,174.0,189.0,170.0,208.0,205.0,183.0,148.0,36.0,38.0,39.0,39.0,42.0,33.0,24.0,331.0,360.0,335.0,356.0,395.0,293.0,269.0],
"weekday":[1.0,2.0,3.0,4.0,5.0,6.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0],
"BOROUGH":["BRONX","BRONX","BRONX","BRONX","BRONX","BRONX","BRONX","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","QUEENS","QUEENS","QUEENS","QUEENS","QUEENS","QUEENS","QUEENS","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown"]
}
},{
"geom":"point",
"stat":"boxplot_outlier",
"mapping":{
},
"show_legend":false,
"data_meta":{
"series_annotations":[{
"column":"weekday",
"factor_levels":[1.0,2.0,3.0,4.0,5.0,6.0,7.0]
}]
},
"data":{
"..middle..":[52.0,52.0,51.0,52.0,57.0,50.0,50.0,42.0,42.0,119.0,120.0,120.0,118.0,120.0,127.0,103.0,95.0,95.0,76.0,85.0,86.0,90.0,92.0,75.0,63.0,100.0,101.0,101.0,100.0,107.0,96.0,83.0,83.0,13.0,13.0,13.0,13.0,13.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,15.0,15.0,15.0,13.0,13.0,13.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,10.0,136.0,139.0,139.0,143.0,152.0,129.0,119.0],
"..lower..":[36.0,37.0,37.0,37.5,42.0,38.0,38.0,33.0,33.0,73.0,71.0,71.0,73.5,74.0,79.0,68.0,66.0,66.0,33.0,36.0,36.0,40.0,39.5,36.0,31.0,56.0,55.0,56.0,55.0,62.0,60.0,56.0,56.0,7.5,7.5,7.5,7.5,7.5,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,101.0,104.0,103.0,105.0,112.0,100.5,93.0],
"..upper..":[62.0,63.0,61.0,63.0,70.0,58.0,58.0,50.0,50.0,142.0,141.0,141.0,137.0,142.0,148.0,119.0,111.0,111.0,102.0,111.5,112.0,117.5,124.0,100.0,83.0,121.0,116.0,117.0,117.0,126.0,110.0,96.5,96.5,19.0,19.0,19.0,19.0,19.0,20.0,20.0,20.0,20.0,20.0,21.0,20.5,20.5,20.5,20.5,20.5,22.0,22.0,22.0,18.0,18.0,18.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,14.0,194.5,209.5,207.0,215.5,227.5,185.0,166.0],
"..ymin..":[12.0,11.0,10.0,13.0,12.0,14.0,14.0,8.0,8.0,24.0,30.0,30.0,15.0,21.0,31.0,26.0,17.0,17.0,5.0,6.0,7.0,5.0,5.0,4.0,3.0,16.0,17.0,18.0,11.0,16.0,18.0,14.0,14.0,1.0,1.0,1.0,1.0,1.0,2.0,2.0,2.0,2.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,2.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,47.0,35.0,37.0,31.0,35.0,37.0,32.0],
"..ymax..":[94.0,93.0,86.0,97.0,112.0,81.0,81.0,70.0,70.0,230.0,192.0,192.0,202.0,214.0,200.0,184.0,171.0,171.0,170.0,204.0,169.0,171.0,209.0,157.0,128.0,174.0,189.0,170.0,208.0,205.0,183.0,148.0,148.0,36.0,36.0,36.0,36.0,36.0,38.0,38.0,38.0,38.0,38.0,39.0,39.0,39.0,39.0,39.0,39.0,42.0,42.0,42.0,33.0,33.0,33.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,24.0,331.0,360.0,335.0,356.0,395.0,293.0,269.0],
"weekday":[1.0,2.0,3.0,4.0,5.0,6.0,6.0,7.0,7.0,1.0,2.0,2.0,3.0,4.0,5.0,6.0,7.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,7.0,1.0,1.0,1.0,1.0,1.0,2.0,2.0,2.0,2.0,2.0,3.0,4.0,4.0,4.0,4.0,4.0,5.0,5.0,5.0,6.0,6.0,6.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,7.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0],
"accident_count":[107.0,132.0,NaN,107.0,127.0,100.0,96.0,76.0,181.0,NaN,247.0,254.0,NaN,NaN,NaN,NaN,180.0,193.0,NaN,NaN,NaN,NaN,NaN,NaN,NaN,250.0,248.0,NaN,214.0,NaN,NaN,185.0,169.0,38.0,57.0,37.0,37.0,37.0,53.0,49.0,51.0,40.0,39.0,NaN,44.0,46.0,46.0,40.0,40.0,44.0,44.0,51.0,37.0,34.0,42.0,29.0,28.0,30.0,26.0,26.0,26.0,27.0,35.0,25.0,26.0,35.0,26.0,25.0,29.0,45.0,NaN,NaN,570.0,469.0,NaN,314.0,NaN],
"BOROUGH":["BRONX","BRONX","BRONX","BRONX","BRONX","BRONX","BRONX","BRONX","BRONX","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","BROOKLYN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","MANHATTAN","QUEENS","QUEENS","QUEENS","QUEENS","QUEENS","QUEENS","QUEENS","QUEENS","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","STATEN ISLAND","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown"]
}
}],
"metainfo_list":[]
};
           var plotContainer = document.getElementById("IdaRJd");
           window.letsPlotCall(function() {{
               LetsPlot.buildPlotFromProcessedSpecs(plotSpec, -1, -1, plotContainer);
           }});
       })();    
   </script>
```

:::
:::


In this graph, we see the distribution of crashes in all of the boroughs 
in New York. We see that crashes are highest on Friday, most likely because it's the weekend and that's when the most people are out driving. Sunday's 
are the days with the least amount of crashes, probably because that's when people aren't out.

