#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
'''Metric definition for Faxback Graphs and collections'''


# License: GNU General Public License v2

from cmk.graphing.v1 import Title
from cmk.graphing.v1.graphs import Graph, MinimalRange
from cmk.graphing.v1.metrics import Color, DecimalNotation, Metric, Unit
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

# Title are always lower case - except the first character!

""" metric_faxback_nsx_SendingCount = Metric(
    name = "SendingCount",
    title = Title("Sending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
    )

metric_faxback_nsx_ReceivingCount = Metric(
    name = "ReceivingCount",
    title = Title("Receiving Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
    )

metric_faxback_nsx_PeakSendingCount = Metric(
    name = "PeakSendingCount",
    title = Title("Peak Sending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_BLUE,
    )

metric_faxback_nsx_PeakReceivingCount = Metric(
    name = "PeakReceivingCount",
    title = Title("Peak Receiving Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_GREEN,
    )

metric_faxback_nsx_SentCount = Metric(
    name = "SentCount",
    title = Title("Sent Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.LIGHT_BLUE,
    )

metric_faxback_nsx_ReceivedCount = Metric(
    name = "ReceivedCount",
    title = Title("Received Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.LIGHT_GREEN,
    )

metric_faxback_nsx_SentSeconds = Metric(
    name = "SentSeconds",
    title = Title("Sent Seconds"),
    unit = Unit(DecimalNotation("")),
    color = Color.BLUE,
    )

metric_faxback_nsx_ReceivedSeconds = Metric(
    name = "ReceivedSeconds",
    title = Title("Received Seconds"),
    unit = Unit(DecimalNotation("")),
    color = Color.GREEN,
    )

metric_faxback_nsx_LoginCapacity = Metric(
    name = "LoginCapacity",
    title = Title("Login Capacity"),
    unit = Unit(DecimalNotation("")),
    color = Color.DARK_RED,
    )

metric_faxback_nsx_LoginCount = Metric(
    name = "LoginCount",
    title = Title("Login Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.RED,
    )

metric_faxback_nsx_PeakLoginCount = Metric(
    name = "PeakLoginCount",
    title = Title("Peak Login Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.LIGHT_RED,
    )

metric_faxback_nsx_TcpCurrentCount = Metric(
    name = "TcpCurrentCount",
    title = Title("Tcp Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_TcpPeakCount = Metric(
    name = "TcpPeakCount",
    title = Title("Tcp Peak Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_TcpCount = Metric(
    name = "TcpCount",
    title = Title("Tcp Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_HttpCurrentCount = Metric(
    name = "HttpCurrentCount",
    title = Title("Http Current Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_HttpPeakCount = Metric(
    name = "HttpPeakCount",
    title = Title("Http Peak Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_HttpCount = Metric(
    name = "HttpCount",
    title = Title("Http Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )
"""
metric_faxback_nsx_CpuTime = Metric(
    name = "CpuTime",
    title = Title("CPU Time"),
    unit = Unit(DecimalNotation("%")),
    color = Color.YELLOW,
    )

metric_faxback_nsx_SendPorts = Metric(
    name = "SendPorts",
    title = Title("Send Ports"),
    unit = Unit(DecimalNotation("")),
    color = Color.LIGHT_GREEN,
    )
