# solid_semantic_sensor 
---Decentralized semantic sensor systems

When it comes to the highly private nature of sensor information, it requires people to value the user's ownership of their own data, which is currently difficult for people to control and organically federate their data.solid as an open protocol allows users the flexibility to take control of their own data.
This repository is a demonstration of using RDF-star and Solid to implement semantic sensor data federation in dynamic knowledge graph. It consists of four main parts:
* Monitoring from the micro-sensor is passed to the Raspberry Pi via MQTT and the data is passed into the time series database in real time
* Solid pod configuration by Community Solid Server
* SSN-log extension module for provenance and timed property
* Sample sensor monitoring datasets
![image](https://github.com/Yingying-Zhang/solid_semantic_sensor/blob/main/img/sensor.png)
