# parkingBuddy
### 2nd Place Winner Best Overall App
#### A Smart Parking app initiative co-developed by Calvin Settachatgul, Terri Wong and Nathan Webster in MTC x Automatic ConnectedCar Hackathon, Oakland CA. 

![parkingbuddy-ui-1](https://cloud.githubusercontent.com/assets/4592446/14429745/8ebcdb8e-ffb3-11e5-8c0c-6e35cc542a42.gif)

**Problem Space**

The taem chose to dive into a real-life **painful** problem in the San Francisco Bay Area: parking.

Some cases:
1. It's hard to know whether a parking garage is full or not
2. It's hard to remember which floor/where the spot is in a large parking structure
3. It's hard to track what time the spot will be expired sometimes

**The idea**
With public data of local parking garages, we can map nearby parking structures according to users' current location, or their input of destination. 

With real-time event data from Automatic, we can keep track of numbers of vehicles coming in and out from the parking structure in past one hour to predict the parking structure's "fullness". The results will reflect by colors on the map: the darker the color, the fuller the structure is.

The app also targets at helping people find their cars inside the building and remind them the if parking is expiring via messages.


**The Hackathon initiative**

Through the two-day Hackathon the team was able to build up the data model and map, tested it on small dataset to map garages locations. An algorithm was developed to give each garage a score based on vehicle data, reflected by 3 tiers in backend and 3 colors on the interface. The higher the score, the more vehicles have arrived the parking garage than have left, so we predict there is less likelihood to find a parking spot easily in that structure. 


**How to run it on local machine**

On your machine: 

>run PostgresSQL app

In Terminal:

>Create virtual environment by `virtualenv env`

>Activate virtual environment by `source env/bin/activate`

>Install dependencies by `pip install < requirements.txt`

>Back in Terminal: Create database by `createdb parkingbuddy`

>Connect to database by `python model.py`

>Inject data by `python seed.py`

>Run the app by `python app.py`

>App runing in http://localhost:5000/

