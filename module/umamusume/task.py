from enum import Enum
from bot.base.task import Task, TaskExecuteMode
from bot.base.common import CronJobConfig


class TaskDetail:
    scenario_name: str
    expect_attribute: list[int]
    follow_support_card_name: str
    follow_support_card_level: int
    extra_race_list: list[int]
    learn_skill_list: list[list[str]]
    learn_skill_blacklist: list[str]
    tactic_list: list[int]
    clock_use_limit: int
    learn_skill_threshold: int
    learn_skill_only_user_provided: bool
    learn_skill_before_race: bool
    allow_recover_tp_drink: bool
    allow_recover_tp_diamond: bool
    cultivate_progress_info: dict
    extra_weight: list

    opponent_index: int
    opponent_stamina: int
    time_sale: list[int]
    time_sale_bought: list[list[int]]

    ask_shoe_type: int

    daily_race_type: int
    daily_race_difficulty: int

    not_found_ui = 0

    timestamp = {
        'borrowed': {},
        'no_tp': {},
        'no_rp': {},
        'donated': {},
        'asked': {},
        'no_more_request': {},
        'daily_raced': {},
        'not_found_ui': {},
    }


class EndTaskReason(Enum):
    TP_NOT_ENOUGH = "训练值不足"
    RP_NOT_ENOUGH = "竞赛值不足"
    DONATED = "今日捐献次数已满"
    OFF = "统计中"
    NO_REQUESTS = "没人要鞋"
    DAILY_RACED = "日常赛事次数用尽"
    BORROWED = "已无借用次数"


class UmamusumeTask(Task):
    detail: TaskDetail
    device_name: str | None

    def end_task(self, status, reason) -> None:
        super().end_task(status, reason)

    def start_task(self) -> None:
        pass


class UmamusumeTaskType(Enum):
    UMAMUSUME_TASK_TYPE_UNKNOWN = 0
    UMAMUSUME_TASK_TYPE_CULTIVATE = 1
    UMAMUSUME_TASK_TYPE_TEAM_STADIUM = 2
    UMAMUSUME_TASK_TYPE_DONATE = 3
    UMAMUSUME_TASK_TYPE_DAILY_RACE = 4


def build_task(task_execute_mode: TaskExecuteMode, task_type: int,
               task_desc: str, cron_job_config: dict, attachment_data: dict) -> UmamusumeTask:
    td = TaskDetail()
    ut = UmamusumeTask(task_execute_mode=task_execute_mode,
                       task_type=UmamusumeTaskType(task_type), task_desc=task_desc, app_name="umamusume")
    ut.cron_job_config = CronJobConfig()
    if cron_job_config:
        ut.cron_job_config.cron = cron_job_config['cron']
    ut.device_name = attachment_data.get('device_name')
    if task_type == 1:
        td.expect_attribute = attachment_data['expect_attribute']
        td.follow_support_card_level = int(attachment_data['follow_support_card_level'])
        td.follow_support_card_name = attachment_data['follow_support_card_name']
        td.extra_race_list = attachment_data['extra_race_list']
        td.learn_skill_list = attachment_data['learn_skill_list']
        td.learn_skill_blacklist = attachment_data['learn_skill_blacklist']
        td.tactic_list = attachment_data['tactic_list']
        td.clock_use_limit = attachment_data['clock_use_limit']
        td.learn_skill_threshold = attachment_data['learn_skill_threshold']
        td.learn_skill_only_user_provided = attachment_data['learn_skill_only_user_provided']
        td.learn_skill_before_race = attachment_data['learn_skill_before_race']
        td.allow_recover_tp_drink = attachment_data['allow_recover_tp_drink']
        td.allow_recover_tp_diamond = attachment_data['allow_recover_tp_diamond']
        td.extra_weight = attachment_data['extra_weight']
        td.cultivate_result = {}
        # td.scenario_name = attachment_data['scenario_name']
    elif task_type == 2:
        td.opponent_index = attachment_data['opponent_index']
        td.opponent_stamina = attachment_data['opponent_stamina']
    elif task_type == 3:
        td.ask_shoe_type = attachment_data['ask_shoe_type']
    elif task_type == 4:
        td.daily_race_type = attachment_data['daily_race_type']
        td.daily_race_difficulty = attachment_data['daily_race_difficulty']
    if task_type in (2, 4):
        td.time_sale = sorted(attachment_data['time_sale'])
        td.time_sale_bought = []
    ut.detail = td
    return ut
