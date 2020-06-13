Skoda Carnet - An home assistant plugin to add integration with your car
============================================================


Description
------------
This platform plugin allows you to see some information from Skoda carnet related to your car that has a valid carnet subscription.

It also allows you to trigger some functions like start climatisation if your car supports that.

Remote engine heating is supported for combustion engine vehicles that uses the carnet portal together provided S-PIN. Probably not availabel for all car models.

Note: Some features included with the new 2020 WeConnect make and models (Golf/Passat 8.5/Tiguan etc) MY2019> are to be considered beta. The current release (2020-06-13) has been tested with an Passat GTE MY2017 and Passat GTE MY2020 with full functionality.

Installation
------------

Make sure you have a account on Skoda carnet.

Clone or copy the root of the repository into `<config dir>/custom_components`

Add a Skodacarnet configuration block to your `<config dir>/configuration.yaml`
```yaml
Skodacarnet:
    username: <username to Skoda carnet>
    password: <password to Skoda carnet>
    spin: <S-PIN to Skoda carnet>  
    scan_interval: 
        minutes: 2
    name:
        wSkoda1234567812356: 'Volkswagen Superb'
    resources:
        - combustion_engine_heating # Note that this option is only available for 2019> Facelift model
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



Automation example
------------
In this example we are sending notifications to a slack channel

`<config dir>/automations.yaml`
```yaml
# Get notifications when climatisation is started/stopped
- alias: skoda_superb_climatisation_on
  trigger:
   platform: state
   entity_id: switch.skoda_superb_climatisation
   from: 'off'
   to: 'on'
  action:
   service: notify.slack
   data_template:
    title: "Skoda climatisation started"
    message: "Skoda climatisation started"

- alias: skoda_superb_climatisation_off
  trigger:
   platform: state
   entity_id: switch.skoda_superb_climatisation
   from: 'on'
   to: 'off'
  action:
   service: notify.slack
   data_template:
    title: "Skoda climatisation stopped"
    message: "Skoda climatisation stopped"
    
# Get notifications when vehicle is charging
- alias: skoda_superb_charging
  trigger:
   platform: state
   entity_id: switch.skoda_superb_charging
   from: 'off'
   to: 'on'
  action:
   service: notify.slack
   data_template:
    title: "Skoda is now charging"
    message: "Skoda is now charging"

# Get notifications when vehicle is fully charged
- alias: skoda_superb_battery_fully_charged
  trigger:
   platform: numeric_state
   entity_id: switch.skoda_superb_battery_level
   above: 99
  action:
   service: notify.slack
   data_template:
    title: "Skoda is now fully charged"
    message: "Skoda is now fully charged"

# Announce that the car is unlocked but home
- id: 'car_is_unlocked'
  alias: The car is at home and unlocked
  trigger:
  - entity_id: binary_sensor.my_passat_gte_external_power
    platform: state
    to: 'on'
    for: 00:10:00
  condition:
  - condition: state
    entity_id: lock.my_passat_gte_door_locked
    state: unlocked
  - condition: state
    entity_id: device_tracker.life360_my_lord
    state: home
  - condition: time
    after: '07:00:00'
    before: '21:00:00'
  action:
# Notification via push message to the lors smartphone
  - data:
      message: "The car is unlocked!"
      target:
      - device/my_device
    service: notify.device
# Notification in a smart speaker (kitchen)
  - data:
      entity_id: media_player.kitchen
      volume_level: '0.6'
    service: media_player.volume_set
  - data:
      entity_id: media_player.kitchen
      message: "My Lord, the car is unlocked. Please attend this this issue at your earliest inconvenience!"
    service: tts.google_translate_say


```

Enable debug logging
------------
```yaml
logger:
    default: info
    logs:
        Skodacarnet: debug
        custom_components.skodacarnet: debug
        custom_components.skodacarnet.climate: debug
        custom_components.skodacarnet.lock: debug
        custom_components.skodacarnet.device_tracker: debug
        custom_components.skodacarnet.switch: debug
        custom_components.skodacarnet.binary_sensor: debug
        custom_components.skodacarnet.sensor: debug
 ```

Lovelace Card
------------
Check out this awesome lovelace card by endor
https://github.com/endor-force/lovelace-carnet

![alt text](https://user-images.githubusercontent.com/12171819/55963632-7d9dd180-5c73-11e9-9eea-c2b211f6843b.png)
