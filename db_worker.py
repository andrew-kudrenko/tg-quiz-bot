# from config import QuizDialogStates
#
#
# class DB:
#     def __init__(self):
#         self.states = {}
#
#     def get_state(self, id: str) -> str:
#         try:
#             return self.states[id]
#         except KeyError:
#             return QuizDialogStates.start.state
#
#     def set_state(self, id: str, value: str):
#         self.states[id] = value
#
#
# db = DB()
#
