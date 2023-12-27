from bot.base.resource import UI
import module.umamusume.asset.template as template

MAIN_MENU = UI("MAIN_MENU", [template.UI_MAIN_MENU], [])
MAIN_MENU_2 = UI("MAIN_MENU_2", [template.UI_MAIN_MENU_1,template.UI_MAIN_MENU_2,template.UI_MAIN_MENU_3], [])
CULTIVATE_SCENARIO_SELECT = UI("CULTIVATE_SCENARIO_SELECT", [template.UI_CULTIVATE_SCENARIO_SELECT], [])
CULTIVATE_FOLLOW_SUPPORT_CARD_SELECT = UI("CULTIVATE_FOLLOW_SUPPORT_CARD_SELECT",
                                          [template.UI_CULTIVATE_FOLLOW_SUPPORT_CARD_SELECT], [])
CULTIVATE_UMAMUSUME_SELECT = UI("CULTIVATE_UMAMUSUME_SELECT",
                                [template.UI_CULTIVATE_UMAMUSUME_SELECT], [])
CULTIVATE_EXTEND_UMAMUSUME_SELECT = UI("CULTIVATE_EXTEND_UMAMUSUME_SELECT",
                                       [template.UI_CULTIVATE_EXTEND_UMAMUSUME_SELECT], [])
CULTIVATE_SUPPORT_CARD_SELECT = UI("CULTIVATE_SUPPORT_CARD_SELECT",
                                   [template.UI_CULTIVATE_SUPPORT_CARD_SELECT], [])

CULTIVATE_MAIN_MENU = UI("CULTIVATE_MAIN_MENU", [template.UI_CULTIVATE_MAIN_MENU], [])
# CULTIVATE_MENU = UI("CULTIVATE_MENU", [template.BTN_TRAIN_DECK_INFO,template.BTN_BATTLE_HISTORY], [])
CULTIVATE_BATTLE_HISTORY = UI("CULTIVATE_BATTLE_HISTORY", [template.UI_CULTIVATE_BATTLE_HISTORY_1,template.UI_CULTIVATE_BATTLE_HISTORY_2], [])
CULTIVATE_TRAINING_SELECT = UI("CULTIVATE_TRAINING_SELECT", [template.UI_CULTIVATE_TRAINING_SELECT, template.UI_CULTIVATE_TRAINING_SELECT_1], [])
CULTIVATE_FINAL_CHECK = UI("CULTIVATE_FINAL_CHECK", [template.UI_CULTIVATE_FINAL_CHECK], [])
INFO = UI("INFO", [template.UI_INFO], [])
CULTIVATE_GOAL_RACE = UI("CULTIVATE_GOAL_RACE", [template.UI_CULTIVATE_GOAL_RACE_1, template.UI_CULTIVATE_GOAL_RACE_2], [])
CULTIVATE_URA_RACE_1 = UI("CULTIVATE_URA_RACE_1", [template.UI_CULTIVATE_GOAL_RACE_1, template.UI_CULTIVATE_URA_RACE_1],[])
CULTIVATE_URA_RACE_2 = UI("CULTIVATE_URA_RACE_1", [template.UI_CULTIVATE_GOAL_RACE_1, template.UI_CULTIVATE_URA_RACE_2],[])
CULTIVATE_URA_RACE_3 = UI("CULTIVATE_URA_RACE_1", [template.UI_CULTIVATE_GOAL_RACE_1, template.UI_CULTIVATE_URA_RACE_3],[])


CULTIVATE_RACE_LIST = UI("CULTIVATE_RACE_LIST", [template.UI_CULTIVATE_RACE_LIST_1, template.UI_CULTIVATE_RACE_LIST_2], [])

BEFORE_RACE = UI("BEFORE_RACE", [template.UI_BEFORE_RACE_1, template.UI_BEFORE_RACE_2], [])
IN_RACE_UMA_LIST = UI("IN_RACE_UMA_LIST", [template.UI_IN_RACE_UMA_LIST_1, template.UI_IN_RACE_UMA_LIST_2], [])
IN_RACE = UI("IN_RACE", [template.UI_IN_RACE_1, template.UI_IN_RACE_2],[])
RACE_RESULT = UI("RACE_RESULT", [template.UI_RACE_RESULT_1, template.UI_RACE_RESULT_2],[])
RACE_REWARD = UI("RACE_REWARD", [template.UI_RACE_REWARD_1, template.UI_RACE_REWARD_2],[])
GOAL_ACHIEVED = UI("GOAL_ACHIEVED", [template.UI_GOAL_ACHIEVED], [])
GOAL_FAILED = UI("GOAL_ACHIEVED", [template.UI_GOAL_FAILED], [])
NEXT_GOAL = UI("NEXT_GOAL", [template.UI_NEXT_GOAL], [])
ALL_GOAL_ACHIEVED = UI("ALL_GOAL_ACHIEVED", [template.UI_ALL_GOAL_ACHIEVED], [])
CULTIVATE_RESULT = UI("CULTIVATE_RESULT", [template.UI_CULTIVATE_RESULT], [])
CULTIVATE_RESULT_1 = UI("CULTIVATE_RESULT", [template.UI_CULTIVATE_RESULT_1], [])
CULTIVATE_RESULT_2 = UI("CULTIVATE_RESULT", [template.UI_CULTIVATE_RESULT_2], [])
CULTIVATE_CATCH_DOLL_GAME = UI("CULTIVATE_CATCH_DOLL_GAME", [template.UI_CULTIVATE_CATCH_DOLL_GAME_1, template.UI_CULTIVATE_CATCH_DOLL_GAME_2], [])
CULTIVATE_CATCH_DOLL_GAME_RESULT = UI("CULTIVATE_CATCH_DOLL_GAME", [template.UI_CULTIVATE_CATCH_DOLL_GAME_RESULT_1, template.UI_CULTIVATE_CATCH_DOLL_GAME_RESULT_2], [])
CULTIVATE_FINISH = UI("CULTIVATE_FINISH", [template.UI_CULTIVATE_FINISH], [])

