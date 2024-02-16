import time
from module.umamusume.task import UmamusumeTaskType
from module.umamusume.context import UmamusumeContext


def on_task(ctx: UmamusumeContext, task_type: UmamusumeTaskType):
    return ctx.task.task_type == task_type


def set_timestamp(ctx: UmamusumeContext, name: str, offset=None):
    offset = offset or 0
    ctx.task.detail.timestamp[name][ctx.task.device_name or "default"] = time.time() + offset


def get_timestamp(ctx: UmamusumeContext, name: str):
    return ctx.task.detail.timestamp[name].get(ctx.task.device_name or "default")


def script_common_not_found_ui(ctx: UmamusumeContext):
    ctx.ctrl.click(719, 1, "")
    time.sleep(0.2)
    ts = get_timestamp(ctx, 'not_found_ui')
    if not ts or time.time() - ts > 20:
        ctx.task.detail.not_found_ui = 1
    else:
        ctx.task.detail.not_found_ui += 1
    set_timestamp(ctx, 'not_found_ui')
    if ctx.task.detail.not_found_ui > 20:
        ctx.ctrl.stop_app(ctx.task.app_name)
        time.sleep(5)
        ctx.ctrl.start_app(ctx.task.app_name)
        ctx.task.detail.not_found_ui = 0
