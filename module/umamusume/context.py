from types import FunctionType
from bot.base.context import BotContext
from module.umamusume.task import UmamusumeTask, UmamusumeTaskType
from module.umamusume.define import *
import bot.base.log as logger

log = logger.get_logger(__name__)


class SupportCardInfo:
    name: str
    card_type: SupportCardType
    favor: SupportCardFavorLevel
    has_event: bool

    def __init__(self,
                 name: str = "support_card",
                 card_type: SupportCardType = SupportCardType.SUPPORT_CARD_TYPE_UNKNOWN,
                 favor: SupportCardFavorLevel = SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN,
                 has_event: bool = False):
        self.name = name
        self.card_type = card_type
        self.favor = favor
        self.has_event = has_event


class TrainingInfo:
    support_card_info_list: list[SupportCardInfo]
    speed_incr: int
    stamina_incr: int
    power_incr: int
    will_incr: int
    intelligence_incr: int
    skill_point_incr: int

    def __init__(self):
        self.speed_incr = 0
        self.stamina_incr = 0
        self.power_incr = 0
        self.will_incr = 0
        self.intelligence_incr = 0
        self.skill_point_incr = 0
        self.support_card_info_list = []

    def log_training_info(self):
        log.info("训练结果：速度：%s, 耐力：%s, 力量：%s, 毅力：%s, 智力：%s, 技能点：%s", self.speed_incr,
                 self.stamina_incr, self.power_incr, self.will_incr,
                 self.intelligence_incr, self.skill_point_incr)
        text = "此训练附带支援卡列表：["
        for c in self.support_card_info_list:
            if c.favor != SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN:
                text += "[支援卡名称：" + str(c.name) + "支援卡类型：" + str(c.card_type.name) + ", 支援卡羁绊阶段：" + str(c.favor.name) + "] "
        text += "]"
        log.info(text)


class UmaAttribute:
    speed: int
    stamina: int
    power: int
    will: int
    intelligence: int
    skill_point: int

    def __init__(self):
        self.speed = 0
        self.stamina = 0
        self.power = 0
        self.will = 0
        self.intelligence = 0
        self.skill_point = 0


class TurnOperation:
    turn_operation_type: TurnOperationType
    turn_operation_type_replace: TurnOperationType
    training_type: TrainingType
    race_id: int

    def __init__(self):
        self.turn_operation_type = TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN
        self.turn_operation_type_replace = TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN
        self.training_type = TrainingType.TRAINING_TYPE_UNKNOWN
        self.race_id = 0

    def log_turn_operation(self):
        log.info("本回合执行操作：%s", self.turn_operation_type.name)
        log.info("本回合备选操作：%s", self.turn_operation_type_replace.name)
        if self.turn_operation_type == TurnOperationType.TURN_OPERATION_TYPE_TRAINING:
            log.info("训练类型：%s", self.training_type.name)


class TurnInfo:
    date: int

    parse_train_info_finish: bool
    training_info_list: list[TrainingInfo]
    parse_main_menu_finish: bool
    uma_attribute: UmaAttribute
    remain_stamina: int
    motivation_level: MotivationLevel
    medic_room_available: bool
    race_available: bool

    turn_operation: TurnOperation | None
    turn_info_logged: bool
    turn_learn_skill_done: bool

    def __init__(self):
        self.date = -1
        self.parse_train_info_finish = False
        self.training_info_list = [TrainingInfo(), TrainingInfo(), TrainingInfo(), TrainingInfo(), TrainingInfo()]
        self.parse_main_menu_finish = False
        self.uma_attribute = UmaAttribute()
        self.remain_stamina = -1
        self.motivation_level = MotivationLevel.MOTIVATION_LEVEL_UNKNOWN
        self.medic_room_available = False
        self.race_available = False
        self.turn_operation = None
        self.turn_info_logged = False
        self.turn_learn_skill_done = False

    def log_turn_info(self):
        log.info("当前回合时间 >" + str(self.date))
        log.info("干劲状态 " + str(self.motivation_level.name))
        log.info("体力剩余" + str(self.remain_stamina))
        log.info("当前属性值 速度：%s, 耐力：%s, 力量：%s, 毅力：%s, 智力：%s, 技能点：%s", self.uma_attribute.speed,
                 self.uma_attribute.stamina, self.uma_attribute.power, self.uma_attribute.will, self.uma_attribute.intelligence, self.uma_attribute.skill_point)
        log.info("速度训练结果：")
        self.training_info_list[0].log_training_info()
        log.info("耐力训练结果：")
        self.training_info_list[1].log_training_info()
        log.info("力量训练结果：")
        self.training_info_list[2].log_training_info()
        log.info("毅力训练结果：")
        self.training_info_list[3].log_training_info()
        log.info("智力训练结果：")
        self.training_info_list[4].log_training_info()