CULTIVATE_EXTEND = UI("CULTIVATE_EXTEND", [template.UI_CULTIVATE_EXTEND], [])

CULTIVATE_EVENT_UMAMUSUME = UI("CULTIVATE_EVENT_UMAMUSUME", [template.UI_CULTIVATE_EVENT_UMAMUSUME], [])
CULTIVATE_EVENT_SUPPORT_CARD = UI("CULTIVATE_EVENT_SUPPORT_CARD", [template.UI_CULTIVATE_EVENT_SUPPORT_CARD], [])
CULTIVATE_EVENT_SCENARIO = UI("CULTIVATE_EVENT_SCENARIO", [template.UI_CULTIVATE_EVENT_SCENARIO], [])

CULTIVATE_LEARN_SKILL = UI("CULTIVATE_LEARN_SKILL",
                           [template.UI_CULTIVATE_LEARN_SKILL_1, template.UI_CULTIVATE_LEARN_SKILL_2], [])

RECEIVE_CUP = UI("CULTIVATE_RECEIVE_CUP",[template.UI_RECEIVE_CUP], [])

CULTIVATE_LEVEL_RESULT = UI("CULTIVATE_LEVEL_RESULT", [template.UI_CULTIVATE_LEVEL_RESULT], [])
FACTOR_RECEIVE = UI("FACTOR_RECEIVE", [template.UI_FACTOR_RECEIVE], [])
HISTORICAL_RATING_UPDATE = UI("HISTORICAL_RATING_UPDATE", [template.UI_HISTORICAL_RATING_UPDATE], [])
SCENARIO_RATING_UPDATE = UI("HISTORICAL_RATING_UPDATE", [template.UI_SCENARIO_RATING_UPDATE], [])
ACTIVITY_RESULT = UI("ACTIVITY_RESULT", [template.UI_ACTIVITY_RESULT], [])
ACTIVITY_REWARD = UI("ACTIVITY_REWARD", [template.UI_ACTIVITY_REWARD], [])

scan_ui_list = [MAIN_MENU,MAIN_MENU_2,
                CULTIVATE_SCENARIO_SELECT, CULTIVATE_UMAMUSUME_SELECT, CULTIVATE_EXTEND_UMAMUSUME_SELECT,
				# CULTIVATE_MENU,
				CULTIVATE_BATTLE_HISTORY,
                CULTIVATE_SUPPORT_CARD_SELECT, CULTIVATE_FOLLOW_SUPPORT_CARD_SELECT, CULTIVATE_FINAL_CHECK, INFO,
                CULTIVATE_MAIN_MENU, CULTIVATE_TRAINING_SELECT, CULTIVATE_EXTEND, CULTIVATE_CATCH_DOLL_GAME,
                CULTIVATE_CATCH_DOLL_GAME_RESULT, CULTIVATE_LEVEL_RESULT,
                CULTIVATE_GOAL_RACE, CULTIVATE_RACE_LIST, CULTIVATE_RESULT, CULTIVATE_RESULT_1, CULTIVATE_RESULT_2,
                CULTIVATE_LEARN_SKILL, RECEIVE_CUP,
                CULTIVATE_URA_RACE_1, CULTIVATE_URA_RACE_2,CULTIVATE_URA_RACE_3,
                BEFORE_RACE, IN_RACE_UMA_LIST, IN_RACE, RACE_RESULT, RACE_REWARD,
                GOAL_ACHIEVED, NEXT_GOAL, ALL_GOAL_ACHIEVED, CULTIVATE_FINISH, GOAL_FAILED,
                FACTOR_RECEIVE, HISTORICAL_RATING_UPDATE, SCENARIO_RATING_UPDATE,
                CULTIVATE_EVENT_UMAMUSUME, CULTIVATE_EVENT_SUPPORT_CARD, CULTIVATE_EVENT_SCENARIO, ACTIVITY_RESULT,
                ACTIVITY_REWARD]
