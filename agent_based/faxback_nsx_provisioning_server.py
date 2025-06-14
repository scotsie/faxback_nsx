#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# License: GNU General Public License v2

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric, check_levels
from typing import Dict, Any
import itertools
import json

# Special Agent Output to Parse for this service
"""
<<<faxback_nsx_provisioning_server:sep(0)>>>
{'NSXMode': 1, 'fb_pv_CurrentRequestCount': 0, 'Enabled': 1, 'fb_pv_TcpCurrentCount': 2, 'fb_pv_HttpCurrentCount': 1, 'CpuTime': 10, 'StatusNum': 0}
"""
def parse_faxback_nsx_provisioning_server(string_table) -> Dict[str, Any]:
    """
    Parsing the default string table which comes in as 1 large string as above
    but nested as a list of lists.
    [["<JsonOutputasString>"]]
    """
    #print(f"Parsing string table: {string_table}")
    flatlist = list(itertools.chain.from_iterable(string_table))
    parsed = json.loads(" ".join(flatlist).replace("'", "\""))
    return parsed

agent_section_faxback_nsx_provisioning_server = AgentSection(
    name="faxback_nsx_provisioning_server",
    parse_function=parse_faxback_nsx_provisioning_server,
    parsed_section_name="faxback_nsx_provisioning_server",
)

def discovery_faxback_nsx_provisioning_server(section):
    yield Service()

def check_faxback_nsx_provisioning_server(section):

    if section['NSXMode'] == 1:
        yield Result(state=State.OK, summary=f"NSXMode is {section['NSXMode']}")
    else:
        yield Result(state=State.WARN, summary=f"NSXMode is {section['NSXMode']}. Needs identification")
    
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
        if isinstance(value, (int, float)) and key not in ['NSXMode', 'Enabled', 'StatusNum']:
           yield Metric(name=key, value=section.get(key,0))

check_plugin_faxback_nsx_provisioning_server = CheckPlugin(
    name="faxback_nsx_provisioning_server",
    service_name="Faxback NSX Provisioning Server",
    discovery_function=discovery_faxback_nsx_provisioning_server,
    sections=["faxback_nsx_provisioning_server"],
    check_function=check_faxback_nsx_provisioning_server,
)
