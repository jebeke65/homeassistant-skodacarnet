
Configuration
------------

Make sure you have a account on Skoda carnet.

```yaml
Skodacarnet:
    username: <username to Skoda carnet>
    password: <password to Skoda carnet>
    spin: <S-PIN to Skoda carnet>  
    scan_interval: 
        minutes: 2
    name:
        wvw1234567812356: 'Skoda Superb'
    resources:
        - combustion_engine_heating
        - position
        - distance
        - service_inspection
        - oil_inspection
        - door_locked
        - trunk_locked
        - request_in_progress
```

* **spin:** (optional) required for supporting combustion engine heating start/stop.

* **scan_interval:** (optional) specify in minutes how often to fetch status data from carnet. (default 5 min, minimum 1 min)

* **name:** (optional) set a friendly name of your car you can use the name setting as in confiugration example.

* **resources:** (optional) list of resources that should be enabled. (by default all resources is enabled).

Available resources:
```
    'position',
    'distance',
    'electric_climatisation',
    'combustion_climatisation',
    'window_heater',
    'combustion_engine_heating',
    'charging',
    'adblue_level',
    'battery_level',
    'fuel_level',
    'service_inspection',
    'oil_inspection',
    'last_connected',
    'charging_time_left',
    'electric_range',
    'combustion_range',
    'combined_range',
    'charge_max_ampere',
    'climatisation_target_temperature',
    'external_power',
    'parking_light',
    'climatisation_without_external_power',
    'door_locked',
    'trunk_locked',
    'request_in_progress'
```

Example of entities
------------
![alt text](https://user-images.githubusercontent.com/12171819/55963464-30216480-5c73-11e9-9b91-3bf06672ef36.png)