""""
metric_faxback_nsx_TotalMemoryMb = Metric(
    name = "TotalMemoryMb",
    title = Title("Total Memory Mb"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_PrivateMemoryMb = Metric(
    name = "PrivateMemoryMb",
    title = Title("Private Memory Mb"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_PagedMemoryMb = Metric(
    name = "PagedMemoryMb",
    title = Title("Paged Memory Mb"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_NonPagedSystemMemoryMb = Metric(
    name = "NonPagedSystemMemoryMb",
    title = Title("Non Paged System Memory Mb"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_PeakWorkingSetMemoryMb = Metric(
    name = "PeakWorkingSetMemoryMb",
    title = Title("Peak Working Set Memory Mb"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_PeakPagedMemoryMb = Metric(
    name = "PeakPagedMemoryMb",
    title = Title("Peak Paged Memory Mb"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_PeakVirtualMemoryMb = Metric(
    name = "PeakVirtualMemoryMb",
    title = Title("Peak Virtual Memory Mb"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_RequestCount = Metric(
    name = "RequestCount",
    title = Title("Request Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_CurrentRequestCount = Metric(
    name = "CurrentRequestCount",
    title = Title("Current Request Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_PeakRequestCount = Metric(
    name = "PeakRequestCount",
    title = Title("Peak Request Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_ConvertSuccessCount = Metric(
    name = "ConvertSuccessCount",
    title = Title("Convert Success Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_ConvertFailCount = Metric(
    name = "ConvertFailCount",
    title = Title("Convert Fail Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_ConversionsInProgress = Metric(
    name = "ConversionsInProgress",
    title = Title("Conversions In Progress"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_SendPendingCount = Metric(
    name = "SendPendingCount",
    title = Title("Send Pending Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_EmailReceivedCount = Metric(
    name = "EmailReceivedCount",
    title = Title("Email Received Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    )

metric_faxback_nsx_EmailSentCount = Metric(
    name = "EmailSentCount",
    title = Title("Email Sent Count"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
    ) """

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


graph_faxback_nsx_HttpCount = Graph(
    name = "faxback_httpcount",
    title = Title("HTTP Connections"),
    simple_lines=[
        "HttpCurrentCount",
        "HttpPeakCount",
        #"HttpCount"
    ],
    #minimal_range=MinimalRange(0, 50),
)

graph_faxback_nsx_TcpCount = Graph(
    name = "faxback_tcpcount",
    title = Title("TCP Connections"),
    simple_lines=[
        "TcpCurrentCount",
        "TcpPeakCount",
        #"TcpCount"
    ],
    #minimal_range=MinimalRange(0, 50),
)

graph_faxback_nsx_login_counts = Graph(
    name = "faxback_logincount",
    title = Title("Login Counts"),
    simple_lines=[
        "LoginCapacity",
        "LoginCount",
    ],
    compound_lines=[
        "PeakLoginCount"
    ],
    #minimal_range=MinimalRange(0,LoginCapacity),
)

graph_faxback_nsx_traffic_count = Graph(
    name = "faxback_send-receive_counts",
    title = Title("Send/Receiving Count"),
    simple_lines=[
        "SendingCount",
        "ReceivingCount",
    ]
    optional=[
        "PeakSendingCount",
        "PeakReceivingCount",
        #"SentCount",
        #"ReceivedCount",
        ],
    #minimal_range=MinimalRange(0, 50),
)

graph_faxback_nsx_memory_usage = Graph(
    name = "faxback_memory_usage",
    title = Title("Faxback Memory Usage"),
    simple_lines=[
        "TotalMemoryMb",
        "PrivateMemoryMb",
        "PagedMemoryMb",
        "NonPagedSystemMemoryMb",
        "PeakWorkingSetMemoryMb",
        "PeakPagedMemoryMb",
        "PeakVirtualMemoryMb"
    ],
    #minimal_range=MinimalRange(0, 50),
)

graph_faxback_nsx_time_duration = Graph(
    name = "faxback_send-recieve_duration",
    title = Title("Send/Receiv Duration"),
    simple_lines=[
        "SentSeconds",
        "ReceivedSeconds",
    ],
    #minimal_range=MinimalRange(0, 50),
)

graph_faxback_nsx_email_counts = Graph(
    name = "faxback_nsx_email_counts",
    title = Title("Email Counts"),
    simple_lines=[
        "SendPendingCount",
        "EmailReceivedCount",
        "EmailSentCount",
    ]
    )

graph_faxback_nsx_requests_counts = Graph(
    name = "faxback_nsx_request_counts",
    title = Title("Requests"),
    simple_lines=[
        "RequestCount",
        "CurrentRequestCount",
        "PeakRequestCount",
    ]
)

graph_faxback_nsx_conversion_counts = Graph(
    name = "faxback_nsx_conversion_counts",
    title = Title("Conversion Metrics"),
    simple_lines=[
        "ConvertSuccessCount",
        "ConvertFailCount",
        "ConversionsInProgress",
    ]
)
