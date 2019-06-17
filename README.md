# Graph-Interpolator
Interpolation from digitizing graphs, also have option to generate rating curve of river section.
It has main 3 functional functions, one is proposed but i have been not able to start that.
## Installation
You can install in or run it in 3 ways. ( check the Prerequisites)
* You can clone this repository and run it as it it, if you have python, you can directly run the main.py (althoug this .py is modified before i made this repo so it is not stable.) So you can use the files inside the "Interpolator_v3.0" which is the last stable build. 
````
git clone https://github.com/Atreyagaurav/Graph-Interpolator.git
````
* You can also download the zip of this repository and do one of the above.
* You can use the Interpolator_v3.0.exe file which is the setup file for windows. Don't install it in C: drive though, the program cannot access the files inside the C: drive and may cause problems.

## Interpolate From Image
The opening Screen first gives you 4 options it is the first one. After clicking it you'll have to do the followings:
* The first screen is the help screen giving information of all the parts in this GUI. Click anywhere to exit.
* if you have any previous data you can just load that.
* The first step is to load the image type in the name of the picture file with full/relative path. and click load. (if you do not have the Prerequisites, follow the steps in that topic.)
* input the origin ordinates and x & y axis extents in the following textboxes.
* choose the type of the curve 2D/3D
* Include origin option will automatically add (0,0) as first data while the high precision option is if you want to click number of times for a single point so that you can correct your mistakes and the average of all the points will be displayed & taken as final data.
* click at 'Input Curve'
* digitize the axis first by clicking at orizin , X-extreme & Y-extreme-the  points should be exactly what value you previously entered.
* if you are inputting 3D curve, type the Z data and submit for every value/contour of Z to start new contour; click submit twice to exit.
* in case of 2D just submit once to finalize. 
* one extra submit is needed for each point if you have choosen the high precision option.
* add variable names in the field. you can add the excel cell names to generate formula for excel.
* Click at which data you want to be interpolated.
* input the file name to save it into.
* click generate formula to generate the Formula for 2D and save the file, while for 3D it only saves the file, you can use the next function "Interpolate from file" to interpolate  3D data.
* the formula for linear and lagrange's interpolation is given, the curve will both is displayed, so if you see the lagrange has the problem of overfitting you can avoid it, it'll be good only for some polynomial curves.
* you can click copy to copy the formula into your clipboard.

## Interpolate From File
This function takes input of a file with x,y or x,y,z data to interpolate a unknown data or interpolate a lot of data stored in a csv (comma seperated text) format. 
This funtion can be used to interpolate both 2D and 3D data, but you have to specify which data you are importing in the first. 
The steps are:
* If you have just digitized your curve click previous data to fill all the relevant input fields. open pic you have it.
* Enter file name and choose the type of data (2D/3D) then click "Load".
* Click Plot Curves to plot the data.
* You can use the fields below "Plot curves" to enter X,Y or Z and calculate the remaining. You can choose from available interpolation methods in the bottom.
* To interpolate large number of data, make a csv file of X or X,Y for 3D, without headers. Load that csv and click interpolate. You can see the interpolated result in the screen. If you click save it'll save the interpolation result in the same path with a suffix.

## Rating Curve Analysis
This is the fuction which uses the digitized section data to analyse the rating curve of the Section. The data of the section is stored in a .3dd file when you digitize it. 
The process to generate rating curve is:
* Same as before the first screen is the help screen, showing the general components of the GUI.
* If you have just digitized the section you can click "Previous Data" to load the inputs. Click at "Open pic" if that is the case.
* If there is no previous data enter Filename.
* Click "Load Data from File". You'll see the table of data on left-top corner.
* Click plot curves from file to plot the graph.
* Input all the hydraulic parameters in the textboxes.
* Click Analyse section and wait for the analysis. You'll see a table in right top corner.
* You can plot the analysed rating curve in matplotliv interface for visualization.
* If you need specific value of discharge for fixed height or vice versa, you can use the textboxes below the analyse section botton.
* To save the rating curve analysis, Give a filename with full path and .csv extension  then click save. It'll save Height, Wetted Perimeter, Top Width, Area, Hydraulic radius and Discharge.

### NOTE: 
You can also use external data by saving a csv of a section data (chainage,elevation) into a .3dd format inside the data folder. Although a method to add external data from excel/AutoCAD can be added in later versions.
You can also use the inter.exe in the file to generate linear interpolation formula. the syntax is:
````
inter <X> <path/filename.ext> <n>
````
where,
* X is the expression of x-variable used,
* n is the number of data in the file to be used for interpolation.
## Prerequisites
You'll need one third party app:
* imgmagick - you can find it [here](https://imagemagick.org/script/download.php)
If you don't have this tool and don't want it- you can manually change the format of the picture you need to digitize to .gif format of maximum size 1000px X 500px and save it in the "pics" folder. the you can normally load the picure without the imgmagick. I have only used imgmagick to do this.