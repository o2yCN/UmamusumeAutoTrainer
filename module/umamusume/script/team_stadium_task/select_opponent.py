import random
from module.umamusume.context import UmamusumeContext


def select_opponent(ctx: UmamusumeContext) -> int:
    index = ctx.team_stadium_detail.opponent_index
    if index is not None:
        if index:
            return index
    return random.randint(1, 3)
