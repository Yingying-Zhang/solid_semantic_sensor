from influxdb import InfluxDBClient
import datetime

def send(dat):
    client = InfluxDBClient('192.168.2.112', 8086, 'root', 'root', 'testdb') 
    #print(client.get_list_database()) 


    current_time = datetime.datetime.utcnow().isoformat("T")
    body = [
        {
            "measurement": "sensor",
            "time": current_time,
            "tags": {
                
            },
            "fields": {
                "GAS": dat
            },
        }
    ]
    res = client.write_points(body)
    #lient.query("drop measurement")

    #query data
    result = client.query('select * from sensor;')
    print("Result: {0}".format(result))


    #client.query('delete ;') # delete data
