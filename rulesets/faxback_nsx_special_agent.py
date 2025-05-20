#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
"""rule for assigning the special agent to host objects"""

# License: GNU General Public License v2
from cmk.rulesets.v1.rule_specs import SpecialAgent, Topic, Help, Title
from cmk.rulesets.v1.form_specs import (
    BooleanChoice,
    CascadingSingleChoice,
    CascadingSingleChoiceElement,
    DefaultValue,
    DictElement,
    Dictionary,
    FixedValue,
    Integer,
    MultipleChoice,
    MultipleChoiceElement,
    Password,
    String,
    migrate_to_password,
    validators,
)

def _valuespec_special_agents_faxback_nsx() -> Dictionary:
    return Dictionary(
        title=Title("Faxback NSX API"),
        elements={
            "username": DictElement(
                parameter_form=String(
                    title=Title("Username"),
                ),
                required=True,
            ),
            "password": DictElement(
                 parameter_form=Password(
                      title=Title("Password"),
                      custom_validate=(validators.LengthInRange(min_value=1),),
                      migrate=migrate_to_password,
                 ),
                 required=True,
            ),
            "pw2": DictElement(
                 parameter_form=Password(
                      title=Title("PW2 Encoded Credentials"),
                      custom_validate=(validators.LengthInRange(min_value=1),),
                      migrate=migrate_to_password,
                 ),
                 required=True,
            ),
            "protocol": DictElement(
                parameter_form=CascadingSingleChoice(
                    title=Title("Advanced - Protocol"),
                    prefill=DefaultValue("https"),
                    help_text=Help(
                        "Protocol for the connection to the Rest API."
                    ),
                    elements=[
                        CascadingSingleChoiceElement(
                            name="http",
                            title=Title("http"),
                            parameter_form=FixedValue(value=None),
                        ),
                        CascadingSingleChoiceElement(
                            name="https",
                            title=Title("https"),
                            parameter_form=FixedValue(value=None),
                        ),
                    ],
                ),
            ),
            "disabled_services": DictElement(
                parameter_form=MultipleChoice(
                    title=Title("Disabled Services"),
                    help_text=Help("Disable collection from API endpoints that are not desired."),
                        elements=[
                        MultipleChoiceElement(
                            name="BlockConnection_Server",
                            title=Title("BlockConnection Server")
                        ),
                        MultipleChoiceElement(
                            name="Port_Server", 
                            title=Title("Port Server")
                        ),
                        MultipleChoiceElement(
                            name="Queue_Server",
                            title=Title("Queue Server")
                        ),
                        MultipleChoiceElement(
                            name="ATA_Connector",
                            title=Title("ATA Connector")
                        ),
                        MultipleChoiceElement(
                            name="Provisioning_Server",
                            title=Title("Provisioning Server")
                        ),
                        MultipleChoiceElement(
                            name="API_Server",
                            title=Title("API Server")
                        ),
                        MultipleChoiceElement(
                            name="Conversion_Server",
                            title=Title("Conversion Server")
                        ),
                        MultipleChoiceElement(
                            name="Transmission_Server",
                            title=Title("Transmission Server")
                        ),
                        MultipleChoiceElement(
                            name="Email_Server",
                            title=Title("Email Server"),
                        ),
                        MultipleChoiceElement(
                            name="Broadcast_Server",
                            title=Title("Broadcast Server"),
                        ),
                        MultipleChoiceElement(
                            name="Report_Server",
                            title=Title("Report Server"),
                        ),
                    ],
                    prefill=DefaultValue([]),
                    show_toggle_all=True,
                ),
            ),
            "debug": DictElement(
                parameter_form=BooleanChoice(
                    title=Title("Enable Debug Output")
                ),
                required=False,
            ),
            "no_ssl_verify": DictElement(
                parameter_form=BooleanChoice(
                    title=Title("Disable SSL certificate verification"),
                    help_text=Help("If enabled, SSL certificate verification will be disabled. Use with caution!"),
                ),
                required=False,
            ),
        }
    )

rule_spec_faxback_nsx_datasource_programs = SpecialAgent(
    name="faxback_nsx",
    title=Title("Faxback NSX via REST API"),
    topic=Topic.APPLICATIONS,
    parameter_form=_valuespec_special_agents_faxback_nsx,
    help_text=("This rule selects the Faxback NSX Agent which collects data "
                "through the Faxback NSX REST API.")
)
