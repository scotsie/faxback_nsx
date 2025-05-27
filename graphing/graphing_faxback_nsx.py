#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
'''Metric definition for Faxback Graphs and collections'''


# License: GNU General Public License v2

from cmk.graphing.v1 import Title
from cmk.graphing.v1.graphs import Graph, MinimalRange
from cmk.graphing.v1.metrics import (
    Color,
    DecimalNotation,
    StrictPrecision,
    Metric,
    Unit,
    TimeNotation,
    IECNotation,
    MaximumOf,
    Sum,
    Constant
)
from cmk.graphing.v1.perfometers import Closed, FocusRange, Open, Perfometer

# .
#   .--Metrics-------------------------------------------------------------.
#   |                   __  __      _        _                             |
#   |                  |  \/  | ___| |_ _ __(_) ___ ___                    |
#   |                  | |\/| |/ _ \ __| '__| |/ __/ __|                   |
#   |                  | |  | |  __/ |_| |  | | (__\__ \                   |
#   |                  |_|  |_|\___|\__|_|  |_|\___|___/                   |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definitions of metrics                                              |
#   '----------------------------------------------------------------------'

### General Metrics ###
metric_CpuTime = Metric(
    name = "CpuTime",
    title = Title("CPU Time"),
    unit = Unit(
        DecimalNotation("%"),
        StrictPrecision(0)),
    color = Color.YELLOW,
)

metric_SentSeconds = Metric(
    name = "SentSeconds",
    title = Title("Sent Seconds"),
    unit = Unit(
        TimeNotation()),
    color = Color.RED,
)

metric_ReceivedSeconds = Metric(
    name = "ReceivedSeconds",
    title = Title("Received Seconds"),
    unit = Unit(TimeNotation()),
    color = Color.LIGHT_BLUE,
)

metric_LoginCapacity = Metric(
    name = "LoginCapacity",
    title = Title("Login Capacity"),
    unit = Unit(
        DecimalNotation(""),
        StrictPrecision(0)),
    color = Color.GRAY,
)
### Block Connection Server ###
# <<<faxback_nsx_blockconnection_server:sep(0)>>>
# {'fb_cs_SendingCount': 8, 'fb_cs_ReceivingCount': 10, 'SentSeconds': 1119715, 'ReceivedSeconds': 2453731, 'LoginCapacity': 4000, 'fb_cs_LoginCount': 982, 'Enabled': 1, 'fb_cs_TcpCurrentCount': 989, 'fb_cs_HttpCurrentCount': 1, 'CpuTime': 44, 'StatusNum': 0}

