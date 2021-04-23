# Information-For-Hamed
Here you have access to SolidAngle.py which basically calculates the efficiency and count
This file takes an excel file called Mesh and for 1000 iteration of montecarlo calculates these parameters.
This code works onl for one detector and you need to give the coordinate of detector manually.
The StoreData.py is another version of SolidAngle.py but only saves the weight factor for alpha and theta and photon traveled path length inside the detector and reactor.
Therefore this code does not calculate efficiency of count directly.
There is another code InegrationCall.py which basically use the stored data, a set of experimental data (count) and do the optimization to find unknown parameters for each detector (Detector dead time, source activity and media attenuation coefficient factor)
You also see here for excel data set wtetha.csv walpha.csv depthReactor.csv depthDetector.csv which are presored parameters for Mesh points that I use them in optimization 
Another excel file you have access is Artificial data set which I generated the by my MonteCarlo code but I consider them as experimental data set to test that does Nelder mead works efficiently to back calculate or not.
