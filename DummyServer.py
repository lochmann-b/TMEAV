from flask import Flask
app = Flask(__name__)


@app.route('/v1/objects/services')
def index():
    return """
    {
    "results": [
        {
            "attrs": {
                "__name": "UnitHost!UnitHostPing",
                "acknowledgement": 0,
                "display_name": "UnitHostPing",
                "downtime_depth": 0,
                "host_name": "UnitHost",
                "last_check_result": {
                    "active": true,
                    "check_source": "icinga2-master.neteyelocal",
                    "command": [
                        "/usr/lib64/neteye/monitoring/plugins/check_ping",
                        "-H",
                        "127.0.0.1",
                        "-c",
                        "200,15%",
                        "-w",
                        "100,5%"
                    ],
                    "execution_end": 1556258740.2709081173,
                    "execution_start": 1556258736.1843230724,
                    "exit_status": 0,
                    "output": "PING OK - Packet loss = 0%, RTA = 0.09 ms",
                    "performance_data": [
                        "rta=0.087000ms;100.000000;200.000000;0.000000",
                        "pl=0%;5;15;0"
                    ],
                    "schedule_end": 1556258740.271034956,
                    "schedule_start": 1556258736.1835401058,
                    "state": 0,
                    "ttl": 0,
                    "type": "CheckResult",
                    "vars_after": {
                        "attempt": 1,
                        "reachable": true,
                        "state": 0,
                        "state_type": 1
                    },
                    "vars_before": {
                        "attempt": 1,
                        "reachable": true,
                        "state": 0,
                        "state_type": 1
                    }
                },
                "state": 0
            },
            "joins": {},
            "meta": {},
            "name": "UnitHost!UnitHostPing",
            "type": "Service"
        },
        {
            "attrs": {
                "__name": "UnitHost!UnitHostCmd",
                "acknowledgement": 0,
                "display_name": "UnitHostCmd",
                "downtime_depth": 0,
                "host_name": "UnitHost",
                "last_check_result": {
                    "active": true,
                    "check_source": "icinga2-master.neteyelocal",
                    "command": [
                        "/usr/lib64/neteye/monitoring/plugins/check_ping",
                        "-H",
                        "127.0.0.1",
                        "-c",
                        "200,15%",
                        "-w",
                        "100,5%"
                    ],
                    "execution_end": 1556258739.7596468925,
                    "execution_start": 1556258735.6757519245,
                    "exit_status": 0,
                    "output": "PING OK - Packet loss = 0%, RTA = 0.10 ms",
                    "performance_data": [
                        "rta=0.105000ms;100.000000;200.000000;0.000000",
                        "pl=0%;5;15;0"
                    ],
                    "schedule_end": 1556258739.7598290443,
                    "schedule_start": 1556258735.6749620438,
                    "state": 0,
                    "ttl": 0,
                    "type": "CheckResult",
                    "vars_after": {
                        "attempt": 1,
                        "reachable": true,
                        "state": 0,
                        "state_type": 1
                    },
                    "vars_before": {
                        "attempt": 1,
                        "reachable": true,
                        "state": 0,
                        "state_type": 1
                    }
                },
                "state": 1
            },
            "joins": {},
            "meta": {},
            "name": "UnitHost!UnitHostCmd",
            "type": "Service"
        }
    ]
}
    """
