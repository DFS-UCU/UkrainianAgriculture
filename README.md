# Data-driven Ukrainian Agriculture

## Introduction
### Problem statement
Despite its tremendous agricultural potential, Ukraine has one of the lowest yield per hectare in Europe. More than 2M ha in Ukraine are used inefficiently, and almost 5M ha are not used at all. 
The mentioned inefficiency could be dealt with if this sector was driven by all the data it produces every day. Collecting and sharing this data would allow us to analyze it and optimize agricultural sector of Ukrainian economics.

### Who could be interested?
* Small agricultural companies that do not have enough lands to waste them on inefficient farming. They also don’t have the means and resources for collecting all the necessary data as well as analyzing it for improving the productivity of their fields. Thanks to a chance to attend and participate in the programme of the “AgroTalks Day” conference, we were able to get in touch with the representatives of four Ukrainian agricultural companies who provided us with the data they were collecting and allowed us to use it in our research. In the following sections we will describe this data and the insights we have collected by analyzing it.

## Similar research
1. [Sen2Agri](http://www.esa-sen2agri.org/) is the Sentinel-2 for Agriculture system; it is designed to automatically generate key products for agriculture monitoring, based on Sentinel-2 and Landsat-8 data. They use ensembles of sophisticated techniques, including computer vision and normalized vegetation indices for labeling the crop lands.
https://github.com/Sen2Agri/Sen2Agri-System - link to project source code.
2. [Cropio](https://about.cropio.com/) is a satellite field management system that facilitates remote monitoring of agricultural land. The System provides real-time updates on current field and crop conditions, determines vegetation levels and identifies problem areas, delivers precise weather forecasts.
3. Geosys is the company that uses images produced by Landsat 8 and Sentinel 2 satellites. Moreover, they also use images from the private satellites and other suppliers of the scientific data. 
4. [Descartes Labs](https://www.descarteslabs.com/) uses satellite imagery to model complex systems on the planet, like forestry and agriculture. They process data flows from all the major satellite constellations at scale to provide instant access to analysis-ready images of the entire world in a massive, searchable, on-demand interface.

## Materials and methods
### Materials (data sources)
1. The main data source we were using was the archive of spreadsheets and shapefiles shared with us by the representatives of the private agricultural companies we’ve met at the conference “AgroTalks Day” in Kyiv, Ukraine. 

 * 5 years data.
 * 160 fields in Odesa region with identification of crop types.
 * Weekly measured NDVI values.
 * Annual yields for each field.

2. Data on the drone flights received from the MegaDrone company.

 * 7 flights performed during the blossom season in 2016.
 * 350 drone pictures merged into orthophoto with the help of DroneDeploy.

3. [Land Parcel Identification System (LPIS)](http://eagri.cz/public/app/eagriapp/lpisdata/). This is the European system for agricultural monitoring created as common agricultural policy for Europe. We explored database of the shape files for Czech republic.

 * Geo-location of parcels with the identification of the crops.
 * Crop size and parcel area.
 * 150 000 of shape files.

4. [NOAA STAR](https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/vh_browse.php). Service that provides global vegetation health products (NDVI, VHI, etc). It could be downloaded in netcdf nc format that contains average value from NDVI in square of size 4 by 4 km.

 * Weekly updated data.
 * Resolution: 4 km per pixel.
 * Produces more than 2 GB of data annually since 1981.

5. [Global Surface Summary of the Day](ftp://ftp.ncdc.noaa.gov/pub/data/gsod). Data on weather conditions derived daily from the global data obtained from the USAF Climatology Center.

 * Up to 20 relevant weather conditions gathered daily.

6. [Planet.com](https://www.planet.com/products/planet-imagery/) is designing, building, launching satellites and providing satellite imagery. Operating in near-real time.

 * Imagery archive dating back to 2009 (daily data).
 * 300M km2/day.
 * 3m per pixel resolution.

7. State Statistics Service of Ukraine. This is national ministry of Ukraine that record statistics. They provided us with the annual data for different agricultures grouped by regions of the country.

8. Ukraine cadaster
 * Rejected our query for the data.

### Methods
* Computing the correlation between different features and the target value of yields per field, using Pearson correlation coefficient, Spearman’s rank correlation coefficient, calculating the p-value.
* Training different regression and ensemble models, such as Linear Regression, Ridge Regression, RandomForest Regressor, LightGBM, for predicting the yields based on the NDVI and weather features.
* Predicting the crop type based on its NDVI curve similarity to the generalized crop curve (curve generated from all parcels for all years). For computing the curve similarity we have used the RMS difference score. The field with the lowest score is considered the most probable target crop type. We received 51% true positive results that is much better result than 10% guess (one out of 10 crops). 

## Results
We proved that there is no correlation between NDVI measures and yields. But when we combine NDVI data with weather data turns out there is some correlation. It can be seen on our visualization that there’s some general pattern for all cultures for every year, however, there are visible year to year differences. We have made an assumption that there could be some unobvious dependencies which affect NDVI, as well as some obvious ones, such as weather parameters. Even though neither NDVI nor any of the weather columns have a direct correlation with the targeted yields column, the models that were trained on both of them resulted in better performance.

## Conclusion
Our team has made a deep and full overview of the open data sources. We analyzed the wide set of factors that affect the culture vegetation and thus the yield. We managed to build both regression and ensemble models that helped to evaluate our hypothesis and the most significant features for forecasting. We have demonstrated that even on that small amount of data that we had we could obtain some interesting insights. Our solution is scalable and it’s possible to apply it to the other regions.

## Aknowledgements
We would like to thank our teacher Oleksandr Romanko, UCU, organizers of the “AgroTalks Day” conference, Vadym Ostapenko, Valeriy Yevtushenko.

## About us
We are the students of the Master's Program in Data Science at the Ukrainian Catholic University (UCU) in Lviv, Ukraine.

* Ivan Ilnytskyi
 * <ilnytskyi@ucu.edu.ua>
* Yuriy Kaminskyi
	* <kaminskyi@ucu.edu.ua>
	* [https://www.linkedin.com/in/ykaminskyi/](https://www.linkedin.com/in/ykaminskyi/)
* Tetiana Martyniuk
 * <t.martynyuk@ucu.edu.ua>
 * [https://www.linkedin.com/in/tetiana-martyniuk-96b866146/](https://www.linkedin.com/in/tetiana-martyniuk-96b866146/)
* Yuriy Pryima
 * <y.pryima@ucu.edu.ua>
 * [https://ua.linkedin.com/in/yuriy-priyma-4a719395](https://ua.linkedin.com/in/yuriy-priyma-4a719395)
* Oleksandr Zaytsev
 * <oleks@ucu.edu.ua>
 * [https://www.linkedin.com/in/-oleks/](https://www.linkedin.com/in/-oleks/)
* Kateryna Zorina
 * <zorina@ucu.edu.ua>
 * [https://www.linkedin.com/in/katerina-zorina-a2217012a/](https://www.linkedin.com/in/katerina-zorina-a2217012a/)
