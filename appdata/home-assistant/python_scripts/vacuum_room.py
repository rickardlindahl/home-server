# Vacuum specific room(s), multiple names for a room can be used

roomConfig = {
  2: ["bedroom"],
  3: ["estelle's room"],
  16: ["hall"],
  17: ["kitchen"],
  18: ["living room"],
}

roomGroups = {
  "all": roomConfig.keys(),
}

entity_id = data.get("entity_id") # pylint: disable=undefined-variable
area = data.get("area").lower() # pylint: disable=undefined-variable

roomsToClean = []
for roomNumber, roomNames in roomConfig.items():
    for name in roomNames:
        if name in area: 
            roomsToClean.append(int(roomNumber))
            continue

for roomGroupName, roomNumbers in roomGroups.items():
    if roomGroupName in area: 
        roomsToClean.extend(roomNumbers)
        continue
        
if entity_id is not None and len(roomsToClean) > 0: 
    service_data = {"entity_id": entity_id, "command": "app_segment_clean", "params": roomsToClean}
    hass.services.call("vacuum", "send_command", service_data, False) # pylint: disable=undefined-variable