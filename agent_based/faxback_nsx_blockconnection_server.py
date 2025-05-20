#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# License: GNU General Public License v2

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric, check_levels
from typing import Dict, Any
import itertools
import json

# Special Agent Output to Parse for this service
"""
<<<faxback_nsx_blockconnection_server:sep(0)>>>
{'SendingCount': '0', 'ReceivingCount': '0', 'PeakSendingCount': '0',
 'PeakReceivingCount': '0', 'SentCount': '0', 'ReceivedCount': '0',
 'SentSeconds': '0', 'ReceivedSeconds': '0', 'LoginCapacity': '4000',
 'LoginCount': '2', 'PeakLoginCount': '2', 'Enabled': '1',
 'TcpCurrentCount': '5', 'TcpPeakCount': '6', 'TcpCount': '2913',
 'HttpCurrentCount': '1', 'HttpPeakCount': '2', 'HttpCount': '388796',
 'CpuPeakTime': '100', 'CpuTime': '19', 'StatusNum': '0'}
"""
def parse_faxback_nsx_blockconnection_server(string_table) -> Dict[str, Any]:
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
            parsed[key] = value
            
    return parsed

agent_section_faxback_nsx_blockconnection_server = AgentSection(
    name="faxback_nsx_blockconnection_server",
    parse_function=parse_faxback_nsx_blockconnection_server,
    parsed_section_name="faxback_nsx_blockconnection_server",
)

def discovery_faxback_nsx_blockconnection_server(section):
    yield Service()

def check_faxback_nsx_blockconnection_server(section):

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


    LoginPercentage = round((section.get('LoginCount', 0)) / section.get('LoginCapacity', 1) * 100, 1)
    
    logincrit = 90
    loginwarn = 80
    if LoginPercentage >= logincrit:
        yield Result(
            state=State.WARN,
            summary=f"Login percentage exceeds {logincrit}%.")
    elif LoginPercentage >= loginwarn:
        yield Result(
            state=State.OK,
            summary=f"Login percentage exceeds {loginwarn}%.")
    else:
        yield Result(
            state=State.OK,
            summary="Login percentage is within desired range.")

    for key, value in section.items():
        if isinstance(value, (int, float)) and key not in ['Enabled', 'StatusNum']:
           yield Metric(name=key, value=section.get(key,0))

check_plugin_faxback_nsx_blockconnection_server = CheckPlugin(
    name="faxback_nsx_blockconnection_server",
    service_name="Faxback NSX BlockConnection Server",
    discovery_function=discovery_faxback_nsx_blockconnection_server,
    sections=["faxback_nsx_blockconnection_server"],
    check_function=check_faxback_nsx_blockconnection_server,
)
