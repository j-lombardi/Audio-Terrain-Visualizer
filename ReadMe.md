# Audio-Terrain-Visualizer
## About
Audio-Terrain-Visualizer was a senior year capstone project between myself and my partner, BenHammond5. The goal of the project was to use an audio file in order to drive a terrain generation algorithm. We wanted to build a brand new audio visualizer the likes of which had not been seen before.
The project itself came together relatively well and works decently but we have now finished up our time in school and have moved to open source this project in case anyone would like to continue working on it in the future. Many of the test code and useless files that we moved past have been left in the [Deprecated](../Deprecated) folder in case anyone would like to see how we progressed forward with this project. 

## Installation
This is a simple Python project that runs almost entirely out of the box, with one dependency you'll have to install into your path directory. Python by default only handles .wav files so for this function to run you must install ffmpeg. Ffmpeg will allow Python to read and manipulate .mp3 file types as well as many others (only mp3 tested with this program).

## Getting ffmpeg set up

You may use **libav or ffmpeg**.

Mac (using [homebrew](http://brew.sh)):

```bash
# libav
brew install libav --with-libvorbis --with-sdl --with-theora

####    OR    #####

# ffmpeg
brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora
```

Linux (using aptitude):

```bash
# libav
apt-get install libav-tools libavcodec-extra

####    OR    #####

# ffmpeg
apt-get install ffmpeg libavcodec-extra
```

Windows:

1. Download and extract libav from [Windows binaries provided here](http://builds.libav.org/windows/).
2. Add the libav `/bin` folder to your PATH envvar
3. `pip install pydub`

## Class Description
There are three main classes that drive this project each with their own uses.
- [AudioAnalysis.py](../AudioAnalysis.py); AudioAnalysis is exactally it sounds like. This class is responsible for the main audio manipulation and analysis of the program and is where the main bulk of the information is generated. 
- [TerrainFunctions.py](../TerrainFunctions.py): This is the main terrain generation class of the program. This uses the VPython library to generate shapes of heights determined by [AudioAnalysis.py](../AudioAnalysis.py) to build the terrain output. 
- [DisplayVisualizer.py](../DisplayVisualizer.py): This is the main driver function of the program. This files defines a couple of drop down menus that are used to control color options within the visualization as well as output the shapes generated by [TerrainFunctions.py](../TerrainFunctions.py)

## Quickstart 
[DisplayVisualizer.py](../DisplayVisualizer.py) already has a quick one line start of the application but just to explain it a little here goes; To simply generate a terrain based on any song file you wish all that needs to be done is simply import [TerrainFunctions.py](../TerrainFunctions.py) then call the function `perform_3d_generation(path_to_file)` where path_to_file is a file extension to the specific .mp3 file you want to visualize. We use TKinter to generate a file dialog box to allow users to browse their directory and select with a mouse click but you may do it however you would like. 

## License ([MIT License](http://opensource.org/licenses/mit-license.php))
Copyright (c) 2020 Julian Lombardi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
