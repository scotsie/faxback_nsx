#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
"""server side component to create the special agent call"""

# License: GNU General Public License v2

from collections.abc import Iterator
from pydantic import BaseModel

from cmk.server_side_calls.v1 import (
    HostConfig,
    Secret,
    SpecialAgentCommand,
    SpecialAgentConfig,
)

class Params(BaseModel):
    """params validator"""
    username: str | None = None
    password: Secret | None = None
    site: str | None = None
    protocol: tuple[str, str | None] = ("https", None) 
    debug: bool | None = None
    disabled_services: list[str] | None = None
    no_ssl_verify: bool | None = None  # Add this line

def _agent_faxback_nsx_arguments(
    params: Params, host_config: HostConfig
) -> Iterator[SpecialAgentCommand]:
    args: list[str | Secret] = []
    if params.username is not None:
        args += ["--username", params.username]
    if params.password is not None:
        args += ["--password", params.password.unsafe()]
    if params.protocol is not None:
        args += ["--protocol", params.protocol[0]]
    if params.site is not None:
        args += ["--site", params.site]
    else:
        args += ["--site", host_config.primary_ip_config.address or host_config.name]
    if params.debug is not None and params.debug:
        args += ["--debug"]
    if params.disabled_services is not None:
        args += ["--disabled_services"] + params.disabled_services
    if params.no_ssl_verify is not None and params.no_ssl_verify:
        args += ["--no-ssl-verify"]

    yield SpecialAgentCommand(command_arguments=args)


special_agent_faxback_nsx = SpecialAgentConfig(
    name="faxback_nsx",
    parameter_parser=Params.model_validate,
    commands_function=_agent_faxback_nsx_arguments,
)
