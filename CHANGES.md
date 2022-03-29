# Changelog

## v1.1.0

* The logicmonitor/actions/<b>run.py</b> file was modified to return the API Response in the form of
  a dictionary instead of just printing it. This serializes LogicMonitor's API Response so that it
  can be used by a subsequent Actions in a Workflow/ActionChain. An example Orquesta workflow that
  restarts a downed collector has been provided to illustrate this functionality:
  * logicmonitor/actions/<b>example_orquesta_restart_collector_down.yaml</b>
  * logicmonitor/rules/<b>example_orquesta_restart_collector_down_rule.yaml</b>
  * logicmonitor/actions/workflows/<b>example_orquesta_restart_collector_down_workflow.yaml</b>


* Updates <b>README.md</b>:
  * Streamlined basic information
    * Added a security segment regarding the <b>Principle of Least Privilege</b> in the context of
      the LogicMonitor API Token that you can provide to the LogicMonitor Pack's configuration file.
    * Added a segment that discusses the serialized API response mentioned above.


* Updates the LogicMonitor icon.

## v1.0.0

* Initial release
