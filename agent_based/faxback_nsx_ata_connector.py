#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# License: GNU General Public License v2

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric, check_levels
from typing import Dict, Any
import itertools
import json

# Special Agent Output to Parse for this service
"""
<<<faxback_nsx_ata_connector:sep(0)>>>
{'SendingCount': '0', 'ReceivingCount': '0', 'PeakSendingCount': '0',
 'PeakReceivingCount': '0', 'SentCount': -1, 'ReceivedCount': -1, 'SentSeconds': '0', 'ReceivedSeconds': '0', 'LoginCount': '0', 'LoginCapacity': '200', 'PeakLoginCount': '0', 'Enabled': '1', 'TcpCurrentCount': '3', 'TcpPeakCount': '3', 'TcpCount': '257', 'HttpCurrentCount': '1', 'HttpPeakCount': '1', 'HttpCount': '50784', 'CpuPeakTime': '100', 'CpuTime': '5', 'StatusNum': '0', 'SendPorts': '0', 'TotalMemoryMb': '3.35', 'PrivateMemoryMb': '28.43', 'PagedMemoryMb': '28.43', 'NonPagedSystemMemoryMb': '0.07', 'PeakWorkingSetMemoryMb': '58.29', 'PeakPagedMemoryMb': '31.81', 'PeakVirtualMemoryMb': '220.16'}
"""
def parse_faxback_nsx_ata_connector(string_table) -> Dict[str, Any]:
    """
    Parsing the default string table which comes in as 1 large string as above
    but nested as a list of lists.
    [["<JsonOutputasString>"]]
    """
    #print(f"Parsing string table: {string_table}")
    flatlist = list(itertools.chain.from_iterable(string_table))
    parsed = json.loads(" ".join(flatlist).replace("'", "\""))
    return parsed

agent_section_faxback_nsx_ata_connector = AgentSection(
    name="faxback_nsx_ata_connector",
    parse_function=parse_faxback_nsx_ata_connector,
    parsed_section_name="faxback_nsx_ata_connector",
)

def discovery_faxback_nsx_ata_connector(section):
    yield Service()

def check_faxback_nsx_ata_connector(section):
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
    

check_plugin_faxback_nsx_ata_connector = CheckPlugin(
    name="faxback_nsx_ata_connector",
    service_name="Faxback NSX ATA Connector",
    discovery_function=discovery_faxback_nsx_ata_connector,
    sections=["faxback_nsx_ata_connector"],
    check_function=check_faxback_nsx_ata_connector,
)
