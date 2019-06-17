# Graph-Interpolator
Interpolation from digitizing graphs, also have option to generate rating curve of river section.
It has main 3 functional functions, one is proposed but i have been not able to start that.
## Installation
You can install in or run it in 3 ways. ( check the Prerequisites)
* You can clone this repository and run it as it it, if you have python, you can directly run the main.py (althoug this .py is modified before i made this repo so it is not stable.)
````
git clone https://github.com/Atreyagaurav/Graph-Interpolator.git
````
* You can use the files inside the "Interpolator_v3.0" which is the last stable build. 
* You can also download the zip of this repository and do one of the above.

## Inerpolate From Image
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
This function takes input of a file with x,y or x,y,z data to interpolate a unknown data or interpolate a lot of data stored in a csv (comma seperated text) format. <will add more>
## Prerequisites
You'll need one third party app:
* imgmagick - you can find it [here](https://imagemagick.org/script/download.php)
If you don't have this tool and don't want it- you can manually change the format of the picture you need to digitize to .gif format of maximum size 1000px X 500px and save it in the "pics" folder. the you can normally load the picure without the imgmagick. I have only used imgmagick to do this.