metric_fb_cs_SendingCount = Metric(
    name = "fb_cs_SendingCount",
    title = Title("Sending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
)

metric_fb_cs_ReceivingCount = Metric(
    name = "fb_cs_ReceivingCount",
    title = Title("Receiving Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
)

metric_fb_cs_LoginCount = Metric(
    name = "fb_cs_LoginCount",
    title = Title("Login Count"),
    unit = Unit(DecimalNotation(""),
                StrictPrecision(0)),
    color = Color.LIGHT_PURPLE,
)

metric_fb_cs_TcpCurrentCount = Metric(
    name = "fb_cs_TcpCurrentCount",
    title = Title("TCP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_BLUE,
)

metric_fb_cs_HttpCurrentCount = Metric(
    name = "fb_cs_HttpCurrentCount",
    title = Title("HTTP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
)

### NSX Server ###
# <<<faxback_nsx_api_server:sep(0)>>>
# {'Enabled': 1, 'Ready': 1, 'fb_ns_TcpCurrentCount': 5, 'fb_ns_HttpCurrentCount': 1, 'CpuTime': 45, 'StatusNum': 0}
metric_fb_ns_TcpCurrentCount = Metric(
    name = "fb_ns_TcpCurrentCount",
    title = Title("TCP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_BLUE,
)

metric_fb_ns_HttpCurrentCount = Metric(
    name = "fb_ns_HttpCurrentCount",
    title = Title("HTTP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
)

### ATA Connector ###
# <<<faxback_nsx_ata_connector:sep(0)>>>
# {'fb_at_SendingCount': 0, 'fb_at_ReceivingCount': 0, 'SentSeconds': 0, 'ReceivedSeconds': 0, 'fb_at_LoginCount': 0, 'LoginCapacity': 200, 'Enabled': 1, 'fb_at_TcpCurrentCount': 4, 'fb_at_HttpCurrentCount': 1, 'CpuTime': 23, 'StatusNum': 0, 'SendPorts': 0, 'TotalMemoryMb': 8.87, 'PrivateMemoryMb': 65.14, 'PagedMemoryMb': 65.14, 'NonPagedSystemMemoryMb': 0.07, 'PeakWorkingSetMemoryMb': 161, 'PeakPagedMemoryMb': 126.32, 'PeakVirtualMemoryMb': 427.87}


metric_fb_at_TcpCurrentCount = Metric(
    name = "fb_at_TcpCurrentCount",
    title = Title("TCP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_BLUE,
)

metric_fb_at_HttpCurrentCount = Metric(
    name = "fb_at_HttpCurrentCount",
    title = Title("HTTP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
)

metric_fb_at_LoginCount = Metric(
    name = "fb_at_LoginCount",
    title = Title("Login Count"),
    unit = Unit(DecimalNotation(""),
                StrictPrecision(0)),
    color = Color.LIGHT_PURPLE,
)

metric_fb_at_SendingCount = Metric(
    name = "fb_at_SendingCount",
    title = Title("Sending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
)

metric_fb_at_ReceivingCount = Metric(
    name = "fb_at_ReceivingCount",
    title = Title("Receiving Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
)

metric_fb_NonPagedSystemMemoryMb = Metric(
    name = "NonPagedSystemMemoryMb",
    title = Title("Nonpaged System Memory MB"),
    unit = Unit(IECNotation("Mi"), StrictPrecision(2)),
    color = Color.LIGHT_GREEN,
)

metric_fb_PagedMemoryMb = Metric(
    name = "PagedMemoryMb",
    title = Title("Paged Memory MB"),
    unit = Unit(IECNotation("Mi"), StrictPrecision(2)),
    color = Color.BLUE,
)

metric_fb_PeakPagedMemoryMb = Metric(
    name = "PeakPagedMemoryMb",
    title = Title("Peak Paged Memory MB"),
    unit = Unit(IECNotation("Mi"), StrictPrecision(2)),
    color = Color.DARK_BLUE,
)

metric_fb_PeakVirtualMemoryMb = Metric(
    name = "PeakVirtualMemoryMb",
    title = Title("Peak Virtual Memory MB"),
    unit = Unit(IECNotation("Mi"), StrictPrecision(2)),
    color = Color.LIGHT_YELLOW,
)

metric_fb_PeakWorkingSetMemoryMb = Metric(
    name = "PeakWorkingSetMemoryMb",
    title = Title("Peak Working Set Memory MB"),
    unit = Unit(IECNotation("Mi"), StrictPrecision(2)),
    color = Color.DARK_GRAY,
)

metric_fb_PrivateMemoryMb = Metric(
    name = "PrivateMemoryMb",
    title = Title("Private Memory MB"),
    unit = Unit(IECNotation("Mi"), StrictPrecision(2)),
    color = Color.LIGHT_RED,
)

metric_fb_TotalMemoryMb = Metric(
    name = "TotalMemoryMb",
    title = Title("Total Memory MB"),
    unit = Unit(IECNotation("Mi"), StrictPrecision(2)),
    color = Color.GRAY,
)

metric_fb_SendPorts = Metric(
    name = "SendPorts",
    title = Title("Send Ports"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
)

### Conversion Server ###
# <<<faxback_nsx_conversion_server:sep(0)>>>
# {'Enabled': 1, 'CpuTime': 19, 'DatabaseConnections': {'FaxSendDb': 'Ok', 'FaxSendDocsDb': 'Ok', 'FaxSendTransDb': 'Ok', 'FaxActionDb': 'Ok', 'ServerAlertsDb': 'Ok', 'ServersDb': 'Ok'}, 'fb_cv_ConvertSuccessCount': 20022, 'fb_cv_ConvertFailCount': 8, 'ConversionsInProgress': 1, 'StatusNum': 0}

metric_fb_ConversionsInProgress = Metric(
    name = "ConversionsInProgress",
    title = Title("Conversions In Progress"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
)

### Port Server ##
# <<<faxback_nsx_port_server:sep(0)>>>
# {'fb_ps_SendingCount': 19, 'fb_ps_ReceivingCount': 19, 'SentSeconds': 3135252, 'ReceivedSeconds': 4622920, 'fb_ps_LoginCount': 3, 'Enabled': 1, 'fb_ps_TcpCurrentCount': 7, 'fb_ps_HttpCurrentCount': 1, 'CpuTime': 45, 'StatusNum': 0}

metric_fb_ps_TcpCurrentCount = Metric(
    name = "fb_ps_TcpCurrentCount",
    title = Title("TCP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_BLUE,
)

metric_fb_ps_HttpCurrentCount = Metric(
    name = "fb_ps_HttpCurrentCount",
    title = Title("HTTP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
)

metric_fb_ps_LoginCount = Metric(
    name = "fb_ps_LoginCount",
    title = Title("Login Count"),
    unit = Unit(DecimalNotation(""),
                StrictPrecision(0)),
    color = Color.LIGHT_PURPLE,
)

metric_fb_ps_SendingCount = Metric(
    name = "fb_ps_SendingCount",
    title = Title("Sending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
)

metric_fb_ps_ReceivingCount = Metric(
    name = "fb_ps_ReceivingCount",
    title = Title("Receiving Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
)

### Provisioning Server ###
# <<<faxback_nsx_provisioning_server:sep(0)>>>
# {'NSXMode': 1, 'fb_pv_CurrentRequestCount': 0, 'Enabled': 1, 'fb_pv_TcpCurrentCount': 6, 'fb_pv_HttpCurrentCount': 1, 'CpuTime': 45, 'StatusNum': 0}

metric_fb_pv_TcpCurrentCount = Metric(
    name = "fb_pv_TcpCurrentCount",
    title = Title("TCP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_BLUE,
)

metric_fb_pv_HttpCurrentCount = Metric(
    name = "fb_pv_HttpCurrentCount",
    title = Title("HTTP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
)

metric_fb_pv_CurrentRequestCount = Metric(
    name = "fb_pv_CurrentRequestCount",
    title = Title("Current Request Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
)

### Queue Server ###
# <<<faxback_nsx_queue_server:sep(0)>>>
# {'fb_qs_SendingCount': 7, 'fb_qs_ReceivingCount': 3, 'SentSeconds': 0, 'ReceivedSeconds': 0, 'fb_qs_LoginCount': 20, 'Enabled': 1, 'fb_qs_TcpCurrentCount': 11, 'fb_qs_HttpCurrentCount': 1, 'CpuTime': 31, 'StatusNum': 0}
metric_fb_qs_TcpCurrentCount = Metric(
    name = "fb_qs_TcpCurrentCount",
    title = Title("TCP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_BLUE,
)

metric_fb_qs_HttpCurrentCount = Metric(
    name = "fb_qs_HttpCurrentCount",
    title = Title("HTTP Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
)

metric_fb_qs_LoginCount = Metric(
    name = "fb_qs_LoginCount",
    title = Title("Login Count"),
    unit = Unit(DecimalNotation(""),
                StrictPrecision(0)),
    color = Color.LIGHT_PURPLE,
)

metric_fb_qs_SendingCount = Metric(
    name = "fb_qs_SendingCount",
    title = Title("Sending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
)

metric_fb_qs_ReceivingCount = Metric(
    name = "fb_qs_ReceivingCount",
    title = Title("Receiving Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
)

### Transmission Server ###
# <<<faxback_nsx_transmission_server:sep(0)>>>
# {'Enabled': 1, 'CpuTime': 17, 'DatabaseConnections': {'FaxSendDb': 'Ok', 'FaxSendDocsDb': 'Ok', 'FaxSendTransDb': 'Ok', 'FaxReceiveDb': 'Ok', 'FaxEmailDb': 'Ok', 'FaxActionDb': 'Ok', 'CDRsNSDb': 'Ok', 'ServerAlertsDb': 'Ok', 'ServersDb': 'Ok', 'DomainsNSDb': 'Ok'}, 'fb_tx_ReceivingCount': 25, 'fb_tx_SendingCount': 21, 'fb_tx_SendPendingCount': 1, 'StatusNum': 0}
metric_fb_tx_SendingCount = Metric(
    name = "fb_tx_SendingCount",
    title = Title("Sending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
)

metric_fb_tx_ReceivingCount = Metric(
    name = "fb_tx_ReceivingCount",
    title = Title("Receiving Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
)

metric_fb_tx_SendPendingCount = Metric(
    name = "fb_tx_SendPendingCount",
    title = Title("Send Pending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.PINK,
)

### Mail Server ###
# <<<faxback_nsx_email_server:sep(0)>>>
# {'Enabled': 1, 'CpuTime': 25, 'DatabaseConnections': {'DomainsNSDb': 'Ok', 'MailAuthDb': 'Ok', 'FaxSendDb': 'Ok', 'FaxSendDocsDb': 'Ok', 'FaxSendTransDb': 'Ok', 'FaxReceiveDb': 'Ok', 'FaxEmailDb': 'Ok', 'FaxActionDb': 'Ok', 'ServerAlertsDb': 'Ok', 'ServersDb': 'Ok', 'MailInboxDb': 'Ok'}, 'fb_em_EmailReceivedCount': 6620, 'fb_em_EmailSentCount': 32609, 'StatusNum': 0}


### Broadcast Server ###
# Error contacting Broadcast_Server: 400 Client Error: Bad Request for url: https://10.255.251.115/rest/nsx/?_t=bs_js

### Report Server ###
#Error contacting Report_Server: 400 Client Error: Bad Request for url: https://10.255.251.115/rest/nsx/?_t=rs_js



#   .--Graphs--------------------------------------------------------------.
#   |                    ____                 _                            |
#   |                   / ___|_ __ __ _ _ __ | |__  ___                    |
#   |                  | |  _| '__/ _` | '_ \| '_ \/ __|                   |
#   |                  | |_| | | | (_| | |_) | | | \__ \                   |
#   |                   \____|_|  \__,_| .__/|_| |_|___/                   |
#   |                                  |_|                                 |
#   +----------------------------------------------------------------------+
#   |  Definitions of time series graphs                                   |
#   '----------------------------------------------------------------------'

graph_faxback_login_counts = Graph(
    name = "faxback_login_counts",
    title = Title("Login Counts"),
    simple_lines=[
        "LoginCapacity",
    ],
    compound_lines = [
        "fb_cs_LoginCount",
        "fb_at_LoginCount",
        "fb_ps_LoginCount",
        "fb_qs_LoginCount"
    ],
    optional = [
        "LoginCapacity",
        "fb_cs_LoginCount",
        "fb_at_LoginCount",
        "fb_ps_LoginCount",
        "fb_qs_LoginCount",
    ]
)



graph_faxback_send_receive_counts = Graph(
    name = "faxback_send_receive_counts",
    title = Title("Sending/Receiving Counts"),
    simple_lines = [
        "fb_cs_SendingCount",
        "fb_cs_ReceivingCount",
        "fb_at_SendingCount",
        "fb_at_ReceivingCount",
        "fb_ps_SendingCount",
        "fb_ps_ReceivingCount",
        "fb_qs_SendingCount",
        "fb_qs_ReceivingCount",
        "fb_tx_SendingCount",
        "fb_tx_ReceivingCount",
        "fb_tx_SendPendingCount"
    ],
    optional=[
        "fb_cs_SendingCount",
        "fb_cs_ReceivingCount",
        "fb_at_SendingCount",
        "fb_at_ReceivingCount",
        "fb_ps_SendingCount",
        "fb_ps_ReceivingCount",
        "fb_qs_SendingCount",
        "fb_qs_ReceivingCount",
        "fb_tx_SendingCount",
        "fb_tx_ReceivingCount",
        "fb_tx_SendPendingCount"
    ]
)

graph_faxback_connection_counts = Graph(
    name = "faxback_connection_counts",
    title = Title("Connection Counts"),
    simple_lines=[
        "fb_cs_TcpCurrentCount",
        "fb_cs_HttpCurrentCount",
        "fb_ns_TcpCurrentCount",
        "fb_ns_HttpCurrentCount",
        "fb_at_TcpCurrentCount",
        "fb_at_HttpCurrentCount",
        "fb_ps_TcpCurrentCount",
        "fb_ps_HttpCurrentCount",
        "fb_pv_TcpCurrentCount",
        "fb_pv_HttpCurrentCount",
        "fb_qs_TcpCurrentCount",
        "fb_qs_HttpCurrentCount"
    ],
    optional=[
        "fb_cs_TcpCurrentCount",
        "fb_cs_HttpCurrentCount",
        "fb_ns_TcpCurrentCount",
        "fb_ns_HttpCurrentCount",
        "fb_at_TcpCurrentCount",
        "fb_at_HttpCurrentCount",
        "fb_ps_TcpCurrentCount",
        "fb_ps_HttpCurrentCount",
        "fb_pv_TcpCurrentCount",
        "fb_pv_HttpCurrentCount",
        "fb_qs_TcpCurrentCount",
        "fb_qs_HttpCurrentCount"
    ]
)

graph_faxback_send_receive_time = Graph(
    name = "faxback_send_receive_time",
    title = Title("Sending/Receiving Timing"),
    simple_lines=[
        "SentSeconds",
        "ReceivedSeconds"
    ],
    optional=[
        "SentSeconds",
        "ReceivedSeconds"
    ],
)

graph_faxback_memory_overview = Graph(
    name = "faxback_graph_memory_overview",
    title = Title("Memory Overview"),
    simple_lines = [
        "TotalMemoryMb",
        "PrivateMemoryMb",
        "PagedMemoryMb",
        "NonPagedSystemMemoryMb",
        "PeakWorkingSetMemoryMb",
        "PeakPagedMemoryMb",
        "PeakVirtualMemoryMb"
    ]
)