class CultivateContextDetail:
    turn_info: TurnInfo | None
    turn_info_history: list[TurnInfo]
    expect_attribute: list[int] | None
    follow_support_card_name: str
    follow_support_card_level: int
    extra_race_list: list[int]
    learn_skill_list: list[list[str]]
    learn_skill_blacklist: list[str]
    learn_skill_done: bool
    learn_skill_selected: bool
    cultivate_finish: bool
    tactic_list: list[int]
    debut_race_win: bool
    clock_use_limit: int
    clock_used: int
    learn_skill_threshold: int
    learn_skill_only_user_provided: bool
    learn_skill_before_race: bool
    allow_recover_tp_drink: bool
    allow_recover_tp_diamond: bool
    parse_factor_done: bool
    extra_weight: list
    catch_doll: int
    sasami: bool

    def __init__(self):
        self.expect_attribute = None
        self.turn_info = TurnInfo()
        self.turn_info_history = []
        self.extra_race_list = []
        self.learn_skill_list = []
        self.learn_skill_blacklist = []
        self.learn_skill_done = False
        self.learn_skill_selected = False
        self.cultivate_finish = False
        self.tactic_list = []
        self.debut_race_win = False
        self.clock_use_limit = 0
        self.clock_used = 0
        self.allow_recover_tp_drink = False
        self.allow_recover_tp_diamond = False
        self.parse_factor_done = False
        self.extra_weight = []
        self.catch_doll = 0
        self.sasami = False

    def reset_skill_learn(self):
        self.learn_skill_done = False
        self.learn_skill_selected = False


class TimeSaleContextDetail:
    buy: list[int]
    bought: list[int]
    buying: int | None
    refresh: FunctionType

    def __init__(self):
        self.buy = []
        self.bought = []
        self.buying = None


class TimeSaleTaskContextDetail:
    time_sale: list[int]
    time_sale_detail: TimeSaleContextDetail

    def __init__(self):
        self.time_sale = []
        self.time_sale_detail = TimeSaleContextDetail()

    def refresh_time_sale(self):
        self.time_sale_detail.buy[:] = self.time_sale
        self.time_sale_detail.bought.clear()
        self.time_sale_detail.buying = None


class TeamStadiumContextDetail(TimeSaleTaskContextDetail):
    opponent_index: int | None
    opponent_stamina: int | None
    raced: bool
    off: bool

    def __init__(self):
        super().__init__()
        self.raced = False
        self.off = False


class DonateContextDetail:
    ask_shoe_type: int
    donated: bool
    asked: bool
    swiped: int

    def __init__(self):
        super().__init__()
        self.donated = False
        self.asked = False
        self.swiped = 0


class DailyRaceContextDetail(TimeSaleTaskContextDetail):
    race: int | None
    difficulty: int | None
    raced: bool

    def __init__(self):
        super().__init__()
        self.raced = False


class UmamusumeContext(BotContext):
    task: UmamusumeTask
    cultivate_detail: CultivateContextDetail
    team_stadium_detail: TeamStadiumContextDetail
    donate_detail: DonateContextDetail
    daily_race_detail: DailyRaceContextDetail
    time_sale_detail: TimeSaleContextDetail

    def __init__(self, task, ctrl):
        super().__init__(task, ctrl)

    def is_task_finish(self) -> bool:
        return False


def build_context(task: UmamusumeTask, ctrl) -> UmamusumeContext:
    ctx = UmamusumeContext(task, ctrl)
    match task.task_type:
        case UmamusumeTaskType.UMAMUSUME_TASK_TYPE_CULTIVATE:
            detail = CultivateContextDetail()
            detail.expect_attribute = task.detail.expect_attribute
            detail.follow_support_card_name = task.detail.follow_support_card_name
            detail.follow_support_card_level = task.detail.follow_support_card_level
            detail.extra_race_list = task.detail.extra_race_list
            detail.learn_skill_list = task.detail.learn_skill_list
            detail.learn_skill_blacklist = task.detail.learn_skill_blacklist
            detail.tactic_list = task.detail.tactic_list
            detail.clock_use_limit = task.detail.clock_use_limit
            detail.learn_skill_threshold = task.detail.learn_skill_threshold
            detail.learn_skill_only_user_provided = task.detail.learn_skill_only_user_provided
            detail.allow_recover_tp_drink = task.detail.allow_recover_tp_drink
            detail.allow_recover_tp_diamond = task.detail.allow_recover_tp_diamond
            detail.extra_weight = task.detail.extra_weight
            ctx.cultivate_detail = detail
        case UmamusumeTaskType.UMAMUSUME_TASK_TYPE_TEAM_STADIUM:
            detail = TeamStadiumContextDetail()
            detail.opponent_index = task.detail.opponent_index
            detail.opponent_stamina = task.detail.opponent_stamina
            detail.time_sale[:] = task.detail.time_sale
            detail.refresh_time_sale()
            ctx.team_stadium_detail = detail
            ctx.time_sale_detail = detail.time_sale_detail
            ctx.time_sale_detail.refresh = detail.refresh_time_sale
        case UmamusumeTaskType.UMAMUSUME_TASK_TYPE_DONATE:
            detail = DonateContextDetail()
            detail.ask_shoe_type = task.detail.ask_shoe_type
            ctx.donate_detail = detail
        case UmamusumeTaskType.UMAMUSUME_TASK_TYPE_DAILY_RACE:
            detail = DailyRaceContextDetail()
            detail.race = task.detail.daily_race_type
            detail.difficulty = task.detail.daily_race_difficulty
            detail.time_sale[:] = task.detail.time_sale
            detail.refresh_time_sale()
            ctx.daily_race_detail = detail
            ctx.time_sale_detail = detail.time_sale_detail
            ctx.time_sale_detail.refresh = detail.refresh_time_sale
    return ctx
