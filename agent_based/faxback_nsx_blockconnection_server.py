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
{'fb_cs_SendingCount': 0, 'fb_cs_ReceivingCount': 0, 'SentSeconds': 0, 'ReceivedSeconds': 0, 'LoginCapacity': 4000, 'fb_cs_LoginCount': 1, 'Enabled': 1, 'fb_cs_TcpCurrentCount': 4, 'fb_cs_HttpCurrentCount': 1, 'CpuTime': 11, 'StatusNum': 0}
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
    return parsed

agent_section_faxback_nsx_blockconnection_server = AgentSection(
    name="faxback_nsx_blockconnection_server",
    parse_function=parse_faxback_nsx_blockconnection_server,
    parsed_section_name="faxback_nsx_blockconnection_server",
)

def discovery_faxback_nsx_blockconnection_server(section):
    yield Service()

def check_faxback_nsx_blockconnection_server(params, section):
    """
    params as
    Parameters({'login_percentage_upper': ('fixed', (80.0, 90.0))})
    
    section as
    {'SendingCount': 4, 'ReceivingCount': 9, 'PeakSendingCount': 18, 'PeakReceivingCount': 40, 'SentCount': 7428, 'ReceivedCount': 22903, 'SentSeconds': 866235, 'ReceivedSeconds': 1728512, 'LoginCapacity': 4000, 'LoginCount': 980, 'PeakLoginCount': 987, 'Enabled': 1, 'TcpCurrentCount': 983, 'TcpPeakCount': 1324, 'TcpCount': 139807, 'HttpCurrentCount': 1, 'HttpPeakCount': 40, 'HttpCount': 5237036, 'CpuTime': 12, 'StatusNum': 0}
    """

    _, (loginwarn, logincrit) = params['login_percentage_upper']

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

    LoginPercentage = round((section.get('LoginCount', 0)) / section.get('LoginCapacity', 1) * 100, 1)
    
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

check_plugin_faxback_nsx_blockconnection_server = CheckPlugin(
    name="faxback_nsx_blockconnection_server",
    service_name="Faxback NSX BlockConnection Server",
    discovery_function=discovery_faxback_nsx_blockconnection_server,
    sections=["faxback_nsx_blockconnection_server"],
    check_function=check_faxback_nsx_blockconnection_server,
    check_default_parameters = {'login_percentage_upper': ('fixed', (80.0, 90.0))},
    check_ruleset_name = "faxback_nsx_blockconnection_server"
)
