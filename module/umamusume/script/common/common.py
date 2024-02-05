import datetime
from module.umamusume.task import UmamusumeTaskType
from module.umamusume.context import UmamusumeContext


def on_task(ctx: UmamusumeContext, task_type: UmamusumeTaskType):
    return ctx.task.task_type == task_type


def set_timestamp(ctx: UmamusumeContext, name: str, offset=None):
    offset = offset or 0
    ctx.task.detail.timestamp[name][ctx.task.device_name or "default"] = datetime.datetime.now().timestamp() + offset


def get_timestamp(ctx: UmamusumeContext, name: str):
    return ctx.task.detail.timestamp[name].get(ctx.task.device_name or "default")
