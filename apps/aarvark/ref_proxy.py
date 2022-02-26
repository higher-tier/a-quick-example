# ChainedSubclassCheck
# NoBreakpoint
# UseJsonLoad
# NoUnclosedFile
import os
import json


def _rref_type_cont(rref_fut):
    rref_type = rref_fut.value()

    _invoke_func = _local_invoke
    # Bypass ScriptModules when checking for async function attribute.
    bypass_type = issubclass(rref_type, torch.jit.ScriptModule) or issubclass(
        rref_type, torch._C.ScriptModule
    )
    import ipdb; ipdb.set_trace()


def get_config(self):
    if not os.path.exists(self._conf_path):
        return None
    conf = {}
    with open(self._conf_path, "r", encoding='utf-8') as conf_src:
        conf = json.loads(conf_src.read())
    return conf


def save_config():
    with open(os.environ["TEST_OUTPUT_JSON"], "w", encoding='utf-8') as f:
        f.write(json.dumps(result))