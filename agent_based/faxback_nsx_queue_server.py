#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# License: GNU General Public License v2

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric, check_levels
from typing import Dict, Any
import itertools
import json

# Special Agent Output to Parse for this service
"""
<<<faxback_nsx_queue_server:sep(0)>>>
{'SendingCount': '0', 'ReceivingCount': '0', 'PeakSendingCount': '0',
 'PeakReceivingCount': '0', 'SentCount': '0', 'ReceivedCount': '0',
 'SentSeconds': '0', 'ReceivedSeconds': '0', 'LoginCount': '0',
 'PeakLoginCount': '0', 'Enabled': '1', 'TcpCurrentCount': '3',
 'TcpPeakCount': '3', 'TcpCount': '259', 'HttpCurrentCount': '1',
 'HttpPeakCount': '1', 'HttpCount': '50800', 'CpuPeakTime': '100',
 'CpuTime': '3', 'StatusNum': '0'}
"""
def parse_faxback_nsx_queue_server(string_table) -> Dict[str, Any]:
    """
    Parsing the default string table which comes in as 1 large string as above
    but nested as a list of lists.
    [["<JsonOutputasString>"]]
    """
    #print(f"Parsing string table: {string_table}")
    flatlist = list(itertools.chain.from_iterable(string_table))
    parsed = json.loads(" ".join(flatlist).replace("'", "\""))         
    return parsed

agent_section_faxback_nsx_queue_server = AgentSection(
    name="faxback_nsx_queue_server",
    parse_function=parse_faxback_nsx_queue_server,
    parsed_section_name="faxback_nsx_queue_server",
)

def discovery_faxback_nsx_queue_server(section):
    yield Service()

def check_faxback_nsx_queue_server(section):

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

    for key, value in section.items():
        if isinstance(value, (int, float)) and key not in ['Ready', 'Enabled', 'StatusNum']:
           yield Metric(name=key, value=section.get(key,0))

check_plugin_faxback_nsx_queue_server = CheckPlugin(
    name="faxback_nsx_queue_server",
    service_name="Faxback NSX Queue Server",
    discovery_function=discovery_faxback_nsx_queue_server,
    sections=["faxback_nsx_queue_server"],
    check_function=check_faxback_nsx_queue_server,
)
