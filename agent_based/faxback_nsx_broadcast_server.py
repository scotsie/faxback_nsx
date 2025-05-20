#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# License: GNU General Public License v2

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric, check_levels
from typing import Dict, Any
import itertools
import json

# Special Agent Output to Parse for this service
"""
<<<faxback_nsx_broadcast_server:sep(0)>>>
{'Enabled': '1', 'CpuPeakTime': '100', 'CpuTime': '3',
 'DatabaseConnections': 'FaxSendDb=Ok; FaxSendDocsDb=Ok; FaxSendTransDb=Ok;
  FaxActionDb=Ok; ServerAlertsDb=Ok; ServersDb=Ok; BroadcastDb=Ok;
  BroadcastRecipientDb=Ok; BroadcastAttachmentDb=Ok; BroadcastValidationDb=Ok;
  FaxReceiveDb=Ok; FaxEmailDb=Ok', 'StatusNum': '0'}
"""
def parse_faxback_nsx_broadcast_server(string_table) -> Dict[str, Any]:
    """
    Parsing the default string table which comes in as 1 large string as above
    but nested as a list of lists.
    [["<JsonOutputasString>"]]
    """
    #print(f"Parsing string table: {string_table}")
    flatlist = list(itertools.chain.from_iterable(string_table))
    parsed = json.loads(" ".join(flatlist).replace("'", "\""))
    
    # Convert string numbers to numeric values
    for key, value in parsed.items():
        if isinstance(value, str) and value.isdigit():
            parsed[key] = int(value)
        elif isinstance(value, str) and value.replace('.', '').isdigit():
            parsed[key] = float(value)
        else:
            if key == 'DatabaseConnections':
                # Split the DatabaseConnections string into a dictionary
                db_connections = {}
                for db in value.split(';'):
                    db_name, db_status = db.split('=')
                    db_connections[db_name.strip()] = db_status.strip()
                parsed[key] = db_connections
            else:
                parsed[key] = value
    return parsed

agent_section_faxback_nsx_broadcast_server = AgentSection(
    name="faxback_nsx_broadcast_server",
    parse_function=parse_faxback_nsx_broadcast_server,
    parsed_section_name="faxback_nsx_broadcast_server",
)

def discovery_faxback_nsx_broadcast_server(section):
    yield Service()

def check_faxback_nsx_broadcast_server(section):

    if section['StatusNum'] == 0:
        yield Result(state=State.OK, summary=f"Status Code is reported as {section['StatusNum']}")
    elif section['StatusNum'] == 30017:
        yield Result(state=State.UNKNOWN, summary=f"Status Code {section['StatusNum']} with descriptor {section.get('Status', 'None provided')}")
    else:
        yield Result(state=State.WARN, summary=f"Status Code {section['StatusNum']} with descriptor {section.get('Status', 'None provided')}")

    if section['Enabled'] == 1:
        yield Result(state=State.OK, summary=f"Service is reporting enabled")
    else:
        yield Result(state=State.WARN, summary=f"Service is reporting as code {section['Enabled']}. Needs identification")
    
    if section['DatabaseConnections']:
        for db_name, db_status in section['DatabaseConnections'].items():
            details = ""
            if db_status == 'Ok':
                state = State.OK
                details += f"Database connection {db_name} is {db_status}\n"
                summary = f"Databases report OK status"
            else:
                state = State.WARN
                details += f"Database connection {db_name} is {db_status}\n"
                summary = f"Databases report issues"
        yield Result(state=state, summary=summary, details=details)

    for key, value in section.items():
        if isinstance(value, (int, float)) and key not in ['Ready', 'Enabled', 'StatusNum']:
           yield Metric(name=key, value=section.get(key,0))


check_plugin_faxback_nsx_broadcast_server = CheckPlugin(
    name="faxback_nsx_broadcast_server",
    service_name="Faxback NSX Broadcast Server",
    discovery_function=discovery_faxback_nsx_broadcast_server,
    sections=["faxback_nsx_broadcast_server"],
    check_function=check_faxback_nsx_broadcast_server,
)